#!/usr/bin/env python3

"""Builds, trains and saves a NN classifier in TensorFlow"""
import tensorflow as tf


def train(X_train, Y_train, X_valid, Y_valid,
          layer_sizes, activations, alpha,
          iterations, save_path="/tmp/model.ckpt"):
    """ Builds, trains and saves a NN classifier
            - X_train is a numpy.ndarray containing the training input data
            - Y_train is a numpy.ndarray containing the training labels
            - X_valid is a numpy.ndarray containing the validation input data
            - Y_valid is a numpy.ndarray containing the validation labels
            - layer_sizes is a list containing the number of
             nodes in each layer of the network
            - activations is a list containing the activation functions
             for each layer of the network
            - alpha is the learning rate
            - iterations is the number of iterations to train over
            - save_path designates where to save the model
    """
    calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
    calculate_loss = __import__('4-calculate_loss').calculate_loss
    create_placeholders = \
        __import__('0-create_placeholders').create_placeholders
    create_train_op = __import__('5-create_train_op').create_train_op
    forward_prop = __import__('2-forward_prop').forward_prop

    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layer_sizes, activations)

    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)

    accuracy = calculate_accuracy(y, y_pred)
    loss = calculate_loss(y, y_pred)
    train_op = create_train_op(loss, alpha)

    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('train_op', train)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)

        for i in range(iterations + 1):

            accuracy_train = sess.run(accuracy,
                                      feed_dict={x: X_train, y: Y_train})
            loss_train = sess.run(loss,
                                  feed_dict={x: X_train, y: Y_train})

            accuracy_valid = sess.run(accuracy,
                                      feed_dict={x: X_valid, y: Y_valid})
            loss_valid = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})

            if i % 100 == 0 or i == iterations:
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(loss_train))
                print("\tTraining Accuracy: {}".format(accuracy_train))
                print("\tValidation Cost: {}".format(loss_valid))
                print("\tValidation Accuracy: {}".format(accuracy_valid))

            if i < iterations:
                sess.run(train_op, feed_dict={x: X_train, y: Y_train})

        return saver.save(sess, save_path)
