#!/usr/bin/env python3

"""Create placeholders"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """Create placeholders"""
    if type(nx) is not int or nx < 1:
        return None
    if type(classes) is not int or classes < 1:
        return None

    x = tf.placeholder(dtype=tf.float32, shape=(None, nx))
    y = tf.placeholder(dtype=tf.float32, shape=(None, classes))

    return x, y
