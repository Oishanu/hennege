import sys

def process_test_cases(data, index=0, results=[]):
    if index >= len(data):
        return results
    
    X = int(data[index])  # Number of integers in this test case
    numbers = list(map(int, data[index + 1].split()))
    
    # Calculate the sum of squares of non-negative integers
    sum_of_squares = sum(map(lambda y: y * y, filter(lambda x: x >= 0, numbers)))
    
    # Accumulate results
    results.append(str(sum_of_squares))
    
    # Recursively process the next test case
    return process_test_cases(data, index + 2, results)

# def main():
#     input_data = sys.stdin.read().strip().splitlines()
#     results = process_test_cases(input_data[1:])
    
#     # Output results without extra blank lines
#     sys.stdout.write("\n".join(results) + "\n")

def main():
    n = int(input())
    results = []
    for _ in range(n):
        x = int(input())
        nums = list(map(int, input().split()))
        sum_of_squares = sum(num ** 2 for num in nums if num > 0)
        results.append(str(sum_of_squares))
    print("\n".join(results))

if __name__ == "__main__":
    main()
    