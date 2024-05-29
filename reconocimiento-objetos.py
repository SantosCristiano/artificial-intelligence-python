# io import BytesIO
#uploaded = files.upload()
#from google.colab import files
#from IPython.display import Image
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from tensorflow.keras.layers import Input, Dense
im = cv2.imread('foto.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Coches detectados: '+ str(label.count('car')))
print('Personas detectadas: '+ str(label.count('car')))