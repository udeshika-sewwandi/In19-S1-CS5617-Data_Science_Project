#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import scipy.stats as st
import scipy.special as sp
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

df = pd.read_csv('Normalized_Prod_Dept_data.csv', parse_dates=True, index_col=0, sep=',')
df

df['Total Production'].corr(df['Total labourers'])

df.corr()

corr, p = pearsonr(df['Total Production Average(previous year & current year)'], df['Total labourers'])
corr, p

dof = 23      
alpha = 0.05    
ntails = 2

tcrit = abs(st.t.ppf(alpha/ntails, dof))
tcrit

mu = 0
variance = 1
sigma = math.sqrt(variance)
xs = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.plot(xs, st.t.pdf(xs,dof), 'k', label="T-Distribution PDF")
plt.vlines([-tcrit, tcrit], 0.0, st.t.pdf(tcrit,dof), colors='b', linestyles='solid', label='')

# two tail test
plt.fill_between(xs, st.t.pdf(xs,dof),where = xs <=-tcrit, color='red')
plt.fill_between(xs, st.t.pdf(xs,dof),where = xs >=tcrit, color='red')
plt.show()

plt.plot(xs, st.t.pdf(xs,dof))
plt.fill_between(xs,st.t.pdf(xs,dof),where = xs <=-1.925, color='lightgrey')
plt.fill_between(xs,st.t.pdf(xs,dof),where = xs >=1.925, color='lightgrey')
plt.show()