# MoveSongs
An ongoing list of worship lyrics.

## Summary
In the folder labeled 'songlib' you will find a long list of songs that we, in the move of God, have been singing for a long time.  I compiled them all from a few different sources, including the Living Word Songbook database, and I would love it if any of you can make use of them or contribute in any way!

Ideally, this database should provide the operator of a lyrics projection software with full and correct information about a song (Author, Title, all verses, correct words, maybe even Spanish words); and would be a reliable source to fall back upon if one wanted to learn a song better.

## These lyrics are in OpenLyrics format
Each song is its own XML file, and they are in the [OpenLyrics XML standard](https://docs.openlyrics.org/en/latest/).  Click the link for an exhaustive description of its features.  This means the songs are not very easy for a human to read just on their own; instead, they need to be used with a computer program that supports the format.  Possibly they could be converted into other formats -- that might be a nice tool to include in this project.

## Useful tool -- OpenLP projection software
[OpenLP](https://openlp.org/) is a free and powerful lyrics projection software that will understand these songs just fine.  It is used to project the words of a song onto a screen for the congregation to follow during a worship service, but it has other features too, which will allow you to delete songs, add new songs, edit existing songs, and import songs that are in different formats.

**Note** that when you export songs from OpenLP, OpenLP uses the title of the song plus the author's name in parentheses as the name of the file.  This can be inconvenient since the author's name often includes illegal filename characters.  I've included a Python3 tool in this repository, 'clean_filenames.py', that will strip the author in parentheses out of the filenames.

## Contributions
If you want to make corrections and/or additions to this database and submit it back to the repository as a pull request, that would be wonderful!

### Things that need to be done
1. *Delete less accurate versions of duplicated songs.*  When I originally compiled all these songs, I wrote a script in Python to automate the process of combining three different databases into one.  In cases where two or more of the exact same song existed, but with slightly differing lyrics, I didn't want the script to have the power to decide which song was the best one, or to make typo corrections on its own.  Therefore, there are sometimes several duplicates of songs and I would like to get them out of there, leaving only one version which has all of the information available pertaining to that song.  These duplicates sometimes have a name which ends in "-1" or "-2".
2. *Alter the titles of similar but actually different songs.*  Occasionally two songs will exist that have the same title in this database, but they are actually different songs.  It would be nice to get rid of this problem so that we don't have, for example, a "Hosanna", "Hosanna(2)", and a "Hosanna(3)" all nestled together.
3. *Alter the titles of songs to be their actual title, not necessarily just the first line of the song.*
4. *Add new information.*  Often a song is missing verses, or appears to be written by a man named "Author Unknown."  Adding Spanish verses could be helpful, and actually there is a capability to include Chords as well, if anyone feels so inclined.
5. *Include new songs.*  If you discover that a song which should be in here isn't.

---

--Ryan Buerge
