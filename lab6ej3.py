import numpy as np
from scipy import linalg
from lab6ej1 import *

def sollu(A,b):
    P,L,U = linalg.lu(A)
    return soltrsup(U,soltrinf(L,P.T @ b))
