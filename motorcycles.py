# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'  # Change the first motorcycle
print(motorcycles)

# Adding elements to a list
# Appending elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')  # Add 'ducati' to the end of the
print(motorcycles)  # Print the updated list

motorcycles = []
motorcycles.append('honda')  # Add 'honda' to the empty list
motorcycles.append('yamaha')  # Add 'yamaha'
motorcycles.append('suzuki')  # Add 'suzuki'
print(motorcycles)  # Print the list with three motorcycles

# Inserting elements at a specific position
motorcycles.insert(1, 'harley')  # Insert 'harley' at the beginning
print(motorcycles)  # Print the updated list

# Removing elements from a list
# Removing an item using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # Print the original list
del motorcycles[0]  # Remove the first motorcycle
print(motorcycles)  # Print the list after deletion 

# Removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # Print the original list
popped_motorcycle = motorcycles.pop()  # Remove the last motorcycle
print(motorcycles)  # Print the list after popping
print(popped_motorcycle)  # Print the popped 

# Popping items from any position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  # Pop the first motorcycle
print(motorcycles)  # Print the list after popping
print(f"The first motorcycle I owned was a {first_owned.title()}.")  # Print the first owned motorcycle

# Removing an item by value using remove()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # Print the original list
motorcycles.remove('yamaha')  # Remove 'yamaha' from the list
print(motorcycles)  # Print the list after removal

