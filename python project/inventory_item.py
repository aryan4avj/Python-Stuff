'''
Created on 13 Feb. 2018

@author: Andreas Jordan
'''
from decimal import Decimal


class InventoryItem:

    __OUT_OF_STOCK = -1

    def __init__(self, name='', quantity=0, price=0.00):
        '''
        Constructor
        '''
        self.__product_name = name
        self.__product_quantity = quantity
        self.__product_price = price
        
        
    # Setter method for product name    
    def set_product_name(self, name):
        self.__product_name = name
    
    # Getter method for product name
    def get_product_name(self):
        return self.__product_name
    
    
    def reduce_product_quantity(self):
        if self.__product_quantity == 0:
            return self.__OUT_OF_STOCK
        self.__product_quantity-=1
        
#     def set_product_quantity(self, quantity):
#         if quantity > self.MAX_ITEMS_PER_PRODUCT:
#             self.__product_quantity = self.MAX_ITEMS_PER_PRODUCT
#             return self.QUANTITY_GREATER_THAN_MAX_ERROR
#         elif quantity == 0:
#             return self.QUANTITY_ZERO_ERROR
#         elif quantity < 0:
#             return self.QUANTITY_LESS_THAN_ZER0_ERROR
        
    def set_product_quantity(self, quantity):
        self.__product_quantity = quantity
         
    def get_product_quantity(self):
        return self.__product_quantity
    
    def set_product_price(self, price):
        self.__product_price = price#.quantize(Decimal('0.01'))
        
    def get_product_price(self):
        return self.__product_price
    
    def __eq__(self, product):
        return self.get_product_name() == product.get_product_name()
    
    def __str__(self):
        sep = ' '
        string = ''
        string += 'Name: ' + self.get_product_name() + sep
        string += 'Price: ' + str(self.get_product_price()) + sep
        string += 'Quantity: '+ str(self.get_product_quantity()) + '\n' # Excellent exercise by making students convert to str
        return string
            
