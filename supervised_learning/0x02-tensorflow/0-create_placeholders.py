#!/usr/bin/env python3

"""Create placeholders"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """Create placeholders"""
    x = tf.placeholder(dtype=tf.float32, shape=(None, nx))
    y = tf.placeholder(dtype=tf.float32, shape=(None, classes))

    return x, y
