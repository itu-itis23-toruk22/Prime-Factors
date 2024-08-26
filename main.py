def control(num1, num2 = 0):
    return num1 > num2

#-------------------------------------------

def get_prime_factors(num):
    
    factors = []
    divisor = 2
    
    if control(num, 0):
        while num > 1:
            if num % divisor == 0:
                factors.append(divisor)
                num /= divisor
            else:
                divisor += 1
            
        return factors
        
    print("Invalid number!")
    return factors
    
#-------------------------------------------

def is_prime(num):
    if control(num, 1):
        return len(get_prime_factors(num)) == 1
    
    return False
    
#-------------------------------------------

def gcd(num1, num2): #Euclid Algorithm
    
    while num2 != 0:
        num1, num2 = num2 , num1 % num2 
    return num1
    

#-------------------------------------------

def main():
    while True:
        
        inp = int(input("\nChoose operations:\n1-Prime Factors\n2-Is Prime\n3-Greatest Common Divisor\n0-Exit\n"))
        num1 = 1
        num2 = 1
        if inp == 0:
            break
        elif inp == 1:
            num1 = int(input("Enter a number: "))
            print("Prime factors of {}: {}".format(num1, get_prime_factors(num1)))
            
        elif inp == 2:
            num1 = int(input("Enter a number: "))
            print("{} is prime number.".format(num1) if is_prime(num1) else "{} is not prime number.".format(num1))
            
        elif inp == 3:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Greatest common divisor of {} and {} is {}.".format(num1, num2, gcd(num1, num2)))
            
        else:
            print("Invalid command!")
            
    
#-------------------------------------------

main()