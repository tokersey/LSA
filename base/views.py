from base.forms import (LoginForm, ContactForm, RegistrationForm)
from base.models import Contact
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'base/index.html', {
            'contacts': Contact.objects.all(),
            'form': form
        })


@csrf_protect
def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
        data = RequestContext(request, {
            'form': form
        })

    return render_to_response(
        'base/register.html',
        data,
    )


def loginView(request):
    # if user is already logged in, send directly to homepage
    if request.user.is_authenticated():
        return redirect('/')

    # form validation handles authenticating user
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            authed_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, authed_user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'base/login.html', {
        'form': form
    })


def logoutView(request):
    logout(request)
    return redirect('login')


@login_required
def contactDetailView(request, num):
    contact = get_object_or_404(Contact, pk=num)

    return render(request, 'base/detail.html', {
        'contact': contact
    })


@login_required
def contactDeleteView(request, num):
    contact = Contact.objects.filter(pk=num)

    contact.delete()

    return render(request, 'base/delete.html')


@login_required
def searchListView(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            contacts = Contact.objects.search(q)
            return render(request, 'base/search.html', {'contacts': contacts, 'query': q})
    return render(request, 'base/search.html', {'error': error})
