from abc import ABCMeta, abstractmethod

#动物园类
class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.animals_type = []
    def __getattr__(self, item):
        if self.animals_type.count( item ) == 1:
            return item
    #动物园添加动物方法
    def add_animal(self, animal):
        #添加动物，同一只动物不能重复添加
        if self.animals.count(animal.animal_name) == 0:
            self.animals.append(animal.animal_name)
        else:
            print(f'{animal.name} 已存在，不可重复添加！')
        #添加动物类型
        if self.animals_type.count(animal.__class__.__name__) == 0:
            self.animals_type.append(animal.__class__.__name__)

class Animal(metaclass=ABCMeta):
   # 动物类有四个属性：“类型”、“体型”、“性格”、“是否属于凶猛动物”
    __animal_type = ''
    __physique = ''
    __character = ''
    __is_fierce = ''
    animal_name = ''

    @property
    def animal_type(self):
        return self.__animal_type  

    @animal_type.setter
    def set_animal_type(self, __type ):
        self.__animal_type = __type

    @property
    def physique(self):
        return self.__physique   

    @physique.setter
    def set_physique(self, physique):
        self.__physique = physique

    @property
    def character(self):
        return self.__character  

    @character.setter
    def set_character(self, character):
        self.__character = character

    @property
    def is_fierce(self):
        if self.physique == '肉食' or self.character == '凶猛' :
            self.__is_fierce = '是'
        else :
            self.__is_fierce = '否' 
        return self.__is_fierce
    
    def __init__(self, name, animal_type,physique,character):
        self.animal_name = name
        self.__physique = physique
        self.__character = character
        self.__animal_type = animal_type
    # def __new__(cls, name,animal_type,physique,character):
    #     pass

#猫类，继承于动物类
class Cat(Animal):   
    sound = '喵'
    __name = ''
    __is_pet = False

    @property
    def is_pet(self):
        if self.physique == '凶猛' :
            self.__is_pet = False
        else :
            self.__is_pet = True
        return self.__is_pet
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value 
    
    def __init__(self, name,animal_type,physique,character):
        self.__name = name
        super().__init__(name,animal_type,physique,character)


#狗类，继承于动物类
class Dog(Animal):
    sound = '汪汪'

    @property
    def name(self):
        return self.__name

    @property
    def is_pet(self):
        if self.physique == '凶猛' :
            self.__is_pet = False
        else :
            self.__is_pet = True
        return self.__is_pet
    
    @name.setter
    def set_name(self, value):
        self.__name = value
    
    def __init__(self, name,animal_type,physique,character):
        self.__name = name
        super().__init__(name,animal_type,physique,character)

#小鸟类，用来测试扩展性
class Bird(Animal):
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self, value):
        self.__name = value
    
    def __init__(self, name,animal_type,physique,character):
        self.__name = name
        super().__init__(name,animal_type,physique,character)


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

    #测试扩展性
    # bird1 = Bird('小鸟', '食肉', '小', '凶猛')
    # z.add_animal(bird1)

    for animal_name in z.animals :
        print(f'动物园的动物：{animal_name}')
    
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)