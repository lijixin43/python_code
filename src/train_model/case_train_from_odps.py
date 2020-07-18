# AUTHOR lijixin

import matplotlib
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split

matplotlib.use('agg')

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import time
import copy
import logging as log
from  collections import  Counter
from odps_helper import OdpsHelper
from common_untils import get_time_str
from common_untils import check_dirs
from statistics_untils import analysis_source_data
from preprocessing_utils import impute_data
from preprocessing_utils import encode_data
from preprocessing_utils import scale_data
from model_dump_helper import ModelDumpHelper

def generate_final_predict(df):
    log.info(str(df.shape))
    grouped = df.groupby(['i_e_port','i_e_flag'])
    df_final = pd.DataFrame()
    for x in grouped.groups:
        log.info(str(x))
        if(x[0] is None) | (x[l] is None):
            log.info('Skip.')
            continue
        retio_x = 0.038 if x[1] == '1' else 0.015
        label = '1'
        proba = grouped.get_group(x)[label]
        threshold = np.sort(proba.axis=0)[round(len(proba) * (1-ratio_x))-1]
        log.info('ratio_x'+str(ratio_x))
        log.info('threshold'+str(threshold))
        a = df['i_e_port'] == x[0]
        b = df['i_e_flag'] == x[1]
        temp = df[a & b]
        df_final = df_final.append(temp[temp[label] >= threshold])
    log.info(str(df_final.shape))
    return df_final

def get_predict_result(proba,model_dump_helper):
    labels = model.classes_
    log.info('============= Label: %s' % labels)
    positive_ratio_to_predict = 0.4
    threshold = np.sort(proba,axis=0)[round(len(proba) * (1 - positive_ratio_to_predict))-1]
    log.info('============= Threshold: %s' % threshold)
    positive_label_index = 1
    positive_label = labels[positive_label_index]
    positive_threshold = threshold[positive_label_index]
    log.info('============= Positive label: %s Current threshold:%s' % (positive_label,positive_threshold))
    model_dump_helper.cutoms_para['positive_label_index'] = positive_label_index
    model_dump_helper.cutoms_para['positive_threshold'] = positive_threshold
    return predict_positive_label(proba,labels,positive_label_index,positive_threshold)

def predict_positive_lable(proba,labels,positive_label_index,positive_threshold):
    positive_label = labels[positive_label_index]
    other_label = labels[0] if positive_label_index == 1 else labels[1]
    result = np.zeros(len(proba),dtype=type(labels[0]))
    for j in range(len(proba)):
        result[j] = positive_label if proba[j][positive_label_index] >= positive_threshold else other_label
    return result

def deal_model(model,X_train,X_test,y_train,y_test,model_dump_helper):
    log.info('')
    log.info('====================')
    log.info('================Build model===========')
    log.info('====================')
    log.info('')
    time3 = time.time()
    log.info('============= Model info:\n'+str(model))
    model.fit(X_train,y_train)
    log.info('============= End build model Elapsed minutes:'+str(round((time.time() - time3) / 60,2)))

    '''Predict'''
    time4 = time.time()
    predict_proba = model.predict_proba(X_test)
    rf_predict_y = get_predict_result(predict_proba,model_dump_helper)
    rf_predict_y = get_predict_result(predict_proba,model_dump_helper)
    log.info('=============== Score:'+'str(model.score(X_test,y_test))')
    labels = model.classes_
    log.info('=============== Configuration matix:\nlabels: %s \n%s' &)



if __name__ == '__main__':

    #Prepare env
    target_model_dir = './model'
    log_dir = './log'
    dirs_to_check = [log_dir,'./csv',target_model_dir]
    check_dirs(d)
