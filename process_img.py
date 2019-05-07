import cv2
import os
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

# define the model options and run

options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 500,
    'threshold': 0.05
}

tfnet = TFNet(options)

# read the color image and covert to RGB

img = cv2.imread('teste4.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)

# pull out some info from the results

tl = (result[0]['topleft']['x'], result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'], result[0]['bottomright']['y'])
label = result[0]['label']


# add the box and label and display it
img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
plt.show()
