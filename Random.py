# Random Select

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

import random
N=10000
d=10
ads_selected = []
t_reward=0
for i in range(0,N):
    ad = random.randrange(d)
    ads_selected.append(d)
    reward = dataset.values[i,ad]
    t_reward = t_reward + reward

#Visualization
plt.hist(ads_selected)