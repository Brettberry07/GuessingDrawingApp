from graph_globals import *

class Network:

    """
        Classification network , right now we're just doing points on a graph,
        but we can extend this to any classification problem later on
        (probably something like, is this a dog?).
    """

    def __init__(self):
        self.input = []
        self.layers = []
        self.weights = []
        self.biases = []
        self.activations = []
        self.outputs = [0, 0]  # The higher one is our final prediction
        self.learning_rate = 0.01

    def add_layer(self, layer):
        self.layers.append(layer)

    def add_weights(self, weights):
        self.weights.append(weights)

    def add_biases(self, biases):
        self.biases.append(biases)

    def add_activations(self, activations):
        self.activations.append(activations)