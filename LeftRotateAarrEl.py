# Function to solve and shift array elements left by one position
def solve(arr, n):
    temp = [0] * n  # Create a temporary array to store the shifted elements

    # Shift the elements to the left by one position
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]  # The first element moves to the last position

    # Print the rotated array
    for num in temp:
        print(num, end=" ")  # Print each element of the rotated array
    print()

# Main function
if __name__ == "__main__":
    n = 5  # Size of the array
    arr = [1, 2, 3, 4, 5]  # Original array

    solve(arr, n)  # Call the solve function to rotate and print the result
