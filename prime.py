def is_prime(number):
    # 0 and 1 are not prime numbers
    if number <= 1:
        return False
    # 2 and 3 are prime numbers
    if number <= 3:
        return True
    # Eliminate even numbers and multiples of 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Check divisibility from 5 to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Input from user
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
