# Upper Confidence Bound (UCB)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
N = 10000
d = 10
ads_selected = []
n_selections = [0] * d
sum_rewards = [0] *d
t_reward = 0
for n in range(0,N):
    ad = 0; 
    max_upperbound = 0
    for i in range(0,d):
        if(n_selections[i]>0):
            avg_reward =  sum_rewards[i]/n_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1)/n_selections[i])
            upper_bound = avg_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upperbound:
            max_upperbound = upper_bound
            ad = i;
    ads_selected.append(ad)
    n_selections[ad] = n_selections[ad] + 1
    reward = dataset.values[n, ad]
    sum_rewards[ad] = sum_rewards[ad] + reward
    t_reward = t_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
    
            

