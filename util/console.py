# ========== Info ===========
"""
Made by Haven Selph - <havenselph@gmail.com>
Class make is specifically there to allow you to reference easy to use unicode. Use {self}.make.{form} to ref the class.
Out is made so console prints look well formatted and more readable.
"""
# ========= Imports =========
from datetime import datetime

# ========= Defined =========

class make:
  header = '\033[95m'
  okb = '\033[94m'
  okg = '\033[92m'
  warn = '\033[93m'
  fail = '\033[91m'
  endc = '\033[0m'
  bold = '\033[1m'
  underline = '\033[4m'
  lib = ['header','okb','okg','warn','fail','bold','underline']

def out(text, user='Console'):
  time = datetime.now()
  print(f'{make.okg}{make.bold}{user}{make.endc} {make.okg}[{time.month}/{time.day}/{time.year}] [Time: {time.hour}:{time.minute}:{time.second}]{make.endc} {make.okb}>>{make.endc} \n{text}\n')

def err(text, err='Undefined'):
  print(f'{make.fail}Error reached!\n{err} : {text}')
