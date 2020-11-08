import streamlit as st
import pandas as pd
import requests
#import camelot

st.write('# VOEC list Reshaped')
st.sidebar.write("""
Info about [VAT On E-Commerce in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/e-commerce-voec/)
The original list of the registered foreign sellers is just a PDF of >1000 rows. I wanted to create something more user friendly.

Date of the info: 15.10.20

Made by [Thibaud Freyd](https://www.linkedin.com/in/thibaud-freyd/)
""")



#loading of the data
df = pd.read_csv('list_complete.csv')
#generation of the list of countries
countries = df['country'].unique().astype(str)
countries = sorted(countries)
#list for country selection
country_selected=st.selectbox("Choose your country: ",countries,index=18)
#df = user_input_features() #for version with sidebar
#
df =df.loc[df['country']==country_selected]
st.write(df)
