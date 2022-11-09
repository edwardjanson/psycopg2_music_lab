import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Oasis')
artist_repository.save(artist_1)

album_1 = Album("Roll With It", "Rock", artist_1)
album_repository.save(album_1)
album_2 = Album("Another Album", "Pop", artist_1)
album_repository.save(album_2)

album_1.genre = "Pop"
album_repository.update(album_1)

artist_1.name = "Bla"
artist_repository.update(artist_1)

for album in album_repository.select_all():
    print(album.__dict__)

for artist in artist_repository.select_all():
    print(artist.__dict__)

print(f"list all albums: {artist_repository.albums(artist_1)}")

pdb.set_trace()
