# -*- coding: utf-8 -*-
# __author__:xiuming
# __QQ__:1365337879
# 2022/4/14 11:02
import http.client
import json
import time
import secrets
import requests
import mp3play
########################################用户配置#################################
timebegin = "06:00"
timeend = '09:00'
datas = "任务已出现"
Name = "超市果蔬开档"
###################################################################################
'''已经失效
#获取token
def login():
  conn = http.client.HTTPSConnection("ework.lzstack.com")
  payload = "0bmi1uor1qVGYWDsqBPtgRVUeqcHJSF25/AwQWI7oGnu6SbOjNTEQrejPGERDK9Q\ng2Fe4r7BzjoeiETjUzI="
  headers = {
    'Content-Type': 'application/json',
    'x-http-module': 'e-work',
    'x-client-nonce': 'QDpbN6mDLOVZfXqms56EBtrTlYchurum',
    'x-http-channel': 'app',
    'x-http-token': '',
    'x-http-screenheight': '667',
    'x-http-devicetype': 'iphone',
    'x-client-pubkey': '4fa1e68e6dad04ce446a15530483ce560bf467d14ab9ebd91776230c1408874d',
    'Host': 'ework.lzstack.com',
    'x-http-osversion': 'iPadOS 16.0',
    'x-http-devicetoken': 'f8dd5b07e322314e80d2f4a792035c3d69f78b97968bef7e843043ee11904520',
    'x-http-version': '2.0.8',
    'x-http-timestamp': '1655351244',
    'User-Agent': 'ework/2.0.8.1 CFNetwork/1378.1 Darwin/22.0.0',
    'j-http-devicetoken': '191e35f7e0ba5f82249',
    'Connection': 'keep-alive',
    'Cookie': 'jt=1655350309022096f298d13fb4086b5c3917b7df5f237_e-work_app; x-http-token=1655350309022096f298d13fb4086b5c3917b7df5f237_e-work_app; SERVERID=127.0.0.1:10080; jt=1655351288273d32ee34fc05648488c136609a5657f85_e-work_app; x-http-token=1655351288273d32ee34fc05648488c136609a5657f85_e-work_app',
    'x-http-screenwidth': '375'
  }
  conn.request("POST", "/api/v1/ework-auth/user/password/login", payload, headers)
  res = conn.getresponse()
  return res
'''
# 检测是否有任务
def post_shuaxin(token):
  try:
    conn = http.client.HTTPSConnection("ework.lzstack.com")
    payload = json.dumps({
      "tenantId": 81,
      "pageNum": 1,
      "pageSize": 10,
      "__hideLoading": True,
      "openPosition": 0
    })
    headers = {
      'x-User-Agent': 'iPad Air (3rd generation, WiFi)<iPad11,3> iOS 15.5',
      'Content-Type': 'application/json',
      'x-http-version': '1.10.3',
      'x-http-module': 'e-work',
      'x-http-devicetype': 'ios',
      'Host': 'ework.lzstack.com',
      'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f20) NetType/WIFI Language/zh_CN',
      'Referer': 'https://servicewechat.com/wxca1be4494e713922/21/page-frame.html',
      'x-http-token': token,
      'x-http-channel': 'miniapp',
      'Cookie': 'SERVERID=127.0.0.1:10080'
    }
    conn.request("POST", "/api/v1/ework-h5-api/taskSearch/listByPageAndTenantId", payload, headers = headers )
    conn.timeout = 2
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    return data
  except Exception as e:
    pass

