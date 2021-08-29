import pandas as pd
import requests 
import camelot 
def refresh_data():
     #retrieve of the pdf and digestation as df
     url_file='https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/voec/registrerte-tilbydere---liste/voec-registrerte-tilbydere-12.08.21.csv'
     pdf_file=requests.get(url_file)
    
     #save as pdf
     open('list_companies_voec.pdf', 'wb').write(pdf_file.content)
     print('PDF file retrived.')
     print('Please Wait ingestion content ≈1min')
    
     #read pdf file with camelot
     tables = camelot.read_pdf('list_companies_voec.pdf',pages='all')
    
     #create the df to merge everything
     full_table=pd.DataFrame()
    
     #merge everyting
     for table in tables:
         full_table = pd.concat([full_table,table.df])
     
     #index
     full_table.reset_index(inplace=True)
     #remove index colum
     full_table=full_table[[0,1,2]]
     #fix columns
     full_table=full_table.iloc[1:]
     full_table.columns=['company','country','url']
     #save to CSV
     full_table.to_csv('list_complete.csv',index=False)
     print('all done')