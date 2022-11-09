from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository


  
def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'],
        row['genre'],
        artist_repository.select(row['artist_id']),
        row['id'])
        albums.append(album)
    return albums


# SAVE
def save(album):
    
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"

    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

# DELETE ALL
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# SELECT
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # Checking if the list return by `run_sql(sql, values` is empty. Empty lists are 'falsy'.
    # Could alternatively have: if len(results) > 0
    if results:
        result = results[0]
        album = Album(result['title'], result['genre'], artist_repository.select(result['artist_id']))
    return album

# DELETE
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)