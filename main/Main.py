'''
Created on May 14, 2019

@author: Brad Bosak
'''

from Rectangle import Rectangle
#import Rectangle

def getNumbers():
    length = eval(input("Enter the length: "))
    width  = eval(input("Enter the width: "))
    return length,width

def main():
    length,width = getNumbers()
    rect=Rectangle(length,width)
    print("The area is" and rect.area())
    

main()