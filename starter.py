#Importing libraries necassary libraries as needed
import tensorflow as tf 
from tensorflow import keras


# Globlal variables that can easily be changed to the requirements of the program
IMG_HEIGHT = 32
IMG_WIDTH = 32
EPOCHS = #Input number of epochs
BS = #input batch size #Batch size => refers to the number of training examples utilized in one iteration

#Load cifar10 dataset into training and testing images and labels to be used for the CNN
# (trainImages, trainLabels), (testImages, testLabels) = something something 

#Shrink pixel values to binary (from a value between 0 to 255 to 0 to 1)
trainImages = trainImages / 255.0
testImages = testImages / 255.0

#Class labels for the dataset (for reference)
classNames = #add matrix of labels

# Now onto the funstuff - The construction of the CNN using 32 nodes and gradually increase the CNN's neurons (in the hidden layer) to increase the quality of the CNN
# and of course it is used with the max pool function witha  kernal size of 2x2 to pool the convolutions.

"""
Note: The convolution and pooling steps can be repeated multiple times to extract additional features and reduce the size of the input to 
the neural network. One of the benefits of these processes is that, by convoluting and pooling, the neural network becomes less sensitive to variation. 
That is, if the same picture is taken from slightly different angles, the input for convolutional neural network will be similar, whereas, without 
convolution and pooling, the input from each image would be vastly different.
"""
model = models.Sequential()
#create your own CNN network!

# model.summary() # You can include this line if you want to see the models' network and parameters 

#Configure the model using adam optimizer, along with Sparse Categorical Cross entropy and and accuracy metric 

model.compile(# add your compiler optimizer and other settings)

# train model and fit data using the following 
reduceLR = #constant that you may require
history = #whatever fitting alg

# Saving model to disk (can be commented off to see the model)
# model.save('CNN_CIFAR.h5') # Remove the first hash to save the model if you would like

# Plot code used to create line graph showing accuracy vs val accuracy

plt.show()
