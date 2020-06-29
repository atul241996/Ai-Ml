digittowordmap = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}

digit = input("Input please")
word = ''
for item in digit:
    word += digittowordmap.get(item,"!")

print(word)
