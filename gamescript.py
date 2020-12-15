#!/usr/bin/env python3

# Created by Megan E Guidry - University of Rhode Island, Dept. of Biological Sciences

# Game to show population evolutionary history differences and oyster population size change in response to changing environmental conditions. 
# This game is intended to be used for science eduction purposes. 

# Population simulation game is set up for oyster populations in coastal Rhode Island, however
# it could be edited to portray another species or another location.


#import general packages for plotting
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#cartopy imports for mapping
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
# time to add in delays for print statements- for dramatic effect
import time
# module designed for input data and pop simulation
import oysterpop as op
from oysterpop import *
# module for assessment questions
import questions as qa

#welcome message 
print("\U0001F9AA"*100, "\n")
print("WELCOME TO THE OYSTER POPULATION SIMULATOR GAME!")
print("    Game maker: Megan Guidry", "\n")
print("\U0001F9AA"*100, "\n")
time.sleep(3)

#input name to add some randomness to the game
name = input("Enter your first name here: ")
name1 = str.lower(name) 
letter1 = name1[0] #pull the first letter of name
# dictionary to create number equivalencies with 1st letter of name -- will be used later for some stochasticity in the game
alpha = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',
    9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',
    18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}

# more info printed to the screen introducing the concepts in the game with some time sleeps for dramatic effect
print("."*200, "\n")
print("Hello ",name,"!","\n*\nThis game is an educational tool that illustrates the issues facing Crassostrea virginica (eastern oyster) populations here in coastal Rhode Island and many other regions.\n*\nEastern oysters are facing population declines due to overfishing, warming waters, disease, storms and so many other reasons.\n*\nBy far the biggest threat to maintaining sustainable oyster populations is climate change and the impacts it has on coastal oceans.\n*\nClimate change will continue to increase water temperatures, increase coastal acidification, and alter coastal salinity patterns.\n*\nFor oysters, who stay in the same spot their whole adult lives, these impacts could have devistating effects.\n*\nSo here's where you come in...", "\n")
time.sleep(5)
input("*Press ENTER to continue*")
print("In the same way that human populations are unique, so too are oyster populations.\n*\nThis game will walk you through deciding the fate of 2 different oyster populations through on-screen prompts.\n*\nThe prompts will ask you to define environmental conditions(water salinity, temperature, and pH),\n*\nand the program will determine how each distinct population reacts to those changing conditions.\n*\nSuccess of a population will be measured through population size.\n*\nAt the end of the game, you will be able to see the population increase and decrease over time because of the decisions you made.", "\n")
time.sleep(2)
input("*Press ENTER to continue*")
print("\nThe goal of this game simulator is to investigate the survival of your oyster populations based on the decisions you make about their environment. So chose wisely!\n*\nThe oysters are depending on you!\U0001F9AA")
print("\nTo play, follow the prompts on the screen as they appear.")
time.sleep(2)
input("*Press ENTER to continue*")
print("\nFirst let's test your knowledge with a few questions about oysters and their environment!\n")
time.sleep(1)

# USE QUESTIONS.PY to prompt user with general knowledge questions 
# print("#1\U0001F9AA\n"); qa.seawater()
# print("#2\U0001F9AA\n"); qa.sal()
# print("#3\U0001F9AA\n"); qa.spawntemp()
# print("#4\U0001F9AA\n"); qa.typicalpH()
# print("#5\U0001F9AA\n"); qa.pHchange()
# print("#6\U0001F9AA\n"); qa.oysterpH()

#continue on to map
print("."*200, "\n")
time.sleep(1)
input("*Press ENTER to continue*")
print("\nNow let's get better aquainted with some fictional oyster populations in coastal Rhode Island.\n*\nA map will appear on the screen momentarily. Thank you for your patience...\n")
input("*Press ENTER to continue*")

