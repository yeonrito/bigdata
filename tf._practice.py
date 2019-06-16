import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

x_data = [1,2,3,4,5]
y_data = [3,5,7,9,11]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = W * X + b
cost = tf.reduce_mean(tf.square(hypothesis - Y)) 

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.004)

train_op = optimizer.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10000):
        _, cost_val = sess.run([train_op, cost], feed_dict={X: x_data, Y : y_data})
        if step % 10 == 0:
            print(step, cost_val, sess.run(W), sess.run(b))

    print("X:10, Y:", sess.run(hypothesis, feed_dict={X : 10.}))
    print("X:2.5, Y:", sess.run(hypothesis, feed_dict={X : 2.5}))