# 3 Quotes if multiline string
# using the Builder Functionality from kivy, functionalities can be used within strings, without importing the module
# for options use : instead of =
username_helper = """   
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "persistent"
    icon_right: 'heart'
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

list_helper_1 = """
Screen:
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: 'Item 1'
                    
                IconLeftWidget: 
                    icon: 'github'
            
            OneLineIconListItem:
                text: 'Item 2'
                
                IconLeftWidget: 
                    icon: 'github'
"""


list_helper_2 = """
Screen:
    ScrollView:
        MDList:
            id: container
"""