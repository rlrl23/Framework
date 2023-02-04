
from urls import urls, fronts
from views import error_view


class App():
     def __init__(self, urls, fronts):
          self.urls=urls
          self.fronts=fronts

     def __call__(self, environ, start_response):
          request = {}
          for front in fronts:
               front(request)
          path=environ['PATH_INFO']
          if path in self.urls:
               view=urls[path]
               answer, data = view(request)
          else:
               answer, data = error_view(request)

          start_response(answer, [
          ("Content-Type", "text/html"),
          ("Content-Length", str(len(data)))
          ])
          return [data]

