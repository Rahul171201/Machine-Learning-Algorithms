# -*- coding: utf-8 -*-
"""K-Nearest-Neighbours.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v1-ZyalQcj7cBtANJFAgoGaLhNWh3B_B
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = pd.read_csv('iris.data')
df = pd.DataFrame(data)
df = df.sample(frac=1)
print(df)

data = df.to_numpy()
# print(data)
training = []
test = []
for i in range(100):
  training.append(data[i])
for i in range(100,150):
  test.append(data[i])

print(len(training))

# for each test sample we predict the species

k_final = 0
accu = 0.00
for k in range(1,10):
  temp_species = []
  for i in range(len(test)):
    dis = 0.00
    arr = []
    for j in range(len(training)):
      dis = (training[j][0]-test[i][0])*(training[j][0]-test[i][0])+(training[j][1]-test[i][1])*(training[j][1]-test[i][1])+(training[j][2]-test[i][2])*(training[j][2]-test[i][2])+(training[j][3]-test[i][3])*(training[j][3]-test[i][3])
      dis = math.sqrt(dis)
      arr.append((dis, training[j][4]))
    arr.sort()
    c_map = {}
    for x in range(k):
      if arr[k][1] in c_map:
        c_map[arr[k][1]] = c_map[arr[k][1]]+1
      else:
        c_map[arr[k][1]] = 1
    maxi = -1
    specs = "op"
    for it in c_map:
      if (c_map[it] > maxi):
        maxi = c_map
        specs = it
    temp_species.append(specs)
  ans = 0
  for i in range(len(test)):
    # print(test[i][4])
    if(temp_species[i] == test[i][4]):
      ans = ans + 1
  ac = (float(float(ans)/float(50.00)))*(float(100.00))
  # print(ans)
  if(ac>accu):
    accu = ac
    k_final = k
  print(ac)
print(k_final)