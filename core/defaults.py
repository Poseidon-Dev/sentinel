import os
from datetime import date

CURRENT_YEAR = str(date.today().year)

ACH_DST_PATH = os.getenv('ACH_DST_PATH').replace('XXXX', CURRENT_YEAR)
ACH_DST_SUFFIX = os.getenv('ACH_DST_SUFFIX')
ACH_SRC_PATH = os.getenv('ACH_SRC_PATH')

GAR_DST_PATH = os.getenv('GAR_DST_PATH').replace('XXXX', CURRENT_YEAR)
GAR_DST_SUFFIX = os.getenv('GAR_DST_SUFFIX')
GAR_SRC_PATH = os.getenv('GAR_SRC_PATH')

EMAIL_UID = os.getenv('EMAIL_UID')
EMAIL_PWD = os.getenv('EMAIL_PWD')
EMAIL_SMTP = os.getenv('EMAIL_SMTP')
EMAIL_SMTP_PORT = int(os.getenv('EMAIL_SMTP_PORT'))