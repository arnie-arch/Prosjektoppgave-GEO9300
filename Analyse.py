#dette er en testfil
#nå skriver jeg kode her..! 

import pandas as pd

Vannforing = pd.read_csv('62.5.0-Vannføring-dogn-v1.csv', delim_whitespace=True, header=None)

print(Vannforing.head())
