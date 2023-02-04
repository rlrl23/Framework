
from wsgiref.simple_server import make_server
from my_frame.main import App
from urls import urls, fronts


app=App(urls, fronts)

# with make_server('', 8000, app) as httpd:
#     print("Load port 8000")
#     httpd.serve_forever()