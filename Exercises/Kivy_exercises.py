from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.uix.textinput import TextInput

# source: e.g. https://www.youtube.com/watch?v=eZzL3Td4o84


Window.clearcolor = (0,0,0,1) # background color for kivy App (0,0,0) = black, (1,1,1)= 'white'
Window.size = (360,600) # output window of app like on mobile phone

class TestApp(App): # inherit all App functionalities from kivy

    def build(self):
        layout = GridLayout(cols = 2, row_force_default = True, row_default_height = 40,
                            spacing = 10, padding =20)
        #layout = BoxLayout(orientation = 'vertical', spacing=20, padding=80)
        #layout = GridLayout(cols=2, padding =100, spacing = 20)
        #layout = GridLayout(cols=2, row_force_default = True, row_default_height = 40)

        #label = Label(text = 'hello', font_size = '20sp', bold=True)
        self.weight = TextInput(text='Enter weight here:')
        self.height = TextInput(text='Enter height here:')
        submit = Button(text='Submit', on_press=self.submit)

        # img = Image(source = 'cute.png')
        # img2 = AsyncImage(source = 'https://www.transparentpng.com/thumb/cute/TZMwWi-cute-clipart-transparent.png') # does not work!

        # btn1 = Button(text='Hello 1',
        #               font_size = '20sp',
        #               size_hint=(None, None), # is needed in combi with width and height
        #               pos_hint = {'center_x':0.5,'center_y':0.5},
        #               width = 200, height = 100, # does not scale when adjusting window size
        #               on_press=self.printpress, # what happens when pressing the button --> function below
        #               on_release=self.printrelease # what happens when releasing the button --> function below
        #               )
        #btn2 = Button(text='World 1')
        #btn3 = Button(text='Hello 2', size_hint = (None, None),width = 100, height =40)
        #btn4 = Button(text='World 2')

        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        #layout.add_widget(btn3)
        #layout.add_widget(btn4)

        return layout

    def printpress(self,obj):
        print('Button has been pressed')

    def printrelease(self,obj):
        print('Button has been released')

    def submit(self,obj):
        print('weight:' + self.weight.text)
        print('height:' + self.height.text)

# run application
TestApp().run()