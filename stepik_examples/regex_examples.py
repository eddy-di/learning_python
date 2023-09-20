import re


# names = ['Finn Bindeballe',
#          'Geir Anders Berge',
#          'HappyCodingRobot',
#          'Ron Cromberge',
#          'Sohil']

# # Find people with first and last name only
# regex = '^\w+ \w+$'

# for name in names:
#     result = re.search(pattern=regex,string=name)
#     if result:
#         print(result)

# # Search for word char sequence starting with C

# regex1 = 'C\w*'
# for name in names:
#     match = re.search(regex1, name)
#     if match:
#         print(name)
#         print(match.span())
#         print(match.group())

names = ['Brian Daugette', 'Veronica Supersonica', 'Tony Gasparovic', 'Patrick Germann', 'm!sha']

# Test for 1 name and last name
# regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$' # parantheses allow you to group expressions

# for name in names:
#     match = re.search(regex, name)
#     if match:
#         print(name)
#         print(match.group('fn'))
#         print(match.group('ln'))


# detecting last name in list
# regex = '^[a-zA-Z!]+$'
# for name in names:
#     if re.search(regex, name):
#         print(name)


# re.findall(pattern, string, flags=0) Return all non-overlapping matches of pattern in string, as a list of strings or tuples

# Scan for block of lower case letters
regex = '[a-z]+'
for name in names:
    matches = re.findall(regex, name)
    if matches:
        print(matches)