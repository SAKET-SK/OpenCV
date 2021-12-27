import cv2 
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


def count(x):
    im = cv2.imread(x)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    return str(label.count('car')), str(label.count('person')), str(label.count('motorcycle')), str(label.count('truck'))


