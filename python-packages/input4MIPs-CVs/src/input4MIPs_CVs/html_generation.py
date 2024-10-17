"""
Generation of our HTML pages

This may be a temporary home, but is fine for now
"""

from __future__ import annotations

import datetime as dt
import difflib
import json
from collections.abc import Iterable
from pathlib import Path

import packaging.version
import pandas as pd


def get_url_esgf_for_html_table(row: pd.Series, search_facets: Iterable[str]) -> str:
    """
    Get the relevant ESGF search URL for a given row in a database view

    Parameters
    ----------
    row
        Row for which to generate the relevant ESGF search URL information

    search_facets
        Search facets to include in the ESGF search URL

    Returns
    -------
    :
        ESGF search URL, formatted for use in an HTML context
    """
    publication_status: str = row["publication_status"]

    if publication_status == "registered":
        res = (
            "<a href='https://github.com/PCMDI/input4MIPs_CVs/blob/main/CVs/input4MIPs_source_id.json' target='_blank'>"
            "Registered in CVs"
            "</a>"
        )
        return res

    if publication_status == "in_publishing_queue":
        res = (
            "<a href='https://github.com/PCMDI/input4MIPs_CVs/blob/main/CVs/input4MIPs_source_id.json' target='_blank'>"
            "In publishing queue"
            "</a>"
        )
        return res

    if publication_status == "abandoned":
        return "Abandoned: registered but never produced"

    if publication_status == "never_published":
        return (
            "Never published: registered but never published on ESGF. "
            "Note: this does not mean "
            "that the dataset wasn't published on a platform other than the ESGF."
        )

    if publication_status == "published":
        publication_text = "Published"

    elif publication_status == "retracted":
        publication_text = "Retracted"

    else:
        raise NotImplementedError(publication_status)

    def _gsfv(search_facet: str, search_facet_value: str) -> str:
        """
        Get search facet value, given there are some unexpected mappings happening on ESGF
        """
        if search_facet == "variable_id" and search_facet_value == "multiple":
            return "Multiple"

        return search_facet_value

    search_components = "%2C".join(
        [f"%22{sf}%22%3A%22{_gsfv(sf, row[sf])}%22" for sf in search_facets]
    )

    url = "".join(
        [
            "https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B",
            search_components,
            "%7D",
        ]
    )

    res = f"<a href='{url}' target='_blank'>{publication_text}</a>"

    return res


def get_esgf_urls_for_html(df: pd.DataFrame, search_facets: Iterable[str]) -> pd.Series:
    """
    Get ESGF URLs for all rows in `df`

    Parameters
    ----------
    df
        Dataframe for which to generate the ESGF URLs

    search_facets
        Search facets to included in the generated URLs

    Returns
    -------
    :
        Generated URLs, ready for use in an HTML table
    """
    urls = df.apply(
        get_url_esgf_for_html_table,
        search_facets=search_facets,
        axis="columns",
    )
    urls.name = "ESGF URL"

    return urls


def get_files_view(
    db: pd.DataFrame,
    view_front_cols: tuple[str, ...] = (
        "mip_era",
        "variable_id",
        "latest",
        "publication_status",
        "comment_post_publication",
        "source_id",
        "contact",
        "sha256",
    ),
) -> pd.DataFrame:
    """
    Get the files view of the database

    This view shows each file as a separate row.

    Parameters
    ----------
    db
        Database for which to generate the view

    view_front_cols
        The columns which should appear first in the generated view.

        All other columns in `db` appear after these columns,
        in alphabetical order.

    Returns
    -------
    :
        Files view of `db`
    """
    col_order = tuple(
        [
            *view_front_cols,
            *sorted([v for v in db.columns if v not in view_front_cols]),
        ]
    )

    res = db[list(col_order)].drop_duplicates()
    # Only keep entries which actually have a file
    res = res[~res["sha256"].isnull()]

    urls = get_esgf_urls_for_html(
        db,
        search_facets=[
            "variable_id",
            "frequency",
            "grid_label",
            "source_id",
            "mip_era",
        ],
    )
    res = pd.concat([urls, res], axis="columns")

    return res


