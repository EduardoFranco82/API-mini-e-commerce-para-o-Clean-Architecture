from typing import List
from src.domain.address.model import Address
from datetime import date
class Customer:
    def __init__(self,first_name:str,last_name:str,phone_number:str,genre:str,
            document_id:str,birth_Date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_Date = birth_Date
        self.list_address: List[Address] = []
    
    
    def add_address(self, address:Address):
        has_address_primary:Address = list(filter(lambda x:x.primary == True , self.list_address))
        if len(has_address_primary)>0:
        
            if address.primary == True :
                has_address_primary[0].primary = False
                
        self.list_address.append(address)
        
