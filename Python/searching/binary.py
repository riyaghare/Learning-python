pos = -1  # This global variable will store the position of the found element
 
def search(lst, n):
    l = 0  # Lower bound of the search interval
    u = len(lst) - 1  # Upper bound of the search interval
    m = 0  # Count the number of iterations
 
    while l <= u:
        m += 1  # Increment iteration count
        mid = (l + u) // 2  # Find the middle index
        print(f"Iteration: {m}, checking position: {mid}, value: {lst[mid]}")
        
        if lst[mid] == n:
            globals()['pos'] = mid
            return mid, m  # Return position and iteration count
        elif lst[mid] < n:
            l = mid + 1  # Move the lower bound up
        else:
            u = mid - 1  # Move the upper bound down

    return -1, m  # If not found, return -1 and iteration count
 
# Test the function
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n = 15
print("List:", lst)
position, iterations = search(lst, n)
if position != -1:
    print(f"Number found at position: {position} in {iterations} iterations")
else:
    print(f"Number not found in {iterations} iterations")
