import os
import numpy as np
import sklearn
import sys

# check python version
assert sys.version_info >= (3, 5)

# check scikit-learn version
assert sklearn.__version__ >= "0.20"

# to make this notebook's output stable across runs
np.random.seed(42)

