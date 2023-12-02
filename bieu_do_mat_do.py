import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'C:\\Users\\admin\\Downloads\\austin_weather.xlsx'
df = pd.read_excel(file_path)

# Chọn cột dữ liệu bạn muốn vẽ biểu đồ mật độ
selected_column = 'TempHighF'

# Vẽ biểu đồ mật độ
sns.kdeplot(df[selected_column], shade=True)
plt.xlabel(selected_column)
plt.ylabel('Mật độ')
plt.title('Biểu đồ Mật độ')
plt.show()

