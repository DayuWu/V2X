# import package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 时间加速度图
df1 = pd.read_csv("data1.csv")

# 添加1s时间戳
df1["TIME_1s"]=pd.date_range(start='2016-11-11 19:50', periods=len(df1),freq="S")
df1.set_index("TIME_1s")

df1.plot(x="TIME_1s",y="LONGACC",title='my plot')
plt.title("Time and Acc")
# my_x_ticks =  设置x轴标签
# plt.xticks(my_x_ticks)
plt.xticks([])

# 前后时刻的图
# diff_Acc = df1["LONGACC"][1:len(df1)]-df1["LONGACC"][0:(len(df1)-1)]
speed_1 =  df1["SPEED"][1:len(df1)]
speed_1
plt.plot(df1["SPEED"][0:(len(df1)-1)],speed_1)
