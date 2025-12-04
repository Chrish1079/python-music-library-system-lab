class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Adds any new genres to a class attribute genres. Ensures there are only unique genres - no duplicates!"""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Adds any new artists to a class attribute artists. Ensures there are only unique artists - no duplicates!"""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates class attribute genre_count. Increments genre key by 1, if genre doesn't exist in genre_count add the key and set it to 1."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates class attribute artist_count. Increments artist key by 1, if artist doesn't exist in artist_count add the key and set it to 1."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
