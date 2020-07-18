# AUTHOR lijixin

import numpy as np
import pandas as pd
from odps import ODPS
from odps.models import Schema,Column
from odps.models.table import Table
from logging as log
import  time

class OdpsHelper:
    def __init__(self,access_id="",secret_access_key="",project="",
                 endpoint="",verbose=1,link_now=1):
        self.access_id = access_id
        self.secret_access_key = secret_access_key
        self.project = project
        self.endpoint = endpoint
        self.varbose = verbose
        self.odps_instance = None
        if link_now:
            self.link()
    def link(self):
        self.odps_instance = ODPS(access_id = self.access_id,
                                  secret_access_key = self.secret_access_key,
                                  project = self.project,
                                  endpoint = self.endpoint)
        return self.odps_instance
    def generate_odps_columns_from_pandas_df(self,df):
        type_dict = {"int64":'BIGINT','float64':'DOUBLE','object':'STRING'}
        column_types = df.dtypes
        odps_columns = []
        for c_name in column_types.index:
            temp_type = type_dict.get(str(c_name),'STRING')
            if self.verbose:
                print("Transfer from pandas columns to odps columns:",
                      o_name +'->'+c_name.lower()+':'+'str(column_type[c_name])+'
                                                      '->'+temp_type)
                odps_columns.append(Column(name=c_name.lower(),type=temp_type))
        return odps_columns
    def generate_table(self,table_name,columns,if_not_exists=True):
        schema = Schema(columns=columns)
        self.odps_instance.create_table(table_name.lower(),schema,if_not_exists=if_not_exists)
        t = self.odps_instance.get_table(table_name)
        return t
    def write_odps_from_pandas_df(self,table,df):
        if isinstance(table,str):
            t = self.generate_table(table,self.generate_odps_columns_from_pandas_df(df))
        elif isinstance(table,Table):
            t = table
        else:
            raise Exception("Unsupported data type")
        df_renamed = df.rename(str.lower,axis=1)
        columns_for_sort = [x.name for x in t.schema.columns]
        df_final = df_renamed.loc[:,columns_for_sort]
        odps_data = np.array(df_final).tolist()
        with t.open_writer() as writer:
            writer.write(odps_data)
        writer.close()

    def write_odps_from_csv(self,table_name,csv_path):
        df = pd.read_csv(csv_path)
        self.write_odps_from_pandas_df(table_name,df)

    def read_odps_to_pandas_df(self,table,top_n=-1):
        if isinstance(table,str):
            t = self.odps_instance.get_table(table)
        elif isinstance(table,Table):
            t = Table
        else:
            raise  Exception("Unsupported data type")

        log.info("============== Table info:\n"+str(t))
        table_name = t.name
        columns = []
        with t.open_reader() as reader:
            count = reader.count
            log.info("=========== row count:"+str(count))
            for row in reader[:1]:
                columns = np.array(row)[:,0]
        data = []
        counter = 0
        step_count = 100
        counters = 0
        step_length = count
        if self.varbose
            print("========= start reading table:",table_name,'total:',count,'step length',step_length)
            print("========= read top:",top_n)
        start_time = time.time()
        columns_len = len(columns)
        for row in t.open_reader():
            temp_data = []
            for j in range(columns_len):
                temp_data.append(row[j])
            data.append(temp_data)
            counter += 1
            if top_n>0:
                if(counters + counter) == top_n:
                    break
            if counter == step_length:
                counters += counter
                step_now = round(counters * 100 /count,1)
                if self.verbose:
                    print("100%")
                    print("============= end reading table.Elasped minutes:",round((time.time() - start_time)/60,2))
                result = pd.DataFrame(data,columns=columns)
                return result






if __name__ == "__main__":
    oh = OdpsHelper(access_id='',
                    secret_access_key='',
                    project='',
                    endpoint='')
    df_titanic = oh.read_odps_to_pandas_df("titanic_test")
    df_titanic.to_csv('./titanic_test.csv')
    print('Done')