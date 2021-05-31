import pandas as pd 
#mandar a llamar archivo y ver la info de sus columnas 
datos = pd.read_csv('Data.csv')
print(datos.info())
#mandar a llamar únicamente los primeros 5 registros 
print(datos.head())
#mandar a llamar rango de filas 
print(datos.iloc[0:5])
#renglones salteados 
print(datos.iloc[[0,3,6,8],])
#rangos columnas 
print(datos.iloc[:,0:2])
#columnas y filas 
print(datos.iloc[[0,3,6,9], [0,1,2,3,4]])
#rangos de columnas y filas 
print(datos.iloc[0:5, 5:8])

