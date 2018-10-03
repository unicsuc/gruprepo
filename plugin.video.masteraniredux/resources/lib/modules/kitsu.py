from resources.lib.modules import control
import requests
import json
import xbmcgui
import time

client_id = 'dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd'
client_secret = '54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151'

class KitsuScrobbler():
    def kitsu_login(self):
        try:
            token_url = 'https://kitsu.io/api/oauth/token'
            resp = requests.post(token_url, params={"grant_type": "password", "username": '%s' %(control.getSetting("kitsu.email")), "password": '%s' %(control.getSetting("kitsu.password"))})
            token = json.loads(resp.text)['access_token']
            control.setSetting("kitsu.token", token)
            useridScrobble_resp = requests.get('https://kitsu.io/api/edge/users?filter[self]=true', headers=self.kitsu_headers())
            userid = json.loads(useridScrobble_resp.text)['data'][0]['id']
            control.setSetting("kitsu.userid", userid)
            control.setSetting("kitsu.login_auth", 'Kitsu')
            dialog = xbmcgui.Dialog()
            dialog.ok('Kitsu', 'Login successful')
        except:
            dialog = xbmcgui.Dialog()
            dialog.ok('Kitsu', 'Login error. Incorrect email or password.')

    def kitsu_logout(self):
        control.setSetting("kitsu.token", '')
        control.setSetting("kitsu.userid", '')
        control.setSetting("kitsu.login_auth", '')
        control.refresh()
        dialog = xbmcgui.Dialog()
        dialog.ok('Kitsu', 'Logout successful')

    def kitsu_headers(self):
        token = control.getSetting("kitsu.token")
        headers = {
            'Content-Type': 'application/vnd.api+json',
            'Accept': 'application/vnd.api+json',
            'Authorization': "Bearer {}".format(token),
            }
        return headers

    def kitsu_initScrobble(self, title, start_date, epnum, epcount):
        initScrobble_url = 'https://kitsu.io/api/edge/anime?filter[text]=%s' %(title)
        initScrobble_resp = requests.get(initScrobble_url)
        data = json.loads(initScrobble_resp.text)['data']
        for i in data:
            if i['attributes']['startDate'] == start_date:
                kitsu_id = i['id']

        if str(epnum) == str(epcount):
            status_data = {"status": "completed"}
        else:
            status_data = {"status": "current",
                           "progress": epnum
                           }

        return self.kitsu_scrobbleAnime(kitsu_id, status_data)

    def kitsu_scrobbleAnime(self, kitsu_id, status_data):
        user_id = int(control.getSetting("kitsu.userid"))
        libraryEntry_url = 'https://kitsu.io/api/edge/library-entries/'
        libraryScrobble_url = libraryEntry_url + '?filter[animeId]=%s&filter[userId]=%d' %(kitsu_id, user_id)
        libraryScrobble_resp = requests.get(libraryScrobble_url).text
        item_dict = json.loads(libraryScrobble_resp)
        if len(item_dict['data']) == 0:
            item_type = 'anime'
            final_dict = {
                    "data": {
                        "type": "libraryEntries",
                        "attributes": status_data,
                        "relationships":{
                            "user":{
                                "data":{
                                    "id": user_id,
                                    "type": "users"
                                }
                            },
                            "anime":{
                                "data":{
                                    "id": kitsu_id,
                                    "type": item_type
                                }
                            }
                        }
                    }
                }

            data = json.dumps(final_dict, separators=(',',':'))
            libraryEntry_post = requests.post(libraryEntry_url, headers=self.kitsu_headers(), data=data)
            if libraryEntry_post.status_code != 201:
                dialog = xbmcgui.Dialog()
                dialog.ok('Kitsu', 'Kitsu scrobble error. Unable to track episode. Try relogging in to resolve error.')
        else:
            _id = item_dict['data'][0]['id']
            final_dict = {
                'data': {
                    'id': _id,
                    'type': 'libraryEntries',
                    'attributes': status_data
                    }
                }

            data = json.dumps(final_dict, separators=(',',':'))
            libraryEntry_patch = requests.patch(libraryEntry_url + _id, headers=self.kitsu_headers(), data=data)
            if libraryEntry_patch.status_code != 200:
                dialog = xbmcgui.Dialog()
                dialog.ok('Kitsu', 'Kitsu scrobble error. Unable to track episode. Try relogging in to resolve error.')
