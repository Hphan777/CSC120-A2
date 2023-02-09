from typing import Dict, Union


class Computer:


    # What attributes will it need?
     description: str = ""
     processor_type: str = ""
     hard_drive_capacity: int = 0
     memory: int = 0
     operating_system: str = ""
     year_made: int = 0
     price: int =0

    # How will you set up your constructor?

    # Remember: in python, all constructors have the same name (__init__)
     def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_model: int, price: int):
        self.description = description
        self.procesor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_model
        self.price = price

    # What methods will you need?
     def printDetails(self):
         print(self.description)
         print(self.processor_type)
         print(self.hard_drive_capacity)
         print(self.memory)
         print(self.operating_system)
         print(self.year_made)
         print(self.price)

     
     





    