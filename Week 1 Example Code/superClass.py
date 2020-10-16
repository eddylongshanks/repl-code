# super()

class Base():
    def __init__(self):
        print('Base __init__ called...')
    
a = Base()

class BaseTwo():
    def __init__(self):
        print('BaseTwo __init__ called...')

a1 = BaseTwo()

class BaseThree(BaseTwo):
    pass

a2 = BaseThree()

class Child(Base, BaseTwo):
    def __init__(self):
        print('Child __init called...')
        super().__init__() # This will call init for Base, because its the first attribute on line 20
    
