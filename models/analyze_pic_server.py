# import analyze
from analyze import check_blob_in_direct_path
import os
import sys
sys.path.insert(0, os.getcwd())
from get_images_from_pi import get_image, get_image_x_times

get_image()
check_blob_in_direct_path(os.getcwd() + "/images/greg.jpg")