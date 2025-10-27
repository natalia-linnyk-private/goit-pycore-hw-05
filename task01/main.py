from caching_fibonacci import caching_fibonacci

def main():
    try:
        fib = caching_fibonacci()
        print(fib(10))
        print(fib(15))
        print(fib(-10))
    except ValueError as err:
        print(err)
    except Exception as err:
        print("Error happened: ", err)

if __name__ == "__main__":
    main()