from io import StringIO
from pathlib import Path

import pandas as pd
import requests

# NASA Exoplanet Archive
URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

QUERY = """
SELECT
    pl_name,
    hostname,
    discoverymethod,
    disc_year,
    pl_orbper,
    pl_rade,
    pl_bmasse,
    pl_eqt,
    st_teff,
    st_rad,
    st_mass
FROM pscomppars
WHERE pl_name IS NOT NULL
"""

params = {
    "query": QUERY,
    "format": "csv"
}

print("Consultando NASA Exoplanet Archive...")

response = requests.get(URL, params=params, timeout=60)
response.raise_for_status()

df = pd.read_csv(StringIO(response.text))

output_path = Path(__file__).resolve().parents[2] / "data" / "raw" / "exoplanets.csv"

df.to_csv(output_path, index=False)

print(f"Dataset guardado en: {output_path}")
print(f"Filas: {len(df)}")
print(f"Columnas: {len(df.columns)}")

print("\nPrimeras filas:")
print(df.head())
print("\nTamaño")
