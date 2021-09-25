import os
from datetime import date

COMPANIES = [('01000', 'APL'), ('30000', 'MEC'), ('40001', 'GCS')]
COMPANIES = [('01000', 'APL')]
CURRENT_YEAR = str(date.today().year)

ACH_DST_PATH = os.getenv('ACH_DST_PATH').replace('XXXX', CURRENT_YEAR)
ACH_DST_SUFFIX = os.getenv('ACH_DST_SUFFIX')
ACH_SRC_PATH = os.getenv('ACH_SRC_PATH')

