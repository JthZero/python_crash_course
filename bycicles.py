# Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # Print the list of bicycles
print(bicycles[0])  # Print the first bicycle
print(bicycles[0].title())  # Print the first bicycle with title case
print(bicycles[-1])
print(bicycles[-1].title())  # Print the last bicycle with title case

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  # Print the message about the first bicycle
message = "My last bicycle was a " + bicycles[-1].title() + "."
print(message)  # Print the message about the last bicycle