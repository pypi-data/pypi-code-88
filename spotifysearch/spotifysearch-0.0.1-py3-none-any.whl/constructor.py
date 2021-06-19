
# THIS FILE IS RESPONSABLE FOR THE CONSTRUCTION OF MANY OBJECTS

from . import classes


def get_available_markets(data):
    try:
        return data['available_markets']
    except KeyError:
        return None


def base_arguments(data):
    arguments = dict(
        data = data,
        type = data['type'],
        name = data['name'],
        url = data['external_urls']['spotify'],
        id  = data['id']
    )
    return arguments


def artist(data):
    return classes.Artist(**base_arguments(data))


def track(data):
    base = base_arguments(data)

    arguments = dict(
        artists = [artist(artist_data) for artist_data in data['artists']],
        album = album(data['album']),
        preview = classes.TrackPreview(data['preview_url']),
        available_markets = get_available_markets(data),
        explicit = data['explicit'],
        disc_number = data['disc_number'],
        popularity = data['popularity'],
        duration = data['duration_ms']
    )
    return classes.Track(**{**base, **arguments})


def album(data):
    base = base_arguments(data)

    arguments = dict(
        images = [classes.AlbumCover(image['width'], image['height'], image['url']) for image in data['images']],
        artists = [artist(artist_data) for artist_data in data['artists']],
        available_markets = get_available_markets(data),
        release_date = data['release_date'],
        total_tracks = data['total_tracks']
    )
    return classes.Album(**{**base, **arguments})
