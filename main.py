import telepot
import sys
import time
import random
import os
import key
import com
import re
import pathlib
import dao
from pprint import pprint
from PIL import Image
from io import BytesIO

reload(sys)
sys.setdefaultencoding('utf-8')
bot = telepot.Bot(key.BOT_KEY)  # token

timeout = {}

tranquiloviejo = u"CAADAQADNwADzxSlAAEpVbCJbOTMsAI"
awanta = u'CAADAQADqwADJaHuBMhw3ty2zbpjAg'
dejesedemamadas = u'CAADAQAD7wEAAs8UpQABdurS64LRGooC'
alapifu = u"CAADAQADkQADJaHuBAABSnzPxbzjJQI"
ticketHell = u'CAADAQADnQADJaHuBGvY1E43XYjJAg'
ticketHeaven = u'CAADAQADswADJaHuBEcjnhhUIqsPAg'
terco = u'CAADAQADqgADJaHuBEK37px2YeW-Ag'

amivalevrgtmb = u'CAADAQADtAADJaHuBJdeO7iayOyQAg'
amivalevrg = u'CAADAQADiAADJaHuBD7kz0JCJne4Ag'
atodosvalevrg = u'CAADAQADigADJaHuBEbW2qfTwX5XAg'
uypuesperdon = u'CAADAQADogADJaHuBLFm_SWQWCPDAg'
foca_gaaay = u'CAADBAADcAQAApv7sgABifFfdnNmjjsC'


kheberga = u'CAADAQADiwADJaHuBCxFUkncLVKjAg'

iscoraline = r"\s?c(a|o)r(a|o)line\s?"
ensalada = r"\s?ensalada\s?"
isgay = r"\s?(gay|maricon|p?inche puto)\s?"
isgod = r"\b((\s+dios|god)\b|\b(dios|god)\b)\s?"
isnigga = r"\s?(negro|niga|nigga|nigger)\s?.*"
trabajaperro = r"\s?trabaja,? perro.*"

mcdinero_gif = u'CgADAQADAQADLm_4TFkwvxivN4ncAg'
hagaaay_gif = u'CgADAwADAQADhjxQTo1Kz-gOAQ_jAg'
ikillu_gif = u'CgADBAADFaAAAloXZAe9o2B4i9CciwI'
racists_gif = u'CgADBAADwKMAAlEXZAcPm6zqHWX1DAI'
trabajaperro_gif = u'CgADBAADeRcAAsUdZAefc7VUnBenbwI'
maradona_gif = u'CgADBAAD758AAvgaZAfNzwLnrluCJAI'


def handle(msg):
    pprint(msg)

def getUserSender(msg):
    if 'username' in msg['from']:
        return msg['from']['username']
    else:
        return msg['from'][u'first_name']


def isBot(msg):
    return 'from' in msg and 'is_bot' in msg['from'] and msg['from']['is_bot']

def reply(msg, response):
    chat_id = msg['chat']['id']
    msgId = msg['message_id']
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msgId )


def replyDocument(msg, docid):
    chat_id = msg['chat']['id']
    msgId = msg['message_id']
    bot.sendDocument(chat_id=chat_id, document=docid, reply_to_message_id=msgId)


def responseDocument(msg, docid, caption=None):
    chat_id = msg['chat']['id']
    bot.sendDocument(chat_id=chat_id, document=docid, caption=caption)


def responseImage(msg, photo, caption=None):
    chat_id = msg['chat']['id']
    photo = pathlib.Path(photo)
    
    im = Image.open(photo)
    im.thumbnail((220, 130), Image.ANTIALIAS)
    im.save(im.filename)

    
    bot.sendPhoto(chat_id=chat_id, photo=im, caption=caption)

def replySticker(msg, sticker):
    chat_id = msg['chat']['id']
    msgId = msg['message_id']
    bot.sendSticker(chat_id=chat_id, sticker=sticker, reply_to_message_id=msgId)

def getAwnser(type):
    return dao.GetAnswer(type)


def newRecord(sender):
    timeout[sender] = {"time": time.time(), "count": 0}

def wait(msg, type):
    sender = getUserSender(msg)
    chat_id = msg['chat']['id']
    user_id = msg["from"]['id']

    reply(msg, "a quien le damos ese?")
    newRecord(sender)

    com.Wait(chat_id, user_id, type)

