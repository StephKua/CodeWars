def divisors(integer):
    answer = [d for d in range(2,integer-1) if integer % d == 0 ] 
    return answer if answer != [] else str(integer) + " is prime"