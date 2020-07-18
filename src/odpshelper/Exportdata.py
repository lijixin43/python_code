# AUTHOR lijixin

from odps import ODPS
from odps.df import DataFrame
import pandas as pd
import xlwt

"""
your-access-id：账户的AccessKey ID。
your-secret-access-key：账户的AccessKey Secret。
your-default-project：使用的项目空间名称。
your-end-point：MaxCompute服务所在区域的Endpoint。
"""
o = ODPS('**your-access-id**', '**your-secret-access-key**', '**your-default-project**',endpoint='**your-end-point**')
t = o.get_table('entry_range_e_info_result')

datas1 = DataFrame(t)

a = []
reader = t.open_reader()
count = reader.count
print(count)

#遍历行和列
for record in reader[0:count]:
    one = []
    for col in t.schema.names:
        one.append(record[col])
    a.append(one)
data1 = pd.DataFrame(a,columns=datas1.schema.names)
data1.to_csv(r'D:\ch06\20200622',index=True)


