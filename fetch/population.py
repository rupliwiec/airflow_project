from libraries.fetch_data import FetchData

class Population:
    def __init__(self, country:str):
        self.country = country
    
    def fetch_population(self):
        url = f'https://data.worldbank.org/country/{self.country}?view=chart'
        FetchData(url=url, file_name=f'{self.country}_total_population').run()

if __name__=='__main__':
    Population('belarus').fetch_population()
    Population('armenia').fetch_population()