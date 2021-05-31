import pandas as pd 
import glob
#datos = pd.read_csv('MEA_MAP.csv', header=4)
#nuevo = datos 
#print(nuevo.head())


#df = pd.DataFrame(nuevo)
#df.to_csv('MEA_nuevo.csv', header=True, index=False)


csv_files = glob.glob('*csv')
print(csv_files)

list_data = []

for filename in csv_files:
    data = pd.read_csv(filename, header=4)
    list_data.append(data)

list_data

total = pd.concat(list_data)
total.set_index("Admin Level 1", inplace = True)


#print(total)

#print(total.loc[['Egiptus','Chodaen'],'Admin Level 2':'Link Id'])

mea = total.loc[['Egiptus','Chodaen','Egiptus', 'Liban', 'Oh Man', 'Sanyukt Arab Ameerat', 'Saudo Arabija', 'Seosahara'],'Admin Level 2':'Link Id']

#print(mea)

df = pd.DataFrame(mea)
#print(df)

freq = df.groupby(['Rule Code']).count()
print(freq)

df2 = pd.DataFrame(freq)
df2.to_csv('pruebacount.csv', header=True, index=True)

#df.to_csv('prueba.csv', header=True, index=True)


#df = pd.DataFrame(total)

#df.to_csv('compilado.csv', header=True, index=False)
#df = pd.DataFrame(doc)
#print(df)
#df.to_csv('compilado.csv', header=True, index=False)