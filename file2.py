# A python program to implement the knapsack problem using dynamic programming

"""
A knapsack problem is a problem where a person has a certain weight capacity 
and a list of items with weights and values. The goal is to choose the items in 
such a way that the total weight is less than or equal to the capacity and 
the total value is maximized.
"""

#Define the knapsack function
def knapsack(capacity, items):
    #Create a matrix to store the values
    matrix = [[0 for x in range(capacity + 1)] for x in range(len(items) + 1)]

    #Fill the matrix
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if items[i - 1][1] <= j:
                matrix[i][j] = max(items[i - 1][0] + matrix[i - 1][j - items[i - 1][1]], matrix[i - 1][j])

            else:
                matrix[i][j] = matrix[i - 1][j]

    #Find the items that were used
    result = []
    i = len(items)
    j = capacity
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            result.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    #Return the result
    return result

#Define the main function
def main():
    #Define the capacity of the knapsack
    capacity = 5

    #Define the items
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]

    #Print the result
    print(knapsack(capacity, items))

#Call the main function
if __name__ == '__main__':
    main()
