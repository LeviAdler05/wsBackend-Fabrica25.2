from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime, Quote
from .forms import AnimeForm, QuoteForm

def anime_list(request):
    animes = Anime.objects.all().order_by('titulo')
    return render(request, "appanime/anime_list.html", {"animes": animes})

def anime_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    quotes = anime.quotes.all()
    form = QuoteForm()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.anime = anime
            new_quote.save()
            return redirect('appanime:anime_detail', pk=anime.pk)

    context = {
        'anime': anime,
        'quotes': quotes,
        'form': form
    }
    return render(request, "appanime/anime_detail.html", context)

def anime_create(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appanime:anime_list')
    else:
        form = AnimeForm()
    return render(request, 'appanime/anime_form.html', {'form': form})

def anime_update(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        form = AnimeForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('appanime:anime_list')
    else:
        form = AnimeForm(instance=anime)
    return render(request, 'appanime/anime_form.html', {'form': form, 'edit': True})

def anime_delete(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        anime.delete()
        return redirect('appanime:anime_list')
    return render(request, 'appanime/anime_confirm_delete.html', {'anime': anime})