import lyricsgenius as lg

file = open("/Users/athou/Downloads/lyrics_1.txt", "w")
genius = lg.Genius('sPD4FscIdqu3n6G6cRQvIEvHL_ZYvdMi6OzlBQvdWfQ7y2JftiJUKuyNZnXrlfa4', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],)

artists = ['AWOLNATION']

def get_lyrics(arr, k): 
    c = 0  # Counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")

get_lyrics(artists, 3)