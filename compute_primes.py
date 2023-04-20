import csv
import random


def main():
    """
    Sieve of Eratosthenes: Algorithm to compute all primes
    up to a given value.
    """
    print("\n\t\t-----------------------------\n",
          "\t\t--- Sieve of Eratosthenes ---\n",
          "\t\t-----------------------------\n\n")
    inputNum = int(input("Input maximum integer to compute all lesser prime numbers: "))
    primes = findPrimes(inputNum)
    numProducts = int(input("Input the number of prime products to compute: "))
    primeProducts = genPrimeProducts(primes, numProducts)
    print("Writing prime products to output/gen_primes.csv")
    with open("output/gen_primes.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in primeProducts:
            writer.writerow(row)
    print("\nComputed primes: ", primes)


def findPrimes(maxVal):
    """
    A simple algorithm for computing all primes up to a given value,
    The Sieve of Eratosthenes:
    1) List all integers from 2 up to the given value
    2) Add the minimum of the list to the (initially empty) set of primes
    3) Cross out the minimum and all its multiples from the list
    4) Repeat 2-4 until the list of candidate primes is empty

    This implementation uses sets to represent the lists of candidates
    and primes. To 'cross out' candidate primes, the candidate set is
    replaced by the difference between itself and the values to be crossed
    out. The set of candidates is iteratively crossed out until it is empty,
    at which point all primes have been found. 
    """
    # Set of all integers from 2 to input value are candidate primes
    candidates = set(x for x in range(2, maxVal))
    # List of primes in specified range is initially empty
    primes = list()
    while len(candidates) > 0:
        # Take out min of the set, it is prime
        minVal = min(candidates)
        primes.append(minVal)
        # Take out all multiples of the current prime
        diff = set(x for x in range(minVal, maxVal, minVal))
        candidates = candidates.difference(diff)
    return(primes[1:])


def genPrimeProducts(primes, numProducts):
    rows = list()
    for i in range(1, numProducts + 1):
        # Choose two random primes
        p1 = random.choice(primes)
        p2 = random.choice(primes)
        # Calc the product and add tuple to list
        row = (p1, p2, p1 * p2)
        rows.append(row)
    return(rows)


if __name__ == "__main__":
    main()
