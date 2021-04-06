import json,os,sys

# 将处理好的数据组织成所需格式的字典
def createoneclass(classname,startweek,endweek,weekday,weeks,classTime,classroom):
    week = {
        "startweek":startweek,
        "endweek":endweek
    }
    oneclass = {
        "className":classname,
        "week":week,
        "weekday":weekday,
        "weeks":weeks,
        "classTime":classTime,
        "classroom":classroom
    }
    return oneclass

with open('DATA/lessonsdata.json', 'r',encoding='UTF-8') as f:
    before = json.load(f)
    after = []
    dic = {}
    # print(type(data))
    # print(data[0])
    num = len(before)
    classInfo = []
    # 代号与课程具体时间和的转换
    dictrans = {
        2:1,
        12:2,
        336:3,
        56:4,
        5040:5,
        132:6,
        1716:7,
        90:8,
        3024:9,
        60:10,
        24024:11
    }
    # 生成课程名称、教室、起止周数、上课日期、时间
    for i in range(num):
        weekdays = []
        startweek = 15
        endweek = 0
        weeks = []
        classtime = []
        classname = before[i]['course']['name']
        classroom = before[i]['classes'][0]['classroom']['name']
        # print('课程名称：'+classname)
        # print('教室'+classroom)

        omeclassnum = len(before[i]['classes'])
        for j in range(omeclassnum):
            if(startweek > before[i]['classes'][j]['schedule']['week']):
                startweek = before[i]['classes'][j]['schedule']['week']
            if(endweek < before[i]['classes'][j]['schedule']['week']):
                endweek = before[i]['classes'][j]['schedule']['week']
        startweek = startweek+1
        endweek = endweek+1

        for j in range(omeclassnum):
            if(before[i]['classes'][j]['schedule']['day']+1 not in weekdays):
                weekdays.append(before[i]['classes'][j]['schedule']['day']+1)
        # 以下部分进行的是上课具体时间的转换
        # weekday（周几）、weeks（单双周）、classtime（第几节课）三个元素，如果同一节课每周有多个时间段，则也有多个，故要以列表形式存储
        for k in range(len(weekdays)):
            classtimes = []
            weeks.append(0)
            flag = 1
            for j in range(omeclassnum):
                if(before[i]['classes'][j]['schedule']['day']==weekdays[k]-1):
                    if (before[i]['classes'][j]['schedule']['week']%2==0):
                        # 单双周同时出现，则为全周
                        if(weeks[k] == 2 or weeks[k] == 3):
                            weeks[k] = 3
                        else:
                            weeks[k] = 1
                    # 双周
                    if (before[i]['classes'][j]['schedule']['week']%2==1):
                        # 单双周同时出现，则为全周
                        if(weeks[k] == 1 or weeks[k] == 3):
                            weeks[k] = 3
                        else:
                            weeks[k] = 2
                    # 上课具体时间
                    if(before[i]['classes'][j]['schedule']['period']+1 not in classtimes):
                        classtimes.append(before[i]['classes'][j]['schedule']['period']+1)
            for l in classtimes:
                flag = flag*l
            if(flag in dictrans and dictrans[flag]):
                classtime.append(dictrans[flag])
        # 调用字典生成函数
        for k in range(len(weekdays)):
            try:
                oneclasss = createoneclass(classname,startweek,endweek,weekdays[k],weeks[k],classtime[k],classroom)
                classInfo.append(oneclasss)
            except:
                print(i)
                sys.exit()

    result = {
        "classInfo":classInfo
    }
    print(result)
# 写入
json_str = json.dumps(result,ensure_ascii=False,indent=4)
with open('DATA/conf_classInfo.json', 'w',) as json_file:
    json_file.write(json_str)

# 运行课表生成程序
os.system("python dataprocess.py")
    # print(classtimes)
        # print(classtime)
        # print(weeks)
        # print(weekdays)
        # print(startweek)
        # print(endweek)
        # after.append()

