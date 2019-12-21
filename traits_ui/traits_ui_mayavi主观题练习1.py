"""
TraitUI中嵌入Mayavi
"""                           

from traits.api import HasTraits, Range, Instance, on_trait_change, Str, Int, Button
from traitsui.api import View, Item, Group
from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from numpy import arange, pi, cos, sin

dphi = pi/300.
phi = arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
def curve(n_mer, n_long):
    mu = phi*n_mer
    x = cos(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    y = sin(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    z = 0.5 * sin(n_long*mu/n_mer)
    t = sin(mu)
    return x, y, z, t

class MyModel(HasTraits):
    n_meridional    = Range(0, 30, 6)
    n_longitudinal  = Range(0, 30, 11)
    # 场景模型实例
    scene = Instance(MlabSceneModel, ())
    # 管线实例
    plot = Instance(PipelineBase)
    #当场景被激活，或者参数发生改变，更新图形
    @on_trait_change('n_meridional,n_longitudinal,scene.activated')
    def update_plot(self): 
        x, y, z, t = curve(self.n_meridional, self.n_longitudinal)
        if self.plot is None:#如果plot未绘制则生成plot3d
            self.plot = self.scene.mlab.plot3d(x, y, z, t,
                        tube_radius=0.025, colormap='Spectral')
        else:#如果数据有变化，将数据更新即重新赋值
            self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t)
    # 建立视图布局
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False), #图形窗口界面
                Group('_', 'n_meridional',  #滑动条
                      Item('model_name',label=u'模型名称'), #模型名称文本框
                      Item('model_file',label=u'文件名'),
                      Item('category',label=u'模型类型'),
                      #Item('number',label=u'模型信息'),                     
                      show_border = True
                      ), 
                title = 'view_range_text',
                buttons = ['OK'],
                resizable=True, #可变窗口大小
                )
    model_name = Str
    category = Str
    model_file = Str
    #model_number = Int
model = MyModel()
model.configure_traits()
