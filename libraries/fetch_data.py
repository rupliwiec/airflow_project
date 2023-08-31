import requests
import os
os.environ['no_proxy']='*'

class FetchData:
    def __init__(self, url: str, file_name):
        self.web_link = url
        self.file_name = file_name

        if not url:
            raise Exception('No url to fetch the data from')

        if not isinstance(url, str):
            msg = f'The type of url should be a string and not {type(url)}'
            raise ValueError(msg)

    def fetch(self):
        html_data = requests.get(self.web_link).content
        return html_data

    def run(self):
        data = self.fetch()
        with open(f'tmp/{self.file_name}.html', 'wb') as file:
            file.write(data)
            file.close()

if __name__=="__main__":
    FetchData('https://www.globalpetrolprices.com/Belarus/gasoline_prices/', 'test fuel prices belarus').run()