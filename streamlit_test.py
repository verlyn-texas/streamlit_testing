import streamlit as st

st.text('Pool Chemical Calculations')

house = st.radio('House',('Mystic Summit','APH'))

if house == 'Mystic Summit':
    pool_volume = 16250
else:
    pool_volume = 10884
    


pH = st.slider('pH', min_value=6.0, max_value=10.0, value=7.0, step=0.1)


if pH > 7.6:
    st.text('Perform Acid Demand Test')
    acid_drops = st.slider('Acid Demand Drops',min_value=0, max_value=10, value=2, step=1)
    if acid_drops == 0:
        st.text('Acid Demand: N/A')
    else:
        demand = 0.00092 * pool_volume * acid_drops
        st.text(f'Acid Demand: {demand:1.1f} ounces')
else:
    st.text('Acid Demand Test Not Required')


alk = st.slider('Alkalinity (drops)', min_value=0, max_value=10, value=10, step=1)

alk_to_add = (0.00022/16)*(100-10*alk)*pool_volume

st.text(f'Baking Soda to Add: {alk_to_add:1.1f} pounds')

