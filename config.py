# API Paths
REGISTER_URL = 'https://apimyplex.manoramamax.com/user/v3/registerDevice'
LOGIN_URL = 'https://id.manoramaonline.com/token'

# Credentials
EMAIL = ''
PASSWORD = ''

# Secrets
MASTER_AES_KEY = b'w3Ypsr5rtifP1ioA'

AES_START = b'1ioA'
AES_END = b'w3Yp'

CERT_FP = '84:5F:C4:C3:4D:C7:5E:F5:C8:09:4C:4B:B5:D9:FE:23:83:41:4E:74'

DEFAULT_HEADERS = {
    'serviceName': 'ManoramaMax',
    'X-myplex-AppVersion': '7087',
    'X-myplex-platform': 'Android',
    'User-Agent': 'okhttp/5.0.0-alpha.7'
}

UA_MMAX = 'manoramaMAX/2.0.86 (Android 13;49c196d03e009b8cBuild/ Redmi Note 12 4G)'
PACKAGE_NAME = 'com.mmtv.manoramamax.android'

MANIFEST_PAYLOAD = b'{"fields":"videos,videoInfo,subtitles,generalInfo,' \
                   b'content,thumbnailSeekPreview,skipConfig","mcc":"404"' \
                   b',"mnc":"96","Cache-Control":"no-cache"}'
