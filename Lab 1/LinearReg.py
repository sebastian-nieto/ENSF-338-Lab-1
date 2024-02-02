import json
import time                                              
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the file
with open('C:\\Users\\joeki\\Documents\\ENSF 338\\Lab1\\ENSF-338-Lab-1\\Lab 1\\large-file.json', 'r',encoding ="UTF-8") as file:
    data = json.load(file)

total_time1 = 0
total_time2 = 0
total_time3 = 0
total_time4 = 0
avgtimes = [0] * (4 * 100)
listlengths = [1000, 2000, 5000, 10000]


for i in range(100):
    j = 0
    start_time1 = time.time()
    start_time2 = time.time()
    start_time3 = time.time()
    start_time4 = time.time()

    for record in data:
        j+=1
        if j == 1000:
           end_time1 = time.time()
        if j == 2000:
           end_time2 = time.time()
        if j == 5000:
           end_time3 = time.time()
        if j == 10000:
           end_time4 = time.time()
    avgtimes[(4*i)] = end_time1 - start_time1
    avgtimes[(4*i)+1] = end_time2 - start_time2
    avgtimes[(4*i)+2] = end_time3 - start_time3
    avgtimes[(4*i)+3] = end_time4 - start_time4

    
    total_time1 += end_time1 - start_time1
    total_time2 += end_time2 - start_time2
    total_time3 += end_time3 - start_time3
    total_time4 += end_time4 - start_time4


average_time1 = total_time1 / 100
average_time2 = total_time2 / 100
average_time3 = total_time3 / 100
average_time4 = total_time4 / 100
super_average = (total_time1 + total_time2 + total_time4 + total_time3)/4



# Now, compute linear regression to find the slope and intercept of the line
# that most accurately describes the relationship between input length and time.
# Then, plot the data and the line.
slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths, linevalues, 'r')