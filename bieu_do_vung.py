import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'C:\\Users\\admin\\Downloads\\austin_weather.xlsx'
df = pd.read_excel(file_path)

# Chọn cột dữ liệu bạn muốn vẽ biểu đồ
x_column = 'TempHighF'
y1_column = 'TempAvgF'
y2_column = 'TempLowF'

# Vẽ biểu đồ vùng
plt.fill_between(df[x_column], df[y1_column], df[y2_column], color='skyblue', alpha=0.4, label='Dữ liệu Y1-Y2')
plt.plot(df[x_column], df[y1_column], label='Dữ liệu Y1', marker='o')
plt.plot(df[x_column], df[y2_column], label='Dữ liệu Y2', marker='o')

plt.legend()
plt.xlabel(x_column)
plt.ylabel('Giá trị')
plt.title('Biểu đồ Vùng')
plt.show()