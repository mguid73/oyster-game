#!/usr/bin/env python3

# Created by Megan E Guidry - University of Rhode Island, Dept. of Biological Sciences

# Module was created to prompt users with marine biology knowledge questions and provide info to fill in knowledge gaps. 
# Designed to be used in conjunction with the game script for science education pop sim model.


# Questions are flesh out, but follow up background info needs to be filled in as well as the "scoring" if/else statements 

#seawater and salinity
#1
def seawater():
    print("\n*","\nWhat is the salinity of full sea water in the ocean?\na) 63ppt\nb) 100ppt\nc) 35ppt\nd) 10ppt\n*\n")
    sw = input("\nanswer (a, b, c, or d): ")   #correct answer is c
    print("\n")
    sw = str.lower(sw)
    #print statemtns based on the response 
    # include ppt explanation 
    # include what can lower the salinity
    return sw

#2
def sal():
    print("\n*","\nIn which salinity would an oyster be able to survive best?\na) 33ppt\nb) 2ppt\nc) 10ppt\n*\n")
    os = input("\nanswer (a, b, c, or d): ")   #correct answer is a
    print("\n")
    os = str.lower(os)
    # print statments about oyster sal tolerance and how oysters are marine animals hence live in seawater
    # coastal esturarines where oysters live can range in salinity due to riverine inputs, storms, etc. 
    # thus oysters have a tolerance to a range of salinities. Their sensitivity to lower salinities is can be determined based on their evolutionary histories
    return os

# temperature
#3
def spawntemp():
    print("\n*","\nWhat season due oysters spawn?\na) winter\nb) summer\nc) fall\nd) spring\n*\n")
    sp = input("\nanswer (a, b, c, or d): ")  #correct answer is b
    print("\n")
    sp = str.lower(sp)
    #print statements about spawning in thw summer and temp that oysters spawn 
    return sp
    
# pH and ocean acidification
#4
def typicalpH():
    print("\n*","\nWhat is the typical pH of seawater?\na) 7.0\nb) 5.5\nc) 8.1\n*\n")
    x = input("\nanswer (a, b, or c): ")  #correct answer is c 
    print("\n")
    x = str.lower(x)
    #print statements about pH and how its predicted to change with climate change
    return x

#5
def pHchange():
    print("\n*","\nWould would reduce the pH of coastal waters?\na) nutrient input\nb) increase in temperature\nc) increase in bacterial respiration\nd) increase in dissolved carbon dioxide\ne) all of the above\n*\n")
    y = input("\nanswer (a, b, c, d, or e): ")  #correct answer is b 
    print("\n")
    y = str.lower(y)
    #print statements about coastal acidification
    return y
    # https://www.fisheries.noaa.gov/feature-story/how-will-changing-ocean-chemistry-affect-shellfish-we-eat
    # https://www.pmel.noaa.gov/co2/story/What+is+Ocean+Acidification%3F#:~:text=The%20Chemistry,or%20%22OA%22%20for%20short.

#6
def oysterpH():
    print("\n*","\nWhat is the biggest impact of low pH on oysters?\na) reduces their filter feeding ability\nb) impacts their ability to make their shells\nc) the oyster meat yield is lower\n","*\n")
    y = input("\nanswer (a, b, or c): ")  #correct answer is b 
    print("\n")
    y = str.lower(y)
    #print statements about how CA affects 
    return y


# how to print out QR code at the end of the script with more resources - link to a github page