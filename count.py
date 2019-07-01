import operator
import os

' variable types: strings, integers, floats, lists, files, dictionaries'

# homework assignment:
# add some loops to count all the songs for taylor and kanye
# create a different dictionary for each artist
# print out the top 30 words for each person

lyric_directory = 'lyrics/'

artist_list = os.listdir(lyric_directory)

word_freq_dict = {}

for artist in artist_list:
    if artist != '.DS_Store':
        song_list = os.listdir(lyric_directory + artist)
        for song in song_list:
            if song != '.DS_Store':
                print(artist, song)
                filehandle = open(lyric_directory + artist + '/' + song)
                for line1 in filehandle:

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
print(sorted_d)

for i in range(50):
    print(sorted_d[i][0], sorted_d[i][1])






