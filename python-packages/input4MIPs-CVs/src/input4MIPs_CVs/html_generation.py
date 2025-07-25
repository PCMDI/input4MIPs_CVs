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
from typing import Any

import packaging.version
import pandas as pd


def format_url_for_html(link: str, desc: str) -> str:
    """
    Forat a URL for display on an HTML page

    Parameters
    ----------
    link
        Link to link to

    desc
        Description to show to the viewer


    Returns
    -------
    :
        Formatted link
    """
    return f"<a href='{link}' target='_blank'>{desc}</a>"


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
        "doi",
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
            toks = v.split("-")
            s = toks[0]
            e = toks[1]
            # Might be one more token if we have a climatology
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
    view_cols_to_aggregate: tuple[str, ...] = (
        "doi",
        "dataset_category",
    ),
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

            tmp[vc] = ", ".join(tmp[vc].unique().tolist())

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
    delivery_summary_info: dict[str, Any],
    dataset_info: dict[str, Any],
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

    delivery_summary_info
        Information to use to create the delivery summary

    dataset_info
        Dataset information

    view_cols_from_db
        The columns from the database which should appear in the generated view.

    Returns
    -------
    :
        Delivery summary view of `db`
    """
    res_l = []
    for ds_id, info_d in delivery_summary_info.items():
        tmp = {}
        tmp["Dataset #"] = dataset_info[ds_id]["dataset_number"]
        input4MIPs_CVs_internal_page = dataset_info[ds_id][
            "input4MIPs_CVS_internal_page"
        ]

        description_html = dataset_info[ds_id]["description_html"]

        if info_d["source_ids"] is None:
            if ds_id == "simple-plumes":
                # Fun exception
                tmp["Forcing dataset"] = (
                    f"<a href='{info_d['url']}' target='_blank'>{description_html}</a>"
                )
                tmp["Source ID"] = (
                    f"NA (not released on ESGF, see {format_url_for_html(info_d['url'], info_d['url'])} instead)"
                )
                if "status" in info_d:
                    tmp["Status"] = info_d["status"]
                else:
                    tmp["Status"] = "Preliminary dataset available"

                tmp["ESGF publication status"] = (
                    f"Available: {format_url_for_html(info_d['url'], info_d['url'])}"
                )

            else:
                if info_d["url"] is not None:
                    tmp["Forcing dataset"] = (
                        f"<a href='{info_d['url']}' target='_blank'>{description_html}</a>"
                    )
                else:
                    tmp["Forcing dataset"] = description_html

                tmp["Source ID"] = "TBD"
                tmp["Status"] = info_d["status"]
                tmp["ESGF publication status"] = (
                    f"Expected: {info_d['expected_publication']}"
                )

        else:
            db_source_ids = db[
                db["source_id"].isin([v.strip() for v in info_d["source_ids"]])
            ]

            url_to_use = None
            if "url" in info_d:
                url_to_use = info_d["url"]

            else:
                further_info_url = db_source_ids["further_info_url"].unique()
                if len(further_info_url) == 1:
                    further_info_url = further_info_url[0]
                    if further_info_url.endswith(".invalid"):
                        further_info_url = None

                else:
                    raise NotImplementedError(further_info_url)

                if further_info_url is not None:
                    url_to_use = further_info_url

            if url_to_use is not None:
                tmp["Forcing dataset"] = (
                    f"<a href='{url_to_use}' target='_blank'>{description_html}</a>"
                )

            else:
                tmp["Forcing dataset"] = description_html

            tmp["Source ID"] = ", ".join(info_d["source_ids"])
            if "status" in info_d:
                tmp["Status"] = info_d["status"]
            else:
                mip_era = db[db["source_id"].isin(info_d["source_ids"])][
                    "mip_era"
                ].unique()
                if len(mip_era) > 1:
                    raise NotImplementedError
                mip_era = mip_era[0]

                if mip_era == "CMIP6Plus":
                    tmp["Status"] = "Preliminary dataset available"
                elif mip_era == "CMIP7":
                    tmp["Status"] = "CMIP7 dataset available"
                else:
                    raise NotImplementedError(mip_era)

            publication_status = db_source_ids["publication_status"].unique()
            if len(publication_status) == 1:
                publication_status = publication_status[0]

            elif set(publication_status) == {"published", "retracted"}:
                publication_status = "published_with_partial_retraction"

            else:
                raise NotImplementedError(publication_status)

            if publication_status in ["published", "published_with_partial_retraction"]:
                disp_urls = []
                for source_id, source_id_df in db_source_ids.groupby("source_id"):
                    # All rows have the same source ID, so can use any
                    esgf_url = get_url_esgf_for_html_table(
                        source_id_df.iloc[0, :], ["source_id"]
                    )

                    ts_min_str = source_id_df["datetime_start"].dropna().min()
                    ts_min_dt = dt.datetime.strptime(ts_min_str, "%Y-%m-%dT%H:%M:%SZ")

                    ts_max_str = source_id_df["datetime_end"].dropna().max()
                    ts_max_dt = dt.datetime.strptime(ts_max_str, "%Y-%m-%dT%H:%M:%SZ")

                    frequencies = set(source_id_df["frequency"].tolist())
                    if "day" in frequencies:
                        ts_min = f"{ts_min_dt.year:04}-{ts_min_dt.month:02}-{ts_min_dt.day:02}"
                        ts_max = f"{ts_max_dt.year:04}-{ts_max_dt.month:02}-{ts_max_dt.day:02}"

                    elif "mon" in frequencies:
                        ts_min = f"{ts_min_dt.year:04}-{ts_min_dt.month:02}"
                        ts_max = f"{ts_max_dt.year:04}-{ts_max_dt.month:02}"

                    elif "yr" in frequencies:
                        ts_min = f"{ts_min_dt.year:04}"
                        ts_max = f"{ts_max_dt.year:04}"

                    else:
                        raise NotImplementedError(frequencies)

                    disp_url = esgf_url.replace(
                        "Published",
                        f"{source_id} ({ts_min} to {ts_max})",
                    )
                    disp_urls.append(disp_url)

                disp_urls_joint = ", ".join(disp_urls)

                if publication_status == "published":
                    tmp["ESGF publication status"] = f"Available: {disp_urls_joint}"

                elif publication_status == "published_with_partial_retraction":
                    tmp["ESGF publication status"] = (
                        f"Available (but some data has been retracted, be careful!): {disp_urls_joint}"
                    )

                else:
                    raise NotImplementedError(publication_status)

            elif publication_status in ["in_publishing_queue", "registered"]:
                if "expected_publication" in info_d:
                    tmp["ESGF publication status"] = (
                        f"Expected: {info_d['expected_publication']}"
                    )

            elif publication_status == "retracted":
                msg = (
                    f"publication status for source_ids={info_d['source_ids']} "
                    f"is {publication_status}. "
                    "Please check the source ID being used in `docs/dataset-info/delivery-summary.json`."
                )
                raise ValueError(msg)

            else:
                raise NotImplementedError(publication_status)

        internal_docs_link = f"Internal docs: <a href='../dataset-overviews/{input4MIPs_CVs_internal_page}' target='_blank'>here</a>"
        tmp["Forcing dataset"] = (
            f"<b>{tmp['Forcing dataset']}</b></br>{internal_docs_link}"
        )

        res_l.append(tmp)

    res = pd.DataFrame(res_l)
    res = res[
        [
            "Dataset #",
            "Forcing dataset",
            "Source ID",
            "Status",
            "ESGF publication status",
        ]
    ]

    return res


def get_db_views_to_write(
    repo_root_dir: Path,
    db_file_path_rel_to_root: Path = Path("Database")
    / "input4MIPs_db_file_entries.json",
    html_dir_rel_to_root: Path = Path("docs") / "database-views",
    delivery_summary_info_p: Path = Path("docs")
    / "dataset-info"
    / "delivery-summary.json",
    dataset_info_p: Path = Path("docs") / "dataset-info" / "dataset-info.json",
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

    delivery_summary_info_p
        Path in which the delivery summary information lives

    dataset_info_p
        Path in which the key dataset information lives

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

    with open(delivery_summary_info_p) as fh:
        delivery_summary_info = json.load(fh)

    with open(dataset_info_p) as fh:
        dataset_info = json.load(fh)

    db = pd.DataFrame(db_raw)

    files_view = get_files_view(db)
    datasets_view = get_datasets_view(db)
    source_id_view = get_source_id_view(db)
    delivery_summary_view = get_delivery_summary_view(
        db=db, delivery_summary_info=delivery_summary_info, dataset_info=dataset_info
    )

    res_l = []
    for mip_era in ["CMIP6Plus", "CMIP7"]:
        entries = [
            # (
            #     view,
            #     path_to_write_in,
            #     header,
            #     special_sort,
            # )
            (
                files_view[files_view["mip_era"] == mip_era],
                repo_root_dir
                / html_dir_rel_to_root
                / f"input4MIPs_files_{mip_era}.html",
                f"input4MIPs {mip_era} files",
                True,
            ),
            (
                datasets_view[datasets_view["mip_era"] == mip_era],
                repo_root_dir
                / html_dir_rel_to_root
                / f"input4MIPs_datasets_{mip_era}.html",
                f"input4MIPs {mip_era} datasets",
                True,
            ),
            (
                source_id_view[source_id_view["mip_era"] == mip_era],
                repo_root_dir
                / html_dir_rel_to_root
                / f"input4MIPs_source-id_{mip_era}.html",
                f"input4MIPs {mip_era} source IDs",
                True,
            ),
        ]
        res_l.extend(entries)

    delivery_summaries = [
        (
            delivery_summary_view,
            page_path,
            "input4MIPs delivery summary",
            False,
        )
        for page_path in (
            repo_root_dir / html_dir_rel_to_root / "input4MIPs_delivery-summary.html",
        )
    ]

    res_l.extend(delivery_summaries)
    res = tuple(res_l)

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
        "<a href='/'>Home</a>",
        "| <a href='input4MIPs_delivery-summary.html'>Delivery summary view</a>",
        "| <a href='input4MIPs_source-id_CMIP7.html'>Source ID-level view CMIP7</a>",
        "| <a href='input4MIPs_datasets_CMIP7.html'>Dataset-level view CMIP7</a>",
        "| <a href='input4MIPs_files_CMIP7.html'>File-level view CMIP7</a>",
        "| <a href='input4MIPs_source-id_CMIP6Plus.html'>Source ID-level view CMIP6Plus</a>",
        "| <a href='input4MIPs_datasets_CMIP6Plus.html'>Dataset-level view CMIP6Plus</a>",
        "| <a href='input4MIPs_files_CMIP6Plus.html'>File-level view CMIP6Plus</a>",
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
