"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import math

def is_prime(num):
    # Numbers less than 2 are not prime.
    if num < 2:
        return False
    else:
        # We check if the number is divisible by some number from 2 to half the number.
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        else:
            return True

def is_fibo(num):
    # We check if 5n^2 + 4 is a perfect square number.
    raiz1 = math.isqrt(5 * num * num + 4)
    if raiz1 * raiz1 == 5 * num * num + 4:
        return True
    
    # We check if 5n^2 - 4 is a perfect square number.
    raiz2 = math.isqrt(5 * num * num - 4)
    if raiz2 * raiz2 == 5 * num * num - 4:
        return True
    
    # If neither of the two previous conditions is met, 
    # the number does not belong to the Fibonacci series.
    return False

def is_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def find_out(num):
    is_prime_result = is_prime(num)
    is_fibo_result = is_fibo(num)
    is_par_result = is_par(num)

    if is_prime_result == True:
        is_prime_str = "is prime"
    else:
        is_prime_str = "not is prime"
    
    if is_fibo_result == True:
        is_fibo_str = "is fibonaci"
    else:
        is_fibo_str = "not is fibonaci"
    
    if is_par_result == True:
        is_par_str = "is an even"
    else:
        is_par_str = "is not an even"
    
    return f"{num}: {is_prime_str}, {is_fibo_str} and {is_par_str}."


while True:
    try:
        num = int(input("enter the number you want to check: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

result = find_out(num)
print(result)