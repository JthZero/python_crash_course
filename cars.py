# Organizing a list 
# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
cars.sort()  # Sort the list in alphabetical order
print(cars)  # Print the sorted list    

# Sorting a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
cars.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(cars)  # Print the list sorted in reverse order

# Sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
print(sorted(cars))  # Print the list sorted temporarily in alphabetical order
print(cars)  # Print the original list again to show it remains unchanged

# Sorting a list temporarily in reverse order with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
print(sorted(cars, reverse=True))  # Print the list sorted temporarily in reverse order
print(cars)  # Print the original list again to show it remains unchanged

# Reversing the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
cars.reverse()  # Reverse the order of the list
print(cars)  # Print the list after reversing

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
print(len(cars))  # Print the length of the list


# Slicing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # Print the original list
print(cars[0:3])  # Print the first three cars
print(cars[1:4])  # Print the last three cars
print(cars[:3])  # Print the first three cars using slicing
print(cars[1:])  # Print all cars starting from the second one
print(cars[-3:])  # Print the last three cars using negative indexing
print(cars[-3:-1])  # Print the second and third last cars using negative indexing  