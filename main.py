# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from playsound import playsound
import random
import time
import webbrowser
import os
from ponicode_rapper import Rapper
import nltk
import tkinter as tk
from gtts import gTTS
import requests

def mp3_function(mp3_):
    tts.save(mp3_)
    playsound(mp3_)
    os.remove(mp3_)


random.seed(1)
sites = ["https://findtheinvisiblecow.com/","http://www.fallingfalling.com/","http://ihasabucket.com/","http://tacospin.com/","https://thatsthefinger.com/","http://corndog.io/","http://www.staggeringbeauty.com/","https://hooooooooo.com/","http://endless.horse/","http://ninjaflex.com/","https://finger-frenzy.now.sh/","https://cat-bounce.com/","http://onemillionlols.com/","https://pointerpointer.com/","https://turbo.fish/","http://www.ismycomputeron.com/","http://iamawesome.com/","http://yeahlemons.com/","http://www.rrrgggbbb.com/","https://chrismckenzie.com/","https://www.adultswim.com/etcetera/elastic-man/"]

games = ["https://www.google.com/logos/2010/pacman10-i.html","https://supermarioemulator.com/mario.php","https://www.miniclip.com/games/bubble-trouble/en/","https://archive.org/details/msdos_Prince_of_Persia_1990"]

Rap = Rapper()
load_path = 'model/Rapper.pkl'
Rap.load_model(load_path)

Poet = Rapper()
load_path = 'model/Harry_styles.pkl'
Poet.load_model(load_path)

Quote = Rapper()
load_path = 'model/quotes_500.pkl'
Quote.load_model(load_path)

options = ["game","website","time","asteroid","written","movie","pokemon","cards","motivate","random","user","space","duck"]

# print(Rap.generate_artistic_verses(NVERSES))
# print(Poet.generate_artistic_verses(NVERSES))
# print(Quote.generate_artistic_verses(NVERSES))


root = tk.Tk()
# T = tk.Text(root, height=30, width=50)
# T.pack()

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'
path='sounds/'
dialogues = [i for i in os.listdir(path) if 'wav' in i]
time.sleep(15)

while True:
    track = random.choice(dialogues)
    playsound(track)
    print(track)
    sleep_time = random.randint(5,15)
    time.sleep(sleep_time)    

    opt = random.choice(options)
    
    if opt == "game":
        # continue
        url = random.choice(games)
        webbrowser.get(chrome_path).open(url)
        print(url)
        time.sleep(15)
        
    elif opt == "written":
        T = tk.Text(root, height=30, width=80)
        T.pack()
        models = [Rap,Poet,Quote]
        model = random.choice(models)
        quote = model.generate_artistic_verses(2)
        T.insert(tk.END, quote)
        tk.mainloop()

    elif opt == "time":
        continue
        t = time.strftime('%X %x')
        tts = gTTS(text="The time is 12:30 PM. It's definately not "+t, lang='en')
        mp3_function("time.mp3")

    elif opt == "website":
        continue
        url = random.choice(sites)
        webbrowser.get(chrome_path).open(random.choice(sites))
        print(url)
        time.sleep(15)
        
    elif opt == 'asteroid':
        r = requests.get("http://www.asterank.com/api/asterank?query={%22e%22:{%22$lt%22:0.1},%22i%22:{%22$lt%22:4},%22a%22:{%22$lt%22:1.5}}&limit=10"
)
        a = r.json()
        tts = gTTS(text="There's an asteroid somewhere in space. It's name is "+a[random.randint(0, 9)]["full_name"], lang='en')
        mp3_function("asteroid.mp3")
    
    elif opt == 'movie':
        r = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=matrix")
        a = r.json()
        n = random.randint(0,2)
        tts = gTTS(text="The movie "+a[n]["title"]+" was released in year "+str(a[n]["year"])+" probably.", lang='en')
        mp3_function("movie.mp3")
        
    elif opt == 'pokemon':
        pokemons = ["charmander","bulbasaur","palkia","heatran"]
        pokemon = random.choice(pokemons)
        r = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        a = r.json()
        tts = gTTS(text=""+a["name"]+"'s height is "+str(a["height"])+" feet. And maybe he can breathe fire. ", lang='en')
        mp3_function("pokemon.mp3")
        
    elif opt == "cards":
        r = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=1")
        a = r.json()    
        tts = gTTS(text="Your card is "+a['cards'][0]['value']+" of "+a['cards'][0]['suit']+". I know you didn't ask but you know, just in case.", lang='en')
        mp3_function("card.mp3")

    elif opt == "motivate":
        h = {'accept':'application/json'}
        r = requests.get("https://www.foaas.com/bm/kiddo/future",headers = h)
        r = r.json()
        tts = gTTS(text=""+r["message"], lang='en')
        mp3_function("motivate.mp3")
     
    elif opt == "random":
        r = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8")
        r = r.json()
        tts = gTTS(text="Your random number generated using  quantum stuff is "+str(r["data"]), lang='en')
        mp3_function("number.mp3")

     
    elif opt == "user":
        r = requests.get("https://randomuser.me/api/")
        r = r.json()
        tts = gTTS(text="From now on, I'll call you "+r['results'][0]['name']["first"]+" "+r['results'][0]['name']["last"], lang='en')
        mp3_function("name.mp3")
        
    elif opt == "space":
        r = requests.get("http://api.open-notify.org/astros.json")
        r = r.json()
        tts = gTTS(text="The number of people currently in space is "+str(r['number']), lang='en')
        mp3_function("space.mp3")
        
    elif opt == "duck":
        r = requests.get("https://api.duckduckgo.com/?q=PlayDate&format=json")
        r = r.json()        
        tts = gTTS(text=""+r["AbstractText"], lang='en')
        mp3_function("abs.mp3")
        
