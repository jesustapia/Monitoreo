#%%
#Se importan la librerías necesarias e insumen los .CSV
import numpy as np
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import funciones as f
from InputsRevolvente import InputsRevolvente


REAL = pd.read_csv('C:\\Users\\usuario\Desktop\Pricing_BCP\Proyectos\Data_TSN\TSN_Reales.csv')
TEORICO = pd.read_csv('C:\\Users\\usuario\Desktop\Pricing_BCP\Proyectos\Data_TSN\TSN_Inputs.csv')
TMIN = pd.read_csv('C:\\Users\\usuario\Desktop\Pricing_BCP\Proyectos\Data_TSN\TSN_Precios.csv')

#%%
#Se crea el objeto
product = InputsRevolvente(REAL,TEORICO,mincosecha=201801,maxcosecha=201812)
product.df_real

#%%
#Se definen los cortes
cortes = ['C_SUBSEGMENTO']
#Se agrupa en base a los cortes definidos
product.condensar(cortes)
product.curvas

#%%
product.stats

#%%
product.promedios

#%%
product.ci_pd

#%%
product.ci_saldo

#%%
#Se puede ver gráficamente los resultados
product.plotear('pd')
product.plotear('can')
product.plotear('saldo')
product.MAE('pd')
product.MAE('can')
product.MAE('saldo')

#%%
#Se puede optimizar
product.optimizar()
product.curvas

#%%
product.stats

#%%
product.promedios

#%%
#También pueden graficarse
product.plotear('pd',optimo=True)
product.plotear('can',optimo=True)
product.plotear('saldo',optimo=True)
product.MAE('pd',optimo=True)
product.MAE('can',optimo=True)
product.MAE('saldo',optimo=True)

#%%
product.impactoTmin(TMIN,impactoTIR=False)
product.Tmin

#%%
product.TminProm

#%%
product.impactoTmin(TMIN,impactoTIR=True)
product.TIR

#%%
product.TIRProm

# %%
