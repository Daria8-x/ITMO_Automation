def task_1()->str:
    a: int=5
    b: float=3.5
    c: str='строка'
    d: list=[1, 2, 3]
    r: bool=True
    print('a=',type(a))
    print('b=',type(b))
    print('c=',type(c))
    print('d=',type(d))
    print('r=',type(r))

task_1()

def task_2()->list:
    a=[1,2,3,5,8,13,21] #числа Фибоначчи
    print(a[0:3])

task_2()

def task_3()->int:
    a=6
    return a**2
print(task_3())

