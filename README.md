#实用统计软件大作业

吴大宇 PB19030934， 金小龙 PB19000314 

### 选题动机

车联网是近年来万物互联领域非常热的方向，是以车内网、车际网和车载移动互联网为基础，按照约定的通信协议和数据交互标准，在车-、路、行人及互联网之间，进行无线通讯和信息交换的系统网络，是能够实现智能化交通管理、智能动态信息服务和车辆智能化控制的一体化网络。

在未来的应用场景中，基于车载传感器和计算设备，汽车终端和信息计算中心共同收集分析交通、天气、路况、周边设施等信息，并提供实时的反应和决策。比如，当前方路堵，周围一个小范围内车辆的速度均变低那么车子就可以将实时路况数据发送至车联网；通过车辆传感器检测事故，事故车辆首先发送安全提醒信息，其次连接交警、保险公司等相关机构进行报备处理，同时周围车辆可暂时存储事故图像备查；如果司机经常采用较危险的驾驶方式，通过车载传感器的数据分析，使用车载智能音箱进行提醒，最后为司机建立驾驶习惯画像；为城市交通提供大数据支持的优化建议，合理规划停车点位和行车路线。

因此我们决定对于数据集中的6.车联网数据和商业价值和13. 基于车联网数据的驾驶行为分析数据进行分析，希望得到有意思的结论。除此之外，在数据分析的过程中，我们对经纬度相关的城市交通数据非常感兴趣，但老师的数据集中经纬度数据不全面，所以我们使用了共享单车的公开数据集进行分析（包括上海和华盛顿地区的共享单车）

同时，我们希望可以利用python和R语言不同的特性来分析数据，因此金小龙使用python进行分析，吴大宇使用R进行分析。

项目报告使用英文书写，相关的代码、数据集和修改讨论历史可以在 https://github.com/DayuWu/V2X 中找到。

如果您对我们的代码、分析结果有任何问题欢迎联系我们！

吴大宇email: wdyknight@mail.ustc.edu.cn

金小龙email: jinxiaolong@mail.ustc.edu.cn

### 分工

| 金小龙                                                       | 吴大宇                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 车联网数据和商业价值数据的基础分析和经纬度相关地图绘制       | 车联网数据和商业价值数据的预测，分类等统计模型挖掘结论       |
| 基于车联网数据的驾驶行为分析数据进行分析的基础分析和驾驶行为分析 | 基于车联网数据的驾驶行为分析数据进行分析的聚类和数据高阶分析 |
| 上海摩拜单车数据集的分析和提出关于停车点的意见                   | 关于华盛顿共享单车订单量的解释和分析                                                            |
| 使用python进行分析                                           | 使用R进行分析                                                |



### 项目简要介绍

文件夹Project_Jxl：金小龙所负责的项目部分

文件夹Project_Wdy：吴大宇所负责的项目部分

Project1：车联网数据和商业价值数据

Project2：基于车联网数据的驾驶行为分析

Project3：共享单车单车数据集分析

其中html文件为分析结果


#data1案例背景
车联网数据，简单而言，就是由车载设备记录的车辆相关数据：包括实时的驾驶速度、加速度、油耗、发动机转速等。通过对车联网数据的统计分析，可以为保险公司、汽车制造商以及驾驶司机带来一定的价值。更多案例背景介绍，可以参考初识车联网。

#data1数据介绍
案例数据提供了一段路程的车联网数据，每一列分别对应：
时间（TIME）
经度（LONG）
纬度（LAT）
油耗（CONSUM）
加速度（LONGACC）
速度（SPEED）
发动机转速（WHEEL）
以及累积行驶里程（CUMDIS）等。
数据的采集频率是秒（经纬度的采集频率是15秒）。

#data2案例背景
  改革开放以来，我国道路交通行业持续发展，汽车保有量不断增加。截止到2017年年底，我国汽车年销量已连续八年排名世界第一。目前，我国汽车保有量达到2亿台、占全球20%，汽车年销量占全球30%。
  道路交通行业迅速发展的同时，道路交通事故也时有发生：2013-2015年，全国汽车交通事故死亡人数分别为42927、42837和42388人。据统计，超过70%的道路交通事故是由驾车人的不良驾驶行为造成的。
  近年来，随着车联网技术的快速发展，人们可以对驾驶员的驾驶行为进行统计分析——包括驾驶习惯分析、驾驶人驾车行为画像，同时也可以对驾驶员的不良驾驶行为进行预警。

#data2数据介绍
本案例所用数据来源于某网站，共包含8辆车信息，分为754段路程
行驶过程中，数据是以每秒戒者每15秒进行记录的；两条数据间隔15分钟以上，视作一段新的路程。
数据共包含14个指标(均为连续型)，分成5个维度：时间维度、速度维度、里程维度、机械维度、驾驶平稳性
时间维度：行驶时长、疲劳驾驶时长、早晚高峰、深夜出行
平均时速、最大时速、速度标准差、极度拥堵、高速行驶
里程维度：行驶里程
机械性能：平均引擎转速、最大引擎转速、引擎转速标准差
驾驶平稳性：平稳性

# Introduction: V2X
V2X means Vehicle-to-Everything, which is a promising technology closely related to Internet of Things (IoT). 

# Description: 
This repo collects data, codes and other files of a V2X data analysis project by Dayu Wu and Xiaolong Jing.

# Data1: a drive
Includes time, longitude, latitude, consumption, acceleration, speed, wheel and cumulated distance.

TIME,LONG,LAT,CONSUM,LONGACC,SPEED,WHEEL,CUMDIS

Longitude and latitude are collected every 15 seconds, while others are collected on a second basis.

# Data2: driving behavior
Includes data from 754 drives of 8 cars. (Data with an interval of 15 min or longer is regarded as a new drive.)

DIST, DRVTIME, SPEED_AVG, SPEED_SD, SPEED_MAX, STAB, WHEEL_AVG, WHEEL_SD, WHEEL_MAX, RUSHOUR, NIGHT, JAM, HIGHSPEED, TIRED, NUM

These 14 items are divided into 5 dimensions:
1. Time: DRVTIME, RUSHOUR, NIGHT, TIRED
2. Speed: SPEED_AVG, SPEED_SD, SPEED_MAX, JAM, HIGHSPEED
3. Distance: DIST
4. Car: WHEEL_AVG, WHEEL_SD, WHEEL_MAX
5. Driving: STAB
