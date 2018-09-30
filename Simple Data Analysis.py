#!/usr/bin/env python
# coding: utf-8

# ### Step 1a: Identify the information in the file your program will read
# 
# When I open global_video_game_sales_in_millions.csv, it contains many rows of information about video game sales. Each row contains:
# 
# - the ranking of the game 
# - the name of the game
# - the platform        (eg: Wii, PS2, DS etc.)
# - the year
# - the genre           (The kind of video game, like action, Role-play, racing, sports etc.)
# - the publisher       (The company producing the games such as Nintendo, Ubisoft, Take-Two Interactive etc.)
# - North America Sales (NA_Sales)
# - Europe Sales        (EU_Sales)		
# - Japan Sales         (JP_Sales)
# - Other Sales         (Other_Sales)
# - Global Sales        (Global_Sales)
# 
# 
# Note: some of the data for years and publisher are not available in the csv file

# ### Step 1b: Write a description of what your program will produce
# 
# Here are a few things I might do with this data:
# 
# - 1) The name of publisher with the highest Global Sales 
# - 2) The global sales of three publishers in a particular year (can use bar chart to represent this)
# - 3) Produce platform with the highest sales in Japan
# 
# Here, I picked to work with #2 

# ### Step 1c: Write or draw examples of what your program will produce
# 
# ```python
# expect(main("global_video_game_sales_in_millions.csv"), None)
# ```
# I expect the test to return none, and it will plot a bar chart such as the one below:
# 
# 
# Bar Chart 
# 
#     global sale
#     ^
#     |       ___
#     |      |   |   __
#     |___   |   |  |  |
#     |   |  |   |  |  |
#     |   |  |   |  |  |
#     |   |  |   |  |  |
#     |___|__|___|__|__|______> Publisher
# 
# 

# ### Step 2a: Design data definitions
# 
# I want to store sufficient data so that I'm able to solve the problem.
# 
# I know that I want to compare the global sales between each of the publishers available in a single year.
# 
# In order to do that, I need to take in the publisher data as I want different kinds of publishers. Afterwhich, I need the global sales data to make the comparisions between the sales of different publishers. 
# 
# However, I do not want all the year's worth of data in the list. So, I will only take in a year in order to make my search easier.
# 
# I will need to use a compound for each video game data stored to represent what data I want to produce, and I will need to create a list for an arbitrary number of video game data.

# In[1]:


from typing import NamedTuple, List
from cs103 import *

VideoGameData = NamedTuple ('VideoGameData', [('publisher', str), # return publisher if publisher is available, otherwise, return None
                                              ('global_sales', float), # range [0, ...)
                                              ('year', int)]) # in range[1956, ...), return None if year is not available
# interp. a video game data record with the with the publisher's name ('Publisher'),
#         global sales ('Global_Sales') and the year ('Year')

VGD1 = VideoGameData('Nintendo', 15.85, 2002)
VGD2 = VideoGameData('Activision', 10.21, 2013)
VGD3 = VideoGameData('Nintendo', 0.63, 'N/A')
VGD4 = VideoGameData('N/A', 1.21, 2007)

# template based on compound 
def fn_for_video_game_data(vgd: VideoGameData) -> ...: 
    return ...(vgd.publisher,
               vgd.global_sales,
               vgd.year)

# List[VideoGameData]
# interp. a list of video game data

LOVGD0 = []
LOVGD1 = [VGD1, VGD2]

# template based on arbitrary-sized and the reference rule
def fn_for_lovgd(lovgd: List[VideoGameData]) -> ...:  
    # description of the acc                           
    acc = ... # type: ...
    for vgd in lovgd:
        acc = ...(acc, fn_for_video_game_data(vgd))
    return acc


# ## Step 2b: Design a function to read the information and store it as data in your program

# In[2]:


import csv

###########
# Functions

def is_valid_year(yr: Optional[int]) -> bool:
    """
    return True if year (yr) is an int and False otherwise
    """
    #return False #body of stub
    if yr is None:
        return False
    else:
        return True
    
def is_valid_publisher(publisher: Optional[str]) -> bool:
    """
    return False if publisher is not available ('N/A'), otherwise return True
    """
    #return False #body of stub
    
    if publisher == 'N/A':
        return False
    else:
        return True
    
