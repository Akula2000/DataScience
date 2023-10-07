# 1.Display Fibonacci Series upto 10 terms
x, y = 0, 1
n = 10
for _ in range(n):
    print(x)
    x,y = y,x+y


#2.Display numbers at the odd indices of a list
my_list = [1, 2, 3, 4, 5]
odd_indices_numbers = my_list[1::2]
print(odd_indices_numbers)

#3.Print a list in reverse order
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

#4.Your task is to count the number of different words in this text
string = """
	ChatGPT has created this text to provide tips on creating interesting paragraphs. 
	First, start with a clear topic sentence that introduces the main idea. 
	Then, support the topic sentence with specific details, examples, and evidence.
	Vary the sentence length and structure to keep the reader engaged.
	Finally, end with a strong concluding sentence that summarizes the main points.
	Remember, practice makes perfect!
	"""
words = string.split()
words = [word.strip('.,!?()[]{}') for word in words]
unique_words = set(words)
num_unique_words = len(unique_words)
print("No of different words:", num_unique_words)

#5.Write a function that takes a word as an argument and returns the number of vowels in the word
def count_vowels(word):
    word = word.lower()
    vowel_count = 0
    vowels = set("aeiou")
    for char in word:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

word = "Varshitha"
result = count_vowels(word)
print("No of vowels in", word, "is:", result)

# 6.Iterate through the following list of animals and print each one in all caps.
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

#7.Iterate from 1 to 15, printing whether the number is odd or even
for n in range(1, 16):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# 8.Take two integers as input from user and return the sum
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
result = n1 + n2
print("The sum of", n1, "and", n2, "is:", result)