def get_datasets_view(
    db: pd.DataFrame,
    view_front_cols: tuple[str, ...] = (
        "mip_era",
        "variable_id",
        "latest",
        "publication_status",
        "comment_post_publication",
        "source_id",
        "contact",
    ),
    view_other_cols: tuple[str, ...] = (
        "source_version",
        "institution_id",
        "license_id",
        "dataset_category",
        "realm",
        "frequency",
        "time_range",
        "grid_label",
        "target_mip",
        "further_info_url",
    ),
) -> pd.DataFrame:
    """
    Get the datasets view of the database

    This view shows each dataset as a separate row,
    aggregating information from the files in the process.

    Parameters
    ----------
    db
        Database for which to generate the view

    view_front_cols
        The columns which should appear first in the generated view.

    view_other_cols
        Other columns from `db` to include in the view.

        These columns are included in alphabetical order.

    Returns
    -------
    :
        Datasets view of `db`
    """
    col_order = tuple(
        [
            *view_front_cols,
            *sorted(view_other_cols),
        ]
    )

    res = db[list(col_order)].drop_duplicates()

    res_aggregated_l = []
    group_cols = [v for v in col_order if v not in ["time_range"]]
    for _, dsvdf in res.groupby(group_cols, dropna=False):
        if all(v is None for v in dsvdf["time_range"]):
            res_aggregated_l.append(dsvdf)
            continue

        # Incredibly slow way of doing this, but fine for now
        all_times = []
        for v in dsvdf["time_range"].tolist():
            s, e = v.split("-")
            all_times.append(s)
            all_times.append(e)

        time_range_summary = f"{min(all_times)}-{max(all_times)}"
        keep = dsvdf[group_cols].drop_duplicates()
        keep["time_range"] = time_range_summary

        res_aggregated_l.append(keep)

    res = pd.concat(res_aggregated_l)

    urls = get_esgf_urls_for_html(
        res,
        search_facets=[
            "variable_id",
            "frequency",
            "grid_label",
            "source_id",
            "mip_era",
        ],
    )
    res = pd.concat([urls, res], axis="columns")

    return res


def get_source_id_view(
    db: pd.DataFrame,
    view_front_cols: tuple[str, ...] = (
        "mip_era",
        "source_id",
        "latest",
        "publication_status",
        "comment_post_publication",
        "contact",
    ),
    view_cols_to_aggregate: tuple[str, ...] = ("dataset_category",),
    view_other_cols: tuple[str, ...] = (
        "source_version",
        "institution_id",
        "license_id",
        "further_info_url",
    ),
) -> pd.DataFrame:
    """
    Get the source ID view of the database

    This view shows each source ID as a separate row,
    mostly dropping information that isn't displayed,
    although there is some aggregation.

    Parameters
    ----------
    db
        Database for which to generate the view

    view_front_cols
        The columns which should appear first in the generated view.

    view_cols_to_aggregate
        The columns which should appear,
        with their values from the underlying data aggregated.

    view_other_cols
        Other columns from `db` to include in the view.

        These columns are included in alphabetical order.

    Returns
    -------
    :
        Source ID view of `db`

    Raises
    ------
    ValueError
        The rows are not unique for each source ID,
        given the choice of columns to display
        and columns to aggregate.
    """
    col_order = tuple(
        [
            *view_front_cols,
            *view_cols_to_aggregate,
            *sorted(view_other_cols),
        ]
    )

    res = db[list(col_order)].drop_duplicates()

    res_aggregated_l = []
    group_cols = [v for v in col_order if v not in view_cols_to_aggregate]
    for _, dsvdf in res.groupby(group_cols, dropna=False):
        tmp = dsvdf.copy()
        for vc in view_cols_to_aggregate:
            # Inredibly slow, but precise so ok for now
            if tmp[vc].apply(lambda x: x is None).all():
                # No need to update
                continue

            tmp[vc] = ", ".join(tmp[vc].tolist())

        tmp_dd = tmp.drop_duplicates()
        if tmp_dd.shape[0] != 1:
            source_id = tmp_dd["source_id"].unique()
            msg = f"Information for {source_id=} isn't as expected. {tmp_dd=}"
            raise ValueError(msg)

        res_aggregated_l.append(tmp_dd)

    res = pd.concat(res_aggregated_l)

    urls = get_esgf_urls_for_html(
        res,
        search_facets=[
            "source_id",
            "mip_era",
        ],
    )
    res = pd.concat([urls, res], axis="columns")

    return res


