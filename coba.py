import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#t =np.array ([0,2,8,12,20])
#T = np.array ([5,3,10,15,14])
#plt.plot (t,T,'co',label='Data')
#plt.legend()
#plt.show()

#makek nearest
#tmodel = np.linspace(t.min(),t.max(),1000)
#nn_fun = interp1d(t,T,kind='nearest')#kedekatan data interpolasi dengan data kita
#plt.plot(t,T,'co',label='Data')
#plt.plot(tmodel,nn_fun(tmodel),'m-',label='Nearest',ms=10)
#plt.legend()
#plt.show()

#makek linear
#lin_fun = interp1d (t,T,kind='linear')
#plt.plot(tmodel,lin_fun(tmodel),'m-',label='Linear',ms=10)
#plt.legend()
#plt.show()

#makek cubic
#cub_fun = interp1d (t,T,kind='cubic')
#plt.plot(tmodel,cub_fun(tmodel),'m-',label='Cubic',ms=10)
#plt.legend()
#plt.show()

#quad_fun = interp1d (t,T,kind='quadratic')
#plt.plot(tmodel,quad_fun(tmodel),'b-',label='Quadratic',ms=10)
#plt.xlabel('t')
#plt.ylabel('T')
#plt.legend()
#plt.savefig('plott.png',dpi=300,bbox_inches = 'tight')