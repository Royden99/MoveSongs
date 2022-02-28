# MoveSongs
An ongoing list of worship lyrics.

## Summary
In the folder labeled 'songlib' you will find a large collection of worship songs that we sing often in the move of God.  I compiled this collection from a few different sources, including the Living Word Songbook database, and I would love if you can make use of it or contribute to it in any way!

This is mostly useful for projecting the song lyrics to the congregation during a live service -- read more about that down below.  Ideally, this database should provide you with full and correct information about a song (Author, Title, all verses, correct words, maybe even Spanish words); and would be a reliable source to fall back upon if you want to learn a song better.

## Downloading the songs for your own use
Click the green button near the top of this page that says "Code".  Then, select "Download ZIP".  This will download the whole project to your own computer, inside a Zip folder.  Then, you can import these songs into the program you want to use.

Or, If you are a Git user, you can clone the project to your own computer.

## These lyrics are in OpenLyrics format
Each song is an XML file, and they are in the [OpenLyrics XML standard](https://docs.openlyrics.org/en/latest/).  Click the link for an exhaustive description of its features.  This means the songs are not very easy for a human to read just on their own; instead, they need to be used with a computer program that supports the format.  Possibly they could be converted into other formats -- that might be a nice tool to include in this project.

## Useful tool -- OpenLP projection software
[OpenLP](https://openlp.org/) is a free program that will help you work with the songs.  It is used to project the words of a song onto a screen for the congregation to follow during a worship service, but it has other features too, which will allow you to delete songs, add new songs, edit existing songs, and import songs that are in different formats.  The link will take you to the website where you can download it. 

**Note** that when you export songs from OpenLP, OpenLP uses the title of the song plus the author's name in parentheses as the name of the file.  This can be inconvenient since the author's name often includes illegal filename characters.  I've included a Python3 tool in this repository, 'clean_filenames.py', that will strip the author in parentheses out of the filenames.

## Contributions
If you want to make corrections and/or additions to this database of songs, that would be wonderful!  To contribute, first make your corrections using OpenLP or another song program.  Then, export the entire collection of songs to a folder on your computer.  From there, you can send them back to me in an email.  I have found the best way to email them is to put them in a Zip (compressed) folder.  Send the email to ryanv.buergeandhank@gmail.com and I will merge your changes into the songs on this website.

Alternatively, if you know how to use git and GitHub, you can fork this project, make your changes, and submit a pull request.

### Things that need to be done
1. *Delete less accurate versions of duplicate songs.*  When I originally compiled all these songs, I used computer programming to combine three different databases into one.  As a result, often you will see the exact same song listed two or three times, but with slightly different lyrics.  I would like to delete the less accurate duplicates, leaving only one version which has all of the available information.
2. *Alter the titles of similar but actually different songs.*  Occasionally two or more songs will exist in this database that have the same title, but they are actually different songs.  It would be nice to get rid of this problem so that we don't have, for example, a "Hosanna", "Hosanna(2)", and a "Hosanna(3)" all nestled together.
3. *Alter the titles of songs to be their actual title, not necessarily just the first line of the song.*
4. *Add new information.*  Often a song is missing verses, or appears to be written by a man named "Author Unknown."  Adding Spanish verses could be helpful, and actually there is a capability to include Chords as well, if anyone feels so inclined.
5. *Include new songs.*  If you discover that a song which should be in here isn't.

---

--Ryan Buerge
