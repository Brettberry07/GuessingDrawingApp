from graph_globals import *



# Representatons:
"""
    Network: [Input, Hidden, Hidden, Output]
    
    Input: [
        1. Get the pixel values of the image (28x28)           Represented by a Input class
    [
    
    Hidden: [
        1. Get the values from the previous layer
        2. Multiply the values by the weights
        3. Add the biases                                       Represented by a Layer class
        4. Apply the activation function (sigmoid)
        5. Pass on to next layer
    ]
    
    Output: [
        1. Get the values from the previous layer
        2. Multiply the values by the weights
        3. Add the biases                                     Represented by a Layer class
        4. Apply the activation function (sigmoid)
        5. Return the output
    ]

"""

# Represents a singular layer in the network
class Layer:

        def __init__(self, neurons: list[float], weights: list[float], biases: list[float]) -> None:
            self.neurons = neurons
            self.biases = biases  # Biases
            self.weights = weights  # Weights (how much this neuron weighs to the given task)

        @staticmethod
        def activation_function(self, x: float) -> float:
            return 1 / (1 + math.exp(-x))

        """
            Example calculation for a single neuron:
            output = activation_function(sum(weight * input) + bias)
            sigmoid(w1a1 + w2a2 + w3a3 + ... + wn2n + b)
            w = weights, a = inputs, b = bias
        """

        # Calculating the output for a singular neuron
        def calculate_output(self, neuron: list[float], weights: list[float], bias: float) -> float:
            return self.activation_function(sum([neuron[i] * weights[i] for i in range(len(neuron))]) + bias)

        # Calculating the output for a layer
        def calculate_layer(self, inputs: list[float]) -> list[float]:
            return [Layer.calculate_output(inputs, self.weights[i], self.biases[i]) for i, neuron in enumerate(self.neurons)]


# Represents the network in its entirety
class Network:

    """
        Classification network , right now we're just doing points on a graph,
        but we can extend this to any classification problem later on
        (probably something like, is this a dog? or is this a t-shirt?).

        Eventually I will optimize this to use numpy arrays for faster calculations (maybe gpu acceleration),
        but for now I'm just going to use lists for simplicity.

        In the future when using the optimized version, I should be able to use these ideas
        to make a digit recognition network.
    """

    def __init__(self, network_input: [float], layers: list[Layer]) -> None:
        self.input: [float] = network_input
        self.output: [float] = []
        self.layers = [network_input] + layers + [self.output]  # The layers of the network (plan to have 1 input, 2 hidden, 1 output)

    @staticmethod
    def flatten(self, input_values: list[[float]]) -> list[[float]]:
        # Takes a multidimensional list and flattens it into a singular dimensional list
        return [value for sublist in input_values for value in sublist]

    def forward_propagation(self) -> None:
        pass

    def back_propagation(self) -> None:
        pass

    def train(self) -> None:
        pass

    def test(self) -> None:
        pass

    def predict(self) -> None:
        pass



