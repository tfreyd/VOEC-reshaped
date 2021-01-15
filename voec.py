import streamlit as st
import pandas as pd
import requests
#import camelot

st.title('Foreign sellers registered in the VOEC scheme')
st.sidebar.write("""
Info about [VAT On E-Commerce in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/e-commerce-voec/)
The original list of the foreign sellers registered is just a PDF with 1000+ rows. I wanted to create something more user friendly.

Source: [Skatteetaten](https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/voec-registrerte-tilbydere-27.11.2020.pdf)

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

    all_countries = df['country'].unique().astype(str)
    all_countries = sorted(all_countries)
    all_countries.append('')

    
    #list of all companies 
    all_companies = df['company'].unique()
    all_companies = sorted(all_companies)
    all_companies.append('')


    return df, all_countries, all_companies

df, all_countries,all_companies=  import_data()

#double columns
left_col_selection,right_col_selection = st.beta_columns(2)

#initiation index
index_country=len(all_countries)-1
index_company=len(all_companies)-1

# box for country selection
country_selection=left_col_selection.selectbox("Country : ",all_countries,index=index_country,format_func=lambda x: 'Select an option' if x == '' else x)

#box for company selection
company_selection=right_col_selection.selectbox("Company: ", all_companies,index=index_company,format_func=lambda x: 'Select an option' if x == '' else x)

# #button country selection
# if left_col_selection.button('Valid',key='country_button'):
#     left_col_selection.write(f'{country_selection} selected')
#     df =df.loc[df['country']==country_selection]
#     df=df.sort_values('company') 


if country_selection or company_selection:
    if company_selection:
        st.success(f' "{company_selection}" selected')
        df =df.loc[df['company']==company_selection]
    elif country_selection:
        st.success(f' "{country_selection}" selected')
        df =df.loc[df['country']==country_selection]
        
else:
    st.warning('Please select a country or a company')


# #company button validation
# if right_col_selection.button('Valid',key='company_button'):
#     st.success('Valided')
#     df =df.loc[df['company']==company_selection]


st.dataframe(df)
st.write('''*Database from 27.11.20*''')



#df = user_input_features() #for version with sidebar
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