def validTimeout(msg, sender):
    if not sender in timeout:
        return True

    elapsed = int(time.time()-timeout[sender]["time"])

    if elapsed <= 30:
        timeout[sender]["count"]+=1

        if timeout[sender]["count"] == 1:
            replySticker(msg, tranquiloviejo)
        elif timeout[sender]["count"] == 5:
            replySticker(msg, awanta)
        elif timeout[sender]["count"] == 10:
            replySticker(msg, dejesedemamadas)
        elif timeout[sender]["count"] == 20:
            replySticker(msg, alapifu)
        elif timeout[sender]["count"] == 25:
            replySticker(msg, dejesedemamadas)
        elif timeout[sender]["count"] == 30:
            replySticker(msg, terco)
        else:
            reply(msg, "esperate {} segundos".format(30-elapsed))

        return False

    return True


def checkSpecialWords(msg):    
    if re.search(iscoraline, msg['text'], re.I | re.M) is not None:
        reply(msg, "si seras, si seras, que se llama Karelia, che terco!")
    elif re.search(isgay, msg['text'], re.I | re.M) is not None:
        responseDocument(msg, hagaaay_gif)
    elif re.search(isgod, msg['text'], re.I | re.M) is not None:
        responseDocument(msg, ikillu_gif)
    elif re.search(isnigga, msg['text'], re.I | re.M) is not None:
        responseDocument(msg, racists_gif)
    elif re.search(trabajaperro, msg['text'], re.I | re.M) is not None:
        responseDocument(msg, trabajaperro_gif)
    elif re.search(ensalada, msg['text'], re.I | re.M) is not None:
        responseDocument(msg, maradona_gif, "ensalada?... noooooo!")

def on_chat_message(msg):
    # responseImage(msg, "images/jesus1.jpg")
    # return 
    # if not has text or sticker
    if isBot(msg) or (not 'text' in msg and not 'sticker' in msg):
        return

    cmd = ''
    user = ''
    userSender = getUserSender(msg)

    ignoreTimeout = False
    chat_id = msg['chat']['id']
    user_id = msg["from"]['id']

    """  if chat_id in ticketWait and ticketWait[chat_id] != user_id:
        reply(msg, "a ti no te pregunte, metiche!")
        return """
    if com.IsWaiting(chat_id, user_id) and 'text' in msg:
        user = msg['text'].split(' ')[0].replace('@', '')

        if user.startswith("/cancel"):
            com.cancel("", "", chat_id)
            replySticker(msg, kheberga)
            return 
        ignoreTimeout = True
        cmd = com.GetWaitingCmd(chat_id, user_id)
        com.cancel("", "", chat_id)
    elif 'text' in msg:
        cmds = msg['text'].split(' ')
        response = ''
        if len(cmds) >= 2:
            cmd = cmds[0]
            user = cmds[1].replace('@', '')        
        elif len(cmds) == 1:
            cmd = cmds[0]
    elif 'sticker' in msg and msg['sticker']['file_id']==ticketHell:
        if not validTimeout(msg, userSender):
            return        
        wait(msg, dao.HELL)
        return
    elif 'sticker' in msg and msg['sticker']['file_id'] == ticketHeaven:
        if not validTimeout(msg, userSender):
            return
        wait(msg, dao.HEAVEN)
        return
    elif 'sticker' in msg and msg['sticker']['file_id'] == amivalevrg:
        replySticker(msg, amivalevrgtmb)
        return
    elif 'sticker' in msg and msg['sticker']['file_id'] == foca_gaaay:
        responseDocument(msg, hagaaay_gif)
        return

    if not cmd.startswith('/') and not 'sticker' in msg:
        checkSpecialWords(msg)
        return

    # acept commands type /command@HellOrHeavenBot
    cmd = cmd.replace('@HellOrHeavenBot', '')

    if not cmd in com.COMMANDS:
        cmd = com.VerifyAlias(cmd)
        if cmd == "":
            return

    # flag to validate or not the timeout
    if not ignoreTimeout:
        ignoreTimeout = not com.COMMANDS[cmd][com.WAIT]

    if not ignoreTimeout and not validTimeout(msg, userSender):
        return

    if user.upper() == 'HELLORHEAVENBOT':
        reply(msg, 'si tu, voy corriendo!')
        return 

    if user.upper() == userSender.upper():
        reply(msg, u'solo dios puede juzgarte... nah!, los demas lo haran \U0001f602')
        return
    
   
    response = com.COMMANDS[cmd][com.FUNC](user, userSender, chat_id)
    
    answer = response["r"]["a"]
    needWait = "needWait" in response and response["needWait"]
    answerype = response["r"]["at"]

    if answerype == com.Answerype.STICKER:
        replySticker(msg, answer)
    elif answerype == com.Answerype.GIF:
        replyDocument(msg, answer)
    elif answerype == com.Answerype.PHOTO:
        responseImage(msg, answer)
    else:  # answerype == com.Answerype.TEXT:
        reply(msg, answer)

    if needWait:
        newRecord(userSender)
        

bot.message_loop({'chat': on_chat_message})

print('Listening ...')

while 1:
    time.sleep(10000)
