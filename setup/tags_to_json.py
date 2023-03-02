tags_file = open('tags.txt', 'r')
data = tags_file.read()
tags_file.close()
data = data.split(',')

choices = tuple(enumerate(data))
