# AUTHOR lijixin
import logging as log
import random
from  collections import Counter

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

def random_under_sample(df,y_name,multiple=1.0):
    [[first_label,first_count],[second_label,second_count]]=Counter(df[y_name]).most_common(2)
    first_index = list(df[df[y_name]== first_label].index)
    second_index = list(df[df[y_name]== second_label].index)
    sampled_index = random.sample(first_index,round(second_count * multiple))+second_index
    return df.loc[random.sample(sampled_index,len(sampled_index)),-1]

def Imputer_data(df,model_dump_helper):
    imputed_data = pd.DataFrame()
    fill_dict = {}
    for c_n in df.columns:
        if df.dtypes[c_n] in ['object']:
            to_fill = Counter(df[pd.notna(df[c_n])][c_n]).most_common(1)[0][0]
            imputed_data[c_n] = df[c_n].fillna(to_fill)
            imputed_data[c_n] = imputed_data[c_n].astype("str")
            fill_dict[c_n] = to_fill
        else:
            imputer_num = Imputer()
            imputed_data[c_n] = imputer_num.fit_transform(df.loc[:,[c_n]]).reshape(-1)
            fill_dict[c_n] = imputer_num.statistics_[0]
    model_dump_helper.apply_steps.append({'type','impute','impute_dict','fill_dict'})
    return imputed_data
def encode_data(df,statistics_data,model_dump_helper):
    types = df.dtypes
    label_encoder_action = {'type':'label','encode_dict':{}}
    model_dump_helper.apply_steps.append(label_encoder_action)
    one_hot_encoder_action = {'type':'label','encode_dict':{}}
    model_dump_helper.apply_steps.append(one_hot_encoder_action)
    for c in df.columns:
        if types[c] in ['object']:
            count_unique = statistics_data['nunique'][c]
            log.info('===========Label encode for'+str(c)+'.Count'+str(count_unique))
            le = LabelEncoder()
            le.fit(df[c].append(pd.Series(['unknown']),ignore_indx=True))
            df[c] = le.transform(df[c])
            label_encoder_action['encode_dict'][c] = le
            if count_unique <= 10:
                log.info('===========one hot for'+str(c)+'.Count:'+str(count_unique))
                one_hot = OneHotEncoder(sparse=False,handle_unknown='ignore')
                temp_transformed = one_hot.fit_transform(df[c].values.reshape(-1,1))
                temp_colums = []
                log.info('==============='+str(one_hot.active_features_))
                for category in one_hot.active_features_:
                    temp_colums.append(str(c)+'_'+str(category))
                df_join = pd.DataFrame(temp_transformed,df.index,temp_colums)
                df = df.join(df_join,lsuffix='_left',rsuffix='_right').drop(c,axis=1)
                one_hot_encoder_action['encode_dict'][c] = one_hot
    return df
def scale_data(df,statistics_data,model_dump_helper):
    temp = list(statistics_data[statistics_data['interval']>5].index)
    colums_need_scaler = [ x for x in temp if x in model_dump_helper.X_columns['names']]
    scale_action = {'type':'scale','scale_dict':{}}
    model_dump_helper.apply_steps.append(scale_action)
    for i in range(len(colums_need_scaler)):
        c = colums_need_scaler[i]
        scaler = MinMaxScaler()
        scaled_column = scaler.fit_transform(df.loc[:,[c]])
        df.loc[:,[c]] = scaled_column
        scale_action['scale_dict'][c] = scaler
    return df



