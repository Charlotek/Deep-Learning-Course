# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
df=pd.read_csv("C:/Users/wzh/Anaconda3/Lib/site-packages/sklearn/datasets/data/boston_house_prices.csv")
ds=df.values
x_data=ds[:,:12]
y_data=ds[:,12]
print("x_data shape=",x_data.shape)
print("y_data shape=",y_data.shape)
train_num=300
valid_num=100
test_num=len(x_data)-train_num-valid_num
#训练集
x_train=x_data[:train_num]
y_train=y_data[:train_num]
#验证集
x_valid=x_data[train_num:train_num+valid_num]
y_valid=y_data[train_num:train_num+valid_num]
#测试集
x_test=x_data[train_num+valid_num:train_num+valid_num+test_num]
y_test=y_data[train_num+valid_num:train_num+valid_num+test_num]

x_train=tf.cast(x_train,dtype=tf.float32)
x_valid=tf.cast(x_valid,dtype=tf.float32)
x_test=tf.cast(x_test,dtype=tf.float32)

def model(x,w,b):
    return tf.matmul(x,w)+b
W=tf.Variable(tf.random.normal([12,1],mean=0.0,stddev=1.0,dtype=tf.float32))