from libraries.fetch_data import FetchData

class Population:
    def __init__(self, country:str):
        self.country = country
    
    def fetch_population(self):
        url = f'https://en.wikipedia.org/wiki/Demographics_of_{self.country}'
        FetchData(url=url, file_name=f'{self.country}_total_population').run()

if __name__=='__main__':
    Population('Belarus').fetch_population()
    Population('Armenia').fetch_population()