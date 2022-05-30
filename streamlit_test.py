import streamlit as st
import numpy as np
import pandas as pd

st.title('Pool Chemical Calculations')

house = st.radio('House',('Mystic Summit','APH'))

if house == 'Mystic Summit':
    pool_volume = 16250
else:
    pool_volume = 10884

st.header('Chlorine')

free_chlorine = st.slider('Free Chlorine (ppm)', min_value=0.0, max_value=10.0, value=3.0, step=0.5)
total_chlorine = st.slider('Total Chlorine (ppm)', min_value=0.0, max_value=10.0, value=3.0, step=0.5)
combined_chlorine = total_chlorine - free_chlorine

# if total_chlorine < 1 or free_chlorine < 1:
#     st.text('RESULT: Chlorine too low.')
# if total_chlorine > 5 or free_chlorine > 5:
#     st.text('RESULT: Chlorine too high.')

chart_data = pd.DataFrame(
     [[free_chlorine,combined_chlorine,0],[0,0,total_chlorine]],
     columns=["Free", "Combined", "Total"])

diff_free_combined = free_chlorine - combined_chlorine


if diff_free_combined > 0:
    st.text('RESULT: Sanitizing')
    if combined_chlorine != 0:
        ratio_free_combined = free_chlorine / combined_chlorine
        st.text(f'RESULT: Ratio of free to combined: {ratio_free_combined:1.1f}.  Ideally 10.')
    else:
        st.text(f'RESULT: Ratio of free to combined: INFINITE.')
        st.text(f'NOTE: Ideally 10.')
else:
    st.text('RESULT: NOT Sanitizing')

st.bar_chart(chart_data)

st.header('Acidity')

pH = st.slider('pH', min_value=6.0, max_value=9.0, value=7.0, step=0.1)

if pH > 7.6:
    st.text('RESULT: Perform Acid Demand Test')
    acid_drops = st.slider('Acid Demand Drops',min_value=0, max_value=10, value=2, step=1)
    if acid_drops == 0:
        st.text('RESULT: Acid Demand: N/A')
    else:
        demand = 0.00092 * pool_volume * acid_drops
        st.text(f'RESULT: Acid Demand: {demand:1.1f} ounces')
else:
    st.text('RESULT: Acid Demand Test Not Required')

st.header('Alkalinity')

test_type = st.radio('Test Type',('Reagent','Test Strips'))

if test_type == 'Reagent':
    alk = st.slider('Alkalinity (drops)', min_value=0, max_value=10, value=10, step=1)
    alk_to_add = (0.00022/16)*(100-10*alk)*pool_volume
    alk_to_add_cups = alk_to_add * 2
    st.text(f'RESULT: Baking Soda to Add: {alk_to_add:1.1f} pounds')
    st.text(f'RESULT: Baking Soda to Add: {alk_to_add_cups:1.1f} cups') 
    st.text(f'NOTE: Do NOT apply more than 4 pounds at a single time.')
    st.text(f'Wait and retest first.')
else:
    alk = st.slider('Alkalinity (ppm)', min_value=0, max_value=240, value=100, step=20)
    alk_drops_calculated = alk / 10
    alk_to_add = (0.00022/16)*(100-10*alk_drops_calculated)*pool_volume
    alk_to_add_cups = alk_to_add * 2
    if alk_to_add_cups < 0:
        st.text(f'RESULT: No action required')
    else:
        st.text(f'RESULT: Baking Soda to Add: {alk_to_add:1.1f} pounds')
        st.text(f'RESULT: Baking Soda to Add: {alk_to_add_cups:1.1f} cups')
        st.text(f'NOTE: Do NOT apply more than 4 pounds at a single time.')
        st.text(f'Wait and retest first.')


