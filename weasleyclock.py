#!/usr/bin/env python
 
# @Author: Nikki Agrawal
# @Email: nikki.ag@gmail.com
# @Date: Nov 11, 2016
#
# Installation:
# Create a server either in home or on Amazon AWS. Create a small Ubuntu instance
# and install mosquitto server which will get the packets from Owntracks
#     sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
#     sudo apt-get update
#     sudo apt-get install mosquitto-dev
# This is install the mosquitto server and start it
#
# please execute 'sudo pip install paho-mqtt'
# to run 'python Project.py'
 
import paho.mqtt.client as mqtt
import json
import math
import mtTkinter as Tkinter
import tkFont
import time
 
EARTH_RADIUS = 6378.1  # kilometers
NUM_LOCATIONS = 3
NUM_FIELDS = 4
NUM_PEOPLE = 3
 
# These are the 3 locations used on the graph.
loc_array = [["home", 37.279564, -121.860081, 1.2], ["nikkiSchool", 37.255628, -121.910108, 2.1], ["piaSchool", 37.240450, -121.926447, 2.1]]
 
# Coordinates for Nikki on the clock
msg1Loc = "Unknown1"
msg1Text = "Nikki"
msg1XCord = 500
msg1YCord = 500
 
# Coordinates for Papa on the clock
msg2Loc = "Unknown2"
msg2Text = "Papa"
msg2XCord = 500
msg2YCord = 550
 
# Coordinates for Pia on the clock
msg3Loc = "Unknown3"
msg3Text = "Pia"
msg3XCord = 500
msg3YCord = 600
 
class newClock():
    global msg1Loc
    global msg1Text
    global msg1XCord
    global msg1YCord
    global msg2Loc
    global msg2Text
    global msg2XCord
    global msg2YCord
    global msg3Loc
    global msg3Text
    global msg3XCord
    global msg3YCord
 
    def __init__(self):
        ''' Constructor. '''
        self.tk = Tkinter.Tk()
        self.tk.wm_title("Navigational Family clock of Doom")
        self.canvas = Tkinter.Canvas(self.tk, width=800, height=800, borderwidth=0, highlightthickness=0, bg="black")
        self.canvas.grid()
        self.canvas.create_circle = self._create_circle
        self.canvas.create_circle_arc = self._create_circle_arc
        self.tk.after(100, self.run)
        self.tk.mainloop()
 
    def _create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)
 
    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.canvas.create_arc(x - r, y - r, x + r, y + r, **kwargs)
 
    def run(self):
        """ makes the clock"""
        xCord = 400
        yCord = 400
        radius = 350
 
        # the basic cicrle is green. Then you add 3 arcs for the 3 other quadrants
        # making total of 4 quadrants.
        # Nikki school is light green
        # Pia school is light pink
        # Home is light blue
        # Unknown is red
 
        self.canvas.create_circle(xCord, yCord, radius, fill="light green", outline="#DDD", width=4)
        self.canvas.create_circle_arc(xCord, yCord, radius, fill="light blue", outline="", start=90, end=180)
        self.canvas.create_circle_arc(xCord, yCord, radius, fill="light pink", outline="", start=180, end=270)
        self.canvas.create_circle_arc(xCord, yCord , radius , fill = "red" , outline="", start=270,end=360)
 
        # These are the 4 texts for the 4 names of the quadrants
        text1XCord = xCord - 150
        text1YCord = yCord - 25
        self.canvas.create_text(text1XCord, text1YCord, anchor="w", font=("Purisa", 15, "bold italic"),   text="Home")
 
        text2XCord = xCord + 50
        text2YCard = yCord - 25
        self.canvas.create_text(text2XCord, text2YCard, anchor="w", font=("Purisa", 15, "bold italic"),   text="NikkiSchool")
 
        text3XCord = xCord - 150
        text3XYCard = yCord + 25
        self.canvas.create_text(text3XCord, text3XYCard, anchor="w", font=("Purisa", 15, "bold italic"),  text="PiaSchool")
 
        text4XCord = xCord + 50
        text4YCard = yCord + 25
        self.canvas.create_text(text4XCord, text4YCard, anchor="w", font=("Purisa", 15, "bold italic"),   text="Unknown")
 
        print("values1 : ", msg1Loc, msg1XCord, msg1YCord, msg1Text)
        print("values2 : ", msg2Loc, msg2XCord, msg2YCord, msg2Text)
 
        # This is the programming for the text of the user names.
        self.canvas.create_text(msg1XCord, msg1YCord, anchor="w", font=("Purisa", 24), text=msg1Text)
        self.canvas.create_text(msg2XCord, msg2YCord, anchor="w", font=("Purisa", 24), text=msg2Text)
        self.canvas.create_text(msg3XCord, msg3YCord, anchor="w", font=("Purisa", 24), text=msg3Text)
 
