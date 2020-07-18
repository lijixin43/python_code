# AUTHOR lijixin
# import pandas as pd
#
#
# df = pd.read_csv('‪D:\apply.csv',sep=',', header=None)
# print(df.info())
#
# df.to_csv("‪D:\ch06\20200529\t_c_health_code_apply_1.csv")

import sys
import pandas as pd

import sys
import imp


df = pd.read_csv('D:/apply.csv',header=None,iterator=True,
                 names=["id","uuid","user_name","cert_type","cert_code","cert_code_hide","cert_code_secret","open_id","channel_id","update_flag","phone","relation_cert_secret","apply_entrust_relation","wx_live_type","is_leave_wx_type","arrive_wx_date","is_from_hb","departure_addr","departure_addr_code","arrive_wx_traffic","arrive_wx_trafficode","is_two_week_virus","household_code","household_name","emergency_person","emergency_phone","district_code","current_district","street_code","current_street","community_code","current_community","police_station_code","police_station","housing_name","live_address","current_person_img","is_hot","is_leave","is_stay","is_healthy","isolation_days","isolation_date","check_code","check_person","punch_date","atten_days","tips_code","alarm_code","is_respira_sick","is_address_right","two_week_travel","pass_addr_name","pass_addr_code","tran_status","status","flag","is_return_wuxi","community_flag","person_auth_flag","round_trip_code","round_trip_name","work_unit","school_code","res_one","res_two","res_three","res_four","res_five","img_update_time","punch_time","response_time","flag_fresh_time","create_time","update_time","nation_code","allopatry_code","allopatry_name","paasway_codes","is_isola_virus_psn","is_cure_virus_psn","is_obser_virus_psn","update_status"
])

df = df.get_chunk(15000000)


df.to_csv('D:/ch06/20200529//apply_back.csv',sep=',')