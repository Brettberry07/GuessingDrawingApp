# importing pytorch and numpy
import torch
import numpy as np

# importing pytorch libraries
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# importing image processing libraries
from PIL import Image



# creating the neural network
# class Network:
#     def __init__(self):
#         pass

# Testing to make sure everything works
x = torch.rand(5, 3)
print(x)

