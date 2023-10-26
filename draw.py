import matplotlib.pyplot as plt

# 读取文件
with open("threads_data3.txt", 'r') as f:
    lines = f.readlines()
    x = [int(line.split(",")[0].strip()) for line in lines]
    y = [int(line.split(",")[1].strip()) for line in lines]

# 绘制散点图，s参数控制点的大小
plt.scatter(x, y, s=1)  # 设置点的大小为10
plt.xlabel('i')
plt.ylabel('threads[i]')
plt.title('Thread Values vs i')
plt.tight_layout()
plt.savefig('threads_plot_small.png')
plt.show()
