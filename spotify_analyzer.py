# Spotify data anylyzer
# Author: Tim 
# Jan 16 2024
import csv

# Create a function that searches through the data
# Finds all songs from a given artist

def find_all_song(artist: str) -> list:
    """Searches through a set of data and returns all songs found from a given artist
    
    Returns:
        list of found songs, an empty list if none are found"""
    




    # Open the file
    with open("./spotify.csv") as f:
        # ---- search for all Drake songs
        # ---- Use linear search
        # create a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to store all songs
        songs = []

        # Create a counter to store the current line number
        line_num = 0

        # For every line in the file:
        for line in csv_reader:

        # if the artist for the song is Drake
            if line_num == 0:
                #print("The columns are: ")
            
                # Print on one line
                #print(", ".join(line))

                #print one on every line
                line_num += 1
            else:
                # If the artist is given artist
            # Store the song info into the list
            # ---- artist, song title, danceability
                if artist.lower()in line['artist'].lower():
                    songs.append((
                        line['artist'],
                        line['song_title'],
                        line['danceability']
                        ))
                    line_num += 1
            return songs
                
drake_songs = find_all_song("drake")
ed_seeran_songs = find_all_song("ed sheeran")
find_all_song("drake")

for song in drake_songs:
    if float(song[-1] >= 0.5):
        print(song)