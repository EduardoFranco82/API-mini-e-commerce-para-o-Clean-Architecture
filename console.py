from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from services.categorie.categorie_service import create_category
from services.supplier.supplier_service import create_supplier
from services.product.product_service import create_product
from services.payment_method.payment_method_service import create_payment_method
from services.coupon.coupon_service import create_coupon
from services.customer.customer_service import create_address, create_custumer 
from src.adapter.database import Session
from src.adapter.orm import start_mapper
from datetime import datetime, date

start_mapper()

db = Session()

uow = SqlAlchemyUnitOfWork(db)

##############################CREATE CUSTUMER OK###############################################
#create_custumer(first_name='eduardo',last_name='franco', phone_number='1234',genre='m',
 #                document_id= '123',birth_Date=datetime.now(),uow=uow)
################################################################################################



##############  CREATE ADDRES SEM CUSTUMER TESTADO, DEU FALHA COMO ESPERADO#######################
create_address(address='rua 156656', city= 'passa 4', state='mg', number='100',zipcode='37464000',
                neighbourhood='n s fatima', primary= True, customer_id= 1, uow= uow)
################################################################################################

##############################CREATE COUPON TESTADO###############################
#create_coupon(code='123',limit= 3,expire_at= datetime.now() ,type= 'value',value =15.0,uow = uow)
##########################################################################################
# c = create_category('laticinios', uow)
# s = create_supplier('alhambra', uow)

# create_product(description='danone', price= 10.0, technical_detail= 'perecivel', image='nao',
# visible=True, categorie=c, supplier= s, uow=uow)





# with uow:
#   pm = PaymentMethod(name='pix', enabled=True, id=1)
#   uow.payment_method_repository.add(pm)


#   c = Category(name='eletronico')
#   uow.category_repository.add(c)
#   s = Supplier(name='HP')
#   uow.supplier_repository.add(s)


#   p = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, category=c, supplier=s)
#   pd = ProductDiscount(mode='value', value=100, payment_method=pm)
#   p.add_discount(pd)

#   uow.product_repository.add(p)

#   print(len(p.discounts))

#   pm2 = PaymentMethod(name='boleto', enabled=True, id=2)
#   uow.payment_method_repository.add(pm2)

#   # pd2 = ProductDiscount(mode='percetage', value=100, payment_method=pm2)
#   # p.add_discount(pd2)


# payment_method_repository = PaymentMethodRepository(db, PaymentMethod)
# category_repository = CategoryRepository(db, Category)
# supplier_repository = SupplierRepository(db, Supplier)
# product_repository = ProductRepository(db, Product)


# ================= 
# Populando o banco de dados





# Adicionando um novo desconto

# p = db.query(Product).filter_by(id=1).first()

# # pm = db.query(PaymentMethod).filter_by(id=1).first()
# pm = PaymentMethod('cartão de crédito', enabled=True, id=3)

# pd = ProductDiscount(mode='value', value=100, payment_method=pm)

# print(len(p.discounts))


# p.add_discount(pd)

# print(p.id)
# db.commit()
# db.close()


# Buscando um desconto no banco de dados

# pd = db.query(ProductDiscount).filter_by(id=1).first()

# print(pd.value)
# print(pd.payment_method.name)


############################################## FORMA QUE EU ESTAVA FAZENDO

# start_mapper()

# db = Session()
# repository = Product_discount_Repository(db)

# categorie = Categorie(name='laticinios')
# categorie2 = Categorie(name='carnes')


# supplier = Supplier (name= 'parmalat')
# supplier2 = Supplier (name= 'comevap')
# supplier3 = Supplier (name= 'friboi')


# product = Product(description='queijo', price=50, technical_details='detalhes tecnicos', image='', visible=True,  categorie=categorie, supplier=supplier)


# payment_method = Payment_Method(name='dinheiro',enable= True)
# payment_method1 = Payment_Method(name='cartão',enable= True)
# payment_method2 = Payment_Method(name='cheque',enable= False)

# product_discount = Product_discount(mode= 'value',value= 10.00,product = product, payment_method= payment_method )



# repository.get()
# repository.add(product_discount)


# print(product_discount.id)
# print(product.id)
# print(payment_method.id)
# print(product.description)


