from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item,Group
from traitsui.menu import ModalButtons


g1 = [Item("model_name", label=u"模型名称"),
      Item("category", label=u"模型类型")]
g2 = [Item("model_number", label=u"模型数量"),
      Item("vertices", label=u"顶点数量")]
class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Str
    vertices = Int
    traits_view = View(
        Group(*g1, label = u"模型信息", show_border = True),
        Group(*g2, label = u"统计数据", show_border = True),
        title = u"内部视图")
global_view = View(
    Group(*g1, label = u"模型信息", show_border = True),
    Group(*g2, label = u"统计数据", show_border = True),
    title = u"外部视图")

model = ModelManager()
