#!/usr/bin/env python3
import time

# set up oyster population class
class oysterpop:
    """This class defines functions for pulling data from the command line, creating environmental data lists, 
    setting starting population size, and a popsim function to model population size.
    Created by Megan Guidry, URI for an oyster pop simulation game."""
    #initializing class
    def __init__(self, site, startSize, saltol, temptol, pHtol):
        """saltol is the lowest salinity the pop can tolerate. 
        temptol is the highest temp the pop can tolerate. 
        pHtol is the lowest pH the pop can tolerate.
        Environmental data ranges and tolerances are based off of Save The Bay Facts and Figures: Vital Narragansett Bay Statistics.
        All 'data' is fictional and used only for educational modeling purposes. This model is a vast oversimplification for general public education."""
        self.saltol = saltol
        self.temptol = temptol
        self.pHtol = pHtol
        self.startSize = startSize
        self.site = site
    # SET SEASON FOR SIMULATION
    def setseason():
    	"""User inputs season which will determine the temperature range they can input and the storm messages that occur later"""
    	print("Pick your season for running each population simulation! ...summer or winter?")
    	season = input("Type season here: ")
    	season = str.lower(season)
    	#print(season)
    	if season == "fall" or season == "spring":
    		print("Incorrect season input... We've selected to run a summer simulation for you! Let's see if the oysters will spawn this month!\nCalibrating game for summer...")
    		season = "summer"
    	else:
    		print("Calibrating game for...", str.upper(season), "\n")
    		time.sleep(2)
    		input("*Press ENTER to continue*")
    		if season == "summer":
    			print("*"*200, "\nSummer is when oysters will spawn to make new oysters! If the temperature reaches 20°C the population size will increase!\nKeep this in mind during the simulation if your population is declining.\n")
    		else:
    			if season == "winter":
    				print("*"*200, "\nThe oysters are in for a chilly winter. Because oysters do not spawn below 20°C, there will be no way to increase their population size in the winter.\n")
    				time.sleep(2)
    				print("*\n" *5, "\n")
    				time.sleep(2)
    				input("*Press ENTER to continue*")
    	return season
    # asking for inputs from user -- add more info 
    def fetchsalinity():
    	"""User inputs salinity values."""
        salin = input("Input salinity (typical range is 24-32ppt): ")
        salfloat = float(salin)
        return salfloat
    
    def fetchtemp(season):
    	"""User inputs temperature values. Includes season dependent messages and requires season variable to be input."""
        if season == "winter":
            tempin = input("Input temperature in °C (typical winter temp ranges from 4°C to 12°C): ")
            tempfloat = float(tempin)
            if (tempfloat > 15):
                print("Sneaky, sneaky! You are in the winter simulation. Your temperature must be below 15°C\n")
                time.sleep(1)
                tempin = input("Input temperature in °C (typical winter temp ranges from 4°C to 12°C): ")
        else:
            if season == "summer":
                tempin = input("Input temperature in °C (typical summer temp ranges from 16°C to 23.5°C): ")
                tempfloat = float(tempin)
                if (tempfloat > 60):
                    print("Wow! that's way too hot! Your oysters would all die, and we don't want that! Pick a temperature between 16°C to 30°C\n")
                    time.sleep(1)
                    tempin = input("Input temperature in °C (typical summer temp ranges from 16°C to 23.5°C): ")
        return tempfloat
    
    def fetchpH():
    	"""User inputs pH."""
        pHin = input("Input pH (range from 7.8 to 8.3): ")
        pHfloat = float(pHin)
        return pHfloat
#setting up storm function 
    def storm(season):
    	"""Function to simulate a storm (hurricane or snow) depending on the season variable."""
        if season == "summer":
            salin = 7 
            print ("****************\n*BREAKING NEWS*\nA huge hurricane has hit the coast! The salinity will drop dramatically.\nSalinity = 7ppt")
            salfloat = float(salin)
        else:
            if season == "winter":
                salin = 10
                print ("****************\n*BREAKING NEWS*\nA huge snowstorm has hit and all the snow is melting reducing the coastal salinity dramatically.\nSalinity = 10ppt\n****************")
                salfloat = float(salin)
        return salfloat
