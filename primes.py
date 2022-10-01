"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError(f"number of primes = {number_of_primes} should have beem a positive number.") # Raises a value error if number is not positive.


        
    list = []
    count = 0 #Keeps the count of for the numbers needed to be print.
    num = 2 # Start with smallest prime and get incremented.
    while count < number_of_primes:  # Keeps running till entered number of prime numbers are added to the list.
       
        for i in range(2,(num//2)+1):  # Loops from 2 to (num//2)+1, to check the if the number is divisibility
            if num%i==0: 
                break 
        else:               #If number is not divivsible, num is added to the list
            list.append(num);
            count+=1  #increments the count
        num+=1  #increments the number

    return list


