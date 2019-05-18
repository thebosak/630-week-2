'''
Created on May 13, 2019

@author: Brad Bosak
'''

class Rectangle:
    '''
    Rectangle class defined by a length and width
    '''


    def __init__(self, length, width):
        self.length=length
        self.width=width
        
        
    def area(self):
        area=self.length*self.width
        
        return area