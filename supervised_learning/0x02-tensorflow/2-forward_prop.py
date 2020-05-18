#!/usr/bin/env python3

"""Forward propagation in TensorFlow"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """Forward propagation
        - x is the placeholder for the input data
        - layer_sizes is a list containing the number of
         nodes in each layer of the network
        - activations is a list containing the activation
         functions for each layer of the network
        Returns: the prediction of the network in tensor form
    """

    layer_output = x
    for i in range(len(layer_sizes)):
        layer_output = create_layer(layer_output,
                                    layer_sizes[i],
                                    activations[i])

    return layer_output
