from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('simon/home.html',
                             context_instance=context)
# end home

@login_required() 
def simon(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('simon/game.html',
                             context_instance=context)
# end simon