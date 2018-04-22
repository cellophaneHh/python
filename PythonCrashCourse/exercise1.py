import tensorflow as tf
#构建计算图，计算图只搭建神经网络计算过程，不计算
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])

result = a + b
print result

