import re

to_rewrite = """Experiment short name | Experiment description | Anthropogenic Forcing | Volcanic Forcing | Solar Forcing | Start Year | End Year | Main purpose
-- | -- | -- | -- | -- | -- | -- | --
amip | Atmosphere with SSTs   and SICs prescribed | Time-varying | Time-varying | Time-varying | 1979 | 2021 | Evaluation, SST/sea   ice forced variability
piControl and/or   esm-piControl | Coupled   atmosphere-ocean pre-industrial control | All 1850, CO2 prescribed   concentration or zero emissions | Fixed mean radiative   forcing matching historical simulation (i.e. 1850–2021 mean) | Fixed mean value   matching first two solar cycles of the historical simulation (i.e. 1850–1873   mean) | 1 | 400+ | Evaluation, unforced   variability
abrupt- 4xCO2 | CO2   prescribed to 4 times   preindustrial | Same as piControl   except CO2 concentration prescribed to 4 times piControl | Same as piControl | Same as piControl | 1 (branching from   year 101 or later of piControl) | 300+   (1000) | Equilibrium climate   sensitivity, feedback, fast responses
1pctCO2 | CO2 prescribed   to increase at 1% yr-1 | Same as piControl   except CO2 prescribed to increase at 1% yr-1 | Same as   piControl | Same as   piControl | 1 (branching from   year 101 or later of piControl) | 150 | Transient climate   sensitivity
historical and/or esm-hist | Simulation of the   recent past | All time varying, CO2   prescribed concentration or emission | Time   varying | Time   varying | 1850 | 2021 | Evaluation
piClim-Control   (amip) | Preindustrial   conditions including SST and SIC prescribed | All 1850, CO2   prescribed concentration | Same as piControl | Same as piControl | 1 | 30 | Baseline for   model-specific   effective radiative   forcing (ERF)   calculations
piClim-anthro (amip) | As piClim-Control    except present-day anthropogenic forcing | All 2021, CO2   prescribed concentration | Same as piControl | Same as piControl | 1 | 30 | Quantify present-day   total   anthropogenic ERF
piClim-4xCO2 (amip) | As piClim-Control    except CO2 concentrations set to 4 times   preindustrial | All 1850 except CO2   prescribed at 4 times preindustrial concentration | Same as piControl | Same as piControl | 1 | 30 | Quantify ERF of 4 ×   CO2
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
