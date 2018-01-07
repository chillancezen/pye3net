#
#Copyright (c) 2018 Jie Zheng
#
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_bases=dict()
db_sessions=dict()
db_engines=dict()



def create_database_entries(db_name,base=None):
    db_bases[db_name]=base if base is not None else declarative_base()
    db_bases[db_name].metadata.create_all(db_engines[db_name])

def init_database(db_name,conn,echo=False):
    db_engines[db_name]=create_engine(conn,echo=echo)
    db_sessions[db_name]=sessionmaker(autocommit=True)
    db_sessions[db_name].configure(bind=db_engines[db_name])


if __name__=='__main__':
    init_database('E3NET_VSWITCH','mysql+pymysql://e3net:e3credientials@localhost/E3NET_VSWITCH',True)
    create_database_entries('E3NET_VSWITCH')
