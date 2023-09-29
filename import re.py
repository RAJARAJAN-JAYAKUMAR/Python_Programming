import re
"""
findall -	Returns a list containing all matches
search  -	Returns a Match object if there is a match anywhere in the string
split   -	Returns a list where the string has been split at each match
sub     -	Replaces one or many matches with a string
"""
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
