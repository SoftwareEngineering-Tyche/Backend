# -*- coding: utf-8 -*-

import telebot
import time ,requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,InlineQueryResultVideo,ReplyKeyboardMarkup,KeyboardButton
import json
from tyche_mes import *
from tyche_data import * 
from datetime import datetime


# import logging
telegram_token = "5439654444:AAEb9a--mRU53bzexazgwtMJnzs3gWpKjUo"
bot=telebot.TeleBot(token=telegram_token)
users_data = Db()

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

def connct_site_inline():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("شروع اتصال حساب",url='https://www.bitycle.com/profile'))
    return markup

def NFT_inline(like=3,id=1,Externallink='google.com'):

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(f"{like}❤️",url=f'https://tyche.ludushub.io/product/{id}'))
    markup.add(InlineKeyboardButton("مشاهده در سایت",url=f'https://tyche.ludushub.io/product/{id}'))
    markup.add(InlineKeyboardButton("لینک اضافه",url=Externallink))

    return markup

def COLLEC_inline(id=1,Externallink='google.com'):

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("مشاهده در سایت",url=f'https://tyche.ludushub.io/collection/{id}'))
    markup.add(InlineKeyboardButton("لینک اضافه",url=Externallink))

    return markup


def search_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('جستجو کاربران🔎')
    itembtn2 = KeyboardButton('جستجو NFT🔎')
    itembtn3 = KeyboardButton('جستجو کالکشن ها🔎')
    itembtn4 = KeyboardButton('برگشت ↪️')

    markup.add(itembtn1, itembtn2,itembtn3,itembtn4)

    return markup
def explore_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('داغ ترین ها🔥')
    itembtn2 = KeyboardButton('جدیدترین ها📆')
    itembtn3 = KeyboardButton('محبوب ترین ها❤️')
    itembtn4 = KeyboardButton('برگشت ↪️')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4)
    return markup

def asset_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('NFT های من☄️')
    itembtn2 = KeyboardButton('کالکشن های من📁')
    itembtn3 = KeyboardButton('محبوب های من❤️')
    itembtn4 = KeyboardButton('برگشت ↪️')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4)
    return markup




def inline_help():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("آموزش اتصال به سایت", callback_data="connct_site"),
                               InlineKeyboardButton("آموزش دستورات", callback_data="commands"))
    return markup

    
def inline_contact():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("پشتیبانی تلگرام",url='https://t.me/bitycle_support'))
    markup.add(InlineKeyboardButton("چت آنلاین",url='https://www.goftino.com/c/MvRUA1'))
    return markup

def inline_not_login():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("ثبت نام",url='www.bitycle.com/signup'))
    return markup

def markup_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('جستجو🔎')
    itembtn2 = KeyboardButton('اکسپلور🎇')
    itembtn3 = KeyboardButton('محبوب های من❤️')
    itembtn3 = KeyboardButton('دارایی های من🗂')
    itembtn4 = KeyboardButton('راهنما🔖')
    itembtn5 = KeyboardButton('تایکی🛒')

    markup.add(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5)

    return markup

def can_use(id):
    return 1

def set_name(id):
    # name = requests.get(url=f"https://devapi.bitycle.com/api/account/brief_profile?telegram_id={id}")
    # if name.json()['status']=='success':
    #     name1 = name.json()["data"]["first_name"]
    #     code = name.json()["data"]["invite_code"]
    #     users_data.set(message.chat.id,'name',name1)
    #     users_data.set(message.chat.id,'invitecode',code)

    # else:
    #     print(',,,')
    users_data.set(id,'name',' کاربر عزیز')




def find_nft(search):
    try:
        # print(search.text)
        params={'search':search.text}
        
        name = requests.post(url=f"https://api.ludushub.io/search",data=params)
        # print('name',name.json())
        if name.json()['status']=='success':
            nfts=name.json()["data"]["NFTs"]
    except:
        bot.send_message(search.chat.id, 'hichiiii',reply_markup=inline_help())
    # print('hora',len(nfts))
    for nft in nfts:
        # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
        # print(nft)
        cap=NFTMES(nft['Name'],nft['Description'],nft['BlockChain'],nft['Price'])
        # print(cap)
        # cap='al'

        bot.send_photo(search.chat.id,'https://api.ludushub.io'+nft['image'],caption =cap,parse_mode="html",reply_markup=NFT_inline(nft['Liked'],nft['id'],nft['Externallink']))

        



