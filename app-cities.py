import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('World Major Cites - Matt Ziomek')
df = pd.read_csv('worldcities.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)  # min, max, default

capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults top 3 countries in population

form = st.sidebar.form('country-form')
country_filter = form.text_input('Enter country name', 'ALL')
form.form_submit_button('Apply')

# filter by population
df = df[df.population >= population_filter]

# filter by country
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)

st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)