#发送push信息到微信
def postserver(tittle,datas):
  app_token = 'AT_R6ust1vsAx4ABpjIUMzMQcdrCH9GNbFf'
  UID = 'UID_Lr8puuOzMExETINPwAxpnrLY4LVs'
  url = 'http://wxpusher.zjiecode.com/api/send/message'
  headers = {
    'Content-Type': 'application/json'
  }
  date = {
    "appToken": "{token}".format(token=app_token),
    "content": "{}".format(datas),
    # //消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
    "summary": "{}".format(tittle),
    # //内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
    "contentType": 3,
    # //发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
    "topicIds": [],
    # //发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
    "uids": [
      "{}".format(UID),"UID_6B9FyEYSnAzJQmaQC9EEXkiLANXe","UID_bdFw2VT7FewKI07tj53wzsBhOAHT","UID_Tez8ZRv7DqiDgntjCpFN38ivrWId"
    ],
    # //原文链接，可选参数
    "url": ""
  }
  date = json.dumps(date, ensure_ascii=False)
  # print(date)
  res = requests.post(url=url, data=date.encode('utf-8'), headers=headers)
  serverdata = json.loads(res.text)
  # print(serverdata)
  if serverdata["msg"] == '处理成功':
    print("\033[1;31m消息已发送成功! \033[0m")
  else:
    print("发送失败")
  return

#获取当前时间
def time_now():
  # 打印当前时间
  time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
  # time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  return time_now
  # 打印按指定格式排版的时间
  # time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  # print(time2)

#验证当前状态
def verify(data):
  code = data["code"]
  if code == 200:
    return 1
  elif code == 11005:
    datas = "token出错，请尽快查看程序！！！"
    print("未登录或登录超时！")
    postserver("未登录或登录超时！",datas)
    return 0

#抢单
def grab_order(token,taskNo):
  try:
    conn = http.client.HTTPSConnection("ework.lzstack.com")
    payload = json.dumps({
      "taskNo": taskNo
    })
    headers = {
      'x-User-Agent': 'iPad Air (3rd generation, WiFi)<iPad11,3> iOS 15.5',
      'Content-Type': 'application/json',
      'x-http-version': '1.10.3',
      'x-http-module': 'e-work',
      'x-http-devicetype': 'ios',
      'Host': 'ework.lzstack.com',
      'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f20) NetType/WIFI Language/zh_CN',
      'Referer': 'https://servicewechat.com/wxca1be4494e713922/21/page-frame.html',
      'x-http-token': token,
      'x-http-channel': 'miniapp',
      'Cookie': 'SERVERID=127.0.0.1:10080'
    }
    conn.request("POST", "/api/v1/ework-h5-api/order-taking", payload, headers =headers)
    
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    print(data)
    return data
  except Exception as result:
    print(result)
    return 0