# map of fictional oyster pops to create some proximity to local environment and make the distinction between two populations with physical distance
# Make a figure object.
fig = plt.figure()
fig = plt.figure(figsize=(12,12))
fname = "landsat.png"
# set image extent #W,E,S,N 
#img_extent = [-72.373, -70.503, 41.337, 42.053] #old extent
img_extent = [-72.373, -70.503, 41.3, 42.063]  
img = plt.imread(fname)
ax = plt.axes(projection=ccrs.PlateCarree())
# figure title
plt.suptitle('Investigate the two populations marked with yellow stars!\nEach fictional oyster population has distinct conditions it thrives in.\nOnce you are finished investigating these populations, exit out of this map and\nthe figure pop-up window to continue the simulator game by following the on-screen prompts.')
# set a margin around the data
ax.set_xmargin(0.5)
ax.set_ymargin(0.5)
# add the image. Because this image was a tif, the "origin" of the image is in the upper left corner
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax.add_feature(cfeature.STATES.with_scale('10m'), linewidth=1) 
#ax.coastlines(resolution='50m', color='yellow', linewidth=1) #not as useful as the states feature
# Add the location of nearby cities
long = [-71.409,  -71.310, -71.4495, -71.8273]
lat= [41.821,  41.492, 41.4501, 41.3776]
# plot landmark locations on the map.  Specify the correct coordinate transform.
plt.plot([long], [lat], marker='o', color="white", transform=ccrs.Geodetic(),) #x=long, y=lat
long2 = [-71.46, -71.3, -71.6, -71.8, -70.7]
lat2= [41.85, 41.5, 41.39, 41.37, 41.3805]
names= ['Providence', 'Newport', 'Narragansett', 'Westerly', "Martha's Vineyard"]
# plotting city names
# providence
plt.text(long2[0], lat2[0], names[0], color = 'white', transform=ccrs.Geodetic())
# newport
plt.text(long2[1], lat2[1], names[1], color = 'white', transform=ccrs.Geodetic())
# narragansett
plt.text(long2[2], lat2[2], names[2], color = 'white', transform=ccrs.Geodetic())
# westerly
plt.text(long2[3], lat2[3], names[3], color = 'white', transform=ccrs.Geodetic())
# martha's vineyard 
plt.text(long2[4], lat2[4], names[4], color = 'white', transform=ccrs.Geodetic())

# Add in fictional OYSTER POPULATIONS based on Jaris et al 2019
# narrow river point and label
plt.plot(-71.4477, 41.4930, marker = '*', color='yellow', transform=ccrs.Geodetic(),) #x=long, y=lat
ax.text(-71.67, 41.5, 'Narrow River', style='italic',
        bbox={'facecolor': 'yellow', 'alpha': 1, 'pad': 1}, 
        transform=ccrs.Geodetic())
# ninigret pond point and label
plt.plot(-71.6718, 41.3546, marker = '*', color='yellow', transform=ccrs.Geodetic(),) #x=long, y=lat
ax.text(-71.7, 41.3, 'Ninigret Pond', style='italic',
        bbox={'facecolor': 'yellow', 'alpha': 1, 'pad': 1}, 
        transform=ccrs.Geodetic())
plt.show()
#after the figure is displayed, all figure windows have to be closed for the game to continue on the command line
input("*Press ENTER to continue*")
# message after viewing map 
print("."*200, "\n")
time.sleep(2)
print("Now that you're oriented to the study populations on the map, Ninigret Pond and Narrow River,\nlet's learn a little more about their tolerance to different environmental conditions.")
time.sleep(2)
print("\n*\nBeause each population experiences different conditions, it will have evolved to survive under a specific set of conditions.\n")
time.sleep(2)
input("*Press ENTER to continue*")
time.sleep(1)
print("\n")
print("."*100, "\n")
# tell user ninigret pond parameters
print("Ninigret Pond oysters can tolerate the following parameters without extreme mortality:\noptimal pH= 8.1 \nlowest salinity= 24ppt \nhighest temperature= 80°F\n") #24, 27, 8.1
print("."*100, "\n")
time.sleep(3)
input("*Press ENTER to continue*")
print("\n", "."*100, "\n")
# tell user narrow river parameters
print("Narrow River oysters can tolerate the following parameters without extreme mortality:\noptimal pH= 7.9 \nlowest salinity= 20ppt \nhighest temperature= 75°F\n")  #20, 24, 7.9
print("."*200, "\n")
time.sleep(3)
input("*Press ENTER to continue*")
print("Configuring population tolerances into simulation...\n")  #dramatic effect -- we actually do this step later 
time.sleep(1)
print("...\n")
time.sleep(1)
print("...\n")
time.sleep(1)
print("...\n")
time.sleep(3)

