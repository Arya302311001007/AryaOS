import webview

def open_browser(url="https://www.google.com"):
    webview.create_window("AryaOS Browser", url, width=1000, height=700)
    webview.start()