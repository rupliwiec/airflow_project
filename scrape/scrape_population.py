import json

from libraries.base_scrape import BaseScrape
from libraries.post_to_api import PostToAPI

class ScrapePopulation(BaseScrape):
    def scrape(self, country:str):
        soup = self.reading_file()
        table_row = soup.find('td',{"class": "infobox-data"}).text.split(" ")[0]
        data_dict={}

        data_dict[f'{country}_population']= int(table_row.replace(',',''))
        data_dict['country']= country

        PostToAPI('http://127.0.0.1:8000/add_population/', json.dumps(data_dict)).api_post()

if __name__=='__main__':
    ScrapePopulation('tmp/Belarus_total_population.html').scrape('BYN')
    ScrapePopulation('tmp/Armenia_total_population.html').scrape('ARM')