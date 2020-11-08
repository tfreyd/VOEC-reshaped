import streamlit as st
import pandas as pd
import requests
#import camelot

st.title('Foreign sellers registered in the VOEC scheme')
st.sidebar.write("""
Info about [VAT On E-Commerce in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/e-commerce-voec/)
The original list of the foreign sellers registered is just a PDF with 1000+ rows.I wanted to create something more user friendly.

Source: [Skatteetaten](https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/voec-registrerte-tilbydere-15.10.2020.pdf)

[Git Repository] (https://github.com/tfreyd/VOEC-reshaped)
""")
st.sidebar.write('** Author: [Thibaud Freyd](https://www.linkedin.com/in/thibaud-freyd/)**')
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
st.write('''*Info from 15.10.2020*''')
#for version with sidebar
# st.sidebar.header('User Input Parameters')
# def user_input_features():
#         country_selected=st.sidebar.selectbox("Choose your country: ",countries,index=18)
#         data_to_display = df.loc[df['country']==country_selected]
#         return data_to_display

#to refresh all the data
# st.sidebar.write('### In order to refresh the database')
# def refresh_data():
#     #retrieve of the pdf and digestation as df
#     url_file='https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/voec-registrerte-tilbydere-15.10.2020.pdf'
#     pdf_file=requests.get(url_file)
#     #save as pdf
#     open('list_companies_voec.pdf', 'wb').write(pdf_file.content)
#     st.write('PDF file retrived.')
#     st.write('Please Wait ingestion content ≈1min')
#     #read pdf file with camelot
#     tables = camelot.read_pdf('list_companies_voec.pdf',pages='all')
#     #create the df to merge everything
#     full_table=pd.DataFrame()
#     #merge everyting
#     for table in tables:
#         full_table = pd.concat([full_table,table.df])
#     #index
#     full_table.reset_index(inplace=True)
#     #remove index colum
#     full_table=full_table[[0,1,2]]
#     #fix columns
#     full_table=full_table.iloc[1:]
#     full_table.columns=['compagny','country','url']
#     #save to CSV
#     full_table.to_csv('list_complete.csv',index=False)
#
#     st.write('Done')
#
#     return full_table
# if st.sidebar.button('Rebuild Database'):
#     refresh_data()


#in order to hide the Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
