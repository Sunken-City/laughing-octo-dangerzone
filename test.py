test = """
Trying out the
Triple double quote
String notation
"""
print test

test = "NR"
print test*5

test = "I only want*this part*of the string"
print test[12:21]

#Writing the fibonacci sequence seems to be really easy:
a, b = 0, 1
while b < 1000:
    print b,
    a, b = b, a+b

asdf = ":) "
print asdf*10