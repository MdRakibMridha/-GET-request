# loading the pakages
import requests
import pandas as pd


class BikeScraper():

    def __init__(self):
        self.scrape()

    def scrape(self):
        self.data = []

             
        url = 'http://api.citybik.es/v2/networks'
        response = requests.get(url)
        data_json = response.json()
        for bikes in range(len(data_json['networks'])):
            com = data_json['networks'][bikes]['company']
            id_name = data_json['networks'][bikes]['id']
            loc = data_json['networks'][bikes]['location']
            nam = data_json['networks'][bikes]['name']            


            dct = {
                'company'    : com,
                'id'         : id_name,
                'location'   : loc,
                'name'       : nam                                                                 
            }
            self.data.append(dct)
        self.export_to_csv()

    def export_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('Project_on_GET_01.csv', index=False)


if __name__ == '__main__':
    scrape = BikeScraper()



        



 
    



                