def find_user(search):
    try:
        # print(search.text)
        params={'search':search.text}
        
        name = requests.post(url=f"https://api.ludushub.io/search",data=params)
        # print('name',name.json())
        if name.json()['status']=='success':
            nfts=name.json()["data"]["accounts"]
    except:
        bot.send_message(search.chat.id, 'hichiiii',reply_markup=inline_help())
    # print('hora',len(nfts))
    for nft in nfts:
        if nft['username']==None:
            nft['username']='.'
        if nft['bio']==None:
            nft['bio']='.'
        if nft['WalletInfo']==None:
            nft['WalletInfo']='.'
        if nft['email']==None:
            nft['email']='.'
        if nft['avatar']==None:
            nft['avatar']='google.com'

        # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
        # print(nft)
        cap=USERMES(nft['username'],nft['bio'],nft['WalletInfo'],nft['email'])
        print(cap)
        # cap='al'
        if nft['avatar'] !='google.com':
            bot.send_photo(search.chat.id,'https://api.ludushub.io'+nft['avatar'],caption =cap,parse_mode="html",reply_markup=NFT_inline())
        else:
            bot.send_message(search.chat.id, cap,reply_markup=inline_help())

        
def find_collec(search):
    try:
        # print(search.text)
        params={'search':search.text}
        
        name = requests.post(url=f"https://api.ludushub.io/search",data=params)
        # print('name',name.json())
        if name.json()['status']=='success':
            nfts=name.json()["data"]["collections"]
    except:
        bot.send_message(search.chat.id, 'hichiiii',reply_markup=inline_help())
    # print(nfts)
    # print('hora',len(nfts))
    if nfts:
        for nft in nfts:
            # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
            # print(nft)
            if nft['Name']==None:
                nft['Name']='.'
            if nft['Description']==None:
                nft['Description']='.'
            if nft['category']==None:
                nft['category']='.'
            if nft['id']==None:
                nft['id']='.'
            if nft['URL']==None:
                nft['URL']='google.com'

            cap=COLLEC(nft['Name'],nft['Description'],nft['category'])
            # print(cap)
            # cap='al'
            # print(nft['id'],nft['URL'])
            bot.send_photo(search.chat.id,'https://api.ludushub.io'+nft['logoimage'],caption =cap,parse_mode="html",reply_markup=COLLEC_inline(nft['id'],nft['URL']))

    else:
        bot.send_message(search.chat.id, 'چیزی پیدا نشد!',reply_markup=inline_help())



def get_wishlist(mes,wallet='0xbd5d8d49f91d538f83df097c597a851445eb29d9'):
    wallet=users_data.get(mes.chat.id,'wallet')
    name = requests.get(url=f"https://api.ludushub.io/Accountfavorites/{wallet}")
    # print(name.json())
    for nft in name.json():
        cap=NFTMES(nft['Name'],nft['Description'],nft['BlockChain'],nft['Price'])
        # print(cap)
        # cap='al'
        bot.send_photo(mes.chat.id,'https://api.ludushub.io'+nft['image'],caption =cap,parse_mode="html",reply_markup=NFT_inline(nft['Liked'],nft['id'],nft['Externallink']))

        # return nft['Name']
        
def explore(search):

    try:
        # print(search.text)
        params={'hotest':True,
                'favorites':True,
                'latest':True}
        
        name = requests.post(url=f"https://api.ludushub.io/explore",data=params)
        # print('name',name.json())
        if name.json()['status']=='success':
            nfts=name.json()["data"][search[1]]
    except:
        bot.send_message(search[0].chat.id, 'چیزی یافت نشد!',reply_markup=inline_help())
    # print(nfts[1])
    # print('hora',len(nfts))
    i=0
    if nfts:
        for nft in nfts[0]:
            i+=1
            # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
            # print(nft)
            if i>=11:
                break

            if nft['Name']==None:
                nft['Name']='.'
            if nft['Description']==None:
                nft['Description']='.'
            if nft['category']==None:
                nft['category']='.'
            if nft['id']==None:
                nft['id']='.'
            if nft['URL']==None:
                nft['URL']='google.com'

            cap=COLLEC(nft['Name'],nft['Description'],nft['category'])
            # print(cap)
            # cap='al'
            # print(nft['id'],nft['URL'])
            bot.send_photo(search[0].chat.id,'https://api.ludushub.io'+nft['logoimage'],caption =cap,parse_mode="html",reply_markup=COLLEC_inline(nft['id'],nft['URL']))

    else:
        bot.send_message(search[0].chat.id, 'چیزی پیدا نشد!',reply_markup=inline_help())

