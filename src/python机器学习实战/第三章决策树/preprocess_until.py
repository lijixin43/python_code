# AUTHOR lijixin

import logging as log
import random
from collections import Counter

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

def random_under_sample(df,y_name,multiple=1.0):
    [[first_label, first_count], [second_label, second_count]] = Counter(df[y_name]).most_common(2)
    first_index = list(df[df[y_name] == first_label].index)
    second_index = list(df[df[y_name] == ])

