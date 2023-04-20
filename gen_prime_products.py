import csv
import random
from sieve_of_eratosthenes import findPrimes


def main():
    inputNum = int(input("Input maximum integer to compute all lesser prime numbers: "))
    primes = findPrimes(inputNum)
    numProducts = int(input("Input the number of prime products to compute: "))
    primeProducts = genPrimeProducts(primes, numProducts)
    print("Writing prime products to output/gen_primes.csv")
    with open("output/primes_and_products.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in primeProducts:
            writer.writerow(row)


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
