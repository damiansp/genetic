class Network:
    def __init__(self, X, y, n_params=2):
        self.X = X
        self.y = y
        self.n_params = n_params
        self.network = self._init_nodes() # Network adjacency matrix

    def _init_nodes(self):
        pass

    def add_node(self):
        pass

    def remove_node(self):
        pass

    def add_param(self):
        pass

    def remove_param(self):
        pass

    
        


class Node:
    def __init__(self, name, activation=None):
        self.name = name
        self.activation = activation
        self.bias = 0
        self.inputs = None
        self.weights = None
        
    def add_input(self):
        pass

    def remove_input(self):
        pass

    def adjust_weights(self):
