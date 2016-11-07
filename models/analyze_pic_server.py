import analyze
from analyze import check_blob_in_direct_path
import os

check_blob_in_direct_path(os.getcwd() + "/images/two.jpg")