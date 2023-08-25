songs = []

song = input("Please enter a first song name: ")
songs.append(song)

song = input("Please enter a second song name: ")
songs.append(song)

song = input("Please enter a third song name: ")
songs.append(song)

print(songs)

songs_count = len(songs)
if songs_count > 0:
    remove_index = songs_count//2
    songs.pop(remove_index)

print(songs)

song = input("Please enter another song name: ")
songs.append(song)

song = input("...And again, enter any song name: ")
songs.append(song)

print(songs[1: -1])
