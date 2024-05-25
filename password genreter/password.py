import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def generate_word_list(num_words, min_length, max_length):
    word_list = []
    for _ in range(num_words):
        length = random.randint(min_length, max_length)
        word_list.append(generate_password(length))
    return word_list

# Example usage:
num_words = 1000000
min_length = 4
max_length = 12
word_list = generate_word_list(num_words, min_length, max_length)
for word in word_list:
    print(word)