from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from django import forms
from iepg.models import Title, Comments, Program, Favorites
from iepg import tvpilib as itv 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
import datetime
from datetime import datetime as dt
#from django.views.decorators.csrf import csrf_exempt

#authsystem
def idx(request):
    if request.user.is_authenticated():
        t = loader.get_template('login_on.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
    else:
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
#login = csrf_exempt(login)
        
def index(request):
    if request.user.is_authenticated():
        latest_program_list = Program.objects.all()[:60]
        usr_id = User.objects.get(username=request.user.username)
        try:
            fav_list = Favorites.objects.filter(user = usr_id).get()
            return render_to_response('iepg/index.html',
                                      {'latest_program_list':latest_program_list,
                                       'fvl':fav_list,
                                       'usr':usr_id}
                                      )
        except:
            return render_to_response('iepg/index.html',
                                      {'latest_program_list':latest_program_list,
                                       'usr':usr_id}
                                      )

    else:
        #return render_to_response('login.html',{},
                                  #context_instance=RequestContext(request)
        #                          )
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

def sta(request, station):
    if request.user.is_authenticated():
        #    current_time = dt.now()
        #    sp1 = Program.objects.all().order_by(datetime('end')>=current_time)
        sp1_list = Program.objects.filter(station = station)[:30]
        return render_to_response('iepg/sta.html',
                                  {'stp_list':sp1_list})
    else:                          
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

#def g1(request, gen_1):
#    g1_program_list = Program.objects.filter(pk = gen_1)[:30]
#    return render_to_response('iepg/g1.html',
#                              {'gen_1_program_list':g1_program_list})

def sg1(request, sgn_1):
    if request.user.is_authenticated():
        #    current_time = dt.now()
        #    sgp1 = Program.objects.all().order_by(datetime('end')>=current_time)
        sg1_program_list = Program.objects.filter(sgn_1 = sgn_1)[:30]
        return render_to_response('iepg/sgn_1.html',
                                  {'sgn_1_program_list':sg1_program_list})
    else:                          
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

def id(request, id):
    if request.user.is_authenticated():
        p_list = Program.objects.filter(pk = id)
        return render_to_response('iepg/id.html',
                                  {'ip_list':p_list})
    else:                          
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

def g1(request, gen_1):
    if request.user.is_authenticated():
        g1_list = Program.objects.filter(gen_1 = gen_1).order_by('start')[:30]
        return render_to_response('iepg/g1.html',
                                  {'ip_list':g1_list})
    else:                          
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

#def idx(request):
#  return HttpResponse("""
#   <h2>go mypage</h2>
#   <a href='/mypage/'>mypage</a><br />
#  <hr>
#   <h2>login</h2>
#     <form action='/enter/' method='post'>
#       name: <input type='text' name='name'><br />
#       pass: <input type='password' name='pass'><br />
#       <input type='submit' value='login'>
#     </form>
#  <hr>
#   <h2>logout</h2>
#     <a href='/out/'>logout</a>
#  <hr>
#    <h2>make new account</h2>
#    <form action='/make/' method='post'>
#      name: <input type='text' name='name'><br />
#      pass: <input type='password' name='pass'><br />
#      <input type='submit' value='make'>
#    </form>
#  """)
#
def make(request):
#    try:
    name = request.POST['name']
    password = request.POST['pass']       
    if len(name) < 1 or len(password) < 1:
        return HttpResponse("name or password is empty")
    if User.objects.filter(username=name):
        return HttpResponse(name + " is already used")
    else:
        user = User.objects.create_user(name,'', password)
        user.save()
        user = authenticate(username=name, password=password)
        login(request, user)
        return HttpResponseRedirect('/iepg/')
#    except:
#        return HttpResponse("Error")

def enter(request):
    try:
        user = authenticate(username=request.POST['name'], password=request.POST['pass'])
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/iepg/')
        else:
            return HttpResponse("could not log in<br><a href=/login/>return to main</a>")
    except:
        return HttpResponse("login error<br><a href=/login/>return to main</a>")
    
def out(request):
  logout(request)
  return HttpResponse("You have logged out<br><a href=/login/>return to main</a>")

def mypage(request):
  if not request.user.is_authenticated():
    return HttpResponse("you don't log in")
  else:
    return HttpResponse("Hello, '%s'" % request.user.username)

#def my_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            return render_to_response('iepg/index.html',
#                               {'latest_program_list':latest_program_list})
            # Redirect to a success page.
#        else:
            # Return a 'disabled account' error message
#    else:
        # Return an 'invalid login' error message.
#
#def logout_view(request):
#    logout(request)
#     Redirect to a success page.

def add(request):
    if request.user.is_authenticated():
        usr_id = User.objects.get(username=request.user.username)
        try:
            fav_list = Favorites.objects.filter(user = usr_id).get()
        except:
            pass
        #d = Favorites.objects.filter(user = usr_id).get()
        if request.method == 'POST':
            #c = {}
            #c.update(csrf(request))
            d = request.POST.getlist('fav')
            #d.update(csrf(request))
            try:
                fav_list = Favorites.objects.filter(user = usr_id).get()
                return render_to_response('iepg/index.html',
                                          {'fvl':fav_list,
                                           'usr':usr_id}, 
                                          context_instance=RequestContext(request))
            except:
                return render_to_response('iepg/index.html',
                                          {'usr':usr_id},
                                          context_instance=RequestContext(request))
        else:
            try:
                fav_list = Favorites.objects.filter(user = usr_id).get()
                return render_to_response('iepg/add.html',
                                          {'fvl':fav_list,
                                           'usr':usr_id},
                                          context_instance=RequestContext(request))
            except:
                return render_to_response('iepg/add.html',
                                          {'usr':usr_id},
                                          context_instance=RequestContext(request))
            
    else:                          
        t = loader.get_template('login_off.html')
        c = RequestContext(request)
        return HttpResponse(t.render(c))
