import operator

' variable types: strings, integers, floats, lists, files, dictionaries'


filename = "lyrics/taylor/bad_blood.txt"
file_handle = open(filename)

word_freq_dict = {}
word_list = []

for line1 in file_handle:

    line2 = line1.strip('!').strip('\n').strip('!')
    tokens = line2.split(' ')

    length = len(tokens)

    for i in range(length):
        tokens[i] = tokens[i].strip(',')
        tokens[i] = tokens[i].strip('!')
        tokens[i] = tokens[i].strip('?')
        tokens[i] = tokens[i].strip('.')
        tokens[i] = tokens[i].lower()
        #print(i, tokens[i])

        if tokens[i] not in word_freq_dict:
            word_freq_dict[tokens[i]] = 1
        else:
            word_freq_dict[tokens[i]] += 1


sorted_d = sorted(word_freq_dict.items(), key=operator.itemgetter(1), reverse=True)
for item in sorted_d:

    print(item[0], item[1])





