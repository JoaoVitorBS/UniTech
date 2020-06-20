import os
from unitech.configs import *
import warnings


warnings.filterwarnings(
    'ignore', r"DateTimeField .* received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields',
)

