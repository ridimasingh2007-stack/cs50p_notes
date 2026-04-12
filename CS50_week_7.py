

# Regular expression ----

# email = input("Enter your email address: ").strip()

# if "@" in email and "." in email: # cheching if the email contains "." also to make it more valid

#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# username, domain = email.split("@")

# if username and "." in domain:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


# if username and domain.endswith(".edu"):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# re lib -- used to define and check for patterns 
# re.search(pattern, string, flags=0) -- returns a match object if the pattern is found in the string, 
# otherwise returns None here patteren is the regex pattern we want to search for, 
# string is the input string we want to check against the pattern and flags is an optional argument 
# that can be used to modify the behavior of the search (e.g., making it case-insensitive).

# import re

# email = input("Enter your email address: ").strip()

# if re.search(".+@.+", email): # here * means zero or more characters before and after the @ symbol and + means one or more characters after the @ symbol and before the dot
#     print("Valid email address.") 
# else:  
#     print("Invalid email address.")

# if re.search(r".+@.+\.(edu)", email): # here we are using raw string notation (r"") to avoid having to escape the backslash character in the regex pattern and \. is used to match a literal dot character in the email address. 
#     print("Valid email address.")
# else:  
#     print("Invalid email address.")

# ^ -- matches the start of the string
# $ -- matches the end of the string or before a newline character

# if re.search(r"^.+@.+\.(edu)$", email):
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# [] -- matches any single character within the brackets. For example, [abc] matches any of the characters 'a', 'b', or 'c'.
# [^] -- matches any single character that is not within the brackets. For example, [^abc] matches any character that is not 'a', 'b', or 'c'.

# if re.search(r"^[^@]+@[^@]+\.+(edu)$", email):
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(edu)$", email):
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# \d -- matches any digit character (0-9)
# \D -- matches any non-digit character
# \s -- matches any whitespace character (spaces, tabs, newlines)
# \S -- matches any non-whitespace character
# \w -- matches any alphanumeric character (letters and digits) and the underscore character. It is equivalent to [a-zA-Z0-9_].
# \W -- matches any non-alphanumeric character (characters that are not letters, digits, or underscores)


# if re.search(r"^\w+@\w+\.(edu)$", email): 
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# A|B -- matches either pattern A or pattern B. For example, (cat|dog) matches either "cat" or "dog".

# if re.search(r"^\w+@\w+\.(edu)$", email):
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# flags -- re.IGNORECASE or re.I -- makes the regex search case-insensitive
# re.MULTILINE or re.M -- allows the ^ and $ anchors to match the start 
# re.DOTALL or re.S -- allows the . character to match newline characters as well


# if re.search(r"^\w+@(\w+\.)?\w+\.(edu)$", email, re.IGNORECASE): 
#     print("Valid email address.")
# else:   
#     print("Invalid email address.")

# re.match() -- checks for a match only at the beginning of the string and re.fullmatch() -- checks for a match of the entire string against the pattern.

# name = input("Enter your name: ").strip()
# if "," in name:
#     last, first = name.split(",")
#     name = f"{first.strip()} {last.strip()}"
# print(f"Hello, {name}!")

# import re
# name = input("Enter your name: ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}!")

# := -- walrus operator -- allows you to assign a value to a variable as part of an expression.

# name = input("Enter your name: ").strip()
# if matches := re.search(r"^(.+), *.+)$", name):

#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}!")

# url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# re.sub(pattern, replacement, string) -- replaces all occurrences of the pattern in the string with the replacement string.

# import re  
# url = input("URL: ").strip()

# username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url) 
# print(f"Username: {username}")

# matches = re.search(r"^https?://(www\.)?twitter\.com(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

# using walrus operator
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(1))




