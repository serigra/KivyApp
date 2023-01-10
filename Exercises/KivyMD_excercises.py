from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDFlatButton
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder # to use e.g. MDTextField within a string --> automatically is imported through Builder
from Builder_helpers import username_helper, list_helper_1, list_helper_2
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget, ImageRightWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp): # inherit all MDApp functionalities

    def build(self):

        # THEME --------------------------------------------------------------------------------------------------------
        self.theme_cls.primary_palette = 'Pink' # theme color for all functionalities in app
        self.theme_cls.primary_hue = '300' # darknesss of main theme color --> see github notes of attreyabhatt
        self.theme_cls.theme_style ='Dark'

        screen = Screen() # similar to layout functionality in kivy basics

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        # BUTTONS ------------------------------------------------------------------------------------------------------
        btn_username = MDRectangleFlatButton(text='Show username', pos_hint={'center_x': 0.4, 'center_y': 0.4},
                                         on_release=self.show_dialogbox)
        btn_list = MDRectangleFlatButton(text='Show list', pos_hint={'center_x': 0.6, 'center_y': 0.4}
                                         #on_release=self.show_list
                                         )
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

        # LISTS --------------------------------------------------------------------------------------------------------
        # item1 = OneLineListItem(text='Item 1')
        # item2 = OneLineListItem(text='Item 2')
        #for i in range(20):
            # Option I ........................................
            # items = OneLineListItem(text='Item ' + str(i))
            # items = ThreeLineListItem(text='Item ' + str(i),
            #                           secondary_text = 'Hello World',
            #                            tertiary_text = 'Third line text')

            # Option II .......................................
            #icon = IconLeftWidget(icon='android')
            #items = ThreeLineIconListItem(text='Item ' + str(i),
            #                              secondary_text = 'Hello World',
            #                              tertiary_text = 'Third line text')
            #items.add_widget(icon)

            # Option III ......................................
            #avatar = ImageRightWidget(source='cute.png') # gives error, kivyMD are trying to fix this
            #avatar = ImageLeftWidget(source='cute.png')  # gives error, kivyMD are trying to fix this
            #items = ThreeLineAvatarListItem(text='Item ' + str(i),
            #                                secondary_text = 'Hello World',
            #                                tertiary_text = 'Third line text')
            #items.add_widget(avatar)
            #list_view.add_widget(items)

            # Option IV --> using Builder method, see below  .....


        # SCREEN OUTPUT ------------------------------------------------------------------------------------------------
        #screen.add_widget(self.username)
        #screen.add_widget(btn_username)
        #screen.add_widget(btn_list)

        #list_view.add_widget(item1)
        #list_view.add_widget(item2)

        #screen.add_widget(scroll)

        screen = Builder.load_string(list_helper_1)

        return screen

    def show_dialogbox(self, obj):
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

    # def on_start(self): # is gonna show up before applications starts running, in this case a list
    #     for i in range(20):
    #         items = OneLineListItem(text='Item ' + str(i))
    #         self.root.ids.container.add_widget(items) # container = name of the ids given in the list_helper_2

# run application
DemoApp().run()