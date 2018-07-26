import tensorflow as tf
import keras.backend as K

tf.reverse
sess = tf.Session()
input = tf.constant([[[1, 1, 1], [2, 2, 2]],
                     [[3, 3, 3], [4, 4, 4]],
                     [[5, 5, 5], [6, 6, 6]]])
data = tf.slice(input, [1, 0, 0], [3, 2, 3])
print(sess.run(data))
