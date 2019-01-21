### 函数的参数
> Python的函数参数
链接 = #位置参数


#### 位置参数

#### 默认参数
1. 必选参数在前，默认参数在后；
2. 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
```
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

#### 可变参数
传入的参数个数是可变的。
可变参数允许传入0个或任意个参数，这些个可变参数在函数调用时自动组装为一个tuple。
```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
```
> numbers接收到的是一个tuple。

#### 关键字参数
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成为一个dict。
```
def person(name,age,**kw):
    print ('name:',name,'age:',age,'other',kw)
```

#### 命名关键字参数

```
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other',kw)
def person(name,age,*,city,job):
    print (name,age,city,job)
```
#### 参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，可以组合使用。参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
