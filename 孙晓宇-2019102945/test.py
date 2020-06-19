import numpy as np
import matplotlib.pyplot as plt
import pickle
from keras.datasets import mnist
# from keras.activations import relu
class classification_two_hidden_layers():

    def __init__(self, learning_rate=0.01, input_dim=100, output_dim=10, hidden_num=[100, 100],
                 norm_initial_weight=1e-5, L2=0.1, epoch=200, lr_decay='decay'):

        self.learning_rate = learning_rate
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.params = {}
        self.hidden_num = hidden_num
        self.norm_initial_weight = norm_initial_weight
        self.L2 = L2
        self.epoch = epoch
        self.lr_decay = lr_decay

        self.loss = []
        self.acc = []
        self.test_acc = []

        self.init_weight_flag = False
        if self.init_weight_flag == False:
            self.init_weights()

    def init_weights(self):
        assert self.init_weight_flag == False
        self.params['W1'] = np.random.randn(self.input_dim, self.hidden_num[0]) * self.norm_initial_weight
        self.params['W2'] = np.random.randn(self.hidden_num[0], self.hidden_num[1]) * self.norm_initial_weight
        self.params['W3'] = np.random.randn(self.hidden_num[1], self.output_dim) * self.norm_initial_weight
        self.params['b1'] = np.zeros(self.hidden_num[0], )
        self.params['b2'] = np.zeros(self.hidden_num[1], )
        self.params['b3'] = np.zeros(self.output_dim, )
        self.init_weight_flag = True

    def loss_softmax(self, x, y):
        
        shifted_logits = x - np.max(x, axis=1, keepdims=True)
        Z = np.sum(np.exp(shifted_logits), axis=1, keepdims=True)
        log_probs = shifted_logits - np.log(Z)
        probs = np.exp(log_probs)
        N = x.shape[0]
        loss = -np.sum(log_probs[np.arange(N), y]) / N
        dx = probs.copy()
        dx[np.arange(N), y] -= 1
        dx /= N
        return loss, dx

    def train(self, input, y):

        for i in range(self.epoch):
            # 前向传播
            hidden1_ = np.dot(input, self.params['W1']) + self.params['b1']
            hidden1 = 1 / (np.exp(-1 * hidden1_) + 1)

            hidden2_ = np.dot(hidden1, self.params['W2']) + self.params['b2']
            hidden2 = 1 / (np.exp(-1 * hidden2_) + 1)

            output = np.dot(hidden2, self.params['W3']) + self.params['b3']

            # 计算损失
            loss, dout = self.loss_softmax(output, y)
            loss += 0.5 * self.L2 * (
                    np.sum(np.square(self.params['W3'])) + np.sum(np.square(self.params['W2'])) + np.sum(
                np.square(self.params['W1'])))

            self.loss.append(loss)

            y_pred = np.argmax(output, axis=1).reshape(1, -1)
            y_true = y.reshape(1, -1)
            sum_ = 0.0
            for c in range(y_pred.shape[1]):
                if y_pred[0, c] == y_true[0, c]:
                    sum_ = sum_ + 1
                    acc = 100.0 * sum_ / y_pred.shape[1]
                    self.acc.append(acc)

            if i % 10 == 0:
                print('Epochs {} -- Acc: [{:.3f}%], Loss: [{:.5f}]'.format(i, 100.0 * sum_ / y_pred.shape[1], loss))

            dW3 = np.dot(hidden2.T, dout)
            db3 = np.sum(dout, axis=0)
            dhidden2 = np.dot(dout, self.params['W3'].T) * (1 - hidden2) * hidden2

            dW2 = np.dot(hidden1.T, dhidden2)
            db2 = np.sum(dhidden2, axis=0)
            dhidden1 = np.dot(dhidden2, self.params['W2'].T) * (1 - hidden1) * hidden1

            dW1 = np.dot(input.T, dhidden1)  # 2*4 and 4*2 => 2*2
            db1 = np.sum(dhidden1, axis=0)  # 1 * 2

            # 正则化权重
            dW3 += self.params['W3'] * self.L2
            dW2 += self.params['W2'] * self.L2
            dW1 += self.params['W1'] * self.L2

            # 后向传播
            self.params['W3'] -= self.learning_rate * dW3
            self.params['b3'] -= self.learning_rate * db3
            self.params['W2'] -= self.learning_rate * dW2
            self.params['b2'] -= self.learning_rate * db2
            self.params['W1'] -= self.learning_rate * dW1
            self.params['b1'] -= self.learning_rate * db1

            # 保存权重
            filehandler = open("parameters.txt", "wb")
            pickle.dump(self.params, filehandler, protocol=2)
            filehandler.close()

            if self.lr_decay == 'decay':
                self.learning_rate = self.learning_rate * 0.999
            elif self.lr_decay == 'multi_step':
                if i < 500:
                    self.learning_rate = self.learning_rate
                elif i < 1000 and i >= 500:
                    self.learning_rate -= self.learning_rate * 0.6
                else:
                    self.learning_rate = self.learning_rate * 0.1

                if self.learning_rate < 0.1:
                    self.learning_rate = 0.1

            if i == self.epoch - 1:
                y_pred = np.argmax(output, axis=1).reshape(1, -1)
                y_true = y.reshape(1, -1)
                sum_ = 0.0
                for c in range(y_pred.shape[1]):
                    if y_pred[0, c] == y_true[0, c]:
                        sum_ = sum_ + 1
                print('Epochs {} -- Acc: [{:.3f}%], Loss: [{:.5f}]'.format(i, 100.0 * sum_ / y_pred.shape[1], loss))


    def test(self, input, y):
        # 计算每个数字的错分率
        def error_mean(y_pred, y_true):
            num0 = 0
            error0 = 0
            num1 = 0
            error1 = 0
            num2 = 0
            error2 = 0
            num3 = 0
            error3 = 0
            num4 = 0
            error4 = 0
            num5 = 0
            error5 = 0
            num6 = 0
            error6 = 0
            num7 = 0
            error7 = 0
            num8 = 0
            error8 = 0
            num9 = 0
            error9 = 0
            for c in range(y_pred.shape[1]):

                if y_true[0, c] == 0:
                    num0 = num0 + 1
                    if y_pred[0, c] != 0:
                        error0 = error0 + 1
                elif y_true[0, c] == 1:
                    num1 = num1 + 1
                    if y_pred[0, c] != 1:
                        error1 = error1 + 1
                elif y_true[0, c] == 2:
                    num2 = num2 + 1
                    if y_pred[0, c] != 2:
                        error2 = error2 + 1
                elif y_true[0, c] == 3:
                    num3 = num3 + 1
                    if y_pred[0, c] != 3:
                        error3 = error3 + 1
                elif y_true[0, c] == 4:
                    num4 = num4 + 1
                    if y_pred[0, c]  != 4:
                        error4 = error4 + 1
                elif y_true[0, c] == 5:
                    num5 = num5 + 1
                    if y_pred[0, c] != 5:
                        error5 = error5 + 1
                elif y_true[0, c] == 6:
                    num6 = num6 + 1
                    if y_pred[0, c] != 6:
                        error6 = error6 + 1
                elif y_true[0, c] == 7:
                    num7 = num7 + 1
                    if y_pred[0, c] != 7:
                        error7 = error7 + 1
                elif y_true[0, c] == 8:
                    num8 = num8 + 1
                    if y_pred[0, c] != 8:
                        error8 = error8 + 1
                elif y_true[0, c] == 9:
                    num9 = num9 + 1
                    if y_pred[0, c] != 9:
                        error9 = error9 + 1

            # print("---------",num0,num1,num2,num3,num4,num5,num6,num7,num8,num9)
            error0_rate = error0 / num0
            error1_rate = error1 / num1
            error2_rate = error2 / num2
            error3_rate = error3 / num3
            error4_rate = error4 / num4
            error5_rate = error5 / num5
            error6_rate = error6 / num6
            error7_rate = error7 / num7
            error8_rate = error8 / num8
            error9_rate = error9 / num9
            print("0错误率", error0_rate)
            print("1错误率", error1_rate)
            print("2错误率", error2_rate)
            print("3错误率", error3_rate)
            print("4错误率", error4_rate)
            print("5错误率", error5_rate)
            print("6错误率", error6_rate)
            print("7错误率", error7_rate)
            print("8错误率", error8_rate)
            print("9错误率", error9_rate)

        hidden1_ = np.dot(input, self.params['W1']) + self.params['b1']
        hidden1 = 1 / (np.exp(-1 * hidden1_) + 1)

        hidden2_ = np.dot(hidden1, self.params['W2']) + self.params['b2']
        hidden2 = 1 / (np.exp(-1 * hidden2_) + 1)

        output_ = np.dot(hidden2, self.params['W3']) + self.params['b3']
        output = 1 / (np.exp(-1 * output_) + 1)

        # 计算测试精度
        y_pred = np.argmax(output, axis=1).reshape(1, -1)
        y_true = y.reshape(1, -1)
        sum_ = 0.0
        error_mean(y_pred, y_true)

        for c in range(y_pred.shape[1]):
            if y_pred[0, c] == y_true[0, c]:
                sum_ = sum_ + 1
                acc = 100.0 * sum_ / y_pred.shape[1]
                self.test_acc.append(acc)

        print('Test acc is {:.5f}'.format(sum_ / y_pred.shape[1]))
        return sum_ / y_pred.shape[1]

    def get_loss_history(self):
        return self.loss

    def get_acc_history(self):
        return self.acc

    def get_test_acc_history(self):
        return self.test_acc


if __name__ == "__main__":
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    train_images = train_images.reshape((60000, 28 * 28))
    train_images = train_images.astype("float32") / 255

    test_images = test_images.reshape((10000, 28 * 28))
    test_images = test_images.astype("float32") / 255

    model = classification_two_hidden_layers(learning_rate=0.1, input_dim=784, output_dim=10, hidden_num=[100, 100],
                                             norm_initial_weight=0.1, L2=1e-6, epoch=2000,
                                             lr_decay='decay')

    model.train(train_images, train_labels)
    # 绘制训练精度曲线
    train_acc = model.get_acc_history()

    epochs = range(1, len(train_acc) + 1)
    plt.plot(epochs, train_acc, "b")
    plt.title('Accuracy Curve')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()

    testacc = model.test(test_images, test_labels)

    # 绘制测试精度曲线
    test_acc = model.get_test_acc_history()

    epochs = range(1, len(test_acc) + 1)
    plt.plot(epochs, test_acc, "b")
    plt.title('Accuracy Curve')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()


