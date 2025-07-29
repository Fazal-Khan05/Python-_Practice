def prime (n):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number.")
        else:
            print(f"{n} is a prime number.")
            break

n = int(input("Enter a number to check if it is prime: "))
prime(n)
            