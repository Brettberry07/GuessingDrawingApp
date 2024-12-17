from graph_globals import *



# Representations:
"""
    Network: [Input, Hidden, Hidden, Output]
    
    Input: [
        1. Get the pixel values of the image (28x28)           xxxxRepresented by a Input classxxx
        2. Flatten the image into a singular list                  Represented by a Layer class
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
    
    
         X  X
    X    X  X
    X    X  X   X
    X    X  X   X
    X    X  X 

"""

# Represents a singular layer in the network
class Layer:

        def __init__(self, neurons: list, weights: list, biases: list) -> None:
            self.neurons = neurons
            self.biases = biases  # Biases
            self.weights = weights  # Weights (how much this neuron weighs to the given task)

        @staticmethod
        def activation_function(x: float) -> float:
            return 1 / (1 + math.exp(-x))  # Sigmoid function
            # return math.tanh(x) # Hyperbolic tangent function
            # return x if x > 0 else 0.0  # ReLU function


        """
            Example calculation for a single neuron:
            output = activation_function(sum(weight * input) + bias)
            sigmoid(w1a1 + w2a2 + w3a3 + ... + wn2n + b)
            w = weights, a = inputs, b = bias
        """

        """
        Psuedo code:
            def calculate_neuron(self, bias)
                return activation_function(sum([self.weight[i] * self.neuron[i] for i in range(len(self.neurons))]) + bias)
            
            def calculate_layer(self):
                return [self.calculate_neuron(self.biases[i]) for i in range(len(self.neurons))]
        
        """

        # def calculate_neuron(self, index):
        #     # return self.activation_function(sum([self.weights[i] * self.neurons[i] for i in range(len(self.neurons))]) + bias)    return self.activation_function(sum([self.weights[i][j] * self.neurons[i] for i in range(len(self.neurons)) for j in range(len)]))
        #     total = []
        #     for i in range(len(self.weights)):
        #         for j in range(len(self.weights[i])):
        #             total.append(self.activation_function(self.weights[i][j] * self.neurons[index]))
        #     return sum(total) + self.biases[index]

        def calculate_neuron(self, prev_layer, neuron_index):
            """
            Calculate the output for a single neuron.
            :param prev_layer: The previous layer object (Layer)
            :param neuron_index: Index of the current neuron in the layer
            :return: Activated output for the neuron
            """
            weighted_sum = sum(
                self.weights[neuron_index][j] * prev_layer.neurons[j]
                for j in range(len(prev_layer.neurons))
            )
            return self.activation_function(weighted_sum + self.biases[neuron_index])


        def calculate_layer(self, prev_layer):
            """
            Calculate outputs for all neurons in the current layer.
            :param prev_layer: The previous layer object (Layer)
            :return: List of neuron outputs for the current layer
            """
            return [self.calculate_neuron(prev_layer, i) for i in range(len(self.neurons))]


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

    def __init__(self, layers: list[Layer]) -> None:
        self.input: Layer = layers[0]
        self.output: Layer = layers[-1]
        self.layers = layers  # The layers of the network (plan to have 1 input, 2 hidden, 1 output)

    @staticmethod
    def flatten(self, input_values: list[[float]]) -> list[[float]]:
        # Takes a multidimensional list and flattens it into a singular dimensional list
        return [value for sublist in input_values for value in sublist]

    def forward(self) -> None:
        print(f'input layer: {self.layers[0].neurons}')
        for i in range(1, len(self.layers)):  # Start at the first hidden layer
            self.layers[i].neurons = self.layers[i].calculate_layer(self.layers[i - 1])
            print(f'{i}th hidden layer: {self.layers[i].neurons}')

        print(f'output layer: {self.layers[-1].neurons}')
        print(self.output_data())

    def output_data(self):
        max_neruon = max(self.layers[-1].neurons)
        return f' the best guess is index: {self.layers[-1].neurons.index(max_neruon)}, with a value of: {max_neruon}'

    def back_propagation(self) -> None:
        pass

    def train(self) -> None:
        pass

    def test(self) -> None:
        pass

    def predict(self) -> None:
        pass



