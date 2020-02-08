import numpy as np
import matplotlib.pyplot as plt


def Heunmethod(a: float, b: float, n: int,y0:float, f) -> list:
    """
    オイラー法　y'=f(x,y) のyを逐次計算し、listで返す
    :param a: xの下限
    :param b: xの上限
    :param n: 分割数
    :param y0: yの初期値
    :param f: 微分方程式の関数
    :return: yの計算結果list
    """
    h = (b - a) / n
    x = np.linspace(a, b, n)
    y = np.zeros(n)
    tmp_y = y0
    k1=0
    k2=0
    for i in range(n):
        k1=f(x[i],tmp_y)
        k2=f(x[i]+h,tmp_y+h*k1)
        tmp_y = tmp_y + h*(k1+k2)/2
        y[i] = tmp_y
    return x,y



def func(x:float,y:float)->float:
    """
    常微分方程式の関数　y'=f(x,y)
    :param x:
    :param y:
    :return: f(x,y)
    """
    return x+y

if __name__=='__main__':
    x,y=Heunmethod(0,1,10,1,func)
    print(y)
    plt.plot(x,y)
    plt.show()