def get_delivery_summary_view(
    db: pd.DataFrame,
    view_cols_from_db: tuple[str, ...] = (
        "source_id",
        "publication_status",
    ),
) -> pd.DataFrame:
    """
    Get the delivery summary view of the database

    This view shows when each dataset is going to be delivered.
    It has more hand-woven components than the other views,
    which are purely views of the database.

    Parameters
    ----------
    db
        Database for which to generate the view

    view_cols_from_db
        The columns from the database which should appear in the generated view.

    Returns
    -------
    :
        Delivery summary view of `db`
    """
    hard_coded_info = [
        {
            "source_id": "CEDS-CMIP-2024-07-08, CEDS-CMIP-2024-07-08-supplemental",
            "description": "Anthropogenic short-lived climate forcer (SLCF) and CO2 emissions",
            "expected_publication": "October 2024",
            "url": "https://www.pnnl.gov/projects/ceds",
            "status": "Bugs being fixed, data in preparation",
        },
        {
            "source_id": "DRES-CMIP-BB4CMIP7-1-0",
            "description": "Open biomass burning emissions",
            "url": "http://www.globalfiredata.org",
            "status": "Preliminary dataset available",
        },
        {
            "source_id": "UofMD-landState-3-0",
            "description": "Land use",
            "url": "http://luh.umd.edu",
            "status": "Preliminary dataset available",
        },
        {
            "source_id": "CR-CMIP-0-3-0",
            "description": "Greenhouse gas concentrations",
            "url": None,
            "status": "Preliminary dataset available",
        },
        {
            "source_id": "UOEXETER-CMIP-1-1-3",
            "description": "Stratospheric volcanic SO2 emissions and aerosol optical properties",
            "url": None,
            "status": "Preliminary dataset available",
        },
        {
            "source_id": None,  # TBD
            "description": "Ozone concentrations",
            "expected_publication": "~January 2025; 3 months after dependent datasets",
            "url": None,
            "status": "Depends on 1, 2, 4, 5 and 8",
        },
        {
            "source_id": None,  # TBD
            "description": "Nitrogen deposition",
            "expected_publication": "~January 2025; 3 months after dependent datasets",
            "url": None,
            "status": "Depends on 1, 2, 4, 5 and 8",
        },
        {
            "source_id": "SOLARIS-HEPPA-CMIP-4-3",
            "description": "Solar",
            "url": "https://solarisheppa.geomar.de/cmip7",
            "status": "Preliminary dataset available",
        },
        {
            "source_id": "PCMDI-AMIP-1-1-9",
            "description": "AMIP sea-surface temperature and sea-ice boundary forcing",
            "url": "https://pcmdi.llnl.gov/mips/amip/",
            "status": "Final v1 dataset available. v2 dataset awaiting HadISST v2.4 release ",
        },
        {
            "source_id": None,  # TBD
            "description": "Aerosol optical properties/MACv2-SP",
            "expected_publication": "~November 2024; Expected a month after dependent datasets",
            "url": None,
            "status": "Depends on 1, test dataset being produced in the meantime",
        },
        {
            "source_id": None,  # TBD
            "description": "Population",
            "expected_publication": "Unknown: data provider TBD",
            "url": None,
            "status": "Unknown: data provider TBD",
        },
    ]

    res_l = []
    for i, info_d in enumerate(hard_coded_info):
        tmp = {}
        tmp["Dataset #"] = i + 1

        if info_d["source_id"] is None:
            if info_d["url"] is not None:
                tmp["Forcing dataset"] = (
                    f"<a href='{info_d['url']}' target='_blank'>{info_d['description']}</a>"
                )
            else:
                tmp["Forcing dataset"] = info_d["description"]

            tmp["Source ID"] = "TBD"
            tmp["Status"] = info_d["status"]
            tmp["ESGF publication status"] = (
                f"Expected: {info_d['expected_publication']}"
            )

        else:
            db_source_id = db[
                db["source_id"].isin(
                    [v.strip() for v in info_d["source_id"].split(",")]
                )
            ]

            further_info_url = db_source_id["further_info_url"].unique()
            if len(further_info_url) == 1:
                further_info_url = further_info_url[0]
                if further_info_url.endswith(".invalid"):
                    further_info_url = None

            else:
                raise NotImplementedError(further_info_url)

            if further_info_url is not None:
                tmp["Forcing dataset"] = (
                    f"<a href='{further_info_url}' target='_blank'>{info_d['description']}</a>"
                )

            else:
                tmp["Forcing dataset"] = info_d["description"]

            tmp["Source ID"] = info_d["source_id"]
            tmp["Status"] = info_d["status"]

            publication_status = db_source_id["publication_status"].unique()
            if len(publication_status) == 1:
                publication_status = publication_status[0]

            else:
                raise NotImplementedError(publication_status)

            if publication_status in "published":
                source_version = db_source_id["source_version"].unique()
                if len(source_version) == 1:
                    source_version = source_version[0]

                else:
                    raise NotImplementedError(source_version)

                if len(db_source_id["source_id"].unique()) != 1:
                    raise AssertionError()

                # All rows have same source ID, hence can use any here
                esgf_url = get_url_esgf_for_html_table(
                    db_source_id.iloc[0, :], ["source_id"]
                )

                ts_min_str = db_source_id["datetime_start"].dropna().min()
                ts_min_dt = dt.datetime.strptime(ts_min_str, "%Y-%m-%dT%H:%M:%SZ")

                ts_max_str = db_source_id["datetime_end"].dropna().max()
                ts_max_dt = dt.datetime.strptime(ts_max_str, "%Y-%m-%dT%H:%M:%SZ")

                frequencies = set(db_source_id["frequency"].tolist())
                if "day" in frequencies:
                    ts_min = (
                        f"{ts_min_dt.year:04}-{ts_min_dt.month:02}-{ts_min_dt.day:02}"
                    )
                    ts_max = (
                        f"{ts_max_dt.year:04}-{ts_max_dt.month:02}-{ts_max_dt.day:02}"
                    )

                elif "mon" in frequencies:
                    ts_min = f"{ts_min_dt.year:04}-{ts_min_dt.month:02}"
                    ts_max = f"{ts_max_dt.year:04}-{ts_max_dt.month:02}"

                elif "yr" in frequencies:
                    ts_min = f"{ts_min_dt.year:04}"
                    ts_max = f"{ts_max_dt.year:04}"

                else:
                    raise NotImplementedError(frequencies)

                tmp["ESGF publication status"] = esgf_url.replace(
                    "Published", f"Available: v{source_version} ({ts_min} to {ts_max})"
                )

            elif publication_status in ["in_publishing_queue", "registered"]:
                if "expected_publication" in info_d:
                    tmp["ESGF publication status"] = (
                        f"Expected: {info_d['expected_publication']}"
                    )

            else:
                raise NotImplementedError(publication_status)

        res_l.append(tmp)

    res = pd.DataFrame(res_l)

    return res


