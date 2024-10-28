##################################################
# Name:Aris Whitney
# Collaborators:N/A
# Estimate of time spent (hr):2
##################################################

def is_magic_square(array: list[list[int]]) -> bool:
    # Check if the outer list and inner lists have the same length
    n = len(array)
    if n == 0 or any(len(row) != n for row in array):
        return False
    
    # Calculate the magic sum from the first row
    magic_sum = sum(array[0])
    
    # Check sum of rows
    for row in array:
        if sum(row) != magic_sum:
            return False
    
    # Check sum of columns
    for col in range(n):
        if sum(array[row][col] for row in range(n)) != magic_sum:
            return False
    
    # Check sum of the main diagonal
    if sum(array[i][i] for i in range(n)) != magic_sum:
        return False
    
    # Check sum of the secondary diagonal
    if sum(array[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False
    
    return True

# Example usage
small = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
print(is_magic_square(small))  

