sentence = input()

words = sentence.split()
dictionary = {};

for i in range(0, len(words)):
    dictionary[len(words[i])] = []

for i in range(0, len(words)):
    dictionary[len(words[i])].append(words[i])

print(dictionary)