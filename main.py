#taking an input from user
st = input("Enter a string: ")
#Using the upper() function to capitalize all letters in the string
st = st.upper()

for letter in st:
    #If the character is a vowel, skip to the next character
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    #Printing characters that are not letters
    print(letter, end="")
