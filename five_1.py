import matplotlib.pyplot as plt #导入库
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

tf.reset_default_graph()
x_data = np.linspace(0,100,500)
y_data = 3.1234*x_data+2.98
plt.scatter(x_data,y_data,color="red",marker="o")
plt.plot(x_data,3.1234*x_data+2.98,color='blue')


x = tf.placeholder("float",name="x")
y = tf.placeholder("float",name="y")


def model(x,w,b):
    return tf.multiply(x,w)+b

w = tf.Variable(1.0,name="w0")
b = tf.Variable(0.0,name="b0")
pred = model(x,w,b)

train_epochs = 10
learning_rate = 0.0001
loss_function = tf.reduce_mean(tf.square(y-pred))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

display_step = 20
step = 0
loss_list = []
for epoch in range(train_epochs):
    for xs,ys in zip(x_data,y_data):
        _,loss = sess.run([optimizer,loss_function],feed_dict={x:xs,y:ys})
        loss_list.append(loss)
        step = step+1
        if(step % display_step ==0):
            print("Train Epoch:",'%02d'%(epoch+1),"Step: %03d"%(step),"loss=","{:.9f}".format(loss))

b0temp = b.eval(session=sess)
w0temp = w.eval(session=sess)
plt.plot(x_data,w0temp*x_data+b0temp)

x_test = 5.79
predict = sess.run(pred,feed_dict={x:x_test})
target = 3.1234*x_test+2.98
print("预测值：%f"%predict)
print("目标值：%f"%target)

logdir = 'E:\pylog'
writer = tf.summary.FileWriter(logdir,tf.get_default_graph())
writer.close()

plt.show()