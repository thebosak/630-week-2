'''
Created on May 14, 2019

@author: Brad Bosak
'''

from Rectangle import Rectangle

#Retrieve length and width from user
def getDimensions():
    length = eval(input("Enter the length: "))
    width  = eval(input("Enter the width: "))
    return length,width

#Main function to get dimensions and return the area
def main():
    length,width = getDimensions()
    rect=Rectangle(length,width)
    print("The area is ",rect.area())
    

main()