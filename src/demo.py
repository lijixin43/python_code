# AUTHOR lijixin

def extract_manifest_trade(json):
    json_m_trade = {}
    json_m_trade['trade_co'] = json["MANIFEST_COP_NEW"][0]["TRADE_CO"]
    return {"status": '1', "data": json_m_trade}

def extract_entry_trade(json):
    json_e_trade = {}
    json_e_trade["trade_co"] = json["entryHeadA"]["tradeCo"]
    con = cx_Oracle.connect("brgg2_qdzb", "qazwsx12", "10.99.87.136:1521/ora11g")
    cur = con.cursor()
    # 企业基本属性
    cur.execute("select signout_flag,re_date_mm,tra_earlist_month,ieport_earlist_month,pro_id,city_id,"
                "qy_id,customs_code,ownership,co_class,corp_type,rg_fund,or_chinese,cp_qy,hg_city"
                "from trade_w_basic where trade_co=:trade_co",json["entryHeadA"]["tradeCo"])
    rows = cur.fetchone()
    json_e_trade["signout_flag"] = rows[0]
    json_e_trade["re_date_mm"] = rows[1]
    json_e_trade["tra_earlist_month"] = rows[2]
    json_e_trade["ieport_earlist_month"] = rows[3]
    json_e_trade["pro_id"] = rows[4]
    json_e_trade["city_id"] = rows[5]
    json_e_trade["qy_id"] = rows[6]
    json_e_trade["customs_code"] = rows[7]
    json_e_trade["ownership"] = rows[8]
    json_e_trade["co_class"] = rows[9]
    json_e_trade["corp_type"] = rows[10]
    json_e_trade["rg_fund"] = rows[11]
    json_e_trade["or_chinese"] = rows[12]
    json_e_trade["cp_qy"] = rows[13]
    json_e_trade["hg_city"] = rows[14]
    cur.close
    con = cx_Oracle.connect("brgg2_qdzb", "qazwsx12", "10.99.87.136:1521/ora11g")
    cur1 = con.cursor()
    # 经营企业 行为+关联字段trade_co
    cur1.execute("select entry_cnt,entry_half_cnt,entry_mon_cnt,tra_half_cnt,tra_half_5_rate,tra_half_10_rate,
        "tra_mon_cnt,tra_mon_5_rate,tra_mon_10_rate,tra_exam_half_cnt,half_danger,tra_exam_mon_cnt,mon_danger "
    "from tra_entry_cnt where trade_co=:trade_co ", json["entryHeadA"]["tradeCo"])
    rows1 = cur1.fetchone()
    json_e_trade["entry_cnt"] = rows1[0]
    json_e_trade["entry_half_cnt"] = rows1[1]
    json_e_trade["entry_mon_cnt"] = rows1[2]
    json_e_trade["tra_half_cnt"] = rows1[3]
    json_e_trade["tra_half_5_rate"] = rows1[4]
    json_e_trade["tra_half_10_rate"] = rows1[5]
    json_e_trade["tra_mon_cnt"] = rows1[6]
    json_e_trade["tra_mon_5_rate"] = rows1[7]
    json_e_trade["tra_mon_10_rate"] = rows1[8]
    json_e_trade["tra_exam_half_cnt"] = rows1[9]
    json_e_trade["half_danger"] = rows1[10]
    json_e_trade["tra_exam_mon_cnt"] = rows1[11]
    json_e_trade["mon_danger"] = rows1[12]
    cur1.close
    json_e_trade["i_e_port"] = json["entryHeadA"]["iEPort"]
    con = cx_Oracle.connect("brgg2_qdzb", "qazwsx12", "10.99.87.136:1521/ora11g")
    cur2 = con.cursor()

    # 经营企业 行为+关联trade_co,i_e_port
    cur2.execute(
        "select i_e_port,ieport_cnt,ieport_mon_cnt,ieport_half_cnt,"
        "tra_exam_iport_half_cnt,half_ie_danger,tra_exam_iport_mon_cnt,mon_ie_danger,ieport_earlist_month  "
        "from tra_ieport_cnt where trade_co=:trade_co and i_e_port=:i_e_port ",
        json["entryHeadA"]["tradeCo"],json["entryHeadA"]["iEPort"])
    rows2 = cur2.fetchone()
    json_e_trade["ieport_cnt"] = rows2[0]
    json_e_trade["ieport_mon_cnt"] = rows2[1]
    json_e_trade["ieport_half_cnt"] = rows2[2]
    json_e_trade["tra_exam_iport_half_cnt"] = rows2[3]
    json_e_trade["half_ie_danger"] = rows2[4]
    json_e_trade["tra_exam_iport_mon_cnt"] = rows2[5]
    json_e_trade["mon_ie_danger"] = rows2[6]
    json_e_trade["ieport_earlist_month"] = rows2[7]
    cur2.close


    json_e_trade["decl_port"] = json["entryHeadA"]["declPort"]
    con = cx_Oracle.connect("brgg2_qdzb", "qazwsx12", "10.99.87.136:1521/ora11g")
    cur3 = con.cursor()
    # 经营企业 行为+关联字段trade_co，decl_port
    cur3.execute(
        "select dport_cnt,dport_mon_cnt,dport_half_cnt,tra_dport_half_cnt,"
        "tra_dport_half_5_rate,tra_deport_half_10_rate,tra_dport_mon_cnt,tra_dport_mon_5_rate,"
        "tra_dport_mon_10_rate from tra_dport_cnt where trade_co=:trade_co and decl_port=:decl_port ",
        json["entryHeadA"]["tradeCo"],json["entryHeadA"]["declPort"])
    rows3= cur3.fetchone()
    json_e_trade["dport_cnt"] = rows3[0]
    json_e_trade["dport_mon_cnt"] = rows3[1]
    json_e_trade["dport_half_cnt"] = rows3[2]
    json_e_trade["tra_dport_half_cnt"] = rows3[3]
    json_e_trade["tra_dport_half_5_rate"] = rows3[4]
    json_e_trade["tra_deport_half_10_rate"] = rows3[5]
    json_e_trade["tra_dport_mon_cnt"] = rows3[6]
    json_e_trade["tra_dport_mon_5_rate"] = rows3[7]
    json_e_trade["tra_dport_mon_10_rate "] = rows3[8]
    cur3.close
    return  {"status": '1', "data": json_e_trade}
