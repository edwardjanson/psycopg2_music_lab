from db.run_sql import run_sql

from models.artist import Artist
import repositories.album_repository as album_repository


  
def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


# SAVE
def save(artist):
    
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"

    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

# DELETE ALL
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# SELECT
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # Checking if the list return by `run_sql(sql, values` is empty. Empty lists are 'falsy'.
    # Could alternatively have: if len(results) > 0
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist

# DELETE
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def albums(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    
    return results