def hello():
    print("hello AkiraChix")

def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name}, you were born in {2024-age}")
    
def my_country(country="Uganda"):
    print(f"Hello AkiraChix from {country}")

# Create a program that takes 2 sorted arrays as an input and merges them into a single sorted array
def my_array(arr1,arr2):
    merged_array = sorted(arr1)+sorted(arr2)

    wholeSorted = sorted(merged_array)

    print(wholeSorted)

# Write a program that takes a string as input and outputs the string reversed 
def my_string(word):
    print(word[::-1])

# Write a program that takes in a string as input and removes all duplicates characters, maintaining the original order
def my_duplicates(word):
    removed_duplicates = set(word)
    print(removed_duplicates)

# Write a program that takes a list of integers as inputs and outputs the list sorted in descending order
def my_integers():
    integers = [3,7,8,4,2]
    integers.sort(reverse=True)
    print(integers)

# Write a program that takes a list of integers as input & removes all duplicates numbers, returning a list with unique numbers only
def my_list():
    x = [30,21,30,40,1,21,40]
    y = set(x)
    z = list(y)
    print(z)

# Write a program that takes a sentence as input and reverses the order of words in it
def my_sentence(sentence):
    words = sentence.split(" ")
    new_word = [word[::-1]for word in words ]  
    new_words = " ".join(new_word)
    print(new_words)
   
#  Write a program that takes a base and an exponent as input 
def my_value(base,exponent):
    print(base**exponent)

# Create a program that takes two strings as input and checks if one is an anagram of the other
def anagram(word1,word2):
    if(sorted(word1) == sorted(word2)):
        print("The strings are anagrams")
    else:
        print("The strings aren't anagrams")

# Create a program that takes a string and a list of characters as input,
# and removes all occurences of those characters from the string
def my_characters(a,r):
    counts = a.count(r)
    a = list(a)

# Create a program that takes a string as input and counts the number of vowels in it
def my_vowels():
   string = "GabrIElla"
   vowels = "a,e,i,o,u,A,E,I,O,U"

   count = sum(string.count(vowel) for vowel in vowels)
   print(count)

# Create a dictionary to store information about your favorite book
# (title, author, genre, year published)
# Access the author's name:book_info["author"]
# Add a new key-vaue pair for the number of pages
   
book_info = {"title":"New Dawn", "author":"Valeria Chebet", "Genre":"fiction", "year_published":2013}
print(book_info["author"])

book_info["number_of_pages"]=300  
print(book_info)

# Create a dictionary using dictionary comprehesion to map numbers to their squares

my_dict = {1:3,2:4,3:9,4:5}
new_dict = my_dict.values()
for i in new_dict: print(i*i)

# A function with only one parameter butput an asterisk before the parameter
def greet (*names):
    for name in names:
        print(f"Hello {name}")

# A function that accepts one parameter but is a keyword argument. We use two asterisks.
def create_sentence(**words): 
    print(words)
    sentence = ""
    for word in words.values():
        sentence+= word
        sentence += " "
    return sentence

def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total += x
    f = kwargs["first_name"]
    l = kwargs["last_name"]
    c = kwargs["country"]
    greeting = f"Hello {f} {l} from {c} the sum of your numbers is {total}"
    return greeting