# Danke_Schoen
A very very annoying assistant

## Inspiration
All the virtual assistants are so nice to us. They respond to our queries, do what we tell them to do and don't disturb us unless necessary. We wanted an assistant that would constantly try to disturb us, lure us into stopping our work and chill for a while. The logic behind this was to create something so annoying that we'll need to use our full concentration to work. We personally found that we work better and are less likely to procrastinate when someone (or something) is disturbing us.

## What it does (or rather, what it doesn't do)
It won't respond to your voice command. Everything is random with this assistant. It will hit you up when you least expect it. It will play dialogues from your favorite sitcoms, open crazy (but also extremely fun) websites and games. It will tell you the time (it might not be from your timezone though). It'll tell you named of asteroids that orbit earth, it'll write poetry, raps and quotes for you. It'll blast you with random movie and pokemon facts. It'll pick a card for you from a deck of 52 cards. It'll say motivation things to you from time to time. It'll give you a randomly generated number. It'll call you different names. It'll tell you how many people are there in space and it'll give you random search results for random queries. It'll move your files from one folder to other constantly to keep you from working.
Tl;dr: It will serve no useful purpose of you whatsoever.

## How we built it
We used *14* APIs in total for this project. The file transferring part is handles by *UI Path*. The entire code is written in python. For the rap, poems and quotes, we used [ponicode_rapper](https://github.com/Legedith/rap_battle) and trained it on poems and quotes respectively. The APIs and where they were used are listed below:
 
1. Asterank api to get information about asteroids
2. Pokeapi to get information on various pokemons
3. Playsound api for playing audio using python
4. Bechdeltest api to get information on movies
5. Webbrowser api to handle websites
6. Deckofcards api to get a random card
7. Foass api for motivation
8. Quantum random number generator api to get a random number
9. Randon user name generator api to generate a random name
10. Tkinter api to display raps, poems and quotes
11. Google text-to-speech api to give voice output for texts
12. Requests api to handle all the http requests using python
13. Open-notify api to get info on people in space
14. DuckDuckGo api for search results
 
## Challenges we ran into
This was our first time using UI Path so it was a little difficult to understand the workflow. Also when had never integrated so many APIs into a single application so that was fun.

## Accomplishments that we're proud of
We successfully created the most annoying and useless assistant ever to exist.

## What we learned
We learnt how to handle api request, use UI Path and handle audio using python.

## What's next for Danke_Schoen
Adding more features that can make it more annoying.
