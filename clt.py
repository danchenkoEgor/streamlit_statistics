import streamlit as stl
import scipy.stats as st 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import poisson

stl.write("""# Central Limit Theorem visualization for normal, exponential and Poisson distribution""")

stl.header("Choose initial distribution")
norm_d = stl.checkbox('Normal distribution')
expo_d = stl.checkbox('Exponential distribution')
pois_d = stl.checkbox('Poisson distribution')


if norm_d:
    distribution = st.norm(0, 1).rvs(size = 1000)
    mean, var, _, _ = norm.stats(moments = 'mvsk')
    fig1, ax1 = plt.subplots()
    sns.distplot(distribution)
    stl.pyplot(fig1)

if expo_d:
    distribution = st.expon.rvs(size = 1000)
    mean, var, _, _ = expon.stats(moments = 'mvsk')
    fig1, ax1 = plt.subplots()
    sns.distplot(distribution)
    stl.pyplot(fig1)

if pois_d:
    mu = stl.slider('Select mu value', 0.0, 1.0, 0.5)
    distribution = st.poisson(mu).rvs(size = 1000)
    mean, var, _, _ = poisson.stats(mu, moments = 'mvsk')
    fig1, ax1 = plt.subplots()
    sns.distplot(distribution)
    stl.pyplot(fig1)


stl.write("""## Now, behold the great Central Limit Theorem!""")


n = stl.slider('Select the number of samples', 1, 100, 50)
m = stl.slider('Select the size of a sample', 1, 100, 50)

samp_means = []
for i in range(n):
    sample = np.random.choice(distribution, size = m)
    samp_means.append(sample.mean())

samp_means = np.array(samp_means)


fig, ax = plt.subplots()
ax.axvline(x = mean, color = 'r')
ax.hist(samp_means)
ax.axvline(x = samp_means.mean(), color = 'g')
stl.pyplot(fig)

stl.write("Absolute difference between the Statistical Population True Mean and Samples Mean:", abs(mean - samp_means.mean()*1000),
          "Standart Deviation of Samples", samp_means.std())


stl.write(""" * Чем больше размер выборки, тем меньше дисперсия выборочного среднего
* Чем больше выборка, тем ближе значения расположены к мат. ожиданию генеральной совокупности
* При достаточном количестве выборок И при достаточно большом их размере, любое распределение 
приближается по форме к нормальному""")