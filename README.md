# Introduction: V2X
V2X means Vehicle-to-Everything, which is a promising technology closely related to Internet of Things (IoT). 

# Description: 
This repo collects data, codes and other files of a V2X data analysis project by Dayu and Xiaolong.

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
