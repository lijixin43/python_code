# AUTHOR lijixin

import os
import struct
import numpy as np
import matplotlib.pyplot as plt


def load_mnist(path,kind = 'train'):
    """load mnist data from 'path'"""
    labels_path = os.path.join(path,'%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,'%s-images-idx3-ubyte'
                               % kind)
    with open(labels_path,'rb') as lbpath:
        magic , n = struct.unpack('>II',lbpath.read(8))

        labels = np.fromfile(lbpath,dtype = np.uint8)
    with open(images_path,'rb') as imgpath:
        magic , num ,rows ,cols = struct.unpack(">IIII",imgpath.read(16))

        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels),784)
    return images,labels

if __name__ == '__main__':
    x_train,y_train = load_mnist('mnist',kind='train')
    print('Rows: %d,columns: %d' % (x_train.shape[0],x_train.shape[1]))
    x_test, y_test = load_mnist('mnist', kind='t10k')
    print('Rows: %d,columns: %d' % (x_test.shape[0], x_test.shape[1]))
    # fig, ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True,)
    # ax = ax.flatten()
    # for i in range(10):
    #     img = x_train[y_train == i][0].reshape(28,28)
    #     ax[i].imshow(img,cmap='Greys',interpolation='nearest')
    # ax[0].set_xticks([1])
    # ax[0].set_yticks([])
    # plt.tight_layout()
    # plt.show()
    fig,ax = plt.subplots(nrows=5,ncols=5,sharex=True,sharey=True)
    ax = ax.flatten()
    for i in range(25):
        img = x_train[y_train==7][i].reshape(28,28)
        ax[i].imshow(img,cmap='Greys',interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()