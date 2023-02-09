
from typing import Dict, Union, Optional

from computer import*
#class is the blueprint of all of the methods
class ResaleShop:

     # What attributes will it need?
     inventory: list = []

    
     def __init__(self)-> None:
          self.inventory = []
     def buy(self, c: Computer):
          self.inventory.append(c)

     def update_price(self, c: Computer, new_price: int):
          if c in self.inventory:
               c.price - new_price
          else:
               print("Item not found. Cannot update price.")
     def update_os(self, c: Computer, new_os):
          if c in self.inventory:
              c.operating_system = new_os
          else:
              print("Item not found, cannot updaate os.")
     

     def sell(self, c: Computer):
          self.inventory.remove(c)

     def print_inventory(self, c:Computer):
     # If the inventory is not empty
          if self.inventory:
        # For each item
               for c in self.inventory:
            # Print its details
                c.printDetails()        #(f'Item ID: {c} : {self.inventory[c]}')
          else:
            print("No inventory to display.")

     def refurbish(self, c: Computer):
          if c in self.inventory: 
               if int(c.year_made) < 2000:
                    c.price = 0 # too old to sell, donation only
               elif int(c.year_made) < 2012:
                    c.price = 250 # heavily-discounted price on machines 10+ years old
               elif int(c.year_made) < 2018:
                    c.price = 550 # discounted price on machines 4-to-10 year old machines
               else:
                    c.price = 1000 # recent stuff
          else:
               print("Item not found. Please select another item to refurbish.")

    


         # 1. call Computer(...) constructor 
         #    to create a new Computer instance 

         # 2. call inventory.apend(...) to add the 
         #    new Computer instance to the inventory