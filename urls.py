from views import home_view, about_view, contact_view
import datetime

#Front controller

def secret_front(request):
     request['key']='secret key'
     return request

def time_front(request):
     request['year']=str(datetime.datetime.now().year)
     return request

fronts=[secret_front, time_front]

#Page controllers
urls={'/':home_view,
      '/about/':about_view,
      '/contacts/':contact_view}