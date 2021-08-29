import streamlit as st
import pandas as pd
import requests


st.title('Foreign sellers registered in the VOEC scheme')
st.sidebar.write("""
Info about [VAT On E-Commerce in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/e-commerce-voec/)
The original list of the foreign sellers registered is just a PDF or CSV file with 1000+ rows. I wanted to create something more user friendly.

Source: [Skatteetaten](https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/registrerte-tilbydere---liste/voec-registrerte-tilbydere-12.08.21.csv)

[Git Repository] (https://github.com/tfreyd/VOEC-reshaped)


""")
st.sidebar.write('''** Author: [Thibaud Freyd](https://www.linkedin.com/in/thibaud-freyd/)**''')

st.sidebar.write('''Version 1.2

''')
#loading of the data
@st.cache
def import_data():

    #downlaod the csv file fro internet
    url_file='https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/registrerte-tilbydere---liste/voec-registrerte-tilbydere-12.08.21.csv'
    pdf_file=requests.get(url_file)
    
    #load csv
    df = pd.read_csv('./list_companies_extraction/list_complete.csv')
    df = df.sort_values('country')
    
    #generation of the list of countries
    all_countries = df['country'].unique().astype(str)
    all_countries = sorted(all_countries)
    all_countries.insert(0,'')
    
    #list of all companies 
    all_companies = df['company'].unique()
    all_companies = sorted(all_companies)
    all_companies.insert(0,'')

    return df, all_countries, all_companies



df, all_countries,all_companies =  import_data()



#double columns
left_col_selection,right_col_selection = st.columns(2)

#initiation index
index_country=0
index_company=0

# box for country selection
country_selection=left_col_selection.selectbox("Country : ",all_countries,index=0,format_func=lambda x: 'Select an option' if x == '' else x)

#box for company selection
company_selection = right_col_selection.selectbox("Company: ", all_companies,index=index_company,format_func=lambda x: 'Select an option' if x == '' else x)



#display result of the search
if country_selection or company_selection:
    if country_selection:
        #st.success(f' "{country_selection}" selected')
        st.write(df.loc[df['country']==country_selection])
    if company_selection:
        #st.success(f' "{company_selection}" selected')
        st.write(df.loc[df['company']==company_selection])


st.write('''*Database from 12.08.21*''')

st.write("*known issue*: need to refresh the page to reset everything" )



#in order to hide the Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