def get_db_views_to_write(
    repo_root_dir: Path,
    db_file_path_rel_to_root: Path = Path("Database")
    / "input4MIPs_db_file_entries.json",
    html_dir_rel_to_root: Path = Path("docs") / "database-views",
) -> tuple[tuple[pd.DataFrame, Path, str], ...]:
    """
    Get the views of the database to write as HTML files

    Parameters
    ----------
    repo_root_dir
        Root directory of the repository

    db_file_path_rel_to_root
        Path to the raw datbase file, relative to `repo_root_dir`

    html_dir_rel_to_root
        Path in which to write the generated HTML files, relative to `repo_root_dir`

    Returns
    -------
    :
        Configuration to use for writing the views of the database as HTML files.

        In each returned tuple, the elements are:

        1. View of the database to write
        2. The path in which to write this view
        3. The string to use as the title of this view's generated page
    """
    db_file = repo_root_dir / db_file_path_rel_to_root

    with open(db_file) as fh:
        db_raw = json.load(fh)

    db = pd.DataFrame(db_raw)

    files_view = get_files_view(db)
    datasets_view = get_datasets_view(db)
    source_id_view = get_source_id_view(db)
    delivery_summary_view = get_delivery_summary_view(db)

    # Hard-code filenames for now
    res = (
        # (
        #     view,
        #     path_to_write_in,
        #     header,
        #     special_sort,
        # )
        (
            files_view[files_view["mip_era"] == "CMIP6Plus"],
            repo_root_dir / html_dir_rel_to_root / "input4MIPs_files_CMIP6Plus.html",
            "input4MIPs CMIP6Plus files",
            True,
        ),
        (
            datasets_view[datasets_view["mip_era"] == "CMIP6Plus"],
            repo_root_dir / html_dir_rel_to_root / "input4MIPs_datasets_CMIP6Plus.html",
            "input4MIPs CMIP6Plus datasets",
            True,
        ),
        (
            source_id_view[source_id_view["mip_era"] == "CMIP6Plus"],
            repo_root_dir
            / html_dir_rel_to_root
            / "input4MIPs_source-id_CMIP6Plus.html",
            "input4MIPs CMIP6Plus source IDs",
            True,
        ),
        (
            delivery_summary_view,
            repo_root_dir
            / html_dir_rel_to_root
            / "input4MIPs_delivery-summary_CMIP6Plus.html",
            "input4MIPs CMIP6Plus delivery summary",
            False,
        ),
    )

    return res


