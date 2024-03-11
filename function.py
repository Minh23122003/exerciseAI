import matplotlib.pyplot as plt
import numpy, math, random
import numpy as np


def cau1(a, b):
    return a + b

def cau2():
    m = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = numpy.array([1, 2, 3])

    print(m.shape)
    print(numpy.linalg.matrix_rank(m))
    print(v.shape)
    print(numpy.linalg.matrix_rank(v))

def cau3():
    m = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    n = m.copy()
    n = n + 3
    print(n)

def cau4():
    m = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = numpy.array([1, 2, 3])

    print(numpy.matrix.transpose(m))
    print(numpy.matrix.transpose(v))

def cau5(x, y):
    v = numpy.array([x, y])
    norm = numpy.linalg.norm(v)
    print(norm)
    if norm == 0:
        print(v)
    else:
        print(v / norm)

def cau6():
    a = numpy.array([10, 15])
    b= numpy.array([8, 2])
    c = numpy.array([1, 2, 3])
    print(a + b)
    print(a - b)
    # print(a - c) không đc vì ko cùng shape

def cau7():
    a = numpy.array([10, 15])
    b = numpy.array([8, 2])
    print(numpy.vdot(a, b))

def cau8():
    a = numpy.array([[2, 4, 9], [3, 6, 7]])
    print(numpy.linalg.matrix_rank(a))
    print(numpy.shape(a))
    num = 7
    # for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         if a[i][j] == 7:
    #             print(i, j)
    print(numpy.where(a == 7))
    print(a[:, 2])

def cau9(a, b):
    arr = [[random.randrange(-10, 10, 1) for x in range(b)] for y in range(a)]
    print(arr)

def cau10(a, b):
    arr = [[0 for x in range(b)] for y in range(a)]
    k = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = k
            k = k + 1
    print(arr)

def cau11(a):
    arr = [[random.randrange(1, 10, 1) for x in range(a)] for y in range(a)]
    print(arr)
    print(numpy.trace(arr))
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i][i]
    print(sum)

def cau12():
    arr = numpy.diag(numpy.full(3, [1, 2, 3]))
    print(arr)

def cau13():
    arr = numpy.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    print(round(numpy.linalg.det(arr), 2))

def cau14():
    a1 = [1, -2, -5]
    a2 = [2, 5, 6]
    arr = numpy.array([a1, a2])
    print(arr.transpose())

def cau15():
    # arr = [[random.randrange(-5, 7, 1) for x in range(3)] for y in range(4)]
    # data = numpy.array(arr)
    # masked = numpy.ma.masked_equal(data, 0)
    # fig = plt.figure()
    # ax = fig.gca()
    # ax.matshow(masked, cmap=plt.cm.autumn_r)
    # plt.show()

    x = numpy.linspace(-5, 6, 12)
    y = np.square(x)
    plt.plot(x, y, 'o')
    plt.show()

def cau16():
    x = numpy.linspace(0, 32, 10)
    y = numpy.add(x, 4)
    plt.plot(x, y, 'o')
    plt.show()

def cau17():
    x = numpy.linspace(-5, 5, 50)
    y = x ** 2
    plt.plot(x, y, 'o')
    plt.show()

def cau18():
    x = numpy.linspace(-5, 5, 10)
    y = numpy.exp(x)
    plt.plot(x, y, 'o')
    plt.show()

def cau19():
    x = numpy.linspace(0, 5, 10)
    y = numpy.log(x)
    plt.plot(x, y, 'o')
    plt.show()

def cau20():
    x = numpy.linspace(1, 5, 10)
    y1 = numpy.exp(x)
    y2 = numpy.exp(2*x)
    # y3 = numpy.log(x)
    # y4 = numpy.log(2*x)
    plt.subplot([x, y1], [x, y2])
    plt.show()

if __name__ == "__main__":
    cau20()