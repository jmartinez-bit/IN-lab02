import pandas as pd
import numpy as np


def ex_1a():
    data_index = pd.Series(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
                           index=[1, 2, 3, 4, 5, 6])
    print(data_index)


def ex_1b():
    data2 = pd.Series({'Enero': 4000, 'Febrero': 3000, 'Marzo': 5000})
    print(data2)


def ex_1c():
    data3 = pd.Series(np.random.rand(10))
    print("Números aleatorios", data3)
    print("Primeros 5: ", data3.head())
    print("Ultimos 5: ", data3.tail())
    print("Primeros 2: ", data3.head(2))
    print("Ultimos 2: ", data3.tail(2))


def ex_2a():
    ventas = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
              'Monto': [50000, 45000, 43000, 70000, 56000, 45000]}
    data = pd.DataFrame(ventas)
    print(data)


def ex_2b():
    ventas = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
              'Monto': [50000, 45000, 43000, 70000, 56000, 45000]}
    data2 = pd.DataFrame(ventas, columns=['Monto', 'Meses'])
    print(data2)


def ex_3():
    archivo = pd.read_csv('Ventas.csv', sep=';')
    data = pd.DataFrame(archivo)
    print(archivo)


def ex_4():
    ventas1 = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
               'Monto': [50000, 45000, 43000, 70000, 56000, 45000]}

    ventas2 = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
               'Monto': [60000, 55000, 40000, 80000, 60000, 45000]}

    data1 = pd.DataFrame(ventas1)
    data2 = pd.DataFrame(ventas2)
    data_fin = data1.add(data2)
    print(data_fin)


def ex_5a():
    data = pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],
                                  [40000, 35000, 50000],
                                  [55000, 60000, 45000],
                                  [65000, 70000, 56000]
                                  ]))
    print(data)


def ex_5b():
    data = pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],
                                  [40000, 35000, 50000],
                                  [55000, 60000, 45000],
                                  [65000, 70000, 56000]
                                  ]))
    print('Numero de registros y campos: ', data.shape)


def ex_5c():
    data2 = pd.DataFrame(np.array([
        [40000, 35000, 50000],
        [55000, 60000, 45000],
        [65000, 70000, 56000]
    ]))
    print('Media: ', data2.mean())
    print('Correlacion: ', data2.corr())
    print('Mas bajo: ', data2.min())
    print('Mas alto: ', data2.max())
    print('Mediana: ', data2.median())
    print('Desviación estandar: ', data2.std())
    print('Primera columna', data2[0])
    print('Dos primeras columnas: ', data2[[0, 1]])
    print('Primera fila: ', data2.loc[0])


def ex_6():
    archivo = pd.read_excel('Ventas02.xlsx', sheet_name='Ventas', skiprows=1)
    data = pd.DataFrame(archivo)
    print(data)


if __name__ == '__main__':
    ex_6()

