def caching_fibonacci():
    cache_fib = {}

    def fibonacci(n):
        #Check if value is not negative
        if n < 0:
            raise ValueError("Number cannot be negative")
        
        #Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        #If cached value exists
        if n in cache_fib:
            return cache_fib[n]
        # Calculate and cache the value
        cache_fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache_fib[n]
    
    return fibonacci