# START SIMULATION MESSAGES
print ("*"*100, "\nThe game will begin to prompt you for inputs about the conditions in Ninigret Pond and then Narrow River.\n...\nEach condition input will last for 5 'game days' with a total of 5 inputs meaning the game simulates 25 'days'\n...\nBe creative with your inputs!\nRemember, you decide the fate of these oyster populations!\n\n")
input("*Press ENTER to continue*")
print ("\nWill a big rainstorm reduce the salinity beyond the suggested range?\n...Will there be coastal pollution that dramatically reduces the pH?\n...Will there be a summer spawn at 68°F?\n")
input("*Press ENTER to continue*")
# countdown -more drama
print("GAME WILL BEGIN IN...")
time.sleep(2)
print("...3...\n"); time.sleep(1); print("...2...\n"); time.sleep(1);print("...1...\n"); time.sleep(1)

# set season for simulations
season = op.oysterpop.setseason()

# ## NINIGRET POND SIMULATION 
print ("\n\n\U0001F9AA NINIGRET POND SIMULATION \U0001F9AA\n\n")
print("Ninigret Pond oysters can tolerate the following parameters without extreme mortality:\noptimal pH= 8.1 \nlowest salinity= 24ppt \nhighest temperature= 80°F\n\n") #24, 27, 8.1
# set up parameters for Ninigret Pond using the op class framework
input("*Press ENTER to continue*")
NP = op.oysterpop("Ninigret Pond", 1000, 24, 27, 8.1)
# create empty lists for user input to be appended to
NPsalinities = []
NPtemperatures = []
NPpHs = []
#ask for user inputs and give updates on oyster pop sizes 
time.sleep(2)
# here, using the alpha dictionary from earlier, the if statement determines if there will be a storm in the simulation or not
# essentially, if the name input in the beginning of the game starts with A-M, there will be a storm in the simulation; 
# if the name begins with N-Z, then there will be no storm/
if letter1 <= alpha[13]: #first senario-- STORMS
    for i in range(1,6):  #will prompt user 5 times for new parameters to simulate a total of 25 days (each input = 5 days)
        if i <=3:
            NPsalinities.append(op.oysterpop.fetchsalinity())
            time.sleep(1)
            NPtemperatures.append(op.oysterpop.fetchtemp(season))
            time.sleep(1)
            NPpHs.append(op.oysterpop.fetchpH())
            time.sleep(2)
            if i == 1:
                print("First 5 day average recorded...\n***********")
            else: print("Next 5 days recorded...\n***********")
            #run simulation
            NPpopulation = op.oysterpop.popsim(NP, NPsalinities, NPtemperatures, NPpHs)
            print("Oysters are at", (NPpopulation[i]/1000)*100,"% of original population size")
            time.sleep(2)    
            if i < 5:
                print("On to the next round!\n***********")
                if i == 5:
                    print("All inputs and population sizes recorded.\n*\n*\n*\n")
                    time.sleep(2)
                    print("Move on to the Narrow River population simulation!!\n*\n*\n*\n")
        else:
            if i == 4:       # on the forth prompt, there will be a hurricane or snow storm
                NPsalinities.append(op.oysterpop.storm(season))
                time.sleep(1)
                NPtemperatures.append(op.oysterpop.fetchtemp(season))
                time.sleep(1)
                NPpHs.append(op.oysterpop.runoffpH(season))
                time.sleep(2)
                if i == 1:
                    print("First 5 day average recorded...\n***********")
                else: print("Next 5 days recorded...\n***********")    
                #run simulation
                NPpopulation = op.oysterpop.popsim(NP, NPsalinities, NPtemperatures, NPpHs)
                print("Oysters are at", (NPpopulation[i]/1000)*100,"% of original population size")
                time.sleep(2)    
                if i < 5:
                    print("On to the next round!\n***********")
                    if i == 5:
                        print("All inputs and population sizes recorded.\n*\n*\n*\n")
                        time.sleep(2)
                        #print("Move on to the Narrow River population simulation!!\n*\n*\n*\n")
            else:
                if i > 4:
                    NPsalinities.append(op.oysterpop.fetchsalinity())
                    time.sleep(1)
                    NPtemperatures.append(op.oysterpop.fetchtemp(season))
                    time.sleep(1)
                    NPpHs.append(op.oysterpop.fetchpH())
                    time.sleep(2)
                    if i == 1:
                        print("First 5 day average recorded...\n***********")
                    else: print("Next 5 days recorded...\n***********")
                    #run simulation
                    NPpopulation = op.oysterpop.popsim(NP, NPsalinities, NPtemperatures, NPpHs)
                    print("Oysters are at", (NPpopulation[i]/1000)*100,"% of original population size")
                    time.sleep(2)    
                    if i < 5:
                        print("On to the next round!\n***********")
                    else:    
                        if i == 5:
                            print("All inputs and population sizes recorded.\n*\n*\n*\n")
                            time.sleep(2)
                            print("Move on to the Narrow River population simulation!!\n*\n*\n*\n")
