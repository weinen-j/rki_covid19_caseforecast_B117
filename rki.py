# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:05:09 2021

@author: Jonas
"""

from io import StringIO
import pandas as pd
import requests

# get rki data and read to df
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"}
URL = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/Nowcasting_Zahlen_csv.csv?__blob=publicationFile"

s = requests.get(URL, headers=headers).text
df = pd.read_csv(StringIO(s), sep=";", index_col=0)

# df.columns = ["Datum", "Schätzer_Neuerkrankungen", "UG_PI_Neuerkrankungen", "OG_PI_Neuerkrankungen", "Schätzer_Neuerkrankungen_ma4", "UG_PI_Neuerkrankungen_ma4", "OG_PI_Neuerkrankungen_ma4", "Schätzer_Reproduktionszahl_R", "UG_PI_Reproduktionszahl_R", "OG_PI_Reproduktionszahl_R", "Schätzer_7_Tage_R_Wert", "UG_PI_7_Tage_R_Wert", "OG_PI_7_Tage_R_Wert"]

# export to csv
# df.to_csv()
