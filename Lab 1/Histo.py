import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_json("C:\\Users\\joeki\\Documents\\ENSF 338\\Lab1\\ENSF-338-Lab-1\\Lab 1\\songdata.json")


below = df[df['loudness'] < -8]
notbelow = df[df['loudness'] >= -8]

plt.hist(below['tempo'], color='red', alpha=1, label='Below -8',edgecolor='black', linewidth=0.5)
plt.title('Tempo for Songs below -8 Loudness')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.legend()

plt.savefig('hist1.png')
plt.clf() 


plt.hist(notbelow['tempo'], color='blue', alpha=1, label='At or Above -8',edgecolor='black', linewidth=0.5)
plt.title('Tempo for Songs at or above -8 Loudness')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.legend()

plt.savefig('hist2.png')
plt.clf()

