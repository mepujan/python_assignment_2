# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(num):
    if num < 2:
        return False
    else:
        if num == 2 :
            return True
        else:
            for n in range(2,num):
                if num % n == 0:
                    return False
            return True

             
number= int(input("Enter the number: "))
print("Prime Number: ",is_prime(number))