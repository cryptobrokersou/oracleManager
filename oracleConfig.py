import pywaves as py
import pandas as pd
import json

py.setNode('https://privatenode.blackturtle.eu', 'TN', 'L')
py.setMatcher('https://privatematcher.blackturtle.eu')
py.DEFAULT_BASE_FEE = 2000000
address = py.Address(seed='no no')
oracle = py.Oracle(seed='no no')

##Black liating scams
SCAM_URL = "https://raw.githubusercontent.com/BlackTurtle123/TN-community/master/scam-v2.csv"

wine_csv_url = SCAM_URL
wine_data = pd.read_csv(wine_csv_url, header=None, nrows=None)
for value in wine_data.values:
    print(value[0])
    oracle.storeData('scam_<' + value[0] + '>', 'boolean', True, minimalFee=2000000)

##Add basic data provider info

oracle.storeData('data_provider_version', 'integer', 0, minimalFee=2000000)
oracle.storeData('data_provider_name', 'string', 'CryptoBrokers', minimalFee=2000000)
oracle.storeData('data_provider_email', 'string', 'support@polarity.exchange', minimalFee=2000000)
oracle.storeData('data_provider_lang_list', 'string', 'en', minimalFee=2000000)
oracle.storeData('data_provider_link', 'string', 'https://polarity.exchange', minimalFee=2000000)
oracle.storeData('data_provider_description_<en>', 'string', 'Description https://polarity.exchange', minimalFee=2000000)
oracle.storeData('data_provider_logo_meta', 'string', 'data:image/svg+xml;base64', minimalFee=2000000)
oracle.storeData('data_provider_logo', 'string', "++++Cg==", minimalFee=2000000)


def add_token(ticker, status, email, asset_id, description='Description', link='example.com', logo='', version=0):
    data = [{
        'type': 'string',
        'key': 'ticker_<' + asset_id + '>',
        'value': ticker
    },
        {
            'type': 'integer',
            'key': 'status_<' + asset_id + '>',
            'value': status
        },
        {
            'type': 'integer',
            'key': 'version_<' + asset_id + '>',
            'value': version
        },
        {
            'type': 'string',
            'key': 'email_<' + asset_id + '>',
            'value': email
        },

        {
            'type': 'string',
            'key': 'description_<en>_<' + asset_id + '>',
            'value': description
        },
        {
            'type': 'string',
            'key': 'link_<' + asset_id + '>',
            'value': link
        }
    ]
    if logo == '':
        data.append({
            'type': 'string',
            'key': 'logo_<' + asset_id + '>',
            'value': logo})
    else:
        data.append({
            'type': 'string',
            'key': 'logo_<' + asset_id + '>',
            'value': 'data:image/svg+xml;base64,' + logo
        })

    ticker_tx = address.dataTransaction(data, baseFee=2000000, minimalFee=2500000)

    print(ticker_tx)


###
# SCAM = -2,
# SUSPICIOUS = -1,
# NOT_VERIFY = 0,
# DETAILED = 1,
# VERIFIED = 2

# TODO: Status 2 seems to be when an asset is active and verified
with open('oracledata.json') as json_file:
    verified = json.load(json_file)

for token in verified:
    add_token(token['ticker'], token['status'], token['email'], token['asset_id'], token['description'], token['link'], token['logo'], token['version'])

# Not verified
add_token('BTN', 0, '------', 'ExbYSuz4DZwf9grp3K8s3CSbNtE9fob2DtTKgbLGFXsJ')
add_token('FR', 0, '------', '4xUv25qFsjQ1Gd6oCmzU14FoPMSDXrwub5PbKRgETf97')
add_token('KA', 0, '------', '5Dy1qVUzEwq6WEUGMy7CkkkbmFuxb2RTBRfs4JKc5b88')
add_token('MLT', 0, '------', '7jcY6DDYsSo7NuZEAruWhrB5apebA2cERhrBx6RFk5tL')
