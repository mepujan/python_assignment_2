# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

from random import shuffle

word= input('Enter the word: ')
word_list=list(word)
print(word_list)

for _ in range(len(word_list)):
    shuffle(word_list)
    print(''.join(word_list))