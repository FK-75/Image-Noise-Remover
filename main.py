# here i am importing other modules into my program so i can use the functions stored in them to carry out the tasks i need to in my code.

import numpy as np
# the numpy module is used for arrays which allows me to plot the images in matplotlib.
# The numpy library also contains the functions needed to calculate the average and median of the arrays gained from the images. 

import matplotlib.pyplot as plt # the matplotlib module allows me to plot the images on axis using the arrays calculated and gathered using the numpy function.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# This section of the code is me importing the images into matplotlib. (variable_name = plt.imread('img')).
# The variable name is what the numpy array will be stored as in the program for this image. pt.imread(‘img’) will take the image file and convert it to an array that will have a shape.
# That will correspond with one of the following (x for width, y for height, and the number is the channel.
# The three types are:(x, y) for grayscale images. (x, y, 3) for RGB images. (x, y, 4) for RGBA images.

saltpepper = plt.imread('saltpepper.png') 
# saltpepper (variable_name) is the variable under which I will be storing the numpy array that will be generated by the program. 
# plt.imread(‘saltpepper.png’) will take the image file and convert it to an array that will have a shape.
# That will correspond with one of the following (x for width, y for height, and the number is the channel.
# The three types are:(x, y) for grayscale images. (x, y, 3) for RGB images.(x, y, 4) for RGBA images.

gaussian = plt.imread('gaussian.png')
# gaussian (variable_name) is the variable under which I will be storing the numpy array that will be generated by the program. 
# plt.imread(‘gaussian.png’) will take the image file and convert it to an array that will have a shape.
# That will correspond with one of the following (x for width, y for height, and the number is the channel.
# The three types are:(x, y) for grayscale images. (x, y, 3) for RGB images.(x, y, 4) for RGBA images.


# I have used .png image because matplotlib can only read PNGs. Other file formats would require the use of pillow.
# Which is a third party library meaning that it would need to be installed using the command prompt of the system and is not included in native python. 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# this section of the code will tell the user that the processing procedure has started and that the images are being denoised.
print("Processing Images ...")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# A user defined function allows me to create a custom function that isn’t built into python natively. This allows me to write the code once in the function and call it multiple times.
# A user defined function uses the following structure:
# def <<function_name>>(<<parameter>>):
#	<<block>>
#	return<<expression>>


def localaveraging(img):
# def <<function_name>>(<<parameter>>) in this user defined function localaveraging is the function name I have used because it tells the user what the function calculates.
# Which is the local average of the arrays of the image. The parameter is img because the user will input the variable name of the variable that has the array for the image stored.
# It will calculate the average of the all of the numbers in the array by adding them up in a 3x3 grid and calculating the average excluding the number selected.


# This part below will describe to the user what the function does and what to input. 
    """
    np.array(img) -> np.array(img) (averaged)
    The function will create a new copy of the image, calculate the shape and store the height(y) and width(x). Using this will run a for loop from 1 to x and 1 to y.
    Due to a 3x3 grid being used, the first coordinate needed is 0 which would be i-1:j-1, and the last coordinate needed is i+1:j+1. it will then use the np.average function
    to calculate the average of each position in the array by adding all the numbers in the 3x3 grid and calculating the average and placing the number in that coordinate.
    The grid will then move by 1 in the x and then 1 in the y until it has covered all the points in the x and y range.

    >>> localaveraging(saltpeper) 
    
    
    """
# >>> localaveraging(saltpeper) is a test example of how the function will look when it is called. 

# this is the <<block>> section of the function, this is the main code that will be executed when the function is called. 
    newimg = img.copy() # this will create a copy of the image so that the original image isn't altered. This is done so when changes are made it is done to a different version of the image so each change is unique.
    x,y,z = (img.shape) # this line of code calculates the shape of the image (height, width and channel). These will be stored as x, y, z. 
    for i in range(1,x): # this for loop will go through the array from the first number (1) to the last number (x). x is used from the shape of the image, for example if the width is 150 then the range is 1 to 150. To ensure that all numbers in the array are included.
        for j in range(1,y): # this for loop will go through the array from the first number (1) to the last number (y). y is used from the shape of the image, for example if the height is 150 then the range is 1 to 150. To ensure that all numbers in the array are included.
            newimg[i,j] = np.average(img[i-1:i+1,j-1:j+1]) # in this part of the code, the copied image (newimg) is selected from i to j.
           # This means that all the numbers in the array are selected and will be replaced with the new numbers.
           # np.average is a numpy function that will be used to calculate the average of the numbers in the array. (img[i-1:i+1,j-1:j+1]) will select i-1 to i+1 and j-1 to j+1.
           # this is done because the program uses a 3x3 grid to calculate the averages which would start at 1 which means that the boarders at 0 would be excluded.
           # however starting the range at 1 for i and j and then taking away 1 means that the range will start at 0.
           # 0 couldnt be used in the original statement because a 3x3 grid cannot be created at this position.
    return (newimg) # this is a return statement that will return the result of the function


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#


def MedianFilter(img):
# def <<function_name>>(<<parameter>>) in this user defined function MedianFilter is the function name I have used because it tells the user what the function calculates.
# Which is the median of the arrays of the image. The parameter is img because the user will input the variable name of the variable that has the array for the image stored.
# It will calculate the median of the all of the numbers in the array by arranging the numbers and finding the middle number. 


    
# This part below will describe to the user what the function does and what to input. 
    """
    np.array(img) -> np.array(img)(median)
    The function will create a new copy of the image, calculate the shape and store the height(y) and width(x). Using this will run a for loop from 1 to x and 1 to y.
    Due to a 3x3 grid being used, the first coordinate needed is 0 which would be i-1:j-1, and the last coordinate needed is i+1:j+1. it will then use the np.median function
    to arrange the numbers in the 3x3 grid in order and placing the middle number in each position from the 3x3 grid. The grid will then move by 1 in the x and then 1 in the y until
    it has covered all the points in the x and y range.

    >>> MedianFilter(saltpeper)
    """
