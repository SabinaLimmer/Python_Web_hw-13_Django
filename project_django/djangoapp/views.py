from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag
from django.contrib.auth import logout

def main(request):
    quotes = Quote.objects.all()
    return render(request, 'djangoapp/main.html', {'quotes': quotes})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:main')
        form = AuthorForm()
    return render(request, 'djangoapp/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:main')
        form = QuoteForm()
    return render(request, 'djangoapp/add_quote.html', {'form': form})

def view_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'djangoapp/view_author.html', {'author': author})

def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'djangoapp/all_authors.html', {'authors': authors})

def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'djangoapp/all_quotes.html', {'quotes': quotes})

def logout_user(request):
    logout(request)
    return redirect('users:login')