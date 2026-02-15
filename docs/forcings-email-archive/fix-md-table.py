import re

to_rewrite = """Scenario | Scenario extension | Primary emission or temperature design criteria
-- | -- | --
High (H) | H-ext | Emissions   as high as plausible consistent with climate policy rollback
**High Low (HL)** | HL-ext | High   emissions until second half of the century, followed by rapid decline to net   zero CO2 in 2100
Medium (M) | M-ext | Emissions   consistent with current policies frozen as of 2025
Medium Low   (ML) | ML-ext | Medium   emissions until 2040 followed by gradual decline to net zero CO2 in 2100
Low (L) | L-ext | Emissions   consistent with staying likely below 2C and not returning to 1.5C before end   of the century
Very Low   (VL)   **(Formerly Very Low Low Overshoot;   VLLO)** | VL-ext | Emissions   consistent with limiting warming to 1.5C at the end of the century with   overshoot as low as plausible
Low to   Negative (LN)   **(Formerly Very Low High Overshoot;   VLHO)** | LN-ext | Emissions   consistent with limiting warming to 1.5C at end of the century with high   overshoot compared to the VL scenario.
"""


def remove_double_space(v: str) -> str:
    if "  " not in v:
        return v

    return remove_double_space(v.replace("  ", " ").replace("\t", ""))


grid = []
for line in to_rewrite.split("\n"):
    if not line:
        continue

    start = re.sub(r"\s", " ", line.strip())
    cells = [remove_double_space(v.strip()) for v in start.split("|")]
    grid.append(cells)

col_widths = []
for col in range(len(grid[0])):
    col_values = [grid[row][col] for row in range(len(grid))]
    col_widths.append(max(len(v) for v in col_values))

out_l = []
for row in range(len(grid)):
    if row == 1:
        row_underlines = ["-" * col_widths[col] for col in range(len(col_widths))]
        out_l.append(" | ".join(row_underlines))
        continue

    entries = [grid[row][col].ljust(col_widths[col]) for col in range(len(col_widths))]
    out_l.append(" | ".join(entries))


out = "\n".join(out_l)
print(out)
