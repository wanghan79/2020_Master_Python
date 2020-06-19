import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
import numpy as np
import PIL
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
#加载数据
def load_data(img,label):
    """
    :param img: 存放训练集/测试集图片的位置
    :param label: 存放训练集/测试集标签的位置
    :return:x:转换为numpy格式的图片
    y:图片的标签
    """
    file=open(label,'r') #读取标签文件的数据
    labels=file.readlines()
    file.close()
    x,y=[],[] #将图片和标签分别存放在x和y中
    for label in labels: #标签文件中每行包括图片名称加标签，以空格分开
        label=label.split() #形成列表，第一个元素为图片名称，第二个元素为对应标签
        img_path=img+label[0]
        image=PIL.Image.open(img_path) #根据图片的地址读出图片来
        image=np.array(image.convert('L'))/255 #将图片转换为np.array格式，并进行归一化处理
        x.append(image)
        y.append(label[1])
    return x,y

#管理数据
def manage_data(x_train,y_train,x_test,y_test):
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    x_test=np.array(x_test)
    y_test=np.array(y_test)
    y_train=y_train.astype(np.int64) #将标签转换为64为整数
    y_test=y_test.astype(np.int64) #将标签转换为64为整数

    x_train_reshape=np.reshape(x_train,(len(x_train),-1))
    x_test_reshape=np.reshape(x_test,(len(x_test),-1))
    x_train=np.reshape(x_train_reshape,(len(x_train_reshape),784))
    x_test=np.reshape(x_test_reshape,(len(x_test_reshape),784))
    x_train=tf.cast(x_train,tf.float32)
    x_test=tf.cast(x_test,tf.float32)
    return x_train,y_train,x_test,y_test

#初始化参数
def initializer_parameter():
    """
    :return:params:包含参数w和b的字典
    """
    w1=tf.Variable(tf.random.truncated_normal([784, 100], stddev=0.1))
    b1=tf.Variable(tf.random.truncated_normal([100], stddev=0.1))
    w2=tf.Variable(tf.random.truncated_normal([100, 100], stddev=0.1))
    b2=tf.Variable(tf.random.truncated_normal([100], stddev=0.1))
    w3=tf.Variable(tf.random.truncated_normal([100, 10], stddev=0.1))
    b3=tf.Variable(tf.random.truncated_normal([10], stddev=0.1))
    params={
        "w1":w1,
        "b1":b1,
        "w2":w2,
        "b2":b2,
        "w3": w3,
        "b3": b3
    }
    return params

#前向传播
def forward_propagation(x,w1,b1,w2,b2,w3,b3):
    """
    :param x:
    :param w1:
    :param b1:
    :param w2:
    :param b2:
    :return: y
    """
    z1=tf.matmul(x,w1)+b1
    y1=tf.nn.relu(z1)
    z2=tf.matmul(y1,w2)+b2
    y2=tf.nn.relu(z2)
    z3=tf.matmul(y2,w3)+b3
    y=tf.nn.softmax(z3)
    return y

#计算成本
def compute_cost(y_train_test,y):
    """
    :param y: 前向传播的结果（预测值）
    :param y_train_test: 转换为one-hot格式的训练集/测试集标签
    :return: loss：损失值
    """
    loss=tf.reduce_mean(tf.losses.categorical_crossentropy(y_train_test,y))
    return loss

