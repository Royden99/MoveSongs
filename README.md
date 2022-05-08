# MoveSongs
An ongoing list of worship lyrics.

## Summary
In the folder labeled 'songlib' you will find a large collection of worship songs that we sing often in the move of God.  I compiled this collection from a few different sources, including the Living Word Songbook database, and I would love if you can make use of it or contribute to it in any way!

This is mostly geared toward those of you who would like to project the song lyrics to the congregation during a live service -- read more about that down below.  It might also be useful if you want to have a copy of these songs for personal reference.  Ideally, this database should provide you with full and correct information about a song (Author, Title, all verses, correct words, maybe even Spanish words); and would be a reliable source to fall back upon if you want to learn a song better.  That's the end goal; the reality is that we are not there yet.

My motivation for this project is to try to set up a way that many of us can work together on the same set of lyrics, to be constantly improving them and adding new songs for all the users to have access to.
If you would like to help further this cause, see the section on 'Contributions'.

## Downloading the songs for your own use
Click the green button near the top of this page that says "Code".  Then, select "Download ZIP".  This will download the whole project to your own computer, inside a Zip folder.  Then, you can import these songs into the program you want to use. See 'Contributions' for more instructions.

Or, If you are a Git user, you can clone the project to your own computer.

## These lyrics are in OpenLyrics format
Each song is an XML file, and they are in the [OpenLyrics XML standard](https://docs.openlyrics.org/en/latest/).  Click the link for an exhaustive description of its features.  This means the songs are not very easy for a human to read just on their own; instead, they need to be used with a computer program that supports the format.  Possibly they could be converted into other formats -- that might be a nice tool to include in this project.

## Useful tool -- OpenLP projection software
[OpenLP](https://openlp.org/) is a free program that will help you work with the songs.  It is used to project the words of a song onto a screen for the congregation to follow during a worship service, but it has other features too, which will allow you to delete songs, add new songs, edit existing songs, and import songs that are in different formats.  The link will take you to the website where you can download it. 

**Note** that when you export songs from OpenLP, OpenLP uses the title of the song plus the author's name in parentheses as the name of the file.  This can be inconvenient since the author's name often includes illegal filename characters.  I've included a Python3 tool in this repository, 'clean_filenames.py', that will strip the author in parentheses out of the filenames.

## Contributions
If you want to make corrections and/or additions to this database of songs, that would be wonderful!  To contribute any changes that you make using the OpenLP program, follow these directions.

---
#### Getting set up
* Download this project onto your own computer as described above.
* You will have a Zip folder named 'MoveSongs-master'.  Extract this folder.
* Inside 'MoveSongs-master', there's a folder named 'songlib'; inside this folder are all the song files.  You probably don't need any of the other things in the 'MoveSongs-master' folder.
* Run the OpenLP program and make sure that it is empty of songs.
* In OpenLP, select 'File' -> 'Import' -> 'Song' from the menu bar.
* Use the Import wizard to select and import **all** the songs in the 'songlib' folder.  These will then be available to use in OpenLP.
#### Making changes to the songs
* Use the OpenLP program over time however you need to, improving the lyrics as you go.  Below, in the 'Things that need to be done' section, I've described a few things that need improving.  Maybe you will find more.
#### Contributing your changes to the central repository
* First, delete all the songs from the 'songlib' folder, so that it is completely empty.  This will not affect the songs in OpenLP.
* In OpenLP, select 'File' -> 'Export' -> 'Song' from the menu bar.
* Use the Export wizard to select **all** the songs and put them into the 'songlib' folder on your computer.  In this way, you replace all the old songs in 'songlib' with the new copies of each song.
* Now, compress the folder 'MoveSongs-master' into a Zip folder again, and send it to me (Ryan Buerge) in an email.
#### Updating your songs to reflect others' changes
* I will do my best to merge together your changes with any changes that others may have made in the same timeframe.  When the merge is complete, the updated copy of these songs will be available on this website.  Unfortunately, if two people make conflicting changes to the same song, then one person's changes may have to be overwritten.
* If you would now like to use the new, updated songs that include your own and everyone else's changes, you can do that.  Delete your entire library of songs in OpenLP, and follow these directions again, starting at step 1.  In theory, you won't lose any work because your changes have been merged into the whole.
---

To contribute any changes made using some other program than OpenLP, the process is very much the same.  Replace the contents of the 'MoveSongs-master\songlib' folder with song files that reflect your changes, and send the folder back to me.  You may have to convert the files into a format that works for you, and convert them back into the 'OpenLyrics' format when you're done.

Instead of sending your files back to me in an email, you could instead use Git or the tools provided by GitHub if you know how.  Fork this project, make your changes, and submit a pull request.

### Sharing an OpenLP database with DropBox
OpenLP has the ability to store its database anywhere you like on your computer.  To learn how to do that, refer to the manual [here](https://manual.openlp.org/configure.html#advanced).  If you store it in a DropBox folder, it can be shared with other people or other devices.  On another computer, then, someone else can use OpenLP to use and modify the exact same database.  Any changes that one person makes are synced with everyone else that uses the shared DropBox folder, as long as everyone has an internet connection.
This is a quick way to collaborate among a few people, or to access the songs from more than one church computer, perhaps.
This method may have a few drawbacks if used on a large scale; for example, all the people using the shared folder have to share the same Themes and Bibles in OpenLP as well as the songs.

### Things that need to be done
1. *Delete less accurate versions of duplicate songs.*  When I originally compiled all these songs, I used computer programming to combine three different databases into one.  As a result, often you will see the exact same song listed two or three times, but with slightly different lyrics.  I would like to delete the less accurate duplicates, leaving only one version which has all of the available information.
2. *Alter the titles of similar but actually different songs.*  Occasionally two or more songs will exist in this database that have the same title, but they are actually different songs.  It would be nice to get rid of this problem so that we don't have, for example, a "Hosanna", "Hosanna(2)", and a "Hosanna(3)" all nestled together.
3. *Alter the titles of songs to be their actual title, not necessarily just the first line of the song.*
4. *Add new information.*  Often a song is missing verses, or appears to be written by a man named "Author Unknown."  Adding Spanish verses could be helpful, and actually there is a capability to include Chords as well, if anyone feels so inclined.
5. *Include new songs.*  If you discover that a song which should be in here isn't.

---

--Ryan Buerge
