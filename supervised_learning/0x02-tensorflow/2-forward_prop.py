#!/usr/bin/env python3

"""Forward propagation in TensorFlow"""
import tensorflow as tf


def forward_prop(x, layer_sizes=[], activations=[]):
    """Forward propagation
        - x is the placeholder for the input data
        - layer_sizes is a list containing the number of
         nodes in each layer of the network
        - activations is a list containing the activation
         functions for each layer of the network
        Returns: the prediction of the network in tensor form
    """

    create_layer = __import__('1-create_layer').create_layer
    prev = x
    for i in range(len(layer_sizes)):
        layer_output = create_layer(prev, layer_sizes[i], activations[i])

    return layer_output
