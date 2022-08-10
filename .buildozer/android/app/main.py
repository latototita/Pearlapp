from kivy.app import App
from jnius import autoclass
from kivy.clock import Clock
from android.runnable import run_on_ui_thread
from kivy.uix.widget import Widget

from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])


WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

@run_on_ui_thread
def create_webview(*args):
	webview = WebView(activity)
	webview.getSettings().setJavaScriptEnabled(True)
	wvc = WebViewClient();
	webview.setWebViewClient(wvc);
	activity.setContentView(webview)
	webview.loadUrl('https://pearlmart.ml')


class Wv(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__functionstable__ = {}
		Clock.schedule_once(create_webview, 10)


class ServiceApp(App):
	def build(self):
		return Wv()

if __name__ == "__main__":
    ServiceApp().run()
