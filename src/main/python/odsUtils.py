'''
pip install pandas odfpy
'''

import pandas as pd

def readODS(file_path : str, skiprows = 0, header = None, names = []):
    return pd.read_excel(file_path, engine='odf', skiprows=skiprows, header=header, names=names)
