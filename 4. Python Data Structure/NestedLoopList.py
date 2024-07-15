'''
Nested List : Nested list also known as 2d list, Each list is a row with columns within the collection. List are zero indexed
'''

fruits = [
    ["apples", "berries", "Kiwi"],
    ["oranges", "berries", "plums"],
    ["mangoes", "bananas", "coconuts"],
    ["pineapples"]
]

print(fruits[1][1])

for row in fruits:
    for col in row:
        print(col)
