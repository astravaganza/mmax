# API Paths
REGISTER_URL = 'https://apimyplex.manoramamax.com/user/v3/registerDevice'

# Credentials
EMAIL = ''
PASSWORD = ''

# Secrets
MASTER_AES_KEY = b'w3Ypsr5rtifP1ioA'

AES_START = b'1ioA'
AES_END = b'w3Yp'

DEFAULT_HEADERS = {
    'serviceName': 'ManoramaMax',
    'X-myplex-AppVersion': '7014',
    'X-myplex-platform': 'Android',
    'User-Agent': 'okhttp/4.9.1'
}

MANIFEST_PAYLOAD = b'{"fields":"videos,videoInfo,subtitles,generalInfo,' \
                   b'content,thumbnailSeekPreview,skipConfig","mcc":"404"' \
                   b',"mnc":"96","Cache-Control":"no-cache"}'
