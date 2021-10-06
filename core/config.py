import os
from datetime import date

COMPANIES = [('01000', 'APL'), ('30000', 'MEC'), ('40001', 'GCS')]
# COMPANIES = [('01000', 'APL')]
COMPANIES = [
    {'src': '01000', 'dst': 'APL'},
    {'src': '30000', 'dst': 'MEE'},
    {'src': '40001', 'dst': 'GCS'},
]
CURRENT_YEAR = str(date.today().year)
DELAY_INTERVAL = 180

ACH_DST_PATH = os.getenv('ACH_DST_PATH').replace('XXXX', CURRENT_YEAR)
ACH_DST_SUFFIX = os.getenv('ACH_DST_SUFFIX')
ACH_SRC_PATH = os.getenv('ACH_SRC_PATH')

EMAIL_UID = os.getenv('EMAIL_UID')
EMAIL_PWD = os.getenv('EMAIL_PWD')
EMAIL_SMTP = os.getenv('EMAIL_SMTP')
EMAIL_SMTP_PORT = int(os.getenv('EMAIL_SMTP_PORT'))


