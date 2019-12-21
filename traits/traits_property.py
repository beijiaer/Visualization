from traits.api import HasTraits, Float, Property, cached_property

class rectangle(HasTraits):
    w = Float(1.0)
    h = Float(2.0)
    area = Property(depends_on = ["w", "h"])

    #cached_property装饰器的作用是可以 让self.w和self.h在没有输入时输出缓存中的保存值
    @cached_property
    def _get_area(self):
        print("computing...")
        return(self.w * self.h)
