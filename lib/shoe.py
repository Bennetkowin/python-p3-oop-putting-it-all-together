#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand
        
    @property
    def size(self):
        return self.__sizeof__
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("Size must be an interger")
            
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")           
    
        
        pass
    pass