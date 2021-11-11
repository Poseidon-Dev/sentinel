import os
from datetime import date

CURRENT_YEAR = str(date.today().year)

# Company settings and folder destination path
COMPANIES = [
    {'src': '01000', 'dst': 'APL'},
    {'src': '30000', 'dst': 'MEE'},
    {'src': '40001', 'dst': 'GCS'},
]

# Delay interval, increase for security, decrease for speed
DELAY_INTERVAL = 10

# File information for ACH directories
ACH_PATHS = ['ach', 'ACH', 'DIRECT DEPOSIT', 'PR2110011.092921.132424.TXT']
ACH_DST_PATH = os.getenv('ACH_DST_PATH').replace('XXXX', CURRENT_YEAR)
ACH_DST_SUFFIX = os.getenv('ACH_DST_SUFFIX')
ACH_SRC_PATH = os.getenv('ACH_SRC_PATH')

# File information for EFT directories
GARN_PATHS = ['eft', 'EFT', 'GARNISHMENTS', 'CTX.AP01000.100821.104909.TXT']
GAR_DST_PATH = os.getenv('GAR_DST_PATH').replace('XXXX', CURRENT_YEAR)
GAR_DST_SUFFIX = os.getenv('GAR_DST_SUFFIX')
GAR_SRC_PATH = os.getenv('GAR_SRC_PATH')

# Email utility information
EMAIL_UID = os.getenv('EMAIL_UID')
EMAIL_PWD = os.getenv('EMAIL_PWD')
EMAIL_SMTP = os.getenv('EMAIL_SMTP')
EMAIL_SMTP_PORT = int(os.getenv('EMAIL_SMTP_PORT'))