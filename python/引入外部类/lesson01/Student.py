import sys;
sys.path.append( r'G:\PythonPro\lesson01')

from People import People

# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, name, age,  grade):
        # 调用父类的构函
        # People.__init__( self, name , age)
        # 在子类Student中，因为重写了父类的__init__方法，如果要调用父类该方法，使用以下语句 调用父类中，因为子类重写而被屏蔽的同名方法。
        #super(Student, self).__init__(name,age)
        super().__init__(name,age)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

stu = Student('wangwu', 10,  3)
stu.speak()