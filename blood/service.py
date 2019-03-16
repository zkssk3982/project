import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#명시적으로 사용하지 않지만 반드시 임포트 선언을 해야함

class BloodService:
    def __init__(self, fname):
        self.fname = fname

    def create_raw_data(self):
        tf.set_random_seed(777)
        raw_data = np.genfromtxt(self.fname, skip_header=36)
        return raw_data

    @staticmethod
    def draw_chart(raw_data):

        xs = np.array(raw_data[:, 2], dtype=np.float32)
        ys = np.array(raw_data[:, 3], dtype=np.float32)
        zs = np.array(raw_data[:, 4], dtype=np.float32)

        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection = '3d')
        ax.scatter(xs, ys, zs)
        ax.set_xlabel('Weight')
        ax.set_ylabel('Age')
        ax.set_zlabel('Blood Fat')
        ax.view_init(15,15)

        plt.show()

    @staticmethod
    def make_session(raw_data):
        x_data = np.array(raw_data[: , 2:4], dtype=np.float32)
        y_data = np.array(raw_data[:, 4], dtype=np.float32)

        y_data = y_data.reshape((25,1))

        X = tf.placeholder(tf.float32, shape=[None, 2], name='x-input')
        Y = tf.placeholder(tf.float32, shape=[None, 2], name='y-input')

        W = tf.Variable(tf.random_normal([2, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')

        hypothesis = tf.matmul(X, Y)+ b

        cost = tf.reduce_mean(tf.square(hypothesis - Y))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)
        train = optimizer.minimize(cost)

        sess = tf.Session()
        sess.run(tf.global_variables_initializer())

        cost_history = []

        for step in range(2000):
            cost_val, hy_val, _= sess.run([
                cost,
                hypothesis,
                train
            ], feed_dict={X: x_data, Y: y_data})
        val = sess.run(hypothesis, feed_dict={X: [weight, age]})#70kg , 25세

        print("혈중 지방농도: {}".format(val))

        result = ''
        if val < 150:
            result = '정상'
        elif 150<=val < 200:
            result = '경계역 주성지방혈증'
        elif 200<=val <500:
            result = '고 중성지방혈증'
        elif 500<=val <1000:
            result = '초고 중성지방혈증'
        elif 1000<val:
            result = '췌장염 발병 가능성 고도화'
        return result




