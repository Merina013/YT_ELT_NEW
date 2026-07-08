import requests
import json
API_KEY = "AIzaSyAR_ZaYz53rRjzpFor25qwVBfy9WAuLYyg"
channel_handle = "MrBeast"

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        #print(json.dumps(data, indent=4))
        channel_items = data['items'][0]
        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']
        #print(channel_playlistId)
        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    print("getplaylist_id will be executed")
    get_playlist_id()
else:
    print("getplaylist_id will not be executed")

        