def main(token):
  global datas
  i = 1
  o = 0
  j = 0
  tittle = "小活儿任务历史列表"
  plan = ''
  while (i > 0):
    try:
      data = post_shuaxin(token)
      # print(data)
      code = verify(data)
      messagecode = data['message']
      if code == 0:
        break
      else:
        list = data['data']['list']
        total = data['data']['total']
        # print('1')
        if total == 0:
          # print('2')
          # print(str(time_now()) + "  第" + str(i) + "次刷新" + str(messagecode) +  '  目前还未出现任务！ 请耐心等待...')
          print("\r\033[1;32m{time}：第{test}次刷新 {message} 目前未出现任务！请耐心等待...\033[0m".format(time=time_now(), test=i, message=messagecode),end=" ")
          i = i + 1
        else:
          # print(total)
          i = i + 1
          totallist = ""
          for j in range(total):
            #---------------------------------------------------
            num = str(j + 1)
            taskNO = str(list[j]['taskNo'])
            taskName = str(list[j]['taskName'])
            shopName = str(list[j]['shopName'])
            shopAddress = str(list[j]['shopAddress'])
            data = str(list[j]['workTime']['workDateStart'])
            begin = str(list[j]['workTime']['workStart'])
            end = str(list[j]['workTime']['workEnd'])
            hours = str(list[j]['workHour'])
            price = str(list[j]['taskPayPrice'])
            timebeg = str(time_now())
            if j == 0 :
              mg = "  ###########################################" 
            else:
              mg = ""
            #--------------------------------------------------
            mg = mg + f'''
  任务{num}
  任务序号：{taskNO}
  任务名称：{taskName}
  超市名称：{shopName}
  超市地址：{shopAddress}
  工作日期：{data}
  工作时间：{begin}——{end}
  工作时长：{hours}小时
  工作单价：{price}元/小时
  '''.format(num=str(j + 1), taskNO=str(list[j]['taskNo']), taskName=str(list[j]['taskName']),shopName=str(list[j]['shopName']), shopAddress=str(list[j]['shopAddress']),data=str(list[j]['workTime']['workDateStart']), begin=str(list[j]['workTime']['workStart']),end=str(list[j]['workTime']['workEnd']), hours=str(list[j]['workHour']),price=str(list[j]['taskPayPrice']),timebeg = str(time_now()))
            # totallist = totallist + '第{num}个任务是：\n任务序号：{taskNO}\n任务名称：{taskName}\n超市名称：{shopName}\n超市地址：{shopAddress}\n工作日期：{data}\n工作时间：{begin}  ———— {end}\n工作时长：{hours}小时\n工作单价：{price}元/小时\n\n'.format(
            #   num=str(j + 1), taskNO=str(list[j]['taskNo']), taskName=str(list[j]['taskName']),
            #   shopName=str(list[j]['shopName']), shopAddress=str(list[j]['shopAddress']),
            #   data=str(list[j]['workTime']['workDateStart']), begin=str(list[j]['workTime']['workStart']),
            #   end=str(list[j]['workTime']['workEnd']), hours=str(list[j]['workHour']),
            #   price=str(list[j]['taskPayPrice']))
            if (j+1) != total :
              mg = mg + "--------------------------------------------"
            else:
              mg = mg + "###########################################" + "\n"
            totallist = totallist + mg
            begintime = list[j]['workTime']['workStart']
            endtime = list[j]['workTime']['workEnd']
            if begintime == timebegin and endtime == timeend and taskName == Name:
              taskNO = list[j]['taskNo']
              print('taskNo:' + str(taskNO))
              print(list[j]['workTime']['dateList'])
              while 1:
                t = grab_order(token, taskNO)
                if t != 0 :
                  break
                else:
                  pass
              message = '已成功抢到第{num}个任务是：\n 时间：{time}\n'.format(num=str(j + 1),
                                                                time=str(list[j]['workTime']['workDateStart']))
              message = message + ' 时间：{begin}  ———— {end}\n\n'.format(begin=str(list[j]['workTime']['workStart']),
                                                                       end=str(list[j]['workTime']['workEnd']))
              
              postserver("已成功抢到小活儿任务",message)
              postserver("出现6：00-9：00小活儿任务",message)
              print("已成功抢到任务！请查看待执行任务")
              music_post()
              i = 0
          
          if totallist != plan:
            plan = totallist
            print( "\n" +str(time_now()) + str(messagecode) + ':出现{}个任务'.format(total))
            print(totallist)
            #print("#"*12)
            datas = datas + '\n' +str(time_now()) + str(messagecode) + ':出现{}个任务\n'.format(total) + str(totallist) + '\n' + "#"*12
            postserver(tittle,datas)
          else:
            print("\r\033[1;32m{time}：第{test}次刷新 {message} 目前出现{iter}个任务！请耐心等待...\033[0m".format(time=time_now(), test=i, message=messagecode, iter = total),end=" ")

    except Exception as result:
      pass
      #print('发生一个错误信息！')
    time.sleep(0.5)

def music_post():
  print('已抢到任务，正在播放歌曲稻香提醒...')
  clip = mp3play.load('test.mp3')
  clip.play()
  # 返回mp3文件共多少秒
  duration = clip.seconds()
  # 返回mp3文件共多少毫秒，注意这里的单位是毫秒
  duration = clip.milliseconds()
  time.sleep(duration)

if __name__ == '__main__':
    # res = login()
    # token = res.headers.get('x-http-token')
    token = input("请输入token：")
    print('token:' + str(token))
    print("抢单目标：" + str(timebegin) + "————" + str(timeend))
    main(token)


