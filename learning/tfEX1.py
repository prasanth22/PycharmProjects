import tensorflow as tf
a = tf.constant(5.0)
b = tf.constant(6.0)
c= a*b
sess = tf.Session()
file_Writer = tf.summary.FileWriter('C:\\Users\\Personal\\PycharmProjects\\learning\\graph',sess.graph)
print(sess.run(c))
sess.close()