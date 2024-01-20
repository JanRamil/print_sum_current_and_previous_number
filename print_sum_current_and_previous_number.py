# Print the sum of the current number and the previous number

#pseudocode

# Creating a starting point
print("Printing current and previous number and their sum in a range(10)")

# Creating a variable or name called previous_number and set to zero
previous_number = 0

# Loop from 1 to 10
for i in range(1,11):
    # Variable or name called previous_number and set to zero
    current_number = i
    # Variable called sum_of_previous_and_current_number and set it to previous_number + current_number
    sum_of_previous_and_current_number = previous_number + current_number

     # Creating code with print indicating current_number, previous_number, and sum_of_previous_and_current_number
    print(
        "The current number is",
        current_number,
        "The previous number is",
        previous_number,
        "finally, the sum of them is",
        sum_of_previous_and_current_number,
    )

    # Indicate previous_number to current_number
    previous_number = current_number