def get_head_foot_row(columns: tuple[str, ...], kind: str = "thead") -> str:
    """
    Get a header/footer row of our HTML table

    Parameters
    ----------
    columns
        Columns included in the table for which we are generating the header/footer

    kind
        Kind of row to generate (either "thead", or "tfoot")

    Returns
    -------
    :
        Header/footer row of an HTML table
    """
    row_l = [f"<{kind}>", "  <tr>"]
    for col in columns:
        # row_l.append(f'    <th scope="col">{col}</th>')
        row_l.append(f"    <th>{col}</th>")

    row_l.extend(
        [
            "  </tr>",
            f"</{kind}>",
        ]
    )

    return "\n".join(row_l)


def generate_table_rows(
    db_view: pd.DataFrame,
    columns: tuple[str, ...],
) -> tuple[str, ...]:
    """
    Generate the table rows for a given database view

    Parameters
    ----------
    db_view
        View of the database to convert to HTML table rows

    columns
        Columns of the generated table

    Returns
    -------
    :
        Generated table rows for `db_view`
    """
    rows_l = []
    for entry in db_view.to_dict(orient="records"):
        row_l = ["<tr>"]
        for col in columns:
            row_l.append(f"  <td>{entry[col]}</td>")

        row_l.append("</tr>")

        rows_l.append("\n".join(row_l))

    return tuple(rows_l)


