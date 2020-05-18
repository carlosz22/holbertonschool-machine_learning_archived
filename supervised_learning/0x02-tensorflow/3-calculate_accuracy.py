#!/usr/bin/env python3

"""Accuracy in TensorFlow"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """ Accuracy
        - y is a placeholder for the labels of the input data
        - y_pred is a tensor containing the network’s predictions
        Returns: a tensor containing the decimal accuracy of the prediction
    """
    y_decoded = tf.argmax(y, 1)
    y_pred_decoded = tf.argmax(y_pred, 1)

    equal = tf.equal(y_pred_decoded, y_decoded)

    accuracy = tf.reduce_mean(tf.cast(equal, tf.float32))
    return accuracy
