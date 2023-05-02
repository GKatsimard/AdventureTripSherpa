import airbnb

def test_get_airbnb_suggestions():
    api = airbnb.AirBNBAPI()
    response = api.get_airbnb_suggestions(location='Saint Prokopis, Naxos', 
                                            checkin='2023-09-16', 
                                            checkout='2023-09-17', 
                                            adults=2, 
                                            children=2,
                                            infants= 0, 
                                            pets = 0, 
                                            page = 1, 
                                            currency='EUR')
    
    print(response['results'])

test_get_airbnb_suggestions()
    