#构建模型
def model(x_train,y_train,x_test,y_test,learning_rate=0.01,epochs=100,regularizer=0.02):
    """
    :param x_train:
    :param y_train:
    :param x_test:
    :param y_test:
    :param learning_rate: 学习率
    :param epochs: 迭代次数
    :param regularizer: 正则化因子
    :return:
    """
    loss_sum=0
    train_cost_plot=[] #存放每轮训练的损失
    parameters=initializer_parameter() #初始化参数，得到包含w和b的列表
    w1=parameters["w1"]
    b1=parameters["b1"]
    w2=parameters["w2"]
    b2=parameters["b2"]
    w3=parameters["w3"]
    b3=parameters["b3"]
    batch_size=50 #批次的大小
    accuracy_test = [] #测试集正确率的列表
    error_test=[] #测试集误差
    error1_test,error2_test,error3_test,error4_test,error5_test=[],[],[],[],[] #10个数字的错误率
    error6_test,error7_test,error8_test,error9_test,error10_test=[],[],[],[],[]
    train_batch=tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(batch_size) #将数据集切分传入
    test_batch = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batch_size)
    for epoch in range(epochs):
        for i,(x_train,y_train) in enumerate(train_batch):
            with tf.GradientTape() as tape:
                y=forward_propagation(x_train,w1,b1,w2,b2,w3,b3) #前向传播
                y_one_hot=tf.one_hot(y_train,depth=10) #将训练集转换为ont—hot格式
                loss=compute_cost(y_one_hot,y) #计算损失
                loss_sum=loss_sum+loss.numpy() #转换为numpy格式，计算每个轮次的总损失
            grads=tape.gradient(loss,[w1,b1,w2,b2,w3,b3]) #计算梯度
            w1.assign_sub(learning_rate*grads[0]) #w进行更新
            b1.assign_sub(learning_rate * grads[1])#b进行更新
            w2.assign_sub(learning_rate*grads[2]) #w进行更新
            b2.assign_sub(learning_rate*grads[3]) #b进行更新
            w3.assign_sub(learning_rate * grads[4])  # w进行更新
            b3.assign_sub(learning_rate * grads[5])  # b进行更新
        print("第{}次迭代，损失为:{}".format(epoch,loss_sum/500))
        train_cost_plot.append(loss_sum/500)
        loss_sum=0

        #使用训练后的参数w和b进行测试
        accuary_sum=0
        sample_sum=0
        number1_error,number2_error,number3_error,number4_error,number5_error=0,0,0,0,0
        number6_error,number7_error,number8_error,number9_error,number10_error=0,0,0,0,0
        for x_test,y_test in test_batch:
            y=forward_propagation(x_test,w1,b1,w2,b2,w3,b3) #前向传播后的结果
            prediction=tf.argmax(y,axis=1) #列中找出最大的即为预测值
            prediction=tf.cast(prediction,dtype=y_test.dtype) #类型转换
            correct=tf.cast(tf.equal(prediction,y_test),dtype=tf.int32) #进行类型转换
            compare=tf.where(tf.equal(correct,0),prediction,-1)
            for i in range(compare.shape[0]):
                if compare[i]==1:
                    number1_error+=1
                elif compare[i] == 2:
                    number2_error += 1
                elif compare[i]==3:
                    number3_error+=1
                elif compare[i]==4:
                    number4_error+=1
                elif compare[i]==5:
                    number5_error+=1
                elif compare[i] == 6:
                    number6_error += 1
                elif compare[i] == 7:
                    number7_error += 1
                elif compare[i] == 8:
                    number8_error += 1
                elif compare[i] == 9:
                    number9_error += 1
                elif compare[i] == 10:
                    number10_error += 1
            correct=tf.reduce_sum(correct) #将每个批次的正确数加起来
            accuary_sum=accuary_sum+int(correct)
            sample_sum+=x_test.shape[0]
        acc=accuary_sum/sample_sum #计算正确率
        accuracy_test.append(acc)
        error=(sample_sum-accuary_sum)/sample_sum #总的误差率
        error_test.append(error)
        error_1,error_2=number1_error/sample_sum,number2_error/sample_sum
        error_3,error_4=number3_error/sample_sum,number4_error/sample_sum
        error_5,error_6=number5_error/sample_sum,number6_error/sample_sum
        error_7,error_8=number7_error/sample_sum,number8_error/sample_sum
        error_9,error_10=number9_error/sample_sum,number10_error/sample_sum
        error1_test.append(error_1)
        error2_test.append(error_2)
        error3_test.append(error_3)
        error4_test.append(error_4)
        error5_test.append(error_5)
        error6_test.append(error_6)
        error7_test.append(error_7)
        error8_test.append(error_8)
        error9_test.append(error_9)
        error10_test.append(error_10)
    return (w1,b1,w2,b2,w3,b3,train_cost_plot,accuracy_test,error_test,
error1_test,error2_test,error3_test,error4_test,error5_test,
error6_test,error7_test,error8_test,error9_test,error10_test)

#绘制损失的曲线图
def loss_curve_plot(train_cost_plot):
    #绘制loss的曲线
    plt.title("Loss")
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.plot(train_cost_plot,label="$Loss$")
    plt.legend()
    plt.show()
#绘制准确率曲线
def accuracy_plot(accuracy_test):
    plt.title("accruracy")
    plt.xlabel("iterations")
    plt.ylabel("accuracy")
    plt.plot(accuracy_test,label="$Accuracy$")
    plt.legend()
    plt.show()
#绘制错误率曲线
def error_plot(error_test):
    plt.title("error")
    plt.xlabel('iterations')
    plt.ylabel('error')
    plt.plot(error_test,label="$Error$")
    plt.legend()
    plt.show()
#绘制每个数字的错误率
def number_error_plot(error1_test,error2_test,error3_test,error4_test,error5_test,error6_test,error7_test,error8_test,error9_test,error10_test):
    plt.title("number error")
    plt.plot(error1_test,label='number1')
    plt.plot(error2_test,label='number2')
    plt.plot(error3_test,label='number3')
    plt.plot(error4_test,label='number4')
    plt.plot(error5_test,label='number5')
    plt.plot(error6_test,label='number6')
    plt.plot(error7_test,label='number7')
    plt.plot(error8_test,label='number8')
    plt.plot(error9_test,label='number9')
    plt.plot(error10_test,label='number10')
    plt.legend()
    plt.show()

if __name__=='__main__':
    #文件存储位置
    x_train = './DataSets/train_data/'
    y_train = './DataSets/train_data/train_label.txt'
    x_test = './DataSets/test_data/'
    y_test = './DataSets/test_data/test_label.txt'
    #加载数据
    x_train, y_train = load_data(x_train, y_train)
    x_test, y_test = load_data(x_test, y_test)
    #处理数据
    x_train, y_train, x_test, y_test = manage_data(x_train, y_train, x_test, y_test)
    #运行模型
    w1,b1,w2,b2,w3,b3,train_cost_plot, accuracy_test, error_test, error1_test, error2_test, error3_test, error4_test, error5_test,error6_test,error7_test,error8_test,error9_test,error10_test=model(x_train,y_train,x_test,y_test)
    #存储w和b
    parameters_path = './DataSets/parameters.txt'
    file=open(parameters_path,'w')
    file.write("parameter w："+"\n")
    for i in range(784):
        file.write(str(w1[i].numpy())+'\n')
    for i in range(100):
        file.write(str(w2[i].numpy())+'\n')
    for i in range(100):
        file.write(str(w3[i].numpy())+'\n')
    file.write("parameter b："+"\n")
    file.write(str(b1.numpy()) + '\n')
    file.write(str(b2.numpy()) + '\n')
    file.close()
    loss_curve_plot(train_cost_plot)
    accuracy_plot(accuracy_test)
    error_plot(error_test)
    number_error_plot(error1_test, error2_test, error3_test, error4_test, error5_test,error6_test,error7_test,error8_test,error9_test,error10_test)


