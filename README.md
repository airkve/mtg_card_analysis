
# Análisis de Cartas de Magic the Gathering – Draft OTJ 2024

Este proyecto analiza el rendimiento y la popularidad de cartas del set *Outlaws of Thunder Junction* en formatos de draft, utilizando datos reales recolectados por la comunidad. Es parte de un portafolio personal para demostrar habilidades de análisis de datos aplicadas a un interés personal.

## Objetivos

- Identificar las cartas más efectivas según su porcentaje de victoria en partidas (`GP WR`).
- Evaluar el impacto real de las cartas al incluirlas en el mazo (`IWD`).
- Visualizar la relación entre popularidad (`ALSA`) y efectividad (`GP WR`).
- Exportar un reporte consolidado en Excel con métricas clave.

## Dataset

- Fuente: [17lands.com](https://www.17lands.com)
- Archivo: `MTG-OTJ-draft-card-ratings-2024-05-25.csv`
- Total de cartas: 376
- Columnas clave:
  - `ALSA`: posición promedio en la que se elige la carta en el draft.
  - `GP WR`: porcentaje de victorias en partidas donde se jugó.
  - `IWD`: diferencia de win rate cuando la carta está en el mazo vs cuando no.

## Tecnologías Utilizadas

- **Python**: procesamiento de datos
- **pandas**: manipulación y agrupamiento
- **matplotlib**: visualización
- **xlsxwriter**: generación de archivos Excel

## Resultados Generados

- `mtg_analisis.xlsx`: archivo con tres hojas:
  - Top 10 cartas por `GP WR`
  - Top 10 cartas por `IWD`
  - Dataset completo
- `mtg_wr_vs_alsa.png`: gráfico de dispersión mostrando la relación entre `ALSA` y `GP WR`

## Cómo Ejecutar

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install pandas matplotlib xlsxwriter
```

2. Coloca el archivo CSV original en el mismo directorio del script.

3. Ejecuta el script:
```bash
python analisis_mtg.py
```

4. Revisa los archivos generados:
   - `mtg_analisis.xlsx`
   - `mtg_wr_vs_alsa.png`

## Autor

**Richard Jiménez**  
Especialista en IT
