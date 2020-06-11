#
# File: fileName.py
# Author: your name
# SAIBT Id: your email id
# Description: Assignment 2 - place assignment description here...
# This is my own work as defined by the University's
# Academic Misconduct policy.

from decimal import Decimal # Leave this here! You're going to need it!
import inventory_item

# Global constants - note you are NOT required to use these
VENDING_MACHINE_WIDTH = 50
PRICE_OUTPUT_LENGTH = 6
PRODUCT_OUTPUT_LENGTH = 44


# Add your description for this function here...
def display_vending_machine(inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print(' '+''.ljust(VENDING_MACHINE_WIDTH,'_'))
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH)+'|')
    print(' '+'|'+"*** Vending Machine Simulator ***".center(VENDING_MACHINE_WIDTH-1)+'|')
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH,'_')+'|')
    n = 1
    for i in inventory_list:
        print(' '+'|'.ljust(VENDING_MACHINE_WIDTH)+'|')
        print(' '+('|'+str(n)+'. '+i.get_product_name()).ljust(VENDING_MACHINE_WIDTH-6)+('$'+i.get_product_price()+' |'))
        n+=1
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH,'_')+'|')
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH)+'|')
    print(' '+'|'+'\___________________________________/'.center(VENDING_MACHINE_WIDTH-1)+'|')
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH)+'|')
    print(' '+'|'.ljust(VENDING_MACHINE_WIDTH,'_')+'|')



# Add your description for this function here...
def read_file(filename, inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    fp = open(filename,'r')
    for i in fp.readlines():
        i.strip()
        l = i.split(',')
        inventory_list.append(inventory_item.InventoryItem(l[0],int(l[2].strip()),l[1]))


# Add your description for this function here...
def write_to_file(filename, inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    f = open(filename,'w')
    for i in inventory_list:
        f.write(i.get_product_name()+","+str(i.get_product_price())+","+str(i.get_product_quantity())+"\n")

# Add your description for this function here...
def accept_money(product_price):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    m = Decimal('0.00')
    am = Decimal(str(product_price))
    print()
    print("Please continue to enter coins until amount reached.")
    print("Valid choices for coins are:")
    print("[1] Ten cents")
    print("[2] Twenty cents")
    print("[3] Fifty cents")
    print("[4] One dollar")
    print("[5] Cancel")
    print()
    t = 0
    while(m<am and t!=5):
        print("Balance: $"+str(m)+" Remainig: $"+str(am))
        t = int(input("Enter coin [1-4] or 5 to cancel:"))
        if t==1:
            m+=Decimal('0.10')
            print()
        elif t==2:
            m+=Decimal('0.20')
            print()
        elif t==3:
            m+=Decimal('0.50')
            print()
        elif t==4:
            m+=Decimal('1.00')
            print()
    print("Change: $"+str(m-am))
    print()
    print("Congratulations on your purchase! Please use us again.")

# Add your description for this function here...
def display_main_menu():
    # The print statement below should be removed eventually
    # and replaced with your own code.
    print()
    print("1. Purchase Item")
    print("2. Quit")
    print()
    print("Please enter 1-2 to select: ",end='')




# Add your description for this function here...
def purchase_product(inventory_list):
    # The print statement below should be removed eventually
    # and replaced with your own code.
    control = 0
    while control==0:
        print()
        n = int(input("Enter selection (1-10): "))
        print()
        if n in range(1,11):
            print("You selected",inventory_list[n-1].get_product_name(),'($'+str(inventory_list[n-1].get_product_price())+')')
            s = ''
            while(s!='a'):
                s = input("Is this correct (y/n): ")
                if s=='y':
                    if (inventory_list[n-1].get_product_quantity())>0:
                        accept_money(inventory_list[n-1].get_product_price())
                        inventory_list[n-1].set_product_quantity((inventory_list[n-1].get_product_quantity())-1)
                        s='a'
                    else:
                        print()
                        print("Sorry out of",inventory_list[n-1].get_product_name(),'!')
                        s = 'a'
                elif s=='n':
                    s='a'
                else:
                    print("Please enter either y or n .")
            control = 1
        else:
            print("Invalid Choice")
            pass

# Add your description for this function here...
def main():
    # Initialise list to contain InventoryItem objects
    inventory_list = []
    read_file('inventory.txt',inventory_list)
    ch = 0
    while ch is 0:
        print()
        display_vending_machine(inventory_list)
        display_main_menu()
        temp = int(input())
        if temp==1:
            purchase_product(inventory_list)
        elif temp==2:
            st = input("Are you sure [y/n]?: ")
            if st=='y':
                print()
                print("GoodBye.")
                write_to_file('new_inventory.txt', inventory_list)
                ch = 1
            elif st=='n':
                ch = 0
            else:
                print()
                print("Please enter either y or n .")
        else:
            print()
            print("Please enter either 1-2.")
    # Read in the inventory file

    # Add code to display products in our vending machine

    # Add code to display the menu

    # Add main program loop

    # After loop exits, write contents of inventory to a new file
    # Caution: Do not overwrite the inventory.txt file

# Call main()
main()
