import sys

def factorize(number):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        factorizations = {}
        with open(input_file, 'r') as file:
            numbers = file.readlines()
            for num in numbers:
                num = int(num.strip())
                if num not in factorizations:
                    factor_pairs = factorize(num)
                    factorizations[num] = factor_pairs

        for num, factors in factorizations.items():
            for pair in factors:
                print(f"{num}={pair[0]}*{pair[1]}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid input in the file.")
        sys.exit(1)

