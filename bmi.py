from tqdm import tqdm
from gtts import gTTS
import os
import time
weight_in_kg = float(input('enter weight in kg: '))
height_in_foot = int(input('enter foot: '))
height_in_inch = int(input('enter inch: '))
inch = height_in_foot * 12
height_in_inch = height_in_inch + inch
a = height_in_inch * 0.0254
bmi = weight_in_kg /(a*a)
for i in tqdm(range(100)):
    time.sleep(0.1)
print ('bmi is ',bmi)
mytext =f'bmi is {int(bmi)} sir ..'
language = 'en'
output = gTTS(text = mytext,lang = language)
output.save('bmi.mp3')
os.system('mpv /data/data/com.termux/files/home/bmi.mp3')
