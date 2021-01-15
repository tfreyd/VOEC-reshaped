import streamlit as st
import pandas as pd
import requests
#import camelot

st.title('Foreign sellers registered in the VOEC scheme')
st.sidebar.write("""
Info about [VAT On E-Commerce in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/e-commerce-voec/)
The original list of the foreign sellers registered is just a PDF with 1000+ rows. I wanted to create something more user friendly.

Source: [Skatteetaten](https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/voec-registrerte-tilbydere-15.10.2020.pdf)

[Git Repository] (https://github.com/tfreyd/VOEC-reshaped)


""")
st.sidebar.write('''** Author: [Thibaud Freyd](https://www.linkedin.com/in/thibaud-freyd/)**

Version 1.1 ''')
#loading of the data
@st.cache
def import_data():
    df = pd.read_csv('./list_companies_extraction/list_complete.csv')
    df = df.sort_values('country')
    
    #generation of the list of countries
    list_countries = df['country'].unique().astype(str)
    list_countries = sorted(list_countries)
    #list of all companies 
    list_companies = df['company'].unique().astype(str)
    list_companies = sorted(list_companies)

    return df, list_countries,list_companies

df, list_countries,list_companies=  import_data()
#double columns
left_col_selection,right_col_selection = st.beta_columns(2)

# box for country selection
country_selection=left_col_selection.selectbox("Country : ",list_countries,index=18)
if left_col_selection.button('Valid',key='country_button'):
    left_col_selection.write(f'{country_selection} selected')
    df =df.loc[df['country']==country_selection]
    df=df.sort_values('company')

#company selected
company_selection=right_col_selection.selectbox("Company: ",list_companies)
if right_col_selection.button('Valid',key='company_button'):
    right_col_selection.write(f'{company_selection} selected')
    df =df.loc[df['company']==company_selection]

#df = user_input_features() #for version with sidebar


st.table(df)
st.write('''*Database from 27.11.20*''')

#for version with sidebar
# st.sidebar.header('User Input Parameters')
# def user_input_features():
#         country_selected=st.sidebar.selectbox("Choose your country: ",countries,index=18)
#         data_to_display = df.loc[df['country']==country_selected]
#         return data_to_display




#in order to hide the Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
