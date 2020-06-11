#
# File: fileName.py
# Author: Aryan Vikas Jain
# SAIBT Id: your email id
# Description: Assignment 2 - place assignment description here...
# This is my own work as defined by the University's
# Academic Misconduct policy.

from decimal import Decimal # Leave this here! You're going to need it!

# Global constants - note you are NOT required to use these
VENDING_MACHINE_WIDTH = 50
PRICE_OUTPUT_LENGTH = 6
PRODUCT_OUTPUT_LENGTH = 44

import inventory_item


# Add your description for this function here...
def display_vending_machine(inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print('In function display_vending_machine(inventory_list)')


# Add your description for this function here...
def read_file(filename, inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.

    file=open("inventory_item.txt",'r')
    try:
        file.readline();
        for line in file:
            strip=line.strip(',');
            data=line.split();
            print(data);
    finally:
        file.close();


# Add your description for this function here...
def write_to_file(filename, inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print('In function write_to_file(filename, inventory_list)')


# Add your description for this function here...
def accept_money(product_price):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print('In function accept_money(product_price)')


# Add your description for this function here...
def display_main_menu():
    # The print statement below should be removed eventually
    # and replaced with your own code.

    print('1. Purchase item')
    print('2.  Quit')

    option= int(input('Please enter 1-2 to select:'))

     
    if option==1:
        print('working')
        read_file();
        main();
    elif option==2:
        exit()
    else:    
        print('Please enter either 1-2.')
        main()

# Add your description for this function here...
def purchase_product(inventory_list):       
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print('In function purchase_product(inventory_list)')


# Add your description for this function here...    
def main(): 
    # Initialise list to contain InventoryItem objects
    inventory_list = []
    
    # Read in the inventory file 
    print('In function main.')
    display_main_menu();
    # Add code to display products in our vending machine    
    
    # Add code to display the menu

    # Add main program loop
    
    # After loop exits, write contents of inventory to a new file
    # Caution: Do not overwrite the inventory.txt file

# Call main()
main()
