

f = open("words_file.txt")

read_data = f.read()

per_word = read_data.split()

#print(per_word)

print("Total Words : ", len(per_word))
