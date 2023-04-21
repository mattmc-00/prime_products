import time
import pandas as pd
from sieve_of_eratosthenes import findPrimes


def factorPrimeProduct_BF(product):
    for i in range(3, product):
        if product % i == 0:
            return(i, product // i)


def timeFactoringFunction(factors, product, func):
    st = time.time()
    p, q = func(product)
    et = time.time()
    if p and q in factors:
        print("Factors: ({a}, {b}); Product: {c}; Time elapsed: {d:0.5f}s".
              format(a = p, b = q, c = product, d = et - st))
    else:
        print("Error, got wrong factors: {a}, {b} for {c}".
              format(a = p, b = q, c = product))


def main():
    factoringFunc = factorPrimeProduct_BF
    prime_products_df = pd.read_csv("output/primes_and_products.csv")
    for row in prime_products_df.itertuples():
        if row.Index > 100:
            break
        timeFactoringFunction([row.p, row.q], row.pq, factoringFunc)


if __name__ == "__main__":
    main()