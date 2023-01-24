from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


# def get_weather():
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   return weather['weather'], math.floor(weather['temp'])

# def get_count():
#   delta = today - datetime.strptime(start_date, "%Y-%m-%d")
#   return delta.days

# def get_birthday():
#   next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#   if next < datetime.now():
#     next = next.replace(year=next.year + 1)
#   return (next - today).days

# def get_words():
#   words = requests.get("https://api.shadiao.pro/chp")
#   if words.status_code != 200:
#     return get_words()
#   return words.json()['data']['text']

# def get_random_color():
#   return "#%06x" % random.randint(0, 0xFFFFFF)


# client = WeChatClient(app_id, app_secret)

# wm = WeChatMessage(client)
# wea, temperature = get_weather()
# data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
# res = wm.send_template(user_id, template_id, data)
# print(res)

def get_weather():
    url = "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + "周口"
    res = requests.get(url).json()
    wet = res['data'][0]
    return wet['tem'], wet['tem1'], wet['tem2'], wet['phrase'], wet['humidity']
    # return weather['weather'], math.floor(weather['temp'])

def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
# cur max min
cur, maxs, mins, weather, humidity = get_weather()
data = {"weather": {"value": weather, "color": get_random_color()},
        "cur": {"value": cur, "color": get_random_color()},
        "humidity": {"value": humidity, "color": get_random_color()},
        "maxs": {"value": maxs, "color": get_random_color()},
        "mins": {"value": mins, "color": get_random_color()},
        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "words": {"value": get_words(), "color": get_random_color()}
        }
# data = {"weather": {"value": weather},
#         "cur": {"value": cur},
#         "humidity": {"value": humidity},
#         "maxs": {"value": maxs},
#         "mins": {"value": mins},
#         "love_days": {"value": get_count()},
#         "birthday_left": {"value": get_birthday()},
#         "words": {"value": get_words(), "color": get_random_color()}
#         }
res = wm.send_template(user_id, template_id, data)
print(res)

