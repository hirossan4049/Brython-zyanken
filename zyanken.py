import random
# from browser import document, ajax, bind
import browser
# https://www.sozai-library.com/policy


zyanken_path = {
    "ぐー":"static/images/guu.png",
    "ちょき":"static/images/tyoki.png",
    "ぱー":"static/images/paa.png",
    }
zyanken_core = {
    "ぐー":"ちょき",
    "ちょき":"ぱー",
    "ぱー":"ぐー",
    }
zyanken_list = ["ぐー","ちょき","ぱー"]
cpu_image = browser.document["cpu_img"]
user_image = browser.document["user_img"]

user_select = None
cpu_select  = None

# @browser.bind("#guu_inpt","click")
def on_press_guu(ev):
    global user_select
    user_select = "ぐー"
    user_image.src = zyanken_path[user_select]
    zyanken()
#
# @browser.bind("#tyoki_inpt","click")
def on_press_tyoki(ev):
    global user_select
    user_select = "ちょき"
    user_image.src = "static/images/tyoki.png"
    zyanken()

#
# @browser.bind("#paa_inpt","click")
def on_press_paa(ev):
    global user_select
    user_select = "ぱー"
    user_image.src = "static/images/paa.png"
    zyanken()


def zyanken():
    # Get the result
    result = random.choice(zyanken_list)
    cpu_image.src = zyanken_path[result]
    # Output
    browser.document["result"].text = "CPU:{}".format(result)
    browser.document["user_result"].text = "User:{}".format(user_select)

    res_comment = ""
    user_lose = zyanken_core[result]
    if not user_select:
        res_comment = "選択しろカス"
    elif result == user_select:
        res_comment = "あいこ"
    elif user_lose == user_select:
        res_comment = "負け"
    else:
        res_comment = "勝ち"

    browser.document["zyanken_result"].text = "結果:" + res_comment



# sub_elt = browser.document["submit_button"]
# sub_elt.bind("click", zyanken)
browser.document["guu_inpt"].bind("click",on_press_guu)
browser.document["tyoki_inpt"].bind("click",on_press_tyoki)
browser.document["paa_inpt"].bind("click",on_press_paa)