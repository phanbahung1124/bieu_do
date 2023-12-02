import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\admin\\Downloads\\austin_weather.xlsx'
df = pd.read_excel(file_path)

def ve_bieu_do_banh(data, column_name):
    data_counts = data[column_name].value_counts()
    labels = data_counts.index
    sizes = data_counts.values

    plt.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.show()

column_name = 'TempHighF'
ve_bieu_do_banh(df, column_name)