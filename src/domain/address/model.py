#from src.domain.customer.model import Customer

class Address:
    def __init__(self,address: str, city:str, state:str, number:str,
                 zipcode:str, neighbourhood:str, primary: bool, customer):
        self.address = address
        self.city = city
        self.state = state
        self.number = number
        self.zipcode = zipcode
        self.neighbourhood = neighbourhood
        self.primary = primary
        self.customer = customer
        