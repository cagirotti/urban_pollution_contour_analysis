import pandas as pd
import matplotlib.pyplot as plt


# ======================
# CONFIGURAÇÃO
# ======================

DATASETS = {
    "location_A": {
        "pollution": "data/pm10_A.xlsx",
        "meteorology": "data/met_A.xlsx"
    },
    "location_B": {
        "pollution": "data/pm10_B.xlsx",
        "meteorology": "data/met_B.xlsx"
    },
    "location_C": {
        "pollution": "data/pm10_C.xlsx",
        "meteorology": "data/met_C.xlsx"
    }
}

VARIABLES = [
    ("pm10", "PM10 (µg/m³)", (10, 60)),
    ("vv", "Wind Speed (m/s)", (1, 6)),
    ("camada limite", "BLH (m)", (120, 1380)),
    ("instabilidade", "ASC", (1, 7)),
    ("Temperature (°C)", "Temperature (°C)", (10, 25)),
    ("Precipitation (mm/h)", "Precipitation (mm/h)", (0, 1))
]


# ======================
# FUNÇÕES
# ======================

def load_and_merge(pm_file, met_file):
    df_pm = pd.read_excel(pm_file)
    df_met = pd.read_excel(met_file)

    for df in [df_pm, df_met]:
        df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S')

    df = pd.merge(df_pm, df_met, on=['data', 'hora'], how='inner')

    df['mes'] = pd.to_datetime(df['data']).dt.month
    df['hora_do_dia'] = df['hora'].dt.hour

    return df


def prepare_data(df, column):
    return df.groupby(['mes', 'hora_do_dia'])[column].mean().reset_index()


def plot_contour(ax, df, column, title, vmin, vmax):
    df_prep = prepare_data(df, column)
    pivot_df = df_prep.pivot(index='mes', columns='hora_do_dia', values=column)

    contour = ax.contourf(
        pivot_df.columns,
        pivot_df.index,
        pivot_df,
        cmap='viridis',
        levels=20,
        vmin=vmin,
        vmax=vmax
    )

    ax.set_title(title)
    return contour


# ======================
# PROCESSAMENTO
# ======================

dataframes = {}

for name, files in DATASETS.items():
    dataframes[name] = load_and_merge(files["pollution"], files["meteorology"])


# ======================
# PLOT
# ======================

fig, axs = plt.subplots(len(VARIABLES), len(DATASETS), figsize=(18, 30))

for col_idx, (location, df) in enumerate(dataframes.items()):
    for row_idx, (var, label, scale) in enumerate(VARIABLES):

        ax = axs[row_idx, col_idx]

        contour = plot_contour(
            ax,
            df,
            var,
            f"{label} - {location}",
            scale[0],
            scale[1]
        )

        plt.colorbar(contour, ax=ax)

plt.tight_layout()
plt.savefig('output.png', dpi=300)
plt.show()