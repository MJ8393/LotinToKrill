#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:44:34 2023

@author: mekhriddinjumaev
"""

from transliterate import to_latin, to_cyrillic
import telebot


TOKEN = "6033223031:AAE9hwKdkL7aAYupD86Wgy-TUB76y_rIBew"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, xush kelibsiz!"
    answer += "\nMatn kiriting: "
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    txt = message.text
    answer = lambda txt: to_cyrillic(txt) if txt.isascii() else to_latin(txt)
    bot.reply_to(message, answer(txt)) 
    
bot.infinity_polling()
