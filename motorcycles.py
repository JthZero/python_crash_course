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