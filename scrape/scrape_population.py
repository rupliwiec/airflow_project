import json

from libraries.base_scrape import BaseScrape
from libraries.post_to_api import PostToAPI

# class ScrapePopulation(BaseScrape):
#     def scrape(self, country:str):
#         soup = self.reading_file()
#         popul = soup.find("div", {"class": "indicator-item__data-info"}).text
