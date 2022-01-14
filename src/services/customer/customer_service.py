from datetime import date
from src.domain.customer.model import Customer
from src.domain.address.model import Address
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.customer.customer_dto import CustomerDTO
from src.services.address.address_dto import AddressDTO

def create_custumer(custumer_dto:CustomerDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
      uow.customer_repository.add(Customer(first_name=custumer_dto.first_name,
      last_name=custumer_dto.last_name, phone_number=custumer_dto.phone_number,
      genre=custumer_dto.genre, document_id=custumer_dto.document_id, birth_Date= custumer_dto.birth_Date))

      uow.commit()

def create_address(address_dto:AddressDTO, uow:SqlAlchemyUnitOfWork):

    with uow:
        customer = uow.customer_repository.get(id = address_dto.customer_id)

        if not customer:
            raise Exception ('Customer not found')

        address = Address(address=address_dto.address, city=address_dto.city, state=address_dto.state,
                            number=address_dto.number, zipcode= address_dto.zipcode,
                            neighbourhood= address_dto.neighbourhood, primary= address_dto.primary,
                            customer= customer)

        customer.add_address(address)

        uow.commit()