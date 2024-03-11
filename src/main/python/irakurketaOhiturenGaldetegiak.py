'''
Irakaslegaien irakurketa ohituren Galdetegietako emaitzak
'''

from directoryUtils import move_to_directory
from directoryUtils import file_exists

from odsUtils import readODS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


data = "/home/ilopez077/scratch/Gatai/Data/Irakaslegaien_Irakurketa_Ohiturak_Galdetegietako_emaitzak"
move_to_directory(data)

fitxategia = "garbia.ods"
file_exists(fitxategia)

df = readODS(fitxategia, skiprows=2, header=None, names=[])








