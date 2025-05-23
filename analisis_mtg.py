
import pandas as pd
import matplotlib.pyplot as mplib

# Cargar el dataset
df = pd.read_csv("MTG-OTJ-draft-card-ratings-2024-05-25.csv")

# Conversion de columnas
df["GP WR"] = df["GP WR"].str.replace('%', '').astype(float)
df["IWD"] = df["IWD"].str.replace('pp', '').astype(float)
df["ALSA"] = pd.to_numeric(df["ALSA"], errors='coerce')

# Top 10 por Win Rate
top_gp_wr = df.sort_values(by="GP WR", ascending=False).head(10)[["Name", "GP WR", "Color", "Rarity"]]

# Top 10 por Impacto
top_iwd = df.sort_values(by="IWD", ascending=False).head(10)[["Name", "IWD", "Color", "Rarity"]]

# Grafico ALSA vs GP WR
mplib.figure(figsize=(8, 5))
mplib.scatter(df["ALSA"], df["GP WR"], alpha=0.6)
mplib.xlabel("ALSA (posición promedio en el pick)")
mplib.ylabel("Game Played Win Rate (%)")
mplib.title("Relación entre ALSA y GP WR")
mplib.grid(True)
mplib.tight_layout()
mplib.savefig("mtg_wr_vs_alsa.png")
mplib.close()

# Exportar a Excel
with pd.ExcelWriter("mtg_analisis.xlsx", engine="xlsxwriter") as writer:
    top_gp_wr.to_excel(writer, sheet_name="Top GP WR", index=False)
    top_iwd.to_excel(writer, sheet_name="Top IWD", index=False)
    df.to_excel(writer, sheet_name="Dataset Completo", index=False)
