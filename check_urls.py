import urllib.request
urls = [
    'https://upload.wikimedia.org/wikipedia/en/4/4d/Valorant_logo.png',
    'https://upload.wikimedia.org/wikipedia/en/7/77/League_of_Legends_logo.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Fortnite_Logo.svg/1200px-Fortnite_Logo.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/2/22/Dead_by_Daylight_logo.png',
    'https://cdn-fastly.obsproject.com/images/press/obs-studio-logo.svg',
    'https://upload.wikimedia.org/wikipedia/en/0/00/Audacity_logo_with_text.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/GIMP_logo.svg/1024px-GIMP_logo.svg.png',
    'https://code.visualstudio.com/assets/images/code-stable.png',
    'https://notepad-plus-plus.org/images/logo.png',
    'https://www.rarlab.com/rar.png',
    'https://www.7-zip.org/favicon.ico',
    'https://handbrake.fr/images/handbrake_logo.svg',
    'https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Black.png',
    'https://store.steampowered.com/public/images/steam/logo.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Opera_2015_icon.svg/1024px-Opera_2015_icon.svg.png',
    'https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png',
    'https://d24cgw3uvb9a9h.cloudfront.net/static/92292/image/new/zoom-logomark.svg',
    'https://media.forgecdn.net/img/cf-logo@2x.png',
    'https://upload.wikimedia.org/wikipedia/en/a/a7/Call_of_Duty_Warzone_logo.png'
]
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            print(r.status, url, r.headers.get('Content-Type'))
    except Exception as e:
        print('ERR', url, type(e).__name__, e)
