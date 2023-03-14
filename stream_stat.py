import streamlit as stl
import scipy.stats as st 
import numpy as np 
import matplotlib.pyplot as plt 



stl.write("""
# Hi! You are here beacause you love statistics!

To the right of you there is a sidebar in wich you can choose a particular dictribution to build

Have fun!)
""")
          
stl.sidebar.header('Please, choose a distribution to build')

norm_d = stl.sidebar.checkbox('I want to build a normal distribution!')
expo_d = stl.sidebar.checkbox('I want to build an exponential distribution!')
pois_d = stl.sidebar.checkbox('I`d rather build a Poisson distribution!')

if norm_d:
    stl.write("""
    ## So you`d rather build a normal distribution, eh? 

    Well, to do so, please choose the mathematical expectation (ME) and the standart deviation (Sigma):
    """)

    x = np.linspace(-10, 10, 100)
    mu = stl.slider('Select ME', -10.0, 10.0, 0.0)

    sigma = stl.slider('Select Sigma', 0.0, 3.0, 1.5)


    density_norm = st.norm(mu, sigma).pdf(x)

    fig, ax = plt.subplots()
    ax.plot(x, density_norm)
    stl.pyplot(fig)

if expo_d:

    stl.write("""
    ## Excellent choice! An exponential distribution does know how to be exciting! 

    To build an exponential dictribution, please enter the rate parameter (lambda):
    """)

    lam = stl.slider('Select lambda', 0.0, 10.0)

    x = np.linspace(lam, 10, 100)

    dens_exp = st.expon(lam).pdf(x)

    fig, ax = plt.subplots()
    ax.plot(x, dens_exp)
    stl.pyplot(fig)

if pois_d:

    stl.write("""
    ## No one regrets building Poisson distribution!

    PLease, select the number of times an event happened (k) and the mean number of events (lambda)
    """)

    k = stl.slider('Select k', 0, 100, 50)
    lam = stl.slider('Select lambda', 0.0, 30.0, 0.5)

    mass_poi = st.poisson(lam).pmf(np.arange(k))

    fig, ax = plt.subplots()
    ax.vlines(np.arange(k), [0]*len(mass_poi), mass_poi, label='Probability mass function of Poi')
    stl.pyplot(fig)