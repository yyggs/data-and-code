import pandas as pd
import numpy as np

# 读取50个csv文件
dataframes = [pd.read_csv(f"data_output_{i}.csv") for i in range(1, 51)]

# 合并所有的数据到一个大的DataFrame
all_data = pd.concat(dataframes)

# 为每个chunksize计算平均值和标准误差
mean_time = all_data.groupby('Chunksize')['Time_Loop2'].mean()
std_error = all_data.groupby('Chunksize')['Time_Loop2'].std() / np.sqrt(50)  # 50是文件的数量

# 计算每个chunksize的方差
variance = all_data.groupby('Chunksize')['Time_Loop2'].var()

# 使用1.96作为z值来计算95%的置信区间
confidence_interval = 1.96 * std_error

# 结果存入DataFrame
results = pd.DataFrame({
    'Chunksize': mean_time.index,
    'Mean': mean_time.values,
    'Variance': variance.values,
    'Lower bound': mean_time - confidence_interval,
    'Upper bound': mean_time + confidence_interval
})

# 将结果存储到CSV文件中
results.to_csv("confidence_interval_and_variance.csv", index=False)

