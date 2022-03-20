# -*- coding: utf-8 -*-
"""
Name
Group members (first names):
COSC-010
BSGO Lab

Note that each of the functions below has some starter code to be used
as inspiration. You will have to re-write most of it, though. Test each
function out individually. 
"""

def main():
    """
    The main function contains a while loop. For each iteration of the
    loop, the program will ask the user for a customer's name and then 
    call the nameInfo function (part 1). It will later call another
    function, calculateTotal. The loop will continue looping until the 
    user enters 'stop' instead of a customer's name

    """
    print("Welcome to BSGO (Buy Some Get One) Company") #Feel free to change name
    running = True
    print('The program will finish once you input "stop"')
    while running:
        name = input("Enter the customer's name: ")
        if name.lower() == 'stop':
            running = False
            break
        customerName = nameInfo(name) #Passes name to nameInfo function and assigns return value to customerName
        print("The customer's first name is",customerName)
        customerTotal = calculateTotal(customerName)
        print(customerName + '\'s total is', customerTotal)



def nameInfo(fullName):
    """
    This is a simple function to be used as an example. It takes a name
    (assigned to the fullName variable), splits it into a list and then
    returns the first element in that list (the first name). You need to
    modify this function so that, in addition to returning firstName,
    it prints out the total number of letters in the customer's full name.
    Parameters
    ----------
    fullName : str 
        A full name, with each name separated by a space

    Returns
    -------
    firstName : str
        The first name (all characters before the first space)

    """
    
    nameList = fullName.split()
    firstName = nameList[0]
    
    counter = 0
    for name in nameList:
        counter += len(name)
    
    print('There are', counter, 'letters in', fullName)
    
    return firstName



def calculateTotal(someName):
    """
    You need to complete this function. It takes a customer's name
    (assisgned to the someName variable) and uses it to ask the user
    to start entering purchases (numbers) for that customer. It will
    use a while loop to do so, looping until the user is done. Then
    it will caclulate the total, excluding the customer's smallest
    purchase (smallest number entered).

    Parameters
    ----------
    someName : str
        The name of the customer

    Returns
    -------
    total : float
        The total of the customer's purchases, excluding the smallest
        purchase (e.g., the total of 4, 2, 5, 3 and 5 would be 17)

    """
    total = 0
    priceList = []
    entering = True
    print('To end loop enter "stop"')
    while entering:
        priceStr = input('Enter a purchase ')
        if priceStr.lower() == 'stop':
            entering = False
            break
        elif priceStr.isnumeric():
            priceList.append(int(priceStr))
        else:
            print("Please enter a number")
    priceList.sort()
    if len(priceList) >= 2:
        total = sum(priceList) - priceList[0]
    else:
        total = sum(priceList)
    return total



    
main() # We need the call to main here, after all functions have been defined
