from traits.api import HasTraits, Button, Int #导入控件模块
from traitsui.api import View

class ButtonEditor(HasTraits):
    my_button = Button(u'点击我')
    counter = Int

    def _my_button_fired(self):
        self.counter +=1
        
    traits_view = View(
        'my_button',
        'counter',
        title = 'ButtonEditor',
        buttons = ['OK'],
        resizable = True
        )

button = ButtonEditor()
button.configure_traits()
