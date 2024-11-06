from nltk.corpus import words
import sys
import re

word_length = 6

def letters_in_word(letters, word):
    return any(c in word for c in letters)

words_used = ["BARELY","CHINKS","GODFUL","CUBISM","EUROPA"]
bigword = "".join(words_used)
good_letters = "AROU"

# Define the pattern and its corresponding fixed letters
pattern = 'AURORA'
regex_pattern = '^' + pattern.replace('*', '.') + '$'


# Unique sorted letters in the words used
all_letters = "".join(sorted(set(bigword)))

# Determine bad letters by excluding those in good_letters
all_bad_letters = "".join(letter for letter in all_letters if letter not in good_letters)

# Alphabet and leftover letters
alfabet = "".join(chr(i) for i in range(65, 91))
leftover_letters = "".join(letter for letter in alfabet if letter not in good_letters and letter not in all_bad_letters)

# Output results
print("All letters:", all_letters)
print("Bad letters:", all_bad_letters)
print("Good letters:", good_letters)
print("Leftover letters:", leftover_letters)
print("Alphabet:", alfabet)

six_letter_words = [word.upper() for word in words.words() if len(word) == word_length]
print("All six-letter words:", len(six_letter_words))

filler_words = []
for word in six_letter_words:
    # Ensure the word has word_lenght unique letters
    if len(set(word)) < word_length:
        continue
    
    # Check if all letters are in leftover_letters and there are no duplicate letters
    if all(letter in leftover_letters for letter in word) and all(word.count(letter) == 1 for letter in word):
        filler_words.append(word)
print("All six-letter filler words:", len(filler_words))
# Lists for each category of words with at least 6, 5, 4... unique letters
# Assuming filler_words is defined and leftover_letters is available

# Create lists to hold words based on the count of letters in leftover_letters
word_groups = [[] for _ in range(6)]

for word in six_letter_words:
    # Get unique letters in the word and check if all letters are unique
    unique_letters = set(word)
    if len(unique_letters) == len(word):
        # Count how many letters from the word are in leftover_letters
        count_in_leftover = sum(1 for letter in unique_letters if letter in leftover_letters)
        
        # Place the word in the appropriate group based on the count
        if 0 <= word_length - count_in_leftover <= word_length:
            word_groups[word_length - count_in_leftover].append(word)

# Output each group
labels = ["6 or more letters in leftover", "5 letters in leftover", "4 letters in leftover", 
          "3 letters in leftover", "2 letters in leftover", "1 letter in leftover"]

for label, words_var in zip(labels, word_groups):
    #pass
    print(f"{label}: {words_var}")
    

print("Filler words:", len(filler_words))
print("All words:", len(words.words()))
# Assuming six_letter_words is defined and good_letters is available

# Convert good_letters to a set for efficient lookup
good_letters_set = set(good_letters)

# Function to check if a word matches the pattern
def matches_pattern(word, pattern):
    for w_char, p_char in zip(word, pattern):
        if p_char != '*' and w_char != p_char:
            return False
    return True

# Filter six-letter words that contain all good letters and match the pattern
words_matching_criteria = [
    word for word in six_letter_words
    if matches_pattern(word, pattern) and all(letter in word for letter in good_letters_set)
]

# Output the result
print("Six-letter words containing all good letters and matching the pattern:", words_matching_criteria)


# Convert good_letters to a set for efficient lookup
good_letters_set = set(all_letters)


# Function to check if a word matches the pattern
def matches_pattern2(word, pattern):
    for w_char, p_char in zip(word, pattern):
        if p_char != '*' and w_char != p_char:
            return False
    return True

# Filter X-letter words that contain all good letters and match the pattern
words_matching_criteria2 = [
    word for word in six_letter_words
    if len(word) == word_length and re.match(regex_pattern, word)
]

# Output the result
print(word_length," letter words containing all good letters and matching the pattern:", words_matching_criteria2)

