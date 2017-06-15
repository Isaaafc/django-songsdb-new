from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddForm, SearchForm
from .models import Author, Publisher, Type, Song, WTime
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def add_song(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            song_id = request.POST.get('song_id') 
            name = form.cleaned_data['song_name']
            link = form.cleaned_data['document_link']
            song_year = form.cleaned_data['year']
            author = form.cleaned_data['author']
            author_choice = form.cleaned_data['author_choice']
            publisher = form.cleaned_data['publisher']
            publisher_choice = form.cleaned_data['publisher_choice']
            song_type = form.cleaned_data['song_type']
            type_choice = form.cleaned_data['type_choice']

            if author_choice is not None:
                new_author, created = Author.objects.get_or_create(author_name=author_choice)
            elif author is not None:
                new_author, created = Author.objects.get_or_create(author_name=author)
            else:
                new_author, created = Author.objects.get_or_create(author_name='--')

            if publisher_choice is not None:  
                new_publisher, created = Publisher.objects.get_or_create(publisher_name=publisher_choice)
            elif publisher is not None:
                new_publisher, created = Publisher.objects.get_or_create(publisher_name=publisher)
            else:
                new_publisher, created = Publisher.objects.get_or_create(publisher_name='--')
            
            if type_choice is not None:
                new_type, created = Type.objects.get_or_create(desc=type_choice)
            elif song_type is not None:
                new_type, created = Type.objects.get_or_create(desc=song_type)
            else:
                new_type, created = Type.objects.get_or_create(desc='--')
            
            new_song, created = Song.objects.get_or_create(song_name=name,document_link=link,year=song_year,author=new_author,publisher=new_publisher,song_type=new_type)
                        
            return HttpResponseRedirect('/view_songs')
        else:
            return render('404.html')
    else:
        form = AddForm()
    return render(request, 'add.html', {'form' : form})

def view_songs(request):
    if request.method == 'GET':
        form = SearchForm()
        order = request.GET.get('order_by', 'song_name')
        page = request.GET.get('page', 1)
        
        query_result = Song.objects.all().order_by(order)
        paginator = Paginator(query_result, 255555)
        
        try:
            song_list = paginator.page(page)
        except PageNotAnInteger:
            song_list = paginator.page(1)
        except EmptyPage:
            song_list = paginator.page(paginator.num_pages)

        return render(request, 'view_songs.html', {'songs' : song_list, 'form' : form, 'order_by': order})
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['search_bar']
            search_field = form.cleaned_data['search_field']
            query_result = None
            if search_field=='year':
                strsplit = keyword.split('-')
                try:
                    start_year = int(strsplit[0])
                    if len(strsplit) > 1:
                        end_year = int(strsplit[1])
                        if end_year >= start_year:
                            query_result = Song.objects.filter(year__gte=start_year, year__lte=end_year)
                    else:
                        query_result = Song.objects.filter(year=start_year)  
                except ValueError:
                    return render(request, 'view_songs.html', {'form' : form})
            elif search_field=='name':
                query_result = Song.objects.filter(song_name__contains=keyword)
            elif search_field=='author':
                query_result = Song.objects.filter(author__contains=keyword)
            elif search_field=='publisher':
                query_result = Song.objects.filter(publisher__contains=keyword)
            elif search_field=='type':
                query_result = Song.objects.filter(song_type__contains=keyword)

            return render(request, 'view_songs.html', {'songs' : query_result, 'form' : form})

def edit_song(request):
    if request.method == 'GET':
        song_id = request.GET.get('song_id')
        song = Song.objects.get(pk=song_id)
        form = AddForm(initial={'song_name' : song.song_name, 'document_link' : song.document_link,
                       'year' : song.year, 'author' : song.author, 'publisher' : song.publisher, 'song_type' : song.song_type})
        return render(request, 'edit_song.html', {'form' : form, 'song_id' : song_id})
    else:
        form = AddForm(request.POST)
        if form.is_valid():
            song_id = request.POST.get('song_id') 
            name = form.cleaned_data['song_name']
            song_link = form.cleaned_data['document_link']
            song_year = form.cleaned_data['year']
            author = form.cleaned_data['author']
            author_choice = form.cleaned_data['author_choice']
            publisher = form.cleaned_data['publisher']
            publisher_choice = form.cleaned_data['publisher_choice']
            song_type = form.cleaned_data['song_type']
            type_choice = form.cleaned_data['type_choice']
            
            if author_choice is not None:
                new_author, created = Author.objects.get_or_create(author_name=author_choice)
            elif author is not None:
                new_author, created = Author.objects.get_or_create(author_name=author)
            else:
                new_author, created = Author.objects.get_or_create(author_name='--')

            if publisher_choice is not None:  
                new_publisher, created = Publisher.objects.get_or_create(publisher_name=publisher_choice)
            elif publisher is not None:
                new_publisher, created = Publisher.objects.get_or_create(publisher_name=publisher)
            else:
                new_publisher, created = Publisher.objects.get_or_create(publisher_name='--')
            
            if type_choice is not None:
                new_type, created = Type.objects.get_or_create(desc=type_choice)
            elif song_type is not None:
                new_type, created = Type.objects.get_or_create(desc=song_type)
            else:
                new_type, created = Type.objects.get_or_create(desc='--')

            song = Song.objects.get(pk=song_id)
            song.song_name = name
            song.document_link = song_link
            song.year = song_year
            song.author = new_author
            song.publisher = new_publisher
            song.song_type = new_type
            song.save()
        return HttpResponseRedirect('/view_songs')
    return render(request, '404.html')

def delete_song(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        song = Song.objects.get(pk=song_id)
        song.delete()
        return HttpResponseRedirect('/view_songs')
    return render(request, '404.html')

def log_time(request):
    time_stamp = long(request.GET.get('t'))
    user = int(request.GET.get('uid'))
    onl = bool(request.GET.get('online'))
    dt_time = datetime.fromtimestamp(time_stamp) + timedelta(hours=8)
    new_row = WTime(user_id=user, time_stamp=dt_time, online=onl)
    new_row.save()
    return render(request, '404.html')

def show_log_time(request):
    user = int(request.GET.get('uid'))
    query_result = WTime.objects.filter(user_id=user)
    return render(request, 'show_time.html', {'result' : query_result})

