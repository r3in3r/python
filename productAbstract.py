from abc import ABC, abstractmethod

class Product:
    name =''
    SKU =''
    price=0
    expiry_date=''
    weight =0
    upload_product_image= ""

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product : Product):
        pass
    
    @abstractmethod
    def edit_product(self, product : Product):
        pass
   
    @abstractmethod
    def get_product_by_id(self):
        pass
    
    @abstractmethod
    def get_all_products(self):
        pass
    
    @abstractmethod
    def upload_product_image(self, upload_product_image ):
        pass
    
    @abstractmethod
    def delete_product(product : Product):
        pass

class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print("New Product added")
        
    def edit_product(self, product: Product):
        pass
    def get_product_by_id(self):
        pass
    def get_all_products(self):
        pass
    def upload_product_image(self, upload_product_image):
        pass
    def delete_product(product: Product):
        pass
product_manager = ProductManager()
#product = Product()
product_manager.create_product(product = Product)


   
   



