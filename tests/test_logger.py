import sys
import os
# Get the current directory (where your_script.py resides)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from src import *
import random, logging
from sqlalchemy import text




logger = logging.getLogger('metric.query')


print(type(logger))

from src.db.evaluation import *

from src.common.test import *