else:
    if letter1 > alpha[13]:  #NO STORM
        for i in range(1,6):  #will prompt user 5 times for new parameters to simulate a total of 25 days (each input = 5 days)
            NPsalinities.append(op.oysterpop.fetchsalinity())
            time.sleep(1)
            NPtemperatures.append(op.oysterpop.fetchtemp(season))
            time.sleep(1)
            NPpHs.append(op.oysterpop.fetchpH())
            time.sleep(2)
            if i == 1:
                print("First 5 day average recorded...\n***********")
            else: print("Next 5 days recorded...\n***********")
            #run simulation
            NPpopulation = op.oysterpop.popsim(NP, NPsalinities, NPtemperatures, NPpHs)
            print("Oysters are at", (NPpopulation[i]/1000)*100,"% of original population size")
            time.sleep(2)    
            if i < 5:
                print("On to the next round!\n***********")
                if i == 5:
                    print("All inputs and population sizes recorded.")
                    time.sleep(2)
                    print("Move on to the Narrow River population simulation!!\n*\n*\n*\n")



## NARROW RIVER SIMULATION
time.sleep(3)
print ("\n\n\U0001F9AA NARROW RIVER SIMULATION \U0001F9AA\n\n")
# tell user narrow river parameters
print("Narrow River oysters can tolerate the following parameters without extreme mortality:\noptimal pH= 7.9 \nlowest salinity= 20ppt \nhighest temperature= 75°F\n\n")  #20, 24, 7.9
input("*Press ENTER to continue*")
# set up parameters for Ninigret Pond using the op class framework
NR = op.oysterpop("Narrow River", 1000, 20, 24, 7.9)
# create empty lists for user input to be appended to
NRsalinities = []
NRtemperatures = []
NRpHs = []
#ask for user inputs and give updates on oyster pop sizes 
time.sleep(2)
# repeated if statement from earlier simulation except the the first half of the alphabet has no storm and the second half has a storm 
if letter1 > alpha[13]: #first senario-- STORMS
    for i in range(1,6):  #will prompt user 5 times for new parameters to simulate a total of 25 days (each input = 5 days)
        if i <=3:
            NRsalinities.append(op.oysterpop.fetchsalinity())
            time.sleep(1)
            NRtemperatures.append(op.oysterpop.fetchtemp(season))
            time.sleep(1)
            NRpHs.append(op.oysterpop.fetchpH())
            time.sleep(2)
            if i == 1:
                print("First 5 day average recorded...\n***********")
            else: print("Next 5 days recorded...\n***********")
            #run simulation
            NRpopulation = op.oysterpop.popsim(NR, NRsalinities, NRtemperatures, NRpHs)
            print("Oysters are at", (NRpopulation[i]/1000)*100,"% of original population size")
            time.sleep(2)    
            if i < 5:
                print("On to the next round!\n***********")
                if i == 5:
                    print("All inputs and population sizes recorded.\n*\n*\n*\n")
                    time.sleep(2)
        else:
            if i == 4:
                NRsalinities.append(op.oysterpop.storm(season))
                time.sleep(1)
                NRtemperatures.append(op.oysterpop.fetchtemp(season))
                time.sleep(1)
                NRpHs.append(op.oysterpop.runoffpH(season))
                time.sleep(2)
                if i == 1:
                    print("First 5 day average recorded...\n***********")
                else: print("Next 5 days recorded...\n***********")    
                #run simulation
                NRpopulation = op.oysterpop.popsim(NR, NRsalinities, NRtemperatures, NRpHs)
                print("Oysters are at", (NRpopulation[i]/1000)*100,"% of original population size")
                time.sleep(2)    
                if i < 5:
                    print("On to the next round!\n***********")
                    if i == 5:
                        print("All inputs and population sizes recorded.\n*\n*\n*\n")
                        time.sleep(2)
            else:
                if i > 4:
                    NRsalinities.append(op.oysterpop.fetchsalinity())
                    time.sleep(1)
                    NRtemperatures.append(op.oysterpop.fetchtemp(season))
                    time.sleep(1)
                    NRpHs.append(op.oysterpop.fetchpH())
                    time.sleep(2)
                    if i == 1:
                        print("First 5 day average recorded...\n***********")
                    else: print("Next 5 days recorded...\n***********")
                    #run simulation
                    NRpopulation = op.oysterpop.popsim(NR, NRsalinities, NRtemperatures, NRpHs)
                    print("Oysters are at", (NRpopulation[i]/1000)*100,"% of original population size")
                    time.sleep(2)    
                    if i < 5:
                        print("On to the next round!\n***********")
                    else:    
                        if i == 5:
                            print("All inputs and population sizes recorded.\n*\n*\n*\n")
                            time.sleep(2)
