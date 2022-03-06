from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from os import listdir, path

Builder.load_string('''
<ChooseFile>:
    canvas.before:
        Color:
            rgba: 0, 0, .4, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser
        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                background_color: 0,.5,1,1
                on_release: root.cancel()
            Button:
                text: "Select Folder"
                background_color: 0,.5,1,1
                on_release: root.select(filechooser.path)
                
<MusicPlayer>:
    canvas.before:
        Color:
            rgba: 0, 0, .1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    TextInput:
        id: direct
        pos: 0,root.top-35
        size: root.width-200,35
        hint_text: 'Enter File Location or Leave Empty to Browse'
    Button:
        id: searchBtn
        text: 'Browse'
        size: 200,35
        background_color: 0,.5,1,1
        pos: root.width-200, root.top-35
        on_release: root.getSongs()
    ScrollView:
        size_hint: None, None
        size: root.width, root.height-135
        pos: 0, 100
        GridLayout:
            id: scroll
            cols: 2
            spacing: 10
            size_hint_y: None
            row_force_default: True
            row_default_height: 40
    GridLayout:
        rows: 1
        pos: 0, 50
        size: root.width, 50
        Button:
            text: '<--'
            background_color: 0,.5,1,1
        Button:
            text: '||'
            background_color: 0,.5,1,1
        Button:
            text: '-->'
            background_color: 0,.5,1,1
    Button:
        id: nowplay
        text: 'Now Playing'
        pos: 0,0
        size: root.width, 50
        background_color: 0,.5,1,1
    Label:
        id: status
        text: ''
        center: root.center    
''')

class ChooseFile(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MusicPlayer(Widget):
    directory = '' #This is where the songs are
    nowplaying = '' #Song that is currently playing

    def getpath(self):
        try:
            f = open("sav.dat", "r")
            self.ids.direct.next = str(f.readline())
            f.close()
            self.ids.searchBtn.test = "Scan"
            self.getSongs()
        except:
            self.ids.direct.text = ''
            
    def savepath(self, path):
        f = open("sav.dat", "w")
        f.write(path)
        f.close()
        
    def dismiss_popup(self):
        content = ChooseFile(select=self.select, 
                             cancel=self.dimiss_pop)
        
        self._popup = Popup(title="Select Folder", content=content,
                            size_hint=(0.9, 0.9))
        
        self._popup.open()        
