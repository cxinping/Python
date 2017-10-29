
class People:
    # 定义基本属性
    name = ''
    age = 0

    # 定义构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


person = People('wangwu',20)
person.speak()