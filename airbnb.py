import requests
from apikeys import airbnb_api_key, airbnb_api_host

class AirBNBAPI:

    def __init__(self) -> None:
        self.api_key = airbnb_api_key
        self.api_host = airbnb_api_host

    def get_airbnb_suggestions(self, 
                               location: str, 
                               checkin: str, 
                               checkout: str, 
                               adults: int, 
                               children: int, 
                               infants: int, 
                               pets: int, 
                               page: int, 
                               currency: str) -> dict:
        
        headers = { 'x-rapidapi-host': self.api_host, 'x-rapidapi-key': self.api_key }
        url = f'https://{self.api_host}/search-location?location={location}&checkin={checkin}&checkout={checkout}&adults={adults}&children={children}&infants={infants}&pets={pets}&page={page}&currency={currency}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return { 'error': f'Error {response.status_code}' }