#runoff function
    def runoffpH(season):
    	"""Run-off function that simulates reduced pH in coastal waters after nutrient input"""
        if season == "summer":
            pHin = 7.5
            time.sleep(1)
            print("****************\nThe hurricane has lead to nutrient rich coastal runoff.\nThe bacteria in coastal waters metabolize these nutrients and reduce the pH\npH = 7.5\n****************")
            pHfloat = float(pHin)
        else: pHin = input("Input pH (range from 7.8 to 8.3): ")
        pHfloat = float(pHin)
        return pHfloat

    #WORK ON POP SIM FUNCTION
    def popsim(self, salinities, temperatures, pHs):
    	"""Simulation function incorporates values that the user inputs on the commandline from the 'fetch' functions."""
        populationSizes = []  #initalize list of pop sizes through generations
        populationSizes.append(self.startSize)  #append start size at time 0 
        environments = zip(salinities, temperatures, pHs)  #group environmental parameters (these are the lists made from the user input)

        for environment in environments:
            salinity = environment[0]
            temperature = environment[1]
            pH = environment[2]
            newSize = populationSizes[-1]   #new pop sizes will make up another column
            
            #SALINITY
            if (salinity >= 18): #if salinity is 18+ppt then use tolerance to set size
                if (salinity < self.saltol):    #if salinity is less than oyster salinity tolerances...
                    newSize = newSize * .9      #only 90% of the oyster population will remain - 10% will die
                else:
                    if (salinity > self.saltol):
                        newSize = newSize
            else:
                if (10 <= salinity < 18):  # if salinity is lower than 18ppt but greater than or equal to 10ppt, pop will decrease even more drastically
                    newSize = newSize * .60 #new oyster population size will decrease by 40% if salinity is less than 18
                else:
                	if (5 <= salinity < 10):  #if salinity is 5 or between 5 and 10, 
                	    newSize = newSize * .40 #pop size will decrease by 60%
                	else:
                		if (salinity < 5):  #if salinity is less than 5,
                			newSize = 0   #pop will die

            #TEMPERATURE
            if (temperature == 20): #if temperature is 20 degrees Celsius
                newSize = newSize * 1.2 #new population size will increase, oysters will spawn
            else:
                if (temperature > self.temptol): #if the temperature is greater than oyster temperature tolerance
                    newSize = newSize * .80 #80% of the oyster population will remain
                else:
                    if (0 < temperature < self.temptol): #if temp is less than temp tolerance, 
                        newSize = newSize  #pop will remain the same size
                    else:
                        if (temperature<0): #if user input is below zero, oysters will freeze and die :(
                            newSize = 0

            #pH
            if ((self.pHtol + .05) > pH > (self.pHtol - .05)):  #if pH is within 0.05 of the pH tolerance
                newSize = newSize   # the pop size stays the same 
            else:
                if (pH >= (self.pHtol + .3)):  #if pH is 0.5 more basic than pH tolerance,
                    newSize = newSize * .65 #the pop size is reduced by 35%
                if (pH <= (self.pHtol - .3)):  #if pH is 0.5 more acidic than pH tolerance,
                    newSize = newSize * .65 #pop size is reduced by 35%
                if (pH <= (self.pHtol - 1)):  #if pH is 1 more acidic than pH tolerance,
                    newSize = newSize * .20 #pop size is reduced by 80%
                if (pH >= (self.pHtol + 1)):  #if pH is 1 more basic than pH tolerance,
                    newSize = newSize * .20 #pop size is reduced by 80%
                

            populationSizes.append(newSize) #with every user input, new oyster population size determined by environment conditions
                                            #will be appended to list of oyster population sizes
        return populationSizes #returns the values of the oyster population sizes