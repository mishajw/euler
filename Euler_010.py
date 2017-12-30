# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def run():
    numbers = range(2,2000000)
    for i in range(len(numbers)):
        if numbers[i] != 0:
            for j in range(numbers[i]+i,len(numbers),numbers[i]):
                numbers[j] = 0
    primes = filter(lambda x: x,numbers)
    return(sum(primes))

if __name__ == "__main__":
    print(run())