def my_nft(search):
    print('bbbb')
    wallet='0x22459b00b44e01fc5cc4361e1d78faae07c5cd9f'
    wallet=users_data.get(search.chat.id,'wallet')

    try:
        # print(search.text)
        params={'search':search.text}
        
        name = requests.get(url=f"https://api.ludushub.io/AccountWorkarts/{wallet}")
        print(name)
        nfts=name.json()
        print('name',name.json())

    except:
        bot.send_message(search.chat.id, 'چیزی یافت نشد',reply_markup=inline_help())
    
    # print('hora',len(nfts))
    if not nfts:
        bot.send_message(search.chat.id, 'چیزی یافت نشد',reply_markup=inline_help())
    for nft in nfts:
        # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
        # print(nft)
        cap=NFTMES(nft['Name'],nft['Description'],nft['BlockChain'],nft['Price'])
        # print(cap)
        # cap='al'

        bot.send_photo(search.chat.id,'https://api.ludushub.io'+nft['image'],caption =cap,parse_mode="html",reply_markup=NFT_inline(nft['Liked'],nft['id'],nft['Externallink']))

        


def my_collec(search):
    wallet='0x22459b00b44e01fc5cc4361e1d78faae07c5cd9f'
    wallet=users_data.get(search.chat.id,'wallet')
    try:

        name = requests.get(url=f"https://api.ludushub.io/Accountcollection/{wallet}")
        nfts=name.json()
        print('name',name.json())
    except:
        bot.send_message(search.chat.id, 'چیزی یافت نشد!',reply_markup=inline_help())
    # print(nfts[1])
    # print('hora',len(nfts))
    i=0
    if nfts:
        for nft in nfts:
            i+=1
            # bot.send_message(search.chat.id, NFTMES(),reply_markup=inline_help())
            # print(nft)
            if i>=11:
                break

            if nft['Name']==None:
                nft['Name']='.'
            if nft['Description']==None:
                nft['Description']='.'
            if nft['category']==None:
                nft['category']='.'
            if nft['id']==None:
                nft['id']='.'
            if nft['URL']==None:
                nft['URL']='google.com'

            cap=COLLEC(nft['Name'],nft['Description'],nft['category'])
            # print(cap)
            # cap='al'
            # print(nft['id'],nft['URL'])
            bot.send_photo(search.chat.id,'https://api.ludushub.io'+nft['logoimage'],caption =cap,parse_mode="html",reply_markup=COLLEC_inline(nft['id'],nft['URL']))

    else:
        bot.send_message(search.chat.id, 'چیزی پیدا نشد!',reply_markup=inline_help())


