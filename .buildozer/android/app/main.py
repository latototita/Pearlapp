from kivy.app import App
from jnius import autoclass
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from android.runnable import run_on_ui_thread
from kivy.uix.widget import Widget
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])




WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

screen_helper = """

ScreenManager:
    NoInternetScreen:

<NoInternetScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Try Again'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'browser'
"""
screen = Builder.load_string(screen_helper)
class NoInternetScreen(Screen):
    pass
@run_on_ui_thread
def create_webview(*args):
    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    wvc = WebViewClient();
    webview.setWebViewClient(wvc);
    activity.setContentView(webview)
    webview.loadUrl('https://adsket.ml')

class Wv(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__functionstable__ = {}
        Clock.schedule_once(create_webview, 0)

sm = ScreenManager()
sm.add_widget(Wv(name='browser'))
sm.add_widget(NoInternetScreen(name='menu'))


class ServiceApp(App):
    def build(self):
        try:
            return Wv()
        except:
            return screen
        

if __name__ == '__main__':
    ServiceApp().run()