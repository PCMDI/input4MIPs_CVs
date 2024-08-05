"""
Generation of our HTML pages

This may be a temporary home, but is fine for now
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

import packaging.version
import pandas as pd


def get_url_esgf(row: pd.Series, search_facets: Iterable[str]) -> str:
    publication_status: str = row["publication_status"]

    if publication_status == "registered":
        publication_text = "Registered"
        res = "<a href='https://github.com/PCMDI/input4MIPs_CVs/blob/main/CVs/input4MIPs_source_id.json' target='_blank'>Registered in CVs</a>"
        return res

    if publication_status == "abandoned":
        return "Abandoned: the dataset was registered but never produced"

    if publication_status == "in_publishing_queue":
        return "In publishing queue"

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


def get_esgf_urls(df: pd.DataFrame, search_facets: Iterable[str]) -> pd.Series:
    urls = df.apply(
        get_url_esgf,
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
        "publication_status",
        "comment_post_publication",
        "source_id",
        "contact",
        "sha256",
    ),
) -> pd.DataFrame:
    col_order = tuple(
        [
            *view_front_cols,
            *sorted([v for v in db.columns if v not in view_front_cols]),
        ]
    )

    res = db[list(col_order)].drop_duplicates()
    urls = get_esgf_urls(
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
        "publication_status",
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
        "latest",
        "further_info_url",
    ),
) -> pd.DataFrame:
    col_order = tuple(
        [
            *view_front_cols,
            *sorted(view_other_cols),
        ]
    )

    res = db[list(col_order)].drop_duplicates()
    urls = get_esgf_urls(
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


def get_db_views_to_write(
    repo_root_dir: Path,
    db_file_path_rel_to_root: Path = Path("Database")
    / "input4MIPs_db_file_entries.json",
    html_dir_rel_to_root: Path = Path("docs"),
) -> tuple[tuple[pd.DataFrame, Path, str], ...]:
    db_file = repo_root_dir / db_file_path_rel_to_root

    with open(db_file) as fh:
        db_raw = json.load(fh)

    db = pd.DataFrame(db_raw)

    files_view = get_files_view(db)
    datasets_view = get_datasets_view(db)

    # Hard-code filenames for now
    res = (
        (
            files_view[files_view["mip_era"] == "CMIP6Plus"],
            repo_root_dir / html_dir_rel_to_root / "input4MIPs_files_CMIP6Plus.html",
            "Input4MIPs CMIP6Plus files",
        ),
        (
            datasets_view[datasets_view["mip_era"] == "CMIP6Plus"],
            repo_root_dir / html_dir_rel_to_root / "input4MIPs_datasets_CMIP6Plus.html",
            "Input4MIPs CMIP6Plus datasets",
        ),
    )

    return res


def head_foot_row(columns: tuple[str, ...], kind: str = "thead") -> str:
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
    ),
) -> None:
    # Little bit of special sorting,
    # so that the initial view of the table makes a bit more sense
    db_view_tmp = db_view.sort_values(by=db_view.columns.tolist()).copy()
    db_view_sorted_l = []
    for publication_status in publication_status_display_order:
        db_view_sorted_l.append(
            db_view_tmp[db_view_tmp["publication_status"] == publication_status]
        )

    db_view_sorted = pd.concat(db_view_sorted_l)
    db_view_sorted = db_view_sorted.reset_index(drop=True)
    db_view_sorted.index.name = "default_sort_index"
    db_view_sorted = db_view_sorted.reset_index()

    columns = list(db_view_sorted.columns)
    table_header_row = head_foot_row(columns, kind="thead")
    table_footer_row = head_foot_row(columns, kind="tfoot")
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
        "    $('#table_id').DataTable();",
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
        # '<table id="table_id" class="display compact" style="width:100%">',
        '<table id="table_id" class="display compact">',
        *[f"  {v}" for v in table_header_row.splitlines()],
        *[f"  {v}" for v in table_footer_row.splitlines()],
        *[f"    {v}" for v in "\n".join(table_rows).splitlines()],
        "</table>",
        "</body>",
        "</html>",
    ]

    with open(file_to_write, "w") as fh:
        fh.write("\n".join(res_l))


def generate_html_pages(
    version: packaging.version.Version, repo_root_dir: Path
) -> None:
    # Get db views to write
    db_views = get_db_views_to_write(repo_root_dir=repo_root_dir)

    for df, write_file, page_title in db_views:
        write_db_view_as_html(
            db_view=df,
            file_to_write=write_file,
            page_title=page_title,
            version=version,
        )
