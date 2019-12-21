from traits.api import Delegate, HasTraits, Instance, Int, Str

class Parent(HasTraits):
    last_name = Str("Zhang")

class Child(HasTraits):
    age = Int
    #验证
    father = Instance(Parent)
    #代理
    last_name = Delegate("father")
    #监听
    def _age_changed(self, old, new):
        print("Age changed from %s to %s" % (old, new))
