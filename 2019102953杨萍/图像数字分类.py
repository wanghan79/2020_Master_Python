
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt
import pickle
tf.compat.v1.disable_eager_execution()

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_data", one_hot=True)


#  Parameters
learning_rate = 0.01
training_epochs = 50
batch_size  = 50
display_step = 1


# 为输入X和y定义placeholder
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
one = 100  # 第一层神经元节点数
two = 100  # 第二层神经元节点数

# 第一层定义权重w和b
W1 = tf.Variable(tf.truncated_normal([784, one], stddev=0.1))
b1 = tf.Variable(tf.zeros(one))
# 第二层定义权重w和b
W2 = tf.Variable(tf.truncated_normal([one, two], stddev=0.1))
b2 = tf.Variable(tf.zeros(two))
# 输出层定义权重w和b
W3= tf.Variable(tf.truncated_normal([two, 10], stddev=0.1))
b3= tf.Variable(tf.zeros(10))
# 计算结果
Y1 = tf.nn.relu(tf.matmul(x, W1) + b1)  # 使用Relu当作激活函数
Y2 = tf.nn.relu(tf.matmul(Y1, W2) + b2)  # 使用Relu当作激活函数

#定义模型结构
pre = tf.nn.softmax(tf.matmul(Y2, W3) + b3)  # 输出层分类应用使用softmax当作激活函数
# 损失函数使用交叉熵
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pre), reduction_indices=1))
W3_grad, b3_grad=tf.gradients(cost,[W3,b3])
#更新参数
new_W3 = W3.assign(W3 - learning_rate * W3_grad)
new_b3 = b3 - learning_rate * b3_grad

W2_grad, b2_grad = tf.gradients(cost, [W2, b2])
new_W2 = W2.assign(W2 - learning_rate * W2_grad)
new_b2 = b2 - learning_rate * b2_grad

W1_grad, b1_grad = tf.gradients(cost, [W1, b1])
new_W1 = W1.assign(W1 - learning_rate * W1_grad)
new_b1 = b1- learning_rate * b1_grad
# 定义准确率
init = tf.global_variables_initializer()
accuracy_mat = tf.equal(tf.argmax(y, 1), tf.argmax(pre, 1))  # 准确率
accuracy_ret = tf.reduce_sum(tf.cast(accuracy_mat, dtype=tf.float32))  # 类型转换

loss_vec= []
test_loss = []
with tf.Session() as sess:
    sess.run(init)
    #训练模型
    for epoch in range(training_epochs):#trainging_epochs=50
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples / batch_size)  # 随机抽取样本，55000/50=110
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            w1, b1, w2, b2, w3, b3, c ,accuracy= sess.run([new_W1, new_b2, new_W2, new_b2, new_W3, new_b3, cost,accuracy_ret],
                                                 feed_dict={x: batch_xs, y: batch_ys})
            avg_cost += c / total_batch
            f = open("multiclass_parameters.txt", "wb")
            pickle.dump(w3, f)
            pickle.dump(b3, f)
            f.close()
        if (epoch + 1) % display_step == 0:
            #print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(avg_cost))
            temp_loss = sess.run(cost, feed_dict={x: batch_xs, y: batch_ys})
            loss_vec.append(temp_loss)
            test_temp_loss= sess.run(cost,feed_dict={x:mnist.test.images,y:mnist.test.labels})
            test_loss.append(test_temp_loss)
    #评估模型
    accuracy=tf.reduce_mean(tf.cast(tf.equal(tf.argmax(pre,1),tf.argmax(y,1)),tf.float32))
    print('test accuracy',accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
    prediction_result = sess.run(tf.argmax(pre, 1), feed_dict={x: mnist.test.images})
    label = sess.run(tf.argmax(mnist.test.labels, 1))
    # 定义 loss 曲线
def plt_plot_loss_images():
    plt.plot(loss_vec, 'k-', label='Train Loss')
    plt.plot(test_loss, 'r--', label='Test Loss')
    plt.title('Loss per Generation')
    plt.legend(loc='upper right')
    plt.xlabel('Generation')
    plt.ylabel('Loss')
    plt.show()
def worry():
    m=len(label)
    sum0=0
    error0=0
    sum1=0
    error1=0
    sum2=0
    error2=0
    sum3=0
    error3=0
    sum4=0
    error4=0
    sum5=0
    error5=0
    sum6=0
    error6=0
    sum7=0
    error7=0
    sum8=0
    error8=0
    sum9=0
    error9=0
    for i in range(m):
        if label[i]==0:
            sum0=sum0+1
            if prediction_result[i]!=0:
                error0=error0+1
        elif label[i]==1:
            sum1=sum1+1
            if prediction_result[i]!=1:
                error1=error1+1
        elif label[i]==2:
            sum2=sum2+1
            if prediction_result[i]!=2:
                error2=error2+1
        elif label[i]==3:
            sum3=sum3+1
            if prediction_result[i]!=3:
                error3=error3+1
        elif label[i]==4:
            sum4=sum4+1
            if prediction_result[i]!=4:
                error4=error4+1
        elif label[i]==5:
            sum5=sum5+1
            if prediction_result[i]!=5:
                error5=error5+1
        elif label[i]==6:
            sum6=sum6+1
            if prediction_result[i]!=6:
                error6=error6+1
        elif label[i]==7:
            sum7=sum7+1
            if prediction_result[i]!=7:
                error7=error7+1
        elif label[i]==8:
            sum8=sum8+1
            if prediction_result[i]!=8:
                error8=error8+1
        elif label[i]==9:
            sum9=sum9+1
            if prediction_result[i]!=9:
                error9=error9+1

    print("数字0分类错误率",error0/sum0)
    print("数字1分类错误率",error1/sum1)
    print("数字2分类错误率",error2/sum2)
    print("数字3分类错误率",error3/sum3)
    print("数字4分类错误率",error4/sum4)
    print("数字5分类错误率",error5/sum5)
    print("数字6分类错误率",error6/sum6)
    print("数字7分类错误率",error7/sum7)
    print("数字8分类错误率",error8/sum8)
    print("数字9分类错误率",error9/sum9)
#显示曲线
plt_plot_loss_images()
worry()