# Refresh every 10 seconds.
        self.tk.after(10000, self.run)
 
# The callback for when the client successfully connects to the broker
def on_connect(client, userdata, rc):
    ''' We subscribe on_connect() so that if we lose the connection
    and reconnect, subscriptions will be renewed.
    '''
    client.subscribe("owntracks/+/+")
 
# The callback for when a PUBLISH message is received from the broker. This method sets
# up all the global variables needed for GUI.
def on_message(client, userdata, msg):
 
    #print("inside on_message")
    topic = msg.topic
 
    try:
        data = json.loads(str(msg.payload))
 
        locLat = data['lat']
        locLon = data['lon']
        locTop = data['tid']
        locDate = data['tst']
        locDateH = time.strftime("%Y/%m/%d, %H:%M:%S %Z", time.localtime(locDate))
        print("TID = {0} is @ at {1}, {2} on {3}".format(locTop, locLat, locLon, locDateH))
 
        global msg1Loc
        global msg1Text
        global msg1XCord
        global msg1YCord
 
        global msg2Loc
        global msg2Text
        global msg2XCord
        global msg2YCord
 
        global msg3Loc
        global msg3Text
        global msg3XCord
        global msg3YCord
 
        msgLoc = ""
        for loc in range(0, NUM_LOCATIONS):
            location = loc_array[loc]
            # print("location : ", loc, location)
            dist = distance(location[1], location[2], locLat, locLon, EARTH_RADIUS)
            # print("dist: ", dist)
            # print("%s distance from %s is: %f kms allowed is %f kms" % (locTop, location[0], dist, location[3]))
            if (dist <= location[3]):
                print("%s is at %s" % (locTop, location[0]))
                msgLoc = location[0]
 
        if (locTop == 'ni'):
            if (msgLoc == "home"):
                msg1XCord = 200
                msg1YCord = 200
            elif (msgLoc == "msgSchool"):
                msg1XCord = 400
                msg1YCord = 200
            elif (msgLoc == "piaSchool"):
                msg1XCord = 200
                msg1YCord = 400
            else:
                msg1XCord = 500
                msg1YCord = 500
 
            msg1Text = "Nikki"
            msg1Loc = msgLoc
        elif (locTop == '99'):
            if (msgLoc == "home"):
                msg2XCord = 200
                msg2YCord = 200 + 50
            elif (msgLoc == "msgSchool"):
                msg2XCord = 400
                msg2YCord = 200 + 50
            elif (msgLoc == "piaSchool"):
                msg2XCord = 200
                msg2YCord = 400 + 50
            else:
                msg2XCord = 500
                msg2YCord = 500 + 50
 
            msg2Text = "Papa"
            msg2Loc = msgLoc
        elif (locTop == '75'):
            if (msgLoc == "home"):
                msg3XCord = 200
                msg3YCord = 200 + 100
            elif (msgLoc == "msgSchool"):
                msg3XCord = 400
                msg3YCord = 200 + 100
            elif (msgLoc == "piaSchool"):
                msg3XCord = 200
                msg3YCord = 400 + 100
            else:
                msg3XCord = 500
                msg3YCord = 500 + 100
 
            msg3Text = "Pia"
            msg3Loc = msgLoc
    except:
        print("Cannot decode data on topic {0}".format(topic))
 
# to calculate the distance of the coordinates from locations
 
def distance(lat1, long1, lat2, long2, radius):
    '''
        Computes the great circle distance between this GeoLocation instance
        and the other.
    '''
    rad_lat1 = math.radians(lat1)
    rad_long1 = math.radians(long1)
    rad_lat2 = math.radians(lat2)
    rad_long2 = math.radians(long2)
 
    return radius * math.acos(
        math.sin(rad_lat1) * math.sin(rad_lat2) +
        math.cos(rad_lat1) *
        math.cos(rad_lat2) *
        math.cos(rad_long1 - rad_long2)
    )
 
mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
 
# This is the local IP address of the Raspberry Pi we used initially for testing.
# mqttclient.connect("192.168.1.99", 1883, 60)
 
# This is the new AWS server
mqttclient.connect("35.162.219.174", 1883, 60)
print(mqttclient.connect)
 
mqttclient.loop_start()
newClock()
