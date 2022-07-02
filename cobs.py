import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mydata.csv",delimiter = "\t")
print (df)
plt.plot(df['Distance'],df['bridge'], 'ko', label='Bridge')
plt.plot(df['Distance'],df['long-bridge'], 'x', label='Long-Bridge')
plt.plot(df['Distance'],df['hollow'], '+', label='Hollow')
plt.plot(df['Distance'],df['top'], '*', label='Top')

plt.xlabel('Distance / Å')
plt.ylabel('Interaction Energy / eV')
plt.legend()
plt.show()