import pyttsx3

import colorama

from colorama import Fore, Back, Style

# pip install tqdm
from tqdm import tqdm, trange
import time

# iterable based
for i in tqdm([1, 2, 3, 4, 5]):
    time.sleep(0.2)

print('done')

#  special optimised instance of tqdm(range(i))
for i in trange(10):
    time.sleep(0.1)

print('done')

# manual: use a with statement
# we can provide the optional 'total' parameter
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)

print('done')

# manual: assign to a variable
# dont forget to call close() at the end
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()

print('done')



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()





print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + "---------------------------------------------------tool creat by deadnet---------------------------------------------")
print(Back.LIGHTYELLOW_EX + "--------------------------------------------------creat for nayhtet birthday present--------------------------------")
print(Back.LIGHTGREEN_EX + "--------------------------------------------------coming soon foreverFA tool---------------------------------------")
print("-----------")
print(Back.LIGHTRED_EX)






if"_main_":
    speak(
        "happybirthday  parr nayhtet  .  mangalarpar Nayhtet ................... noght  kyat  ter  lo..sorry..parr .....deadnet  su  toung  pay   lite   parr   tel  . sul  mam  man  yat  parr  cee")

print(Fore.LIGHTWHITE_EX + 'end--wait--for--next--tool----coming soon')





