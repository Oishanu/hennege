# THIS CODE IS SUBMITTED BY SURYANSHU CHOUDHARY (suryanshuc30@gmail.com) FOR THE INTERNSHIP EVALUATION OF HENNEGE CHALLENGE

def calculate_sum_of_squares():

    # Read the number of test cases
    num_test_cases = int(input())
    
    # Initialize an empty list to store the results
    results = []
    
    # process each test case here
    def process_test_case(n):
        if n == 0:
            return
        # Read the number of integers in this test case
        num_integers = int(input())
        
        # Read the integers themselves
        integers = input().split()
        
        # Initialize the sum of squares to 0 to calculate the final sum
        sum_of_squares = 0
        
        # Use recursion to process each integer
        def process_integer(i):
            nonlocal sum_of_squares
            if i == num_integers:
                return
            # Get the current integer
            integer = int(integers[i])
            
            # If the integer is non-negative, add its square to the sum
            if integer >= 0:
                sum_of_squares += integer ** 2
            
            # Recursively process the next integer
            process_integer(i + 1)
        
        # Start processing the integers
        process_integer(0)
        
        # Append the result to the list of results
        results.append(sum_of_squares)
        
        # Recursively process the next test case
        process_test_case(n - 1)
    
    # Start processing the test cases
    process_test_case(num_test_cases)
    
    # Print the results
    for result in results:
        print(result)

# Call the outer function
calculate_sum_of_squares()
