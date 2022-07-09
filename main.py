from unittest import result
from urllib.parse import _ResultMixinBytes
from bs4 import BeautifulSoup
import requests
import logging
from schedule import every, repeat, run_pending
import time


url = ''

FORMAT = '%(asctime)s, %(levelname)s: (%(Response Code)s, %(URL)s) -> %(message)s'
logging.basicConfig(filename='main.log', filemode='w', level=logging.INFO, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')

already_queried_properties = []

def get_response(url):
    res = requests.request('GET', url)
    if res.status_code == 200:
        logging.info('Successful request', extra={'Response Code': str(res.status_code), 'URL': str(url)})
        return res.text
    elif res.status_code in (400, 404,):
        logging.error('Error in URL', extra={'Response Code': str(res.status_code), 'URL': str(url)})
    else:
        logging.error('Shit went down', extra={'Response Code': str(res.status_code), 'URL': str(url)})
    return None


@repeat(every(10).minutes, url)
def check_new_listings(url):
    res_text = get_response(url)
    if res_text is not None:
        soup = BeautifulSoup(res_text, 'html.parser')
        properties = soup.find_all("div", class_="regi-item d-flex flex-wrap")
        for property in properties:
            property_name = str(property.find("h4").contents[0]).strip()
            property_url = str(property.find("div").parent["data-url"]).strip()
            if property_name not in already_queried_properties:
                already_queried_properties.append(property_name)
                send_new_property_email(property_name, property_url)

def send_new_property_email():
    pass

if __name__ == "__main__":
    check_new_listings(url)
    while True:
        run_pending()
        time.sleep(1)
        