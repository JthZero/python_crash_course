first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f-strings f is for format
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# Adding Whitespace to Strings With Tabs or Newlines
print("Languages: \n\tPython, \n\tC++, \n\tJavaScript")

# Stripping Whitespace
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())  # Remove trailing whitespace
print(favorite_language.lstrip())  # Remove leading whitespace
print(favorite_language.strip())   # Remove both leading and trailing whitespace

print(len(favorite_language))  # Length of the string
print(len(favorite_language.rstrip()))  # Length after stripping whitespace  
print(len(favorite_language.lstrip()))  # Length after stripping leading whitespace
print(len(favorite_language.strip()))  # Length after stripping both sides

# Removing prefixes
nostach_url = 'https://nostach.io'
print("\n" + nostach_url.removeprefix('https://'))  # Remove 'https://'
print(f"\n{nostach_url.removeprefix('https://')}")  # Remove 'https://'

