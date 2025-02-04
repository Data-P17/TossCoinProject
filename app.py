import scipy.stats
import streamlit as st
import time
import numpy as np
import pandas as pd

st.header('Tossing a Coin')

chart = st.line_chart([{"Mean": 0.5}])

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    outcome_no = 0
    outcome_1_count = 0
    means = []

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        means.append(mean)
        
        # Convert to DataFrame to properly update chart
        chart.add_rows(pd.DataFrame({"Mean": [mean]}))

        time.sleep(0.05)  # Simulating real-time update

    return mean

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment with {number_of_trials} trials.')
    toss_coin(number_of_trials)
