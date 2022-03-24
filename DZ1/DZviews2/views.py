from django.shortcuts import render
from django.db.models import F, Max, Min, Avg
from .models import Movie

# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))

    return render(request, 'all_movies.html', context={
        'movies':movies,
        'agg':agg,

    })
