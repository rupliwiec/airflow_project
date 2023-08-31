from libraries.fetch_data import FetchData

class Petrol:
    def __init__(self, country:str):
        self.country = country
    
    def fetch_petrol(self):
        url = f'https://www.globalpetrolprices.com/{self.country}/gasoline_prices/'
        FetchData(url=url, file_name=f'{self.country.lower()}_petrol_price').run()

if __name__ == '__main__':
    Petrol('Belarus').fetch_petrol()
    Petrol('Armenia').fetch_petrol()