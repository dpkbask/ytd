from kivy.app import App

from kivy.uix.screenmanager import ScreenManager,Screen

from kivy.lang import Builder

import pafy

import threading as th

loaded_kivy = Builder.load_file("style.kv")

class WindowManager(ScreenManager):pass

wm = WindowManager()

download_location = "."

class PathSelect(Screen):
    def setPath(self,download_path):
        global download_location
        download_location = download_path.path
        wm.current = "ytd"
        
class YouTubeDownloader(Screen):
    def downloadByThread(self,link):
        download_thread = th.Thread(
            name = "DownloadThread",
            target= self.download,
            args=(link,)
        )
        download_thread.start()

    def download(self,link):
        self.sts.text = "Downloading is going on please wait...."
        media = pafy.new(link)
        media.getbest().download(filepath=download_location,quiet=True)
        self.sts.text = f"file downloaded at {download_location}"
        
ps = PathSelect(name="ps")
ytd = YouTubeDownloader(name="ytd")

wm.add_widget(ps)
wm.add_widget(ytd)

wm.current = "ytd"

class MainApp(App):
    def build(self):
        return wm

MainApp().run()

