import math

palindrome = input("Provide a number or string:")
prime = int(input("Provide a number:"))

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

if palindrome[::-1] == palindrome:
    print(f"{palindrome} is palindrome")
else: print(f"{palindrome} is not palindrome")

if is_prime(prime):
    print(f"Number {prime} is prime")
else: print(f"Number {prime} is not prime")