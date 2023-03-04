import psycopg2 as pg
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

class action_:
    def __init__(self):
        self.conn = None
        self.cursor = None
    def connect(self):
        try:
            self.conn = pg.connect(
                host="database-2.cf5cyqhkjo5q.us-east-1.rds.amazonaws.com",
                port=5432,
                user="postgres",
                password="sam42671209",
                database="postgres"
            )
            self.cursor = self.conn.cursor()
            self.conn.autocommit = True
        except Exception as error:
                print (error)

    def disconnect(self):
        self.conn.close()
        self.cursor.close()
    # distribution part
    def add(self, id, size, color, num, new=None):
        if new:
            sql = f"insert into distribution(id,size,color,of_num) " \
                  f"values ('{id}', {size}, {color},{num})"

        else:
            sql = f"update distribution " \
                  f"set of_num = of_num + {num} " \
                  f"where id='{id}' and size = {size} and color= {color}"
        self.cursor.execute(sql)

    def importClothes(self, id, place_of_origin, material, sale, manufacture, item_no, cost, price):
        sql = f"insert into clothes(id,place_of_origin,material,sale,manufacture,item_no,cost,price) "\
              f"values('{id}','{place_of_origin}','{material}','{sale}',{manufacture},{item_no},{cost},{price})"
        self.cursor.execute(sql)

    def decrease(self,id,size,color,num,store):
        sql = f"update distribution "\
              f"set {store}_num = {store}_num - {num} "\
              f"where id='{id}' and size = {size} and color= {color}"
        self.cursor.execute(sql)

    def deliver(self,id,size,color,num,store1,store2):
        sql = f"update distribution "\
              f"set {store1}_num = {store1}_num - {num} "\
              f"where id='{id}' and size = {size} and color= {color}; "\
              f"update distribution "\
              f"set {store2}_num = {store2}_num + {num} "\
              f"where id='{id}' and size = {size} and color= {color}; "
        self.cursor.execute(sql)

    # sale part
    def sold(self, id, size, color, num, cash_or_card, sales, store,income):
        now = datetime.datetime.now()
        time = now - datetime.timedelta(minutes=10)
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        time = time[:-4] + '0:00'
        sql = f"update distribution "\
              f"set {store}_num = {store}_num - {num} "\
              f"where id='{id}' and size = {size} and color= {color}; "\
              f"insert into sold(id,size,color,num,cash_or_card,timestamp,sales,store,income) "\
              f"values('{id}',{size},{color},{num},'{cash_or_card}','{time}','{sales}','{store}',{income})"
        self.cursor.execute(sql)

    def exchange(self, id, size,color, num, store,sold_date):
        now = datetime.datetime.now()
        time = now - datetime.timedelta(minutes=10)
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        time = time[:-4] + '0:00'
        sql = f"select timestamp "\
              f"from sold "\
              f"where id = '{id}' and color = {color} and size = {size} and store = '{store}' and date(timestamp) = '{sold_date}'"
        self.cursor.execute(sql)
        sold_date_ = self.cursor.fetchall()
        sql = f"update distribution "\
              f"set {store}_num = {store}_num + {num} "\
              f"where id='{id}' and size = {size} and color= {color}; "\
              f"insert into exchange(id, size, color, num, sold_date, return_date, store)"\
              f"values('{id}',{size},{color},{num},'{sold_date_[0][0].strftime('%Y-%m-%d %H:%M:%S')}','{time}','{store}')"
        self.cursor.execute(sql)

    #look-up part
    def number(self, id):
        sql = f"select * "\
              f"from distribution "\
              f"where id ='{id}' " \
              f"order by id, size"
        table = pd.read_sql(sql,self.conn)
        return table

    def colorAndsize(self,id):
        sql = f"select color, size "\
              f"from distribution "\
              f"where id = '{id}' "\
              f"order by id, size"
        table = pd.read_sql(sql,self.conn)
        return table

    def detail(self,id):
        sql = f"select * "\
              f"from clothes "\
              f"where id ='{id}'"
        #self.cursor.execute(sql)
        table = pd.read_sql(sql,self.conn)
        return table
    def soldRecord(self, date, store):
        sql = f"select * " \
              f"from sold " \
              f"where date(timestamp) = '{date}' and store = '{store}' " \
              f"order by id, size"
        table = pd.read_sql(sql,self.conn)
        return table

    def exchangeRecord(self):
        sql = f"select * " \
              f"from exchange " \
              f"order by return_date"
        table = pd.read_sql(sql, self.conn)
        return table

    #static part
    def salesVolume(self,period,date):
        if period == 'daily':
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) = '{date}' and store = 'k1') as r1 "\
                f"group by r1.sales"
            k1_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) = '{date}' and store = 'k3') as r1 "\
                f"group by r1.sales"
            k3_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) = '{date}' and store = 'k4') as r1 "\
                f"group by r1.sales"
            k4_report = pd.read_sql(sql,self.conn)
            return k1_report,k3_report,k4_report
        elif period == 'monthly':
            end = datetime.datetime.strptime(date, '%Y-%m')
            end = end + relativedelta(months=1)
            end = end.strftime("%Y-%m")
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01' and date(timestamp) < '{end}-01' and store = 'k1') as r1 "\
                f"group by r1.sales"
            k1_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01' and date(timestamp) < '{end}-01' and store = 'k3') as r1 "\
                f"group by r1.sales"
            k3_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01' and date(timestamp) < '{end}-01' and store = 'k4') as r1 "\
                f"group by r1.sales"
            k4_report = pd.read_sql(sql,self.conn)
            return k1_report,k3_report,k4_report
        elif period == 'year':
            end = datetime.datetime.strptime(date, '%Y')
            end = end + relativedelta(years=1)
            end = end.strftime("%Y")
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01-01' and date(timestamp) < '{end}-01-01' and store = 'k1') as r1 "\
                f"group by r1.sales"
            k1_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01-01' and date(timestamp) < '{end}-01-01' and store = 'k3') as r1 "\
                f"group by r1.sales"
            k3_report = pd.read_sql(sql,self.conn)
            sql = f"select r1.sales, sum(r1.income) "\
                f"from (select * "\
                f"from sold "\
                f"where date(timestamp) >= '{date}-01-01' and date(timestamp) < '{end}-01-01' and store = 'k4') as r1 "\
                f"group by r1.sales"
            k4_report = pd.read_sql(sql,self.conn)
            return k1_report,k3_report,k4_report
        else:
            print('period error')