def is_2010(one_year: int) -> bool:
    """
    return True if year is 2010
    """
    #return True #body of stub
    
    return one_year == 2010
    

def read(filename: str) -> List[VideoGameData]:
    """    
    reads information from the specified file and returns a list of video game data in year 2010
    """
    #return []   #stub
    #template from HtDAP
    
    # lovgd contains the result so far
    lovgd = [] # type: List[VideoGameData]

    with open(filename, encoding='ISO-8859-1') as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip header line
        
        for row in reader:
            publisher = row[5]
            global_sales = parse_float(row[10])
            year = parse_int(row[3])
            if is_valid_publisher(publisher) and is_valid_year(year) and is_2010(year): 
                vgd = VideoGameData(publisher,
                                    global_sales,
                                    year)  
                lovgd.append(vgd)
    return lovgd


# Begin testing
start_testing()

# examples and tests for is_valid_year
expect(is_valid_year(899813), True)
expect(is_valid_year(None), False)

# examples and tests for is_valid_publisher
expect(is_valid_publisher('Nintendo'), True)
expect(is_valid_publisher('N/A'), False)

# examples and tests for is_2010
expect(is_2010(2010), True)
expect(is_2010(2004), False)

# examples and tests for read
expect(read('global_video_games_sales_in_millions_test1.csv'), [VideoGameData('Microsoft Game Studios', 21.82, 2010)])
       
expect(read('global_video_games_sales_in_millions_test2.csv'),[])   

# show testing summary
summary()


# ## Step 2c: Design functions to analyze the data

# In[3]:


import matplotlib.pyplot as plt
from typing import List
from cs103 import *

def main(filename: str) -> None:
    """
    Reads the file from given filename, analyze the data from it and returns the result of the 
    global sales between Nintendo, Sony Entertainment and Activison in the year 2010
    """
    # template as a function composition
    return plot_global_sales_and_publisher(read(filename))
                    

def get_global_sales_1(lovgd: List[VideoGameData]) -> float:
    """
    return the total global sales of Nintendo
    """
    #return 0.0 #body of stub
    #template taken from List[VideoGameData]
    
    # nintendo_acc is the total global sales of Nintendo seen so far                          
    nintendo_acc = 0.0 # type: float
    for vgd in lovgd:
        if publisher_is_nintendo(vgd):
            nintendo_acc = nintendo_acc + vgd.global_sales
    return nintendo_acc

def publisher_is_nintendo(vgd: VideoGameData) -> bool:
    """
    return True if publisher is Nintendo
    """
    # return True #body of stub
    # template taken from VideoGameData
    
    return vgd.publisher == 'Nintendo'

def get_global_sales_2(lovgd: List[VideoGameData]) -> float:
    """
    return the total global sales of Microsoft Game Studios 
    """
    #return 0.0 #body of stub
    #template taken from List[VideoGameData]
    
     # mgs_acc is the total global sales of Nintendo seen so far                        
    mgs_acc = 0.0 # type: float
    for vgd in lovgd:
        if publisher_is_microsoft_game_studios(vgd):
            mgs_acc = mgs_acc + vgd.global_sales
    return mgs_acc

def publisher_is_microsoft_game_studios(vgd: VideoGameData) -> bool:
    """
    return True if publisher is Microsoft Game Studios
    """
    # return True #body of stub
    # template taken from VideoGameData
    
    return vgd.publisher == 'Microsoft Game Studios'

def get_global_sales_3(lovgd: List[VideoGameData]) -> float:
    """
    return the total global sales of Activision
    """
    #return 0.0 #body of stub
    #template taken from List[VideoGameData]
    
    # activision_acc is the total global sales of Nintendo seen so far                          
    activision_acc = 0.0 # type: float
    for vgd in lovgd:
        if publisher_is_activision(vgd):
            activision_acc = activision_acc + vgd.global_sales
    return activision_acc

def publisher_is_activision(vgd: VideoGameData) -> bool:
    """
    return True if publisher is Activision
    """
    # return True #body of stub
    # template taken from VideoGameData
    
    return vgd.publisher == 'Activision'
       

def plot_global_sales_and_publisher(lovgd: List[VideoGameData]) -> None:
    """
    Display a bar chart showing the global sales of Nintendo, Microsoft Game Studios, and Activision in the year 2010
    
    Draws the plot and returns None.
    """
    #return None  #body of stub
    
    global_sales_nintendo =  get_global_sales_1(lovgd)
    global_sales_microsoft_game_studios =  get_global_sales_2(lovgd)
    global_sales_activision =  get_global_sales_3(lovgd)
    
    all_global_sales = [global_sales_nintendo, global_sales_microsoft_game_studios, global_sales_activision]                        
   
    # the width of each bar
    bar_width = 5
    
    # the left side for each of the bars for the bar chart
    left_side_of_bars = [10, 40, 65]
    
    
    # the opacity for the bars. It must be between 0 and 1, and higher numbers are more opaque (darker)
    opacity = 0.8
    
    # create the first bar chart
    rects1 = plt.bar(left_side_of_bars,
                     all_global_sales, 
                     bar_width,
                     alpha=opacity,                  # set the opacity
                     color='b')                     # set the colour (blue)

    # set the labels for the x-axis, y-axis, and plot title
    plt.xlabel('Publishers')
    plt.ylabel('Global Sales')
    plt.title('Global Sales of Publishers')
    
    # set the range for the axes
    # [x-min, x-max, y-min, y-max]
    plt.axis([0, 80, 0, 100])
    
    # set the x-coordinate for positioning the labels. Here, we want each label to be in the middle of each bar
    x_coord_labels = [10, 40, 65]
    
    # set the labels for each 'tick' on the x-axis
    tick_labels = ['Nintendo', 'Microsoft Game Studios', 'Activision']
    
    plt.xticks(x_coord_labels, tick_labels)
    
    # show the plot
    plt.show()
    
    # by default, Python returns None if it gets to the end of a function and there is no call to return
    # so we could have omitted the next line of code. It also returns None when there is a return 
    # statement that does not explicitly return a value (like we have here)
    return
    
start_testing()

#tests and examples for main
expect(main("global_video_game_sales_in_millions.csv"), None)

#tests and examples for get_global_sales_1
expect(get_global_sales_1(LOVGD0), 0.0)
expect(get_global_sales_1(LOVGD1), 15.85)
expect(get_global_sales_1([VideoGameData('Activision', 14.76, 2011), VGD2, VGD4]), 0.0)

#tests and examples for publisher_is_nintendo
expect(publisher_is_nintendo(VGD3), True)
expect(publisher_is_nintendo(VGD2), False)

#tests and examples for get_global_sales_2
expect(get_global_sales_2(LOVGD0), 0.0)
expect(get_global_sales_2([VideoGameData('Sony Computer Entertainment', 10.95, 1997), VideoGameData('Nintendo', 10.79, 2011), VGD2]), 0.0)
expect(get_global_sales_2([VGD1, VGD2, VideoGameData('Microsoft Game Studios', 21.82, 2010)]), 21.82)

#tests and examples for publisher_is_microsoft_game_studios
expect(publisher_is_microsoft_game_studios(VideoGameData('Microsoft Game Studios',21.82, 2010)), True)
expect(publisher_is_microsoft_game_studios(VGD3), False)

#tests and examples for get_global_sales_3
expect(get_global_sales_3(LOVGD0), 0.0)
expect(get_global_sales_3([VideoGameData('Activision', 12.73, 2010), VideoGameData('Microsoft Game Studios', 12.14, 2007)]), 12.73)
expect(get_global_sales_3([VGD1, VGD3, VGD4]), 0.0)

#tests and examples for publisher_is_activision
expect(publisher_is_activision(VideoGameData('Activision', 14.76, 2011)), True)
expect(publisher_is_activision(VideoGameData('Nintendo', 12.21, 2011)), False)

#tests and examples for plot_global_sales_and_publisher
expect(plot_global_sales_and_publisher(LOVGD1), None)
expect(plot_global_sales_and_publisher([VideoGameData('Nintendo', 15.85, 2010), VideoGameData('Microsoft Game Studios', 21.82, 2010), VideoGameData('N/A', 1.21, 2007)]), None)
expect(plot_global_sales_and_publisher([VideoGameData('Nintendo', 82.74, 2006), VideoGameData('Activision', 10.21, 2013), VideoGameData('Nintendo', 1.03, 'N/A')]), None)

summary()

