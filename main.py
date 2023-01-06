from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDIconButton


# Window.clearcolor = (1,0,0,1) # background color for kivy App

class DemoApp(MDApp): # inherit all MDApp functionalities

    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Push button', pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        # icon_btn = MDIconButton(icon = 'android', pos_hint = {'center_x':0.5, 'center_y':0.5})
        screen.add_widget(btn_flat)
        # halign = horizontal align
        # label = MDLabel(text="Hallöchen", halign="center", theme_text_color="Error",
        #                 font_style="H1")
        # label = Label(text = 'hello', bold=True) # kivy, not MDKivy
        # label = MDLabel(text="Hello world", halign="center",theme_text_color="Custom",
        #                 text_color=(0,0,1,1))
        # label = MDIcon(icon="android", halign="right")
        return screen

# run application
DemoApp().run()