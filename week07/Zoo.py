from abc import ABCMeta, abstractclassmethod
import sys

class Zoo(object):

    def __init__(self, name):
        self.name = name
        self.cats = []
        self.dogs = []

    def __getattr__(self, item):
        if sys._getframe().f_back.f_lineno < 37 :
            print(f'__getattr__ called item:{item}')
            setattr(self,item,[])
            return item

    #动物园添加动物方法
    def add_animal(self, animal):
        if animal.__class__.__name__ == 'Cat':   
            if self.cats.count(animal.name) == 0  :
                self.cats.append( animal.name)
            else :
                print(f'{animal.name} 已存在，不可重复添加！')
        
        if animal.__class__.__name__ == 'Dog':
            if self.dogs.count(animal.name) == 0  :
                self.dogs.append( animal.name)
            else :
                print(f'{animal.name} 已存在，不可重复添加！')


class Animal(metaclass=ABCMeta):
   # “类型”、“体型”、“性格”、“是否属于凶猛动物”
    type = ''
    physique = ''
    character = ''
    is_fierce = ''

    def is_fierce_creatures(self):
        if self.physique == '肉食' or self.character == '凶猛' :
            self.is_fierce = '是'
        else :
            self.is_fierce = '否'

class Cat(Animal):
    
    def __init__(self, name,type,physique,character):
        #猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性
        # 动物名typetype
        self.name = name
        self.type = type
        self.physique = physique
        self.character = character
        self.sound = '喵'

        if self.physique == '凶猛' :
            self.forpet = '不适合'
        else :
            self.forpet = '适合'

        self.is_fierce_creatures()


class Dog(Animal):

    def __init__(self, name,type,physique,character):
        # 动物名
        self.name = name
        self.type = type
        self.physique = physique
        self.character = character
        self.sound = '汪汪'

        if self.physique == '凶猛' :
            self.forpet = '不适合'
        else :
            self.forpet = '适合'

        self.is_fierce_creatures()


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化Cat，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('小花猫 1', '食肉', '小', '温顺')
    # 增加猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(cat2)

     # 实例化dog，属性包括名字、类型、体型、性格
    dog1 = Dog('大狗 1', '食肉', '大', '温顺')
    dog2 = Dog('小狗 2', '食肉', '小', '凶猛')
    z.add_animal(dog1)
    z.add_animal(dog2)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)