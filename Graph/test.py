from graph_globals import *
from classification_network import Layer, Network

layer1 = Layer([0, 0, 0], [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], [0.1, 0.2, 0.3])
layer2 = Layer([0, 0, 0], [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], [0.1, 0.2, 0.3])
output = Layer([0.0, 0.0], [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], [0.1, 0.2, 0.3])
input_layer = Layer([0.1, 0.2, 0.3], [[0.1, 0.2, 0.3],[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]], [0.1, 0.2, 0.3])

network = Network([input_layer, layer1, layer2, output])
network.forward()