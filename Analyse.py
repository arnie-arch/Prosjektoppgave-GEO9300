#Libraries
import pandas as pd
import matplotlib.pyplot as plt

vf = pd.read_csv('62.5.0-Vannføring-dogn-v1.csv', delimiter=';', on_bad_lines='skip', skiprows=[0])

print(vf.head())

#vf1 = Data fra 1991 - 2020
#vf2 = Data fra 1961 - 1990

vf1 = vf[(vf['Tidspunkt'] >= '1991-01-01') & (vf['Tidspunkt'] <= '2020-12-31')]
print(vf1.head())
vf2 = vf[(vf['Tidspunkt'] >= '1961-01-01') & (vf['Tidspunkt'] <= '1990-12-31')]
print(vf2.tail())

plt.plot(vf1['Tidspunkt'], vf1['Vannføring'], label='1991-2020')