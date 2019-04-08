import datetime

print("Hello world,this is my first exe file !")
nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 现在
begin = nowTime + " 00:00:00"
end = nowTime+" 23:59:59"
print(nowTime)
print(begin)
print(end)
