# Exercise - Liked Songs

# Define a dictionary
liked_songs = {
    'Magnetic': 'Illit',
    'Cry for Me': 'Twice',
    'Russian Roulette': 'Red Velvet',
    'Lovesick Girls': 'Blackpink',
    'Pied Piper': 'BTS'
}

# Create function to display and write liked songs to a file
def write_liked_songs_to_file(songs, file_name):
    with open('songs.txt','w') as file:
        file.write('Liked Songs:\n')
        for song, artist in songs.items():
            file.write(f'{song} by {artist}\n')

write_liked_songs_to_file(liked_songs, "songs.txt")