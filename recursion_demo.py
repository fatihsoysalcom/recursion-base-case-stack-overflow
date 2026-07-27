import sys

def factorial(n):
    """Calculates the factorial of a non-negative integer using recursion."""
    # Base Case: The simplest case that stops the recursion.
    # If n is 0 or 1, the factorial is 1.
    if n == 0 or n == 1:
        print(f"Base case reached for n={n}. Returning 1.")
        return 1
    else:
        # Recursive Step: The function calls itself with a smaller input.
        # This breaks the problem down into smaller, similar subproblems.
        print(f"Recursive step for n={n}. Calling factorial({n-1}).")
        return n * factorial(n - 1)

def infinite_recursion(n):
    """Demonstrates infinite recursion leading to stack overflow."""
    # This function lacks a proper base case and will call itself indefinitely.
    print(f"Infinite recursion at n={n}. Calling infinite_recursion({n+1}).")
    # To prevent immediate crash, we'll add a safety break after many calls,
    # but conceptually, this is what causes stack overflow.
    if n > 1000: # Safety break to avoid immediate hard crash
        print("Safety break reached to prevent immediate crash.")
        return
    infinite_recursion(n + 1)

if __name__ == "__main__":
    # Example 1: Factorial calculation (demonstrates base case and recursion)
    print("--- Factorial Calculation ---")
    num = 5
    print(f"Calculating factorial of {num}:")
    result = factorial(num)
    print(f"Factorial of {num} is: {result}")
    print("\n")

    # Example 2: Demonstrating potential stack overflow
    # Python has a default recursion depth limit to prevent actual crashes.
    # We can try to exceed it to show the concept.
    print("--- Stack Overflow Demonstration ---")
    print("Attempting to demonstrate stack overflow (Python has a limit).")
    print("This will likely stop due to Python's recursion depth limit before a true OS stack overflow.")
    try:
        # Increase recursion depth limit for demonstration purposes
        # Be cautious with very high numbers as it can still crash your system.
        sys.setrecursionlimit(2000) # Default is often around 1000
        print(f"Current recursion limit set to: {sys.getrecursionlimit()}")
        infinite_recursion(1)
    except RecursionError as e:
        print(f"Caught expected RecursionError: {e}")
        print("This demonstrates that the call stack has a finite size.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
