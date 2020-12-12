from kivymd.app import MDApp
from kivymd.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image, AsyncImage
from kivymd.uix.list import TwoLineIconListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.network.urlrequest import UrlRequest
from functools import partial


screen_helper = """
ScreenManager:
    MenuScreen:
    PlattegrondScreen:
    VerkenDeSchool:
    VakkenLocaties:
    ProeflesScreen:
    MenNScreen:
    WisScreen:
    NLScreen:
    RekenenScreen:
    MuziekScreen:
    MMScreen:
    LOScreen:
    EngScreen:
    XLScreen:
    BVScreen:
    
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: "horizontal"
        MDToolbar:
            title: "Welkom bij het Kompaan College!"
    
    MDRectangleFlatButton:
        text: 'Proefles'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'Proeflessen'
        
    MDRectangleFlatButton:
        text: 'School Plategrond'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'Plattegrond'
    MDRectangleFlatButton:
        text: 'Verken de school'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'verken'
    MDToolbar:
        title: 'Example BottomSheet'
        pos_hint: {"top": 1}
        elevation: 10

    MDRaisedButton:
        text: "Credits"
        on_press: partial(webbrowser.open, 'https://youtube.com')
        pos_hint: {"center_x": .5, "center_y": .5}
        
    
        
        
    Image: 
        source: 'kompaanlogo.png'
        size_hint: (0.3,0.3)
        pos_hint: {'center_x':0.2, 'center_y':0.9}
        
        
<PlattegrondScreen>:
    name: 'Plattegrond'
    MDRectangleFlatButton:
        text: 'Terug'
        pos_hint: {'center_x':0.9,'center_y':0.9}
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'School Plategrond'
        bold: True
        font_style: 'H5'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.8}
    Image:
        source: 'getresource.jpg'
        size_hint: (1,1)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
    Image: 
        source: 'kompaanlogo.png'
        size_hint: (0.3,0.3)
        pos_hint: {'center_x':0.2, 'center_y':0.9}
<VerkenDeSchool>:
    name:'verken'
    MDLabel:
        text: 'Verken de School'
        pos_hint: {'center_x':0.67,'center_y':0.8} 
        size_hint: (0.78,0.9) 
        font_style: "H4"
        bold: True   
    MDRectangleFlatButton:
        text: 'Vakken'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint:(0.4,0.07)
        on_press: root.manager.current = 'Vakken&Locaties'
    MDRectangleFlatButton:
        text: 'School Informatie'
        pos_hint: {'center_x':0.5,'center_y':0.5} 
        size_hint:(0.4,0.07)
    MDRectangleFlatButton:
        text: 'Gebouw Regels'
        pos_hint: {'center_x':0.5,'center_y':0.4}  
        size_hint:(0.4,0.07)
    MDRectangleFlatButton:
        text: 'Streetview Gebouw'
        pos_hint: {'center_x':0.5,'center_y':0.3}  
        size_hint:(0.4,0.07)    
        
    MDRectangleFlatButton:
        text: 'Terug'
        pos_hint: {'center_x':0.9,'center_y':0.9}
        on_press: root.manager.current = 'menu'
    Image: 
        source: 'kompaanlogo.png'
        size_hint: (0.3,0.3)
        pos_hint: {'center_x':0.2, 'center_y':0.9}
    
        
<VakkenLocaties>:
    name: 'Vakken&Locaties'
    ScrollView:
        MDList:
            TwoLineIconListItem:
                text: "Nederlands"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Wiskunde"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Rekenen"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Muziek"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Mensen en Maatschappij"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Lichamelijke Opvoeding"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Engels"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "XL"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Beeldende Vorming"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
    MDRectangleFlatButton:
        text: "Terug"
        pos_hint: {'center_x':0.9,'center_y':0.9}
        on_press: root.manager.current = 'verken'


<ProeflesScreen>:
    name: "Proeflessen"
    Image: 
        source: 'kompaanlogo.png'
        size_hint: (0.1,0.1)
        pos_hint: {'center_x':0.9,'center_y':0.1}
    ScrollView:
        MDList:
            TwoLineIconListItem:
                text: "XL"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
            TwoLineIconListItem:
                text: "Duits"
                secondary_text: "Klik hier voor het vak en de informatie"
                IconLeftWidget:
                    icon: "book"
    MDRectangleFlatButton:
        text: "Terug"
        pos_hint: {'center_x':0.9,'center_y':0.9}
        on_press: root.manager.current = 'menu'
        
    
<MenNScreen>:
    name: "MenN"
<WisScreen>:
    name: "Wiskunde"
<NLScreen>:
    name: "Nederlands"
<RekenenScreen>:
    name: "Rekenen"
<MuziekScreen>:
    name: "Muziek"
<LOScreen>:
    name: "LO"
<EngScreen>:
    name: "Eng"
<XLScreen>:
    name: "XL"
<BVScreen>:
    name: "BV"  
    

"""


# Declare both screens
class MenuScreen(Screen):
    pass


class VerkenDeSchool(Screen):
    pass


class PlattegrondScreen(Screen):
    pass

class VakkenLocaties(Screen):
    pass

class ProeflesScreen(Screen):
    pass
class MenNScreen(Screen):
    pass
class WisScreen(Screen):
    pass
class NLScreen(Screen):
    pass
class RekenenScreen(Screen):
    pass
class MuziekScreen(Screen):
    pass
class MMScreen(Screen):
    pass
class LOScreen(Screen):
    pass
class EngScreen(Screen):
    pass
class XLScreen(Screen):
    pass
class BVScreen(Screen):
    pass
class List_view(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(PlattegrondScreen(name='Plattegrond'))
sm.add_widget(VerkenDeSchool(name='verken'))
sm.add_widget(VakkenLocaties(name='Vakken&Locaties'))
sm.add_widget(ProeflesScreen(name='Proeflessen'))
sm.add_widget(BVScreen(name='BV'))
sm.add_widget(XLScreen(name='XL'))
sm.add_widget(EngScreen(name='Eng'))
sm.add_widget(LOScreen(name='LO'))
sm.add_widget(MuziekScreen(name='Muziek'))
sm.add_widget(RekenenScreen(name='Rekenen'))
sm.add_widget(NLScreen(name='Nederlands'))
sm.add_widget(WisScreen(name='Wiskunde'))
sm.add_widget(MenNScreen(name='MenN'))




class SchoolApp(MDApp):
    def build(self):

        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "900"
        screen = Builder.load_string(screen_helper)
        return screen

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook-box",
            "YouTube": "youtube",
            "Twitter": "twitter-box",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()




SchoolApp().run()
