#!/usr/bin/env python3

# Created by Megan E Guidry - University of Rhode Island, Dept. of Biological Sciences

# Package was created to prompt users with marine biology knowledge questions and provide info to fill in knowledge gaps. 
# Designed to be used in conjunction with the game script for science education pop sim model.

# assessment questions function
def questions():
    """Assessment of knowledge questions."""
    print("\n*","\nWhat is the salinity of full sea water?\na) 63ppt\nb) 100ppt\nc) 35ppt\nd) 10ppt\n","*\n")
    sw = input("\nanswer (a, b, c, or d): ")
    print("\n")
    sw = str.lower(sw)
    return sw