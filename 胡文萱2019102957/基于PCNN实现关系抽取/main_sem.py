# -*- coding: utf-8 -*-

from config import opt
import numpy as np
import models
import dataset
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torch.optim as optim
from torch.autograd import Variable
import time
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
# 保证所有数据能够显示，而不是用省略号表示，np.inf表示一个足够大的数
np.set_printoptions(threshold=np.inf)
# z:
np.set_printoptions(suppress=True)
# torch.set_printoptions(profile="full")

def now():
    return str(time.strftime('%Y-%m-%d %H:%M%S'))


def test(**kwargs):
    pass


def train(**kwargs):
    print("断点开始")
    # kwargs.update({'model': 'PCNN'})
    opt.parse(kwargs)
    if opt.use_gpu:
        torch.cuda.set_device(opt.gpu_id)

    # loading data
    DataModel = getattr(dataset, 'SEMData') # 用DataModel 来接收 SEMData 这个类，这样可以用DataModel来构造对象

    train_data = DataModel(opt.data_root, train=True) # ./dataset/SemEval/
    # print(train_data)
    # 加载数据，第一个参数是dataset对象，因为SEMData类继承了Dataset类，batch_ze 128 ,shuffle = true 将数据打乱, num_works 多进程加载数据，
    train_data_loader = DataLoader(train_data, opt.batch_size, shuffle=True, num_workers=opt.num_workers)

    test_data = DataModel(opt.data_root, train=False)
    test_data_loader = DataLoader(test_data, batch_size=opt.batch_size, shuffle=False, num_workers=opt.num_workers)
    print('train data: {}; test data: {}'.format(len(train_data), len(test_data)))

    # criterion and optimizer
    # lr = opt.lr
    model = getattr(models, 'PCNN')(opt)
    # print(model)
    if opt.use_gpu:
        torch.cuda.set_device(opt.gpu_id)
        # print("设置gpu_id为", opt.gpu_id)
        model.cuda()

    criterion = nn.CrossEntropyLoss()
    #  optimizer = optim.Adam(model.out_linear.parameters(), lr=0.0001)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    # optimizer = optim.Adadelta(model.parameters(), rho=0.95, eps=1e-6)

    best_acc = 0.0
    # train
    for epoch in range(opt.num_epochs): # num_epochs 100

        total_loss = 0.0

        for ii, data in enumerate(train_data_loader):
            # torch.LongTensor(data)
            for i in range(len(data)):
                # print("i ", i,"len ",len(data[i]),"类型",data[i].dtype)
                """
                分别是 （len=128）
                      lexical_feature,
                      word_feautre,
                      self.left_pf,
                      self.right_pf,
                      self.labels
                """
                data[i] = data[i].long()
                # print("转换之后",data[i].dtype)
            if opt.use_gpu:
                # 转换为 cuda 的tensor
                data = list(map(lambda x: Variable (x.cuda()), data))
            else:
                data = list(map(Variable, data))
            # 将梯度设置0
            model.zero_grad()
            # 除了 data[4] 即 关系标签，
            out = model(data[:-1])
            # print(out)
            print("over3")
            loss = criterion(out, data[-1])
            loss.backward()
            optimizer.step()
            total_loss += loss.data.item()

        train_avg_loss = total_loss / len(train_data_loader.dataset)
        acc, f1, eval_avg_loss, pred_y = eval(model, test_data_loader, opt.rel_num)
        if best_acc < acc:
            best_acc = acc
            write_result(model.model_name, pred_y)
            model.save(name="SEM_CNN")
        # toy_acc, toy_f1, toy_loss = eval(model, train_data_loader, opt.rel_num)
        print('Epoch {}/{}: train loss: {}; test accuracy: {}, test f1:{},  test loss {}'.format(
            epoch, opt.num_epochs, train_avg_loss, acc, f1, eval_avg_loss))

    print("*" * 30)
    print("the best acc: {};".format(best_acc))


def eval(model, test_data_loader, k):

    model.eval()
    avg_loss = 0.0
    pred_y = []
    labels = []
    for ii, data in enumerate(test_data_loader):

        if opt.use_gpu:
            data = list(map(lambda x: torch.LongTensor(x).cuda(), data))
        else:
            data = list(map(lambda x: torch.LongTensor(x), data))

        out = model(data[:-1])
        loss = F.cross_entropy(out, data[-1])

        pred_y.extend(torch.max(out, 1)[1].data.cpu().numpy().tolist())
        labels.extend(data[-1].data.cpu().numpy().tolist())
        avg_loss += loss.data.item()

    size = len(test_data_loader.dataset)
    assert len(pred_y) == size and len(labels) == size
    f1 = f1_score(labels, pred_y, average='micro')
    acc = accuracy_score(labels, pred_y)
    model.train()
    return acc, f1, avg_loss / size, pred_y


def write_result(model_name, pred_y):
    out = open('./semeval/sem_{}_result.txt'.format(model_name), 'w')
    size = len(pred_y)
    start = 8001
    end = start + size
    for i in range(start, end):
        out.write("{}\t{}\n".format(i, pred_y[i - start]))


if __name__ == "__main__":
    import fire
    fire.Fire()
