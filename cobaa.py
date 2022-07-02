import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
import pandas as pd
df = pd.read_csv("mydata.csv",delimiter="\t")
#print(df)
#plt.plot(df['Distance'],df['bridge'], 'ko', label='Bridge')
#plt.plot(df['Distance'],df['long-bridge'], 'x', label='Long-Bridge')
#plt.plot(df['Distance'],df['hollow'], '+', label='Hollow')
#plt.plot(df['Distance'],df['top'], '*', label='Top')

#plt.xlabel('Distance / Å')
#plt.ylabel('Interaction Energy / eV')
#plt.legend()
#plt.show()
tmod = np.linspace(df['Distance'].min(),df['Distance'].max(),10000)
lin_bri = interp1d(df['Distance'], df['bridge'],kind='cubic')
cs_bri = CubicSpline(df['Distance'], df['bridge'],bc_type='natural') #natural tipe menyelesaikan algoritmanya defaultnya natural
plt.plot(df['Distance'],df['bridge'], 'ko', label='Bridge')
plt.plot(tmod, lin_bri(tmod),'r-',label='Lin_Cubic',ms=1)
plt.plot(tmod, cs_bri(tmod),'b-',label='CSpline_Natural',ms=1)

plt.xlabel('Distance / Å')
plt.ylabel('Interaction Energy / eV')
plt.legend()
plt.show()