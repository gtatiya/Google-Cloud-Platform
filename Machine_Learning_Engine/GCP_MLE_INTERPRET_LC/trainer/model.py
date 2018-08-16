"""Define a custom model"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import multiprocessing

import six
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.estimators.model_fn import ModeKeys as Modes

from sklearn.model_selection import ShuffleSplit

# def read_and_decode(filename_queue):
#   reader = tf.TFRecordReader()
#   _, serialized_example = reader.read(filename_queue)

#   features = tf.parse_single_example(
#       serialized_example,
#       features={
#           'image_raw': tf.FixedLenFeature([], tf.string),
#           'label': tf.FixedLenFeature([], tf.int64),
#       })

#   image = tf.decode_raw(features['image_raw'], tf.uint8)
#   image.set_shape([784])
#   image = tf.cast(image, tf.float32) * (1. / 255)
#   label = tf.cast(features['label'], tf.int32)

#   return image, label


# def input_fn(filename, batch_size=100):
#   filename_queue = tf.train.string_input_producer([filename])

#   image, label = read_and_decode(filename_queue)
#   images, labels = tf.train.batch(
#       [image, label], batch_size=batch_size,
#       capacity=1000 + 3 * batch_size)

#   return {'inputs': images}, labels

def read_dadaset(db_file_name):
  bin_file = open(db_file_name, "rb")

  features = pickle.load(bin_file)
  bi_lables = pickle.load(bin_file)

  bin_file.close()

  y_lables = bi_lables
  ss = ShuffleSplit(n_splits=1, test_size=0.25, random_state=0)

  for train_index, test_index in ss.split(features):
      print("TRAIN:", len(train_index), "TEST:", len(test_index))
      X_train, X_test = features[train_index], features[test_index]
      y_train, y_test = y_lables[train_index], y_lables[test_index]

  return X_train, y_train, X_test, y_test

def train_input_fn(filename, batch_size=100):
  X_train, y_train, X_test, y_test = read_dadaset(filename)

  """An input function for training"""
  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

  # Shuffle, repeat, and batch the examples.
  dataset = dataset.shuffle(1000).repeat().batch(batch_size)

  # Return the dataset.
  return dataset


def eval_input_fn(filename, batch_size=100):
  X_train, y_train, X_test, y_test = read_dadaset(filename)
  """An input function for evaluation or prediction"""
  #features=dict(features)
  # if labels is None:
  #     # No labels, use only features.
  #     inputs = features
  # else:
  #     inputs = (features, labels)

  # Convert the inputs to a Dataset.
  dataset = tf.data.Dataset.from_tensor_slices(X_test)

  # Batch the examples
  assert batch_size is not None, "batch_size must not be None"
  dataset = dataset.batch(batch_size)

  # Return the dataset.
  return dataset


# def my_model(features, labels, mode):
#   # Input Layer
#   input_layer = tf.reshape(features['inputs'], [-1, 28, 28, 1])

#   # Convolutional Layer #1
#   conv1 = tf.layers.conv2d(
#       inputs=input_layer,
#       filters=32,
#       kernel_size=[5, 5],
#       padding='same',
#       activation=tf.nn.relu)

#   # Pooling Layer #1
#   pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

#   # Convolutional Layer #2 and Pooling Layer #2
#   conv2 = tf.layers.conv2d(
#       inputs=pool1,
#       filters=64,
#       kernel_size=[5, 5],
#       padding='same',
#       activation=tf.nn.relu)
#   pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

#   # Dense Layer
#   pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
#   dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
#   dropout = tf.layers.dropout(
#       inputs=dense, rate=0.4, training=(mode == Modes.TRAIN))

#   # Logits Layer
#   logits = tf.layers.dense(inputs=dropout, units=10)

#   # Define operations
#   if mode in (Modes.INFER, Modes.EVAL):
#     predicted_indices = tf.argmax(input=logits, axis=1)
#     probabilities = tf.nn.softmax(logits, name='softmax_tensor')

#   if mode in (Modes.TRAIN, Modes.EVAL):
#     global_step = tf.train.get_or_create_global_step()
#     label_indices = tf.cast(labels, tf.int32)
#     loss = tf.losses.softmax_cross_entropy(
#         onehot_labels=tf.one_hot(label_indices, depth=10), logits=logits)
#     tf.summary.scalar('OptimizeLoss', loss)

#   if mode == Modes.INFER:
#     predictions = {
#         'classes': predicted_indices,
#         'probabilities': probabilities
#     }
#     export_outputs = {
#         'prediction': tf.estimator.export.PredictOutput(predictions)
#     }
#     return tf.estimator.EstimatorSpec(
#         mode, predictions=predictions, export_outputs=export_outputs)

#   if mode == Modes.TRAIN:
#     optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
#     train_op = optimizer.minimize(loss, global_step=global_step)
#     return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

#   if mode == Modes.EVAL:
#     eval_metric_ops = {
#         'accuracy': tf.metrics.accuracy(label_indices, predicted_indices)
#     }
#     return tf.estimator.EstimatorSpec(
#         mode, loss=loss, eval_metric_ops=eval_metric_ops)

def my_model(features, labels, mode, params):
  print(features, labels, mode, params)
    
  net = tf.layers.dense(inputs=features, units=1024, activation=tf.nn.relu)
  print(net)
  net = tf.layers.dense(inputs=net, units=512, activation=tf.nn.relu)
  print(net)
  net = tf.layers.dense(inputs=net, units=256, activation=tf.nn.relu)
  print(net)
  net = tf.layers.dense(inputs=net, units=128, activation=tf.nn.relu)
  print(net)
  logits = tf.layers.dense(net, 2, name='logits')
  print("logits: ", logits)

  # Compute predictions.
  predicted_classes = tf.argmax(logits, 1)
  if mode == tf.estimator.ModeKeys.PREDICT:
      predictions = {
          'class_ids': predicted_classes[:, tf.newaxis],
          'probabilities': tf.nn.softmax(logits),
          'logits': logits,
      }
      return tf.estimator.EstimatorSpec(mode, predictions=predictions)
  
  
  # Compute loss.
  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=labels))

  # Compute evaluation metrics.
  labels_new = tf.argmax(labels, 1)
  accuracy = tf.metrics.accuracy(labels=labels_new,
                                 predictions=predicted_classes,
                                 name='acc_op')
  
  metrics = {'accuracy': accuracy}
  tf.summary.scalar('accuracy', accuracy[1])
  
  if mode == tf.estimator.ModeKeys.EVAL:
      print(mode, loss, metrics)
      return tf.estimator.EstimatorSpec(mode, loss=loss, eval_metric_ops=metrics)

  # Create training op.
  assert mode == tf.estimator.ModeKeys.TRAIN

  optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
  
  train_op = optimizer.minimize(loss, global_step=tf.train.get_global_step())

  return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)


def build_estimator(model_dir):
  return tf.estimator.Estimator(
      model_fn=my_model,
      model_dir=model_dir)


# def serving_input_fn():
#   inputs = {'inputs': tf.placeholder(tf.float32, [None, 784])}
#   return tf.estimator.export.ServingInputReceiver(inputs, inputs)
