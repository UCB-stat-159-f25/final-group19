from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
import re

def write_inaugural_addresses(n_speeches):
    base_url = "https://www.presidency.ucsb.edu/documents/inaugural-address"
    
    speech_pres_name = np.empty(n_speeches, dtype=object)
    speech_pres_num = np.empty(n_speeches, dtype=object)
    speech_date = np.empty(n_speeches, dtype=object)
    speech_content = np.empty(n_speeches, dtype=object)

    for i in range(n_speeches):
        curr_url = base_url + '-' + str(i) if i > 0 else base_url
        response = requests.get(curr_url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        h3 = soup.find('h3', class_='diet-title')
        pres_name = h3.find('a').get_text()
        speech_pres_name[i] = pres_name
        
        pres_number_str = soup.find('div', class_="diet-by-line president").get_text(strip=True)
        pres_number = int(re.search("[0-9][0-9]?", pres_number_str).group())
        speech_pres_num[i] = pres_number

        date_span = soup.find('span', class_='date-display-single')['content']
        date = pd.to_datetime(date_span)
        speech_date[i] = date

        content_div = soup.find('div', class_='field-docs-content')
        content = content_div.get_text()
        speech_content[i] = content

        time.sleep(0.05) # don't make the api cry

    # sorting because they are out of order in url for some reason?
    colnames = ['president_name', 'president_number', 'date', 'text']
    inaugural_address = pd.DataFrame(
        np.column_stack([
            speech_pres_name,
            speech_pres_num,
            speech_date,
            speech_content
        ]),
        columns=colnames
    ).sort_values('date').reset_index(drop=True)
    
    inaugural_address.to_csv("data/inaugural_address.csv")

if __name__ == "__main__":
    # number of speeches will change as new presidents come
    NUM_SPEECHES = 55
    write_inaugural_addresses(n_speeches=NUM_SPEECHES)
