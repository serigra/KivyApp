from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDFlatButton
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder # to use e.g. MDTextField within a string --> automatically is imported through Builder
from helpers import username_helper


class DemoApp(MDApp): # inherit all MDApp functionalities

    def build(self):

        # THEME --------------------------------------------------------------------------------------------------------
        self.theme_cls.primary_palette = 'Pink' # theme color for all functionalities in app
        self.theme_cls.primary_hue = '300' # darknesss of main theme color --> see github notes of attreyabhatt
        self.theme_cls.theme_style ='Dark'

        screen = Screen() # similar to layout functionality in kivy basics

        # BUTTONS ------------------------------------------------------------------------------------------------------
        btn_flat = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_release=self.show_data)
        # icon_btn = MDIconButton(icon = 'android', pos_hint = {'center_x':0.5, 'center_y':0.5})
        # btn_action = MDFloatingActionButton(icon = 'android', pos_hint = {'center_x':0.5, 'center_y':0.5})

        # TEXT INPUT ---------------------------------------------------------------------------------------------------
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x':0.5, 'center_y':0.5}, # position on screen
        #                        size_hint_x=None, # when changing screen, size of textinput should NOT change
        #                        width=300 # 300 pixels
        #                        )
        self.username = Builder.load_string(username_helper)

        # LABELS -------------------------------------------------------------------------------------------------------
        # halign = horizontal align
        # label = MDLabel(text="Hallöchen", halign="center", theme_text_color="Error",
        #                 font_style="H1")
        # label = Label(text = 'hello', bold=True) # kivy, not MDKivy
        # label = MDLabel(text="Hello world", halign="center",theme_text_color="Custom",
        #                 text_color=(0,0,1,1))
        # label = MDIcon(icon="android", halign="right")

        # SCREEN OUTPUT ------------------------------------------------------------------------------------------------
        screen.add_widget(self.username)
        screen.add_widget(btn_flat)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exist'
        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_btn = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username check',
                          text=check_string,
                          size_hint=(0.7, 1), # that dialogbox adjusts to smaller/bigger screen
                          buttons = [close_btn, more_btn])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()

# run application
DemoApp().run()