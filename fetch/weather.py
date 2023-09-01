from libraries.fetch_data import FetchData

class Weather:
    def __init__(self, city:str):
        self.city = city

    def fetch_weather(self):
        url = f'https://www.ventusky.com/{self.city.lower()}'
        print(url)
        FetchData(url=url, file_name=f'{self.city}_weather').run()

if __name__=='__main__':
    Weather('minsk').fetch_weather()
    Weather('yerevan').fetch_weather()