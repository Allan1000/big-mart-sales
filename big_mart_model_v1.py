import pandas as pd
import numpy as np

# Reading in files
train = pd.read_csv('data\\formatted_data\\train.csv')
test = pd.read_csv('data\\formatted_data\\test.csv')

test.describe()