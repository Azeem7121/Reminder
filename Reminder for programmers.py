""" Reminder For Programmers
assuming job hrs 9am-5pm ie: 8 hrs approx
1-Drink water reminder (play water.mp3 every 40min, display message drink 3.5l water a day, make log of water drank )
2-Eyes exercise reminder (play eyes.mp3 every 40min, display message do eyes exercise for 1 min, make log done)
3-Physical Activity reminder (play physical.mp3 every 90min,display message do physical activity for 5min,make log done)
4-Use pygame module to play mp3 """
from pygame import mixer
from time import time
from datetime import datetime


def playmusic(file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=30)  # music in playing in loop for 30 time
    while True:
        user = input("To stop reminder type [Done]: ").title()
        if user == stop:
            mixer.music.stop()
            break


def log(text):
    with open("log.txt", "a") as L:
        L.write(f"{text} |{datetime.now()}\n")


def water_reminder():
    global water
    if time() - water > water_time:
        print("Drink water! Approx 250ml or more")
        playmusic("water.mp3", "Done")
        water = time()
        log("Drank Water At ")


def eyes_reminder():
    global eyes
    if time() - eyes > eyes_time:
        print("Do eyes exercise! For 1 minute")
        playmusic("eyes.mp3", "Done")
        eyes = time()
        log("Eyes Exercise Done At ")


def activity_reminder():
    global activity
    if time() - activity > activity_time:
        print("Do Physical Activity! For 5 minutes")
        playmusic("physical.mp3", "Done")
        activity = time()
        log("Physical Activity Done At ")


if __name__ == '__main__':
    water = time()
    eyes = time()
    activity = time()
    water_time = 2400  # you change reminder time for Water here in secs
    eyes_time = 2405  # you change reminder time for eyes exercise here in secs
    activity_time = 5400  # you change reminder time for physical activity here in secs
    print("")
    print("""Caution: As you sit and continuously stair your computer screen "IT DOES IMPACT OUR HEALTH"
     So here is the solution for, You will be remind :
     1-Every 40min for drinking water to complete daily water limits of human ie; (3.5 liter of water)
     2-Every 40min for Eyes exercise to relax your eyes at least for 1 minute
     3-Every 90min for Physical activity to relife body stress at least for 5 minute
     BE HEALTHY! LIVE YOUNG AND ACTIVE
     """)
    print("To Start press: [S]")
    user_input = input(":").upper()
    while True:
        water_reminder()
        eyes_reminder()
        activity_reminder()