else:
    if letter1 <= alpha[13]:
        for i in range(1,6):  #will prompt user 5 times for new parameters to simulate a total of 25 days (each input = 5 days)
            NRsalinities.append(op.oysterpop.fetchsalinity())
            time.sleep(1)
            NRtemperatures.append(op.oysterpop.fetchtemp(season))
            time.sleep(1)
            NRpHs.append(op.oysterpop.fetchpH())
            time.sleep(2)
            if i == 1:
                print("First 5 day average recorded...\n***********")
            else: print("Next 5 days recorded...\n***********")
            #run simulation
            NRpopulation = op.oysterpop.popsim(NR, NRsalinities, NRtemperatures, NRpHs)
            print("Oysters are at", (NRpopulation[i]/1000)*100,"% of original population size")
            time.sleep(2)    
            if i < 5:
                print("On to the next round!\n***********")
                if i == 5:
                    print("All inputs and population sizes recorded.")
                    time.sleep(2)


#PLOTTING POP SIZES
# print statement about plots
print("\nAll simulations are complete! Hopefully your oysters faired out well!\n")
print("Let's visualize the changes in population sizes on a graph\nWhen you are finished viewing the graph, close out of the graphing window to continue in the game window.\n")
time.sleep(3)
input("*Press ENTER to continue*")
print("\nGRAPHING...")
time.sleep(2)

# create x axis list for plotting
t = [0, 5, 10, 15, 20, 25]

# plot
fig, ax = plt.subplots(figsize=(14,8))
ax.plot(t, NPpopulation, 'blue' ,linewidth= 5, label='Ninigret Pond')
ax.plot(t, NRpopulation, 'green',linewidth= 5, label='Narrow River')
# y limit
ax.set_ylim([0,1500])
#legend
ax.legend()
# title
fig.suptitle("Populations over 25 days", fontsize = 40)
# axis labels
ax.set_xlabel("Days in the Game", fontsize = 30)
ax.set_ylabel("Population Size", fontsize = 30)
# tick labels
ax.tick_params(axis="x", labelsize=24)
ax.tick_params(axis="y", labelsize=24) 
ax.grid()
# show and save figure
plt.show()
#fig.savefig('graph.png')


# include in end message
print("\nYou should have seen some difference in the population sizes over time.\n*\nPart of this variation is due to the differences in the populations themselves,\n...part of it is due to the decisions you made for each population,\n...and sometimes populations are influenced by random events.\n")
time.sleep(2)
input("*Press ENTER to continue*")
print("\nMuch like this simulation game, humans have the chance to make the right choices to save valuable species like oysters.\n...\nThrough making smarter decisions and supporting policy that mitigates the effects of climate change, we can be better stewards of our planet.\n")
time.sleep(10)
print("\U0001F9AA\n")
time.sleep(1)
print("\U0001F9AA\n")
time.sleep(1)
print("\U0001F9AA\n")
time.sleep(1)
print("THANK YOU FOR PLAYING!\n")

#final statement
time.sleep(3)
print("*"*200)
print("*"*200, "\n")
print("For more information on this simple model simulation, please contact Megan Guidry (by email at mguidry@uri.edu or on Twitter @meg_guidry)\n")
print("*"*200)
print("*"*200, "\n")

