
import os
import xml.etree.ElementTree as ET

# locate the directory
try:
    os.chdir('songlib')
except FileNotFoundError:
    print("ERROR\nCould not locate song files. Make sure they are in a folder labeled 'songlib' in this directory:", os.getcwd())

# loop through all songs
change_count = 0
for song in os.listdir():
    
# open for xml parsing
    tree = ET.parse(song)
    root = tree.getroot()

# find the Author
    authors = []
    for author in root.iter('{http://openlyrics.info/namespace/2009/song}author'):
        authors.append(author.text)

# string formatting, because illegal filename characters show up as underscores
    for i in range(len(authors)):
        authors[i] = authors[i].replace(':', '_')
        authors[i] = authors[i].replace('/', '_')
        authors[i] = authors[i].replace('\\', '_')
        authors[i] = authors[i].replace('?', '_')

# check that the author is in the filename, if so, remove it
    author_string = ', '.join(authors)
    authors.reverse()
    reverse_author_string = ', '.join(authors)

    if author_string in song:
        new_title = song.replace(" ({})".format(author_string), '')
    elif reverse_author_string in song:
        new_title = song.replace(" ({})".format(reverse_author_string), '')
    else:
        continue

# check whether the new filename exists already
    i = 2
    while True:
        if os.path.exists(new_title):
            if i == 2:
                new_title = new_title[:-4] + "(2).xml"
            else:
                new_title = new_title[:-7] + "({}).xml".format(str(i))
            i += 1
        else:
            break

# rename the file
    os.rename(song, new_title)
    if song != new_title:
        print(song, " -> ", new_title)
        change_count += 1 

# print info about changes made
print( "\n{} song titles were renamed.".format(str(change_count)))
