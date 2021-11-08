#定义了一个类：人类,只是一个虚拟的类，还没有实例
class Person:
    # name,age,gender,weight,height  都是类变量
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0
    height = 0

    # 构造方法，初始化的一个方法,实例化对象的时候，首先会执行这个init方法
    def __init__(self,name,age,gender,weight,height):
        # self.name 创建实例的时候，实例变量，每一个实例都拥有自己的名字，年龄，性别，体重，身高
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height


    def set_myname(self,name):
        self.name = name
    def set_myage(self,age):
        self.age = age

    @classmethod #加装饰器后，类就可以访问这个实例方法了
    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def jump(self):
        print(f"{self.name} is jumping")

myself = Person('lxj',18,'female',88,160) #执行Person()实例化的时候，实际上是执行了Person类的 init 方法
#myself.set_myname("lxj")

#myself.set_myage(18)
'''
#类变量
print(Person.name)
Person.name = 'TOM'
print(Person.name)
#实例变量
print(myself.name)
myself.name = 'LILI'
print(myself.name)
'''
print(Person.eat())
#print(myself.eat())


#print(f"我是第一个人类的实例，\n我的姓名是：{myself.name},\n我的年龄是：{myself.age},\n性别：{myself.gender},\n体重：{myself.weight},\n身高：{myself.height}")
#myself.eat()
#myself.drink()
#myself.jump()