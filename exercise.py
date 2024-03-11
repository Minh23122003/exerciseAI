def cau1(name):
    for i in name:
        print(i, end=' ')

def cau2():
    for i in range(11):
        if i % 2 != 0:
            print(i, end=' ')

def cau3a():
    sum = 0
    for i in range(11):
        if i % 2 != 0:
            sum = sum + i
    print(sum)

def cau3b():
    sum = 0
    for i in range(7):
        sum = sum + i
    print(sum)

def cau4a():
    mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for keys, values in mydict.items():
        print(keys, end=' ')

def cau4b():
    mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for keys, values in mydict.items():
        print(values, end=' ')

def cau4c():
    mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for keys, values in mydict.items():
        print(keys, ':', values, sep=' ')

def cau5():
    courses = [131, 141, 142, 212]
    names = ['Maths', 'Physics', 'Chem', 'Bio']

    print(tuple(zip(courses, names)))

def cau6a():
    s = 'jabbawocky'
    for i in s:
        if i not in 'aeiou':
            print(i, end=' ')

def cau6b():
    s = 'jabbawocky'
    for i in s:
        if i in 'aeiou':
            print(i, end=' ')

def cau7():
    for i in range(-2, 3):
        try:
            print(float(10/i))
        except:
            print('cannot divided by zero')

def cau8():
    ages = [23, 10, 80]
    names = ['Hoa', 'Lam', 'Nam']

    tuples = tuple(zip(ages, names))
    print(sorted(tuples, key=lambda x:x[0]))

def cau9():
    f = open('D:\Firstname.txt', 'r')
    print(f.read())

if __name__ == "__main__":
    cau9()