@bot.message_handler(func=lambda message: True)
def send_welcomes(message):

    # try:
    #     pass
    #     # bot.send_message(message.chat.id, users_data.get(message.chat.id,'wallet'),reply_markup=markup_menu())
    # except:
    #     pass



            
    # print('market',market,'res',res)

    if  not can_use(message.chat.id):
        bot.send_message(message.chat.id, MUST_SIGNUP(message.from_user.username),reply_markup=inline_not_login())
    elif 'start' in message.text:
        # print('////////')
        set_name(message.chat.id)
        # print(users_data.get(message.chat.id,'name'))
        bot.send_message(message.chat.id, WELLCOME(users_data.get(message.chat.id,'name')),reply_markup=markup_menu())
        users_data.set(message.chat.id,'username',message.from_user.username)
        # print(message.text)
        print(message.text.split('start'))
        print(message.text.split('start')[1])
        wal=message.text.split('start')[1][1:]
        print(wal)
        users_data.set(message.chat.id,'wallet',str(wal))





    elif 'راهنما' in message.text or 'help' in message.text:
        print(users_data.get(message.chat.id,'wallet'))
        bot.send_message(message.chat.id, users_data.get(message.chat.id,'wallet'),reply_markup=inline_help())
        bot.send_message(message.chat.id, HELP(users_data.get(message.chat.id,'name')),reply_markup=inline_help())









    elif 'ارتباط باما' in message.text:
        bot.send_message(message.chat.id, CONTACTUS(users_data.get(message.chat.id,'name')),reply_markup=inline_contact())




    elif 'تایکی' in message.text:
        bot.send_message(message.chat.id, 'اولین و بزرگ‌ترین پلتفرم ایرانی در حوزه توکن‌های غیر قابل تعویض (NFT) برای جمع‌آوری، خرید، فروش و جستجو در اقلام دیجیتال منحصر به فرد\n\n\n\n\n\n\n🌐tyche.ludushub.io')




    elif  'برگشت' in message.text:
        bot.send_message(message.chat.id, BACK(users_data.get(message.chat.id,'name')),reply_markup=markup_menu())




    elif 'جستجو🔎' == message.text:
        bot.send_message(message.chat.id, 'دسته مورد نظر خودرا انتخاب نمایید',reply_markup=search_menu())
        
    elif 'جستجو NFT🔎' == message.text:
        sent=bot.send_message(message.chat.id, 'کلمه مورد نظر خودرا وارد نمایید',reply_markup=search_menu())
        bot.register_next_step_handler(sent,find_nft)

    elif 'جستجو کاربران🔎' == message.text:
        sent=bot.send_message(message.chat.id, 'کلمه مورد نظر خودرا وارد نمایید',reply_markup=search_menu())
        bot.register_next_step_handler(sent,find_user)

    elif 'دارایی های من' in message.text:
        sent=bot.send_message(message.chat.id, 'گزینه مورد نظر خودرا انتخاب نمایید',reply_markup=asset_menu())

        

    elif 'جستجو کالکشن ها🔎' == message.text:
        sent=bot.send_message(message.chat.id, 'کلمه مورد نظر خودرا وارد نمایید',reply_markup=search_menu())
        bot.register_next_step_handler(sent,find_collec)

    elif  'محبوب های من' in message.text:
        get_wishlist(message)

    elif 'اکسپلور' in message.text:
        sent=bot.send_message(message.chat.id, 'دسته مورد نظر خودرا انتخاب نمایید',reply_markup=explore_menu())

    elif 'داغ' in message.text:
        explore((message,'hotest'))
    
    elif 'جدیدترین' in message.text:
        explore((message,'latest'))

    elif 'محبوب ترین' in message.text:
        explore((message,'favorites'))

    elif 'NFT های من' in message.text:
        my_nft(message)

    elif 'کالکشن های من' in message.text:
        my_collec(message)




@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print(call.data__dict__)
    # print(call.id)
    if call.data == "connct_site":
        # bot.answer_callback_query(call.id, "بیا یادت بدم")
        bot.send_message(call.from_user.id, 'از داخل پروفایل خود روی دکمه اتصال به تلگرام کلیک نمایید و سپس داخل تلگرام ربات را استارت کنید\n\n\n tyche.ludushub.io/profile',parse_mode="html",disable_web_page_preview=True)

        # image = bot.send_photo(call.from_user.id,open('./help_connect.png', 'rb') , caption =CONNECTSITE(users_data.get(call.from_user.id,'name')),reply_markup=connct_site_inline())
        # video = bot.send_video(call.from_user.id,open('./test.mp4', 'rb') , caption =CONNECTSITE(users_data.get(call.from_user.id,'name')),reply_to_message_id = call.message.id,reply_markup=connct_site_inline())
        # video = bot.send_video(call.from_user.id,open('./test.mp4', 'rb') , caption =CONNECTSITE(users_data.get(call.from_user.id,'name')),reply_markup=connct_site_inline())
        # bot.send_photo(call.from_user.id,image.json['photo'][0]['file_id'], caption ='file id photo',reply_markup=connct_site_inline())
        # bot.send_video(call.from_user.id,video.json["video"]["file_id"], caption ='file id video',reply_markup=connct_site_inline())
    
    
    elif call.data == "commands":
        bot.send_message(call.from_user.id, 'دستورات خیلی واضح هستند',parse_mode="html",disable_web_page_preview=True)
        # bot.answer_callback_query(call.id, "بیا یادت بدم")
        # bot.send_message(call.from_user.id, COMMANDS(users_data.get(call.from_user.id,'name'),call.from_user.id),parse_mode="html",disable_web_page_preview=True)
        # bot.send_document(call.from_user.id,open('./test.xlsx', 'rb'),caption =COMMANDS(users_data.get(call.from_user.id,'name'),call.from_user.id),parse_mode="html",visible_file_name=f'{call.from_user.username}.xlsx',disable_notification = True)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
















