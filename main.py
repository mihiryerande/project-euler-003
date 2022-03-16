# Problem 3:
#     Largest Prime Factor
#
# Description:
#     The prime factors of 13195 are 5, 7, 13 and 29.
#
#     What is the largest prime factor of the number 600851475143 ?

from math import ceil, sqrt


def main(n):
    """
    Return the sorted prime factorization of `n`.

    Args:
        n (int): Natural number

    Returns:
        Prime factorization of `n` (sorted in increasing order)

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    factorization = []
    sieve = range(2, ceil(sqrt(n)))
    while len(sieve) > 0 and n > 1:
        p = sieve[0]  # Next prime to try
        sieve = [x for x in sieve if x % p != 0]  # Drop any multiple of p, including p itself
        while n % p == 0:
            n /= p
            factorization.append(p)

    if n > 1:
        # Sieve ran out of primes as it only began up to sqrt(n)
        # Remaining `n` value must be prime
        factorization.append(n)
    return factorization


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    p_fact = main(num)
    print('Prime factorization:\n{}'.format(p_fact))
    print('Largest Prime Factor:\n{}'.format(p_fact[-1]))
