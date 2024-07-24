"""
Generate html pages from our database
"""

from __future__ import annotations

from pathlib import Path

import json

import pandas as pd

import typer

HTML_DIR = Path(__file__).parents[2] / "docs"
assert HTML_DIR.exists()


def generate_table_rows(
    json_entries: dict[str, str | None],
    columns: tuple[str, ...],
) -> tuple[str, ...]:
    rows_l = []
    for entry in json_entries:
        row_l = ["<tr>"]
        for col in columns:
            row_l.append(f"  <td>{entry[col]}</td>")

        row_l.append("</tr>")

        rows_l.append("\n".join(row_l))

    return tuple(rows_l)


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


def write_json_as_html(
    json_entries: dict[str, str | None],
    page_title: str,
    table_title: str,
    out_file: Path,
    columns: tuple[str, ...],
) -> None:
    table_header_row = head_foot_row(columns, kind="thead")
    table_footer_row = head_foot_row(columns, kind="tfoot")
    table_rows = generate_table_rows(
        json_entries,
        columns,
    )

    header_lines = [
        "<head>",
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>',
        '<meta name="author" content="Paul J. Durack" />',
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
        f"<title>{table_title}</title>",
        "</head>",
    ]

    res_l = [
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
        '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">',
        *header_lines,
        "<body>",
        f"<p><h1>{page_title}</h1><p>",
        # '<table id="table_id" class="display compact" style="width:100%">',
        '<table id="table_id" class="display compact">',
        *[f"  {v}" for v in table_header_row.splitlines()],
        *[f"  {v}" for v in table_footer_row.splitlines()],
        # "  <tbody>",
        *[f"    {v}" for v in "\n".join(table_rows).splitlines()],
        # "  </tbody>",
        "</table>",
        "</body>",
        "</html>",
    ]

    with open(out_file, "w") as fh:
        fh.write("\n".join(res_l))

    print(f"Wrote {out_file}")


def main() -> None:
    """
    Generate html pages from our database
    """
    DB_FILE = (
        Path(__file__).parents[2] / "DatasetsDatabase" / "input4MIPs_datasets.json"
    )

    with open(DB_FILE) as fh:
        db_raw = json.load(fh)

    db = pd.DataFrame(db_raw)

    files_view_front_cols = [
        "tracking_id",
        "mip_era",
        "source_id",
        "variable_id",
        "contact",
        "publication_status",
        "comment_post_publication",
    ]
    files_view_col_order = tuple(
        [
            *files_view_front_cols,
            *[v for v in db.columns if v not in files_view_front_cols],
        ]
    )

    for selection, columns, page_title, table_title, out_file_name in (
        (
            db[db["mip_era"] == "CMIP6Plus"],
            (
                "mip_era",
                "source_id",
                "source_version",
                "institution_id",
                "license_id",
                "dataset_category",
                "realm",
                "variable_id",
                "frequency",
                "time_range",
                "grid_label",
                "target_mip",
                "creation_date",
                "latest",
                "publication_status",
                "contact",
                "further_info_url",
            ),
            "Input4MIPs CMIP6Plus datasets: version info to be added",
            "Input4MIPs CMIP6Plus datasets",
            "input4MIPs_datasets_CMIP6Plus.html",
        ),  # CMIP6Plus datasets
        (
            db[db["mip_era"] == "CMIP6Plus"],
            files_view_col_order,
            "Input4MIPs CMIP6Plus files: version info to be added",
            "Input4MIPs CMIP6Plus all files",
            "input4MIPs_files_CMIP6Plus.html",
        ),  # CMIP6Plus all files
        # Similar logic for all and just CMIP6
    ):
        for_html = selection[list(columns)].drop_duplicates()
        write_json_as_html(
            json_entries=for_html.to_dict(orient="records"),
            page_title=page_title,
            table_title=table_title,
            out_file=HTML_DIR / out_file_name,
            columns=columns,
        )


if __name__ == "__main__":
    typer.run(main)
