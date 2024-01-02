import sys

def factorization(n):
    def smallest_factor(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return n  # Return n itself if it's prime

    p = smallest_factor(n)
    q = n // p

    return p, q

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read numbers from the file and factorize each number
    try:
        with open(input_file, 'r') as file:
            numbers = file.readlines()
            for num in numbers:
                num = int(num.strip())
                p, q = factorization(num)
                result = "{}={}*{}".format(num, q, p)
                print(result)

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid input in the file.")
        sys.exit(1)

