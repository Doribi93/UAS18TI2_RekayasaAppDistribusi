#BASIC LYRICS FINDER
This is a basic lyrics finder program made with the [Genius REST API](https://docs.genius.com/) and Python. Most of the functions can be modified by opening the .py file in a compatible IDE and make changes to a certain section of the code.

###CHANGING FILE OUTPUT LOCATION
On the section of the code: 
* file = open("/Users/athou/Downloads/lyrics_1.txt", "w")
Enter and replace the url "/Users/athou/Downloads/lyrics_1.txt" to the one you wanted. DO NOT forget to include the filename (e.g. lyrics_1.txt) at the end of the URL (you can rename it to anything, and there MUST be a file extension written down after the name. .Txt File is the safest file extension for the output of the program).

###CHANGING THE ARTIST NAME FOR THE SEARCH
On the section of the code: 
* artists = ['AWOLNATION']
Enter and replace the name of an artist in between [ and ], with quotes (e.g. 'Martin Garrix'). You can add as many artists within as possible (e.g. ['AWOLNATION', 'Martin Garrix', 'Frank Klepacki', etc..]).

###CHANGING THE LIMIT OF NUMBER OF SONGS FOR OUTPUT
On the section of the code: 
* get_lyrics(artists, 1)
Enter and replace the number to change the limit of songs to be sent to your output (e.g. get_lyrics(artists, 3) will output 3 songs for each artists listed).
