# Yield is a keyword that is used like return,
# except the function will return a generator.

# Traditional function that returns a list of factors.
def factors(n):
    results = []  # Store factors in a new list
    for k in range(1, n + 1):
        if n % k == 0:  # If k is a factor of n
            results.append(k)
    return results  # Return the entire list at once


# Generator function using yield
def factors_yield(n):
    for k in range(1, n + 1):
        if n % k == 0:
            print(f"Yielding {k}")  # Print to show when yield happens
            yield k  # Pause here and return k to the caller


# Optimized version iterating up to sqrt(n)
def factors_sqrt(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            print(f"Yielding {k}")
            yield k
            print(f"Yielding {n // k}")
            yield n // k
        k += 1
    if k * k == n:
        print(f"Yielding {k}")  # Perfect square case
        yield k


# Using 'yield from' to delegate work
def factors_combined(n):
    print(f"Starting 'yield from' for {n}")
    yield from factors_sqrt(n)  # Delegates to another generator
    print("Finished 'yield from'")


def main():
    print("\nTraditional function (returns all factors at once):")
    print(factors(100))

    print("\nGenerator function (step-by-step using yield):")
    gen1 = factors_yield(100)
    for value in gen1:  # Iterate to see the pausing effect
        print(f"Received: {value}")

    print("\nOptimized generator function (yielding factors in pairs):")
    gen2 = factors_sqrt(100)
    for value in gen2:
        print(f"Received: {value}")

    print("\nUsing 'yield from' (delegation in generators):")
    gen3 = factors_combined(100)
    for value in gen3:
        print(f"Received: {value}")


if __name__ == '__main__':
    main()
