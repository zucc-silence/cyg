# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class CygPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("delete from tl_cyg_copy")
        self.conn.commit()

    def process_item(self, item, spider):
        data =dict(item)
        if "/" in data['area']:
            data['area'] = pymysql.escape_string(str(data['area']))
        sql = "insert into tl_cyg_copy(sect,sex,level,name,score,xiulian,jinjie,price,area,is_tag) values('{}','{}','{}','{}','{}','{}','{}','{}','{}',{});".format(
            data['sect'], data['sex'], data['level'], data['name'], int(data['score']), data['xiulian'], data['jinjie'], int(data['price']),data['area'],data['is_tag'])
        try:
            self.cur.execute(sql)
        except Exception as e:
            print(e)
            print(data)
        self.conn.commit()
        #print(data)
        return item