def write_db_view_as_html(
    db_view: pd.DataFrame,
    file_to_write: Path,
    page_title: str,
    version: packaging.version.Version,
    publication_status_display_order: tuple[str, ...] = (
        "registered",
        "in_publishing_queue",
        "published",
        "retracted",
        "abandoned",
        "never_published",
    ),
    check_unchanged: bool = False,
    special_sort: bool = True,
) -> None:
    """
    Write a view of the database as HTML

    Parameters
    ----------
    db_view
        Database view to write as HTML

    file_to_write
        File in which to write the generated HTML

    page_title
        Title of the page we are writing

    version
        Version of the database for which we are writing the view

    publication_status_display_order
        Order in which the publication status of the rows in the view
        should appear when the page is first loaded.

    check_unchanged
        Should we raise an error if `file_to_write`'s content would change?

    special_sort
        Should we apply our special sorting to this view before writing?
    """
    if special_sort:
        # Little bit of special sorting,
        # so that the initial view of the table makes a bit more sense
        db_view_tmp = db_view.sort_values(by=db_view.columns.tolist()).copy()
        db_view_sorted_l = []

        db_view_publication_statuses = set(db_view["publication_status"])
        missing_publication_statues = db_view_publication_statuses.difference(
            set(publication_status_display_order)
        )
        if missing_publication_statues:
            raise AssertionError(missing_publication_statues)

        for publication_status in publication_status_display_order:
            db_view_sorted_l.append(
                db_view_tmp[db_view_tmp["publication_status"] == publication_status]
            )

        db_view_sorted = pd.concat(db_view_sorted_l)
        db_view_sorted = db_view_sorted.reset_index(drop=True)
        db_view_sorted.index.name = "default_sort_index"
        db_view_sorted = db_view_sorted.reset_index()

    else:
        db_view_sorted = db_view.copy()

    columns = list(db_view_sorted.columns)
    table_header_row = get_head_foot_row(columns, kind="thead")
    table_footer_row = get_head_foot_row(columns, kind="tfoot")
    table_rows = generate_table_rows(db_view_sorted, columns)

    header_lines = [
        "<head>",
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>',
        '<meta name="author" content="Paul J. Durack, Zebedee Nicholls" />',
        '<meta name="description" content="Controlled vocabulary for input4MIPs" />',
        '<meta name="keywords" content="HTML, CSS, JavaScript" />',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        '<link rel="stylesheet" type="text/css" charset="utf-8" href="https://pcmdi.github.io/assets/dataTables/jquery.dataTables.min.css" />',
        '<script type="text/javascript" charset="utf-8" src="https://pcmdi.github.io/assets/jquery/jquery.slim.min.js"></script>',
        '<script type="text/javascript" charset="utf-8" src="https://pcmdi.github.io/assets/dataTables/jquery.dataTables.min.js"></script>',
        "<!-- Global site tag (gtag.js) - Google Analytics -->",
        '<script type="text/javascript" src="https://pcmdi.github.io/assets/google/googleAnalyticsTag.js" ></script>',
        '<script type="text/javascript">',
        "//<![CDATA[",
        "$(document).ready( function () {",
        # "    $('#table_id').DataTable();",
        "    $('#table_id').DataTable({pageLength: 25});",
        "    } );",
        "//]]>",
        "</script>",
        f"<title>{page_title}</title>",
        "</head>",
    ]

    res_l = [
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
        '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">',
        *header_lines,
        "<body>",
        f"<p><h1>{page_title}: v{version}</h1><p>",
        "<h4>",
        "<a href='/database-views/#database-views'>Database views homepage</a>",
        "| <a href='input4MIPs_delivery-summary_CMIP6Plus.html'>Delivery summary view</a>",
        "| <a href='input4MIPs_source-id_CMIP6Plus.html'>Source ID-level view</a>",
        "| <a href='input4MIPs_datasets_CMIP6Plus.html'>Dataset-level view</a>",
        "| <a href='input4MIPs_files_CMIP6Plus.html'>File-level view</a>",
        "</h4>",
        '<table id="table_id" class="display compact">',
        *[f"  {v}" for v in table_header_row.splitlines()],
        *[f"  {v}" for v in table_footer_row.splitlines()],
        *[f"    {v}" for v in "\n".join(table_rows).splitlines()],
        "</table>",
        "</body>",
        "</html>",
    ]

    to_write = "\n".join(res_l)
    if not to_write.endswith("\n"):
        # Ensure content ends with new line
        to_write = f"{to_write}\n"

    if check_unchanged:
        with open(file_to_write) as fh:
            current_status = fh.read()

        if to_write != current_status:
            diff_view = "".join(
                difflib.unified_diff(
                    current_status.splitlines(keepends=True),
                    to_write.splitlines(keepends=True),
                    fromfile="current_status",
                    tofile="to_write",
                )
            )
            msg = f"Web page would be updated by the write operation\n{diff_view}"
            raise AssertionError(msg)

    else:
        with open(file_to_write, "w") as fh:
            fh.write(to_write)


def generate_html_pages(
    version: packaging.version.Version,
    repo_root_dir: Path,
    check_unchanged: bool = False,
) -> None:
    """
    Generate the HTML pages we capture in the repository

    Parameters
    ----------
    version
        Version of the database for which we are generating HTML pages

    repo_root_dir
        Root directory of the repository

    check_unchanged
        Should we raise an error if the web pages would be updated?
    """
    # Get db views to write
    db_views = get_db_views_to_write(repo_root_dir=repo_root_dir)

    for df, write_file, page_title, special_sort in db_views:
        write_db_view_as_html(
            db_view=df,
            file_to_write=write_file,
            page_title=page_title,
            version=version,
            check_unchanged=check_unchanged,
            special_sort=special_sort,
        )
