import tensorflow as tf
import numpy as np

def gettingStarted():
    node1 = tf.constant(3.0, dtype=tf.float32)
    node2 = tf.constant(4.0) # also tf.float32 implicitly
    print(node1, node2)

    sess = tf.Session()
    print(sess.run([node1, node2]))

    node3 = tf.add(node1,node2)
    print(node3)
    print(sess.run([node3]))

    #placeholder
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a+b
    print("\nplaceholder\n",sess.run(adder_node, {a:3, b:4.5}))
    print(sess.run(adder_node, {a:[1,3], b:[2,4]}))

    add_and_triple = adder_node * 3.
    print(sess.run(add_and_triple, {a: 3, b: 4.5}))

    W = tf.Variable([.3], dtype=tf.float32)
    b = tf.Variable([-.3], dtype=tf.float32)
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b    #W, b - defined, x - placeholder
    # To initialize all the variables, Constants are initialized when you call tf.constant
    init = tf.global_variables_initializer()
    sess.run(init)
    print("\nlinear_model\n",sess.run(linear_model, {x: [1, 2, 3, 4]}))

    # loss function
    y = tf.placeholder(tf.float32)
    squared_deltas = tf.square(linear_model - y)
    loss = tf.reduce_sum(squared_deltas)
    print("\nloss:\n",sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

    fixW = tf.assign(W, [-1.])
    fixb = tf.assign(b, [1.])
    sess.run([fixW, fixb])
    print("\nNew\n",sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

    #Gradient Descent
    optimizer= tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    sess.run(init) # reset values to incorrect defaults.
    for i in range(1000):
      sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

    print(sess.run([W, b]))

def linearRegression():
    # Model parameters
    W = tf.Variable([.3], dtype=tf.float32)
    b = tf.Variable([-.3], dtype=tf.float32)
    # Model input and output
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b
    y = tf.placeholder(tf.float32)

    # loss
    loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares
    # optimizer
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    # training data
    x_train = [1, 2, 3, 4]
    y_train = [0, 1, 2, 3]
    # training loop
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)  # reset values to wrong
    for i in range(1000):
        sess.run(train, {x: x_train, y: y_train})

    # evaluate training accuracy
    curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
    print("\n\nLinear Regression: \nW: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))
    input=10
    print("Test:",curr_W*input+curr_b)

def estimator():
    # Declare list of features. We only have one numeric feature. There are many
    # other types of columns that are more complicated and useful.
    feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

    # An estimator is the front end to invoke training (fitting) and evaluation
    # (inference). There are many predefined types like linear regression,
    # linear classification, and many neural network classifiers and regressors.
    # The following code provides an estimator that does linear regression.
    estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

    # TensorFlow provides many helper methods to read and set up data sets.
    # Here we use two data sets: one for training and one for evaluation
    # We have to tell the function how many batches
    # of data (num_epochs) we want and how big each batch should be.
    x_train = np.array([1., 2., 3., 4.])
    y_train = np.array([0., -1., -2., -3.])
    x_eval = np.array([2., 5., 8., 1.])
    y_eval = np.array([-1.01, -4.1, -7, 0.])
    input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)

    # We can invoke 1000 training steps by invoking the  method and passing the
    # training data set.
    estimator.train(input_fn=input_fn, steps=1000)

    # Here we evaluate how well our model did.
    train_metrics = estimator.evaluate(input_fn=train_input_fn)
    eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
    print("train metrics: %r" % train_metrics)
    print("eval metrics: %r" % eval_metrics)


def customModel():
    estimator = tf.estimator.Estimator(model_fn=model_fn) # model_fn declared below
    # define our data sets
    x_train = np.array([1., 2., 3., 4.])
    y_train = np.array([0., -1., -2., -3.])
    x_eval = np.array([2., 5., 8., 1.])
    y_eval = np.array([-1.01, -4.1, -7, 0.])
    input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)

    # train
    estimator.train(input_fn=input_fn, steps=1000)
    # Here we evaluate how well our model did.
    train_metrics = estimator.evaluate(input_fn=train_input_fn)
    eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
    print("\nCustom Model\ntrain metrics: %r" % train_metrics)
    print("eval metrics: %r" % eval_metrics)

# Declare list of features, we only have one real-valued feature
def model_fn(features, labels, mode):
  # Build a linear model and predict values
  W = tf.get_variable("W", [1], dtype=tf.float64)
  b = tf.get_variable("b", [1], dtype=tf.float64)
  y = W * features['x'] + b
  # Loss sub-graph
  loss = tf.reduce_sum(tf.square(y - labels))
  # Training sub-graph
  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(0.01)
  train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
  # EstimatorSpec connects subgraphs we built to the
  # appropriate functionality.
  return tf.estimator.EstimatorSpec(
      mode=mode,
      predictions=y,
      loss=loss,
      train_op=train)


gettingStarted()
linearRegression()
estimator()
customModel()