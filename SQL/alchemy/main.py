from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password':'hitema',
    'database':'classicmodels'
}
db_user = config.get('user')
db_pwd =config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connexion_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connexion_str)
connexion = engine.connect()
##sql raw ->
rs = connexion.execute('SELECT * FROM payments')

for row in rs:
    print(row)

##metadata
metadata = MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()
##
payments= Base.classes.payments
##session
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(payments).all()
for row in result:
    print("customer number : ",row.customerNumber,"checknumber :", row.checkNumber,"paymentdate :", row.paymentDate,"amount :", row.amount)