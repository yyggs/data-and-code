import pandas as pd

# 用于保存各个CSV文件的数据的列表
data_list = []

# 从每个CSV文件中读取数据并将其添加到data_list中
for i in range(11, 21):
    filepath = f"data_output_{i}.csv"
    data = pd.read_csv(filepath)
    data_list.append(data)

# 使用第一个CSV文件的数据初始化average_data
average_data = data_list[0].copy()

# 遍历其余的CSV文件数据，并将其值添加到average_data中
for data in data_list[1:]:
    average_data['Time_Loop1'] += data['Time_Loop1']
    average_data['Time_Loop2'] += data['Time_Loop2']

# 将总和除以文件数量，以计算平均值
average_data['Time_Loop1'] = (average_data['Time_Loop1'] / len(data_list)).round(6)
average_data['Time_Loop2'] = (average_data['Time_Loop2'] / len(data_list)).round(6)

# 将平均值保存到新的CSV文件中
average_data.to_csv('average_output16.csv', index=False)

print("Results saved to average_output.csv")
