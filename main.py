#Sukhmaan Singh
text = str(input("Import any piece of text: ")).lower()  #Asks user for text
first = str(input("Enter First Letter: ")).lower(
)  #Asks the user for a letter to search in text
print("First Letter:", first)  #Prints the letter provided
second = str(input("Enter Second Letter: ")).lower(
)  #Asks the user for a letter to search in text
print("First Letter:", second)  #Prints the letter provided
third = str(input("Enter Third Letter: ")).lower(
)  #Asks the user for a letter to search in text
print("Third Letter:", third)  #Prints the letter provided

#the reason for the .lower is so when our code is searching for the letter provided by the user it will find the total amount of letters in the given text because we lowered the text

searchfirst = text.count(first)
print(f"The first letter appears {searchfirst} times")

searchsecond = text.count(second)
print(f"The second letter appears {searchsecond} times")

searchthird = text.count(third)
print(f"The third letter appears {searchthird} times")

letters = {
    "firstletter": searchfirst,
    "secondletter": searchsecond,
    "thirdletter": searchthird
}
wordsInText = len(text.split())
print("The amount of words in the text is {} words".format(wordsInText))

first_letter = text[0]
last_letter = text[-1]
print("The first letter of the text is {} and the last letter is {}".format(
    first_letter, last_letter))

# reversing words in a given string
a = text.split()[::-1]
b = []
for i in a:  #i is a temporary variable that stores a value
  # appending reversed words to l
  b.append(i)
# printing reverse words
print("Reversed Order: ")
print(" ".join(b))

specialWord = "Python" and "python"
result = specialWord in text
print("Python in text = {}".format(result))
