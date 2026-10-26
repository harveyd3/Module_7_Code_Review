def doubles_even_triples_odd(numbers_list):
    """
    Function takes a list of numbers from the numbers_list parameter. These values are used for calculations.
    If a number is even then it gets multiplied by 2, but if the number is odd then it gets multiplied by 3.
    Finally, the function returns the value of completed list of calculated numbers.
    """
    calculated_numbers = [(number * 2) if number % 2 == 0 else (number * 3) for number in numbers_list]
    return calculated_numbers

def lowercase_uppercase_fruits(fruits_list):
    """
    Functions creates an empty string to store the processed fruit names.
    Uses for loops to make strings greater than 5 uppercase letters and strings less than 5 lowercase letters.
    Returns the finalized fruit strings. The finalized string uses strip to clean up the names by removing whitespace
    at the beginning and end of the string.
    """
    finalized_fruits = ""
    for fruit in fruits_list:
        if len(fruit) > 5:
            finalized_fruits += fruit.upper() + " "
        else:
            finalized_fruits += fruit.lower() + " "
    return finalized_fruits.strip()


def main():
    """
    The main() function creates two lists, passing them to the processing functions, and stores the results
    in variables. Those variables are used to display the results from our functions, doubles_even_triples_odd and
    lowercase_uppercase_fruits. Finally, the function prints the processed numbers and strings.
    """
    numbers_list = [1, 2, 3, 4, 5, 6, 7]
    fruits_list = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = doubles_even_triples_odd(numbers_list)
    processed_strings = lowercase_uppercase_fruits(fruits_list)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
