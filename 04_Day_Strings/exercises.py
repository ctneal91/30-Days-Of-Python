# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_word = "Thirty"
second_word = "Days"
third_word = "Of"
fourth_word = "Python"
formatted_title = '%s %s %s %s' %(first_word, second_word, third_word, fourth_word)
print("1. ", formatted_title, "\n")

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = "Coding"
_for = "For"
_all = "All"
formatted_subtitle = '{} {} {}'.format(coding, _for, _all)
print("2. ", formatted_subtitle, "\n")

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = formatted_subtitle

# 4. Print the variable company using _print()_.
print("4.", company, "\n")

# 5. Print the length of the company string using _len()_ method and _print()_.
print("5.", len(company), "\n")

# 6. Change all the characters to uppercase letters using _upper()_ method.
print("6.", company.upper(), "\n")

# 7. Change all the characters to lowercase letters using _lower()_ method.
print("7.", company.lower(), "\n")

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print("8.", company.capitalize(), company.title(), company.swapcase(), "\n")

# 9. Cut(slice) out the first word of _Coding For All_ string.
print("9.", company[6:], "\n")

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print("10.", company.find("Coding"), "\n")

# 11. Replace the word coding in the string 'Coding For All' to Python.
print("11.", company.replace("Coding", "Python"), "\n")

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
print("12.", company.replace("All", "Everyone"), "\n")

# 13. Split the string 'Coding For All' using space as the separator (split())
print("13.", company.split(" "), "\n")

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14.", big_tech.split(", "), "\n")

# 15. What is the character at index 0 in the string _Coding For All_.
print("15.", company[0], "\n")

# 16. What is the last index of the string _Coding For All_.
print("16.", company[-1], "\n")

# 17. What character is at index 10 in "Coding For All" string.
print("17.", company[10], "\n")

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_company = "Python For Everyone"

def create_acronym(string):
    string_array = string.split(" ")
    acronym = ""
    for word in string_array:
        acronym += word[0]
    return acronym

print("18.", create_acronym(python_company), "\n")

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("19.", create_acronym(company), "\n")


# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print("20.", company.find("C"), "\n")

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("21.", company.find("F"), "\n")

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("22.", company.rfind("l"), "\n")

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print("23.", sentence.find("because"), "\n")

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("24.", sentence.rfind("because"), "\n")

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("25.", sentence.rfind("because because because"), "\n")

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# see 23

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("27.", sentence.replace(" because because because", ""), "\n")

# 28. Does 'Coding For All' start with a substring _Coding_?
print("28.", "Coding" in company, "\n")

# 29. Does 'Coding For All' end with a substring _coding_?
print("29.", company.endswith("coding"), "\n")

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
string = '\n\n Coding For All \n\n\n\n'
print("30.", string.strip(), "\n")

# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
def tell_if_string_is_identifier(string):
    if string.isidentifier():
        print(string, "is an identifier", "\n")
    else:
        print(string, "is not an identifier", "\n")

tell_if_string_is_identifier("30DaysOfPythong")
tell_if_string_is_identifier("thirty_days_of_python")

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("32.", " #".join(libraries), "\n")

# 33. Use the new line escape sequence to separate the following sentences.
string  = "I am enjoying this challenge. \n I just wonder what is next."
print("33.", string, "\n")

# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
table = "Name\tAge\tCountry\tCity\nCT\t33\tUSA\tMinneapolis"
print("34.", "\n", table, "\n", sep="")

# 35. Use the string formatting method to display the following:
radius = 10
area = int(3.14 * radius ** 2)
print("35.", "The area of a circle with radius {} is {} meters square.".format(radius, area), "\n")

# 36. Make the following using string formatting methods:
# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ```