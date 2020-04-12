import mysql.connector  as connector
import random
from threading import Thread, activeCount, Lock
from mysql.connector import pooling

#  用户表结构
# '''
# CREATE TABLE `users` (
#   `user_id` int(11) NOT NULL AUTO_INCREMENT,
#   `username` varchar(30) DEFAULT NULL,
#   `realname` varchar(45) DEFAULT NULL,
#   `password` varchar(45) DEFAULT NULL,
#   `province` varchar(45) DEFAULT NULL,
#   `city` varchar(5) DEFAULT NULL,
#   `age` tinyint(2) DEFAULT NULL,
#   `sex` enum('男','女') DEFAULT NULL,
#   `mylike` set('钓鱼','旅游','看书','唱歌') DEFAULT NULL,
#   `reg_date` datetime DEFAULT NULL,
#   `last_login` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY (`user_id`),
#   UNIQUE KEY `username_UNIQUE` (`username`)
# ) ENGINE=InnoDB AUTO_INCREMENT=560026 DEFAULT CHARSET=utf8mb4;


# 批量设置注册时间，登陆时间
# 批量设置省份,城市
from datetime import datetime, timedelta

provinces = ['江苏', '浙江', '上海', '北京', '重庆', '广东', '山东', '湖北']
citys = {}
citys['江苏'] = ["南京", "苏州", "无锡", "常州", "泰州", "扬州"]
citys['浙江'] = ["杭州", "宁波", "嘉兴", "丽水", "台州", "温州"]
citys['上海'] = ['黄埔区', '静安区', '杨浦区', '虹口区', '松江区', '浦东新区']
citys['北京'] = ['东城区', '西城区', '朝阳区', '丰台区', '昌平区', '通州区']
citys['重庆'] = ['万州区', '江北区', '渝北区', '南岸区', '巴南区', '江津区']
citys['广东'] = ['广州', '佛山', '肇庆', '中山', '珠海', '江门']
citys['山东'] = ['济南', '青岛', '烟台', '威海', '菏泽', '临沂']
citys['湖北'] = ['武汉', '宜昌', '黄石', '十堰', '襄阳', '鄂州']

# max = round(datetime.timestamp(datetime.now()))
# min = round(datetime.timestamp(datetime.now() - timedelta(days=365)))

pooling.CNX_POOL_MAXSIZE = 32
cnxpool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=30, user='root', password='123456',
                                      host='localhost', database='mycms')
print("pool:", type(cnxpool))


def set_fields(last_id):
    print(last_id)
    sql = "update `mycms`.`users` set `province`='{province}', `city`='{city}', `reg_date`='{reg_date}', `last_login`='{last_login}' where `user_id`='{last_id}'"
    province = random.choice(provinces)
    reg_date = datetime.now() - timedelta(days=random.randint(0, 365))
    params = {
        'province': province,
        'city': random.choice(citys[province]),
        'reg_date': reg_date,
        'last_login': reg_date + timedelta(days=random.randint(0, 300)),
        'last_id': last_id,
    }
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
    except Exception as e:
        print("no get", e)
        return False
    try:
        sql = sql.format(**params)
        cursor.execute(sql)
        cnx.commit()
    except Exception as err:
        print('error:', err)
    finally:
        cursor.close()
        cnx.close()


last_id = 0


def run():
    global last_id
    while True:
        print("active_count:", activeCount())
        if activeCount() < 30:
            try:
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
            except:
                print("等待释放")
            else:
                sql = "select user_id from users where user_id > {last_id} and province is null limit 30 "
                sql = sql.format(last_id=last_id)
                print(sql)
                cursor.execute(sql)
                ids = cursor.fetchall()
                cursor.close()
                cnx.close()
                print(ids)
                if not ids:
                    break
                else:
                    last_id = ids[-1][0]
                    for id in ids:
                        t = Thread(target=set_fields, args=(id[0],))
                        t.start()
                        pass


if __name__ == '__main__':
    run()
