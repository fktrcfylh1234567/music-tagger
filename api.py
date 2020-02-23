import http.client
import json

api_url = "macgyverapi-music-graph-v1.p.rapidapi.com"


def get_album(artist, title):
    connection = http.client.HTTPSConnection(api_url)

    data = {"search": title + ' ' + artist}
    payload = {'key': 'free', 'id': '9m9c8U4f', 'data': data}
    payload = json.dumps(payload)

    headers = {
        'x-rapidapi-host': "macgyverapi-music-graph-v1.p.rapidapi.com",
        'x-rapidapi-key': "c692a60e0cmshe19a99b25288a50p110f07jsnaf4fb6232867",
        'content-type': "application/json",
        'accept': "application/json"
    }

    connection.request("POST", "/", payload, headers)

    res = connection.getresponse().read().decode("utf-8")

    try:
        data = json.loads(res)
    except json.decoder.JSONDecodeError:
        return

    # Nothing found
    if data['result'] == ["off"]:
        return

    # Fields: ['albumTitle']
    # ['releaseDate']
    # ['thumbnails']['standard']
    # ['thumbnails']['high-quality']
    # ['genre']
    album = data['result'][0]['albumTitle']

    return album
