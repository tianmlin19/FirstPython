import pymysql
import os
import datetime

# 打开数据库连接
db = pymysql.connect(host='172.27.48.181', user='search', password='search@zyfax.com', db='invest')
#db = pymysql.connect(host='10.3.100.110', user='mysqluser', password='mysqluser@zyxr.com')

# 使用cursor()方法获取操作游标
cur = db.cursor()
nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 现在
begin = nowTime + " 00:00:00"
end = nowTime + " 23:59:59"
print("begin:%s", begin)
print("end:%s", end)


class MonitRepay(object):

    def get_asset_info(self):
        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql1 = "SELECT COUNT(1) AS amount,k.`business_name` FROM invest.`t_investment_payoffs` t,product.`t_assets` k WHERE t.`financial_plan_id` = k.`asset_id`  AND t.state = 0  AND t.`create_time` BETWEEN '%s' AND '%s' GROUP BY k.`business_name` ;  "
        print("sql1:", sql1 % (begin, end))

        cur.execute(sql1 % (begin, end))

        result1 = cur.fetchall()
        if result1 is None:
            return
        try:
            for res in result1:
                amount = res[0]
                businessName = res[1]
                print("待回款的标的名称为：", businessName, nowTime, "待回款的数量为：", amount, "\n")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("稍等,正在查询......\n")
    repay = MonitRepay()
    try:
        repay.get_asset_info()
    except Exception as e:
        print(e)
    finally:
        input("请输入任意字符，继续....")
        db.close()  # 关闭连接
    # os.system('pause')
