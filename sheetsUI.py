
# work in progress

import gspread
import numpy as np

gc = gspread.service_account()
sh = gc.create('Testing')
worksheet = sh.sheet1

class sheetsUI(object):
        def __init__(self, data):
            self.data = data



# write to sheet
def write_data(data):
    worksheet.clear()
    ar = np.array(data)
    worksheet.update(ar.all(), 'A2')
    return

