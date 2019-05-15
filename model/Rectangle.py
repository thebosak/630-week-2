'''
Created on May 13, 2019

@author: Brad Bosak
'''

class Rectangle:
    '''
    classdocs
    '''


    def __init__(self, length, width):
        self.length=length
        self.width=width
        
        
    def area(self):
        area=self.length*self.width
        
        return area
'''
def getNumbers():
    length = eval(input("Enter the length: "))
    width  = eval(input("Enter the width: "))
    return length, width

def main():
    length,width = getNumbers()
    rect=Rectangle(length,width)
    print(rect.area())
    
main()'''