import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 两组数据：
data1 = np.random.rand(10, 50) # 具有10 x 50维度的随机数组A
data2 = np.random.rand(10, 50) # 具有10 x 50维度的随机数组B

# 添加时间维度 (即：把两组数据连接在一起)
data = np.concatenate((data1, data2), axis=1)


fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    current_data = data[:, frame]
    ax.bar(range(len(current_data)), current_data)


ani = FuncAnimation(fig, update, frames=data.shape[1], interval=100)

# 显示动画：
plt.show()

# 或者将动画保存为GIF或MP4文件：
ani.save('animation.gif', writer='imagemagick', fps=15)
ani.save('animation.mp4', writer='ffmpeg', fps=15)
