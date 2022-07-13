from unittest import result
from urllib.parse import _ResultMixinBytes
from bs4 import BeautifulSoup
import requests
import logging
from schedule import every, repeat, run_pending
import time

# Add the website URL here
url = ''

FORMAT = '%(asctime)s, %(levelname)s: (%(Response Code)s, %(URL)s) -> %(message)s'
logging.basicConfig(filename='main.log', filemode='w', level=logging.INFO, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')

already_queried_properties = []

def get_response(url: str):
    res = requests.request('GET', url)
    if res.status_code == 200:
        logging.info('Successful request', extra={'Response Code': str(res.status_code), 'URL': str(url)})
        return (res.text, res.status_code)
    elif res.status_code in (400, 404,):
        logging.error('Error in URL', extra={'Response Code': str(res.status_code), 'URL': str(url)})
    else:
        logging.error('Shit went down', extra={'Response Code': str(res.status_code), 'URL': str(url)})
    return None


@repeat(every(10).minutes, url)
def check_new_listings(url: str):
    """Positive approach to finding new listings. If any errors, it just logs and does nothing."""
    res_text = get_response(url)
    if res_text is not None:
        properties = get_all_properties(res_text, url)
        if properties is not None:
            for property in properties:
                property_name = str(property.find("h4").contents[0]).strip()
                property_url = str(property.find("div").parent["data-url"]).strip()
                if property_name not in already_queried_properties:
                    already_queried_properties.append(property_name)
                    send_new_property_email(property_name, property_url)

def get_all_properties(res_text: str, url: str):
    try:
        soup = BeautifulSoup(res_text, 'html.parser')
        properties = soup.find_all("div", class_="regi-item d-flex flex-wrap")
        logging.info('Found property listings', extra={'Response Code': '200', 'URL': str(url)})
        return properties
    except:
        logging.error('There might be a change in the HTML structure', extra={'Response Code': '406', 'URL': 'None'})
        return None

def send_new_property_email(property_name, property_url):
    # The variables property_name and property_url contains new 
    # property listings that you should pass to the email template
    # Your code goes below here
    pass

if __name__ == "__main__":
    check_new_listings(url)
    while True:
        run_pending()
        time.sleep(1)
        