# >>> MedianFilter(saltpeper) is a test example of how the function will look when it is called.


# this is the <<block>> section of the function, this is the main code that will be executed when the function is called. 
    newimg = img.copy() # this will create a copy of the image so that the original image isn't altered. This is done so when changes are made it is done to a different version of the image so each change is unique.
    x,y,z = (img.shape) # this line of code calculates the shape of the image (height, width and channel). These will be stored as x, y, z. 
    for i in range(1,x): # this for loop will go through the array from the first number (1) to the last number (x). x is used from the shape of the image, for example if the width is 150 then the range is 1 to 150. To ensure that all numbers in the array are included.
        for j in range(1,y): # this for loop will go through the array from the first number (1) to the last number (y). y is used from the shape of the image, for example if the height is 150 then the range is 1 to 150. To ensure that all numbers in the array are included.
            newimg[i,j] = np.median(img[i-1:i+1,j-1:j+1]) # in this part of the code, the copied image (newimg) is selected from i to j.
           # This means that all the numbers in the array are selected and will be replaced with the new numbers.
           # np.median is a numpy function that will be used to calculate the median of the numbers in the array. (img[i-1:i+1,j-1:j+1]) will select i-1 to i+1 and j-1 to j+1.
           # this is done because the program uses a 3x3 grid to calculate the median which would start at 1 which means that the boarders at 0 would be excluded.
           # however starting the range at 1 for i and j and then taking away 1 means that the range will start at 0.
           # 0 couldnt be used in the original statement because a 3x3 grid cannot be created at this position.
    return (newimg) # this is a return statement that will return the result of the function

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# this code places the images in one figure so they are displayed together at once

fig = plt.figure("Denoising images") # This line of code will place all of the images below in one figure and name the figure "Denoising images".

a = fig.add_subplot(2, 3, 1) # this is code for subplotting. (2,3,1) means there are 2 rows with 3 columns (3 items per row), and the 1 is the item number. so 2,3,1 means that it's the first image in the figure. 
plt.imshow(gaussian) # plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This will place the original image in matplotlib with an axis. 
a.set_title('Gaussian Noise Image') # this is the title that will be placed above the image.

a = fig.add_subplot(2, 3, 2) # this is code for subplotting. (2,3,2) means there are 2 rows with 3 columns (3 items per row), and the 2 is the item number. so 2,3,2 means that it's the second image in the figure.
plt.imshow(localaveraging(gaussian))# plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This is calling the localaverage function on the guassian image and will place it in matplotlib by converting the averaged array to an image.
a.set_title('Gaussian Noise Image - Local Averaging') # this is the title that will be placed above the image.

a = fig.add_subplot(2, 3, 3) # this is code for subplotting. (2,3,3) means there are 2 rows with 3 columns (3 items per row), and the 3 is the item number. so 2,3,3 means that it's the third image in the figure.
plt.imshow(MedianFilter(gaussian)) # plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This is calling the MedianFilter function on the guassian image and will place it in matplotlib by converting the median array to an image.
a.set_title('Gaussian Noise Image - Median Filter') # this is the title that will be placed above the image.

a = fig.add_subplot(2, 3,4) # this is code for subplotting. (2,3,4) means there are 2 rows with 3 columns (3 items per row), and the 4 is the item number. so 2,3,4 means that it's the fourth image in the figure and therfore will be placed on the second row because it is limited to 3 images per row. 
plt.imshow(saltpepper) # plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This will place the original image in matplotlib with an axis.
a.set_title('Salt & Pepper Noise Image') # this is the title that will be placed above the image.

a = fig.add_subplot(2, 3, 5) # this is code for subplotting. (2,3,5) means there are 2 rows with 3 columns (3 items per row), and the 5 is the item number. so 2,3,5 means that it's the fifth image in the figure and therfore will be placed on the second row because it is limited to 3 images per row. 
plt.imshow(localaveraging(saltpepper)) # plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This is calling the localaverage function on the saltpepper image and will place it in matplotlib by converting the averaged array to an image.
a.set_title('Salt & Pepper Noise Image - Local Averaging') # this is the title that will be placed above the image.

a = fig.add_subplot(2, 3, 6) # this is code for subplotting. (2,3,6) means there are 2 rows with 3 columns (3 items per row), and the 5 is the item number. so 2,3,6 means that it's the sixth image in the figure and therfore will be placed on the second row because it is limited to 3 images per row. 
plt.imshow(MedianFilter(saltpepper))  # plt.imshow displays an array as an image. plt.imshow takes in a 2d array and turns it into an image along as it has a shape that has an x and y value that is readable by matplotlib. This is calling the MedianFilter function on the saltpepper image and will place it in matplotlib by converting the median array to an image.
a.set_title('Salt & Pepper Noise Image - Median Filter') # this is the title that will be placed above the image.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Done Processing Images") # this message will tell the user that the images have been processed. 
plt.show() # plt.show is used to display a figure and place items in a figure. so here it will place the images in the figure and display it. 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
