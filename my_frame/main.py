
from urls import urls, fronts
from views import error_view
import pprint

class App():
     def __init__(self, urls, fronts):
          self.urls=urls
          self.fronts=fronts

     def str_parser(self, query_string):
          result={}
          if query_string:
               data = query_string.split('&')
               for item in data:
                    key, val = item.split('=')
                    result[key] = val
          return result

     def get_wsgi_input_data(self, env):
          content_length_data=env.get('CONTENT_LENGTH')
          content_length=int(content_length_data) if content_length_data else 0
          data=env['wsgi.input'].read(content_length) if content_length > 0 else b''
          return data

     def byte_parser(self, data):
          result = {}
          if data:
               data_str=data.decode(encoding='utf-8')
               result=self.str_parser(data_str)
          return result

     def __call__(self, environ, start_response):
          request = {}
          method= environ['REQUEST_METHOD']
          if method=='GET':
               query_string=environ['QUERY_STRING']
               request['GET']= self.str_parser(query_string)
          elif method=='POST':
               data= self.get_wsgi_input_data(environ)
               request['POST']=self.byte_parser(data)

          pprint.pprint(environ)
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

          print(request)
          return [data]

