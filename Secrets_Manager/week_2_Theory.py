import time

def bubble_sort(arr):
    n = len(arr)
    print(f"Original List: {arr}\n")
    
    # Traverse through all elements
    for i in range(n):
        print(f"Pass {i + 1}:")
        swapped = False  # To track if any swapping happens

        # Last i elements are already sorted, so ignore them
        for j in range(0, n - i - 1):
            print(f" Comparing {arr[j]} and {arr[j + 1]}")
            
            # Swap if elements are in the wrong order
            if arr[j] > arr[j + 1]:
                print(f"  Swapping {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print("  No swap needed")

        print(f"Result after pass {i + 1}: {arr}\n")

        # If no elements were swapped, the list is already sorted
        if not swapped:
            print("No swaps in this pass, so the list is sorted early!")
            break
    
    print(f"Final Sorted List: {arr}")
    return arr

# Example for bubble sort
numbers = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(numbers)

# Idea: Build the sorted list one element at a time.
# For each element, insert it into the correct position
# among the elements before it.
def insertion_sort(arr):
    print(f"Original List: {arr}\n")

    # Start from the 2nd element (index 1), since the first element is "sorted"
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to insert
        j = i - 1
        print(f"Step {i}: Insert {key} into the sorted part {arr[:i]}")

        # Shift elements of the sorted portion that are greater than key
        while j >= 0 and arr[j] > key:
            print(f"  {arr[j]} is greater than {key}, shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key
        print(f"Inserted {key}, current list: {arr}\n")

    print(f"Final Sorted List: {arr}")
    return arr


# Example usage for insertion sort
numbers = [12, 11, 13, 5, 6]
# insertion_sort(numbers)

# Quick Sort in Python
# Idea: Divide and Conquer
# 1. Choose a pivot
# 2. Partition: put smaller elements on the left, larger on the right
# 3. Recursively sort the sublists
def quick_sort(arr, depth=0):
    indent = " " * depth  # for pretty printing recursion depth
    
    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        print(f"{indent}Returning {arr} (already sorted)")
        return arr
    
    # Choose pivot (here: middle element)
    pivot = arr[len(arr) // 2]
    print(f"{indent}Pivot chosen: {pivot} from {arr}")
    
    # Partition step
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"{indent}Left: {left}, Middle: {middle}, Right: {right}")
    
    # Recursively apply quicksort to left and right, combine results
    return quick_sort(left, depth + 1) + middle + quick_sort(right, depth + 1)


# Example usage for quick sort
numbers = [10, 7, 8, 9, 1, 5]
# print("Original List:", numbers, "\n")
# sorted_numbers = quick_sort(numbers)
# print("\nFinal Sorted List:", sorted_numbers)

# Linear Search in Python
# Linear search means we go through the list one by one
# until we find the target element or reach the end.
def linear_search(arr, target):
    start = time.time()
    print(f"Searching for {target} in {arr}")
    
    # Go through the list element by element
    for index in range(len(arr)):
        print(f"Step {index + 1}: Checking element at index {index} -> {arr[index]}")
        
        # If the current element matches the target, return its position
        if arr[index] == target:
            end = time.time()
            print(f"Found {target} at index {index}")
            print(f"Search took {end - start:.6f} seconds.")  # ✅ always prints time
            return index
    
    # If loop finishes without finding the target
    end = time.time()
    print(f"{target} was not found in the list.")
    print(f"Search took {end - start:.6f} seconds.")
    return -1


def linear_search_enumerate(arr, target):
    start = time.time()
    print(f"Searching for {target} in {arr}")
    
    # Go through the list element by element
    for step, value in enumerate(arr, start=1):
        print(f"Step {step}: Checking element at index {step - 1} -> {value}")
        
        # If the current element matches the target, return its position
        if value == target:
            end = time.time()
            print(f"Found {target} at index {step - 1}")
            print(f"Search took {end - start:.6f} seconds.")  # ✅ always prints time
            return step - 1
    
    # If loop finishes without finding the target
    end = time.time()
    print(f"{target} was not found in the list.")
    print(f"Search took {end - start:.6f} seconds.")
    return -1
# Example usage for linear search
numbers = [10, 23, 45, 70, 11, 15]

# Try searching for a number that exists
# linear_search(numbers, 70)
# linear_search_enumerate(numbers, 70)

# print("\n---\n")

# # Try searching for a number that does not exist
# linear_search(numbers, 99)
# linear_search_enumerate(numbers, 99)

# Binary Search in Python
# Works only on a sorted list
# Idea: Repeatedly divide the search range in half until the target is found.
def binary_search(arr, target):
    print(f"Searching for {target} in {arr}")
    
    left = 0
    right = len(arr) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: Checking middle index {mid} -> {arr[mid]}")
        
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}, so search right half.")
            left = mid + 1
        else:
            print(f"{target} is smaller than {arr[mid]}, so search left half.")
            right = mid - 1
        
        step += 1
    
    print(f"{target} was not found in the list.")
    return -1


# Example usage for binary search
numbers = [11, 15, 23, 45, 70, 80, 99]  # Sorted list

# Searching for a number that exists 
# binary_search(numbers, 70)

# print("\n---\n")

# # Searching for a number that does not exist
# binary_search(numbers, 50)

# Simple Hashing Example in Python

# Step 1: Define a hash function
# We'll use a simple hash function: value modulo table size
def simple_hash(key, table_size):
    return key % table_size
# 5 % 10 = 5
# 10 % 10 = 0
# 11 % 10 = 1

# Step 2: Create a hash table with chaining to handle collisions
def create_hash_table(size):
    # Each slot will hold a list to handle collisions
    return [[] for _ in range(size)]

# Step 3: Insert a value into the hash table
def insert(hash_table, key, value):
    index = simple_hash(key, len(hash_table))
    print(f"Inserting ({key}, {value}) at index {index}")
    
    # Check if key already exists and update
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            return
    
    # If not, append the key-value pair
    hash_table[index].append([key, value])

# Step 4: Search for a value by key
def search(hash_table, key):
    index = simple_hash(key, len(hash_table))
    print(f"Searching for key {key} at index {index}")
    
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f"Found value: {pair[1]}")
            return pair[1]
    
    print("Key not found")
    return None

# Step 5: Demonstrate the hash table
hash_table = create_hash_table(10)

# Insert some key-value pairs
insert(hash_table, 1, "Alice")
insert(hash_table, 2, "Bob")
insert(hash_table, 3, "Charlie")
insert(hash_table, 5, "David")
insert(hash_table, 6, "Alice2")
insert(hash_table, 7, "Bob2")
insert(hash_table, 8, "Charlie2")
insert(hash_table, 9, "David2")

# Print table state
print("\nHash Table State:")
for i, bucket in enumerate(hash_table):
    print(f"Index {i}: {bucket}")

# Search examples
print("\nSearch Examples:")
search(hash_table, 2)  # Should find Bob
search(hash_table, 5)  # Should find David
search(hash_table, 0)  # Should report not found
