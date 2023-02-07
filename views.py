from my_frame.render import render

def home_view(request):
     page= render('templates/index.html', context=request)
     return "200 OK", page.encode('utf-8')

def about_view(request):
     page = render('templates/about.html')
     return "200 OK", page.encode('utf-8')

def contact_view(request):
     page = render('templates/contacts.html')
     try:
          print(request.get('POST'))
     except:
          pass
     return "200 OK", page.encode('utf-8')

def error_view(request):
     print(request)
     return "404 ", b'Not found'