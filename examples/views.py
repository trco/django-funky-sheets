from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from funky_sheets.formsets import HotView

from .models import Movie


def index(request):
    return HttpResponseRedirect(reverse('update'))


class CreateMovieView(HotView):
    model = Movie
    template_name = 'examples/create.html'
    prefix = 'table'
    success_url = reverse_lazy('update')
    fields = (
        'id',
        'title',
        'director',
        'release_date',
        'parents_guide',
        'imdb_rating',
        'genre',
        'imdb_link',
    )

    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true'
    }


class UpdateMovieView(CreateMovieView):
    template_name = 'examples/update.html'
    action = 'update'
    button_text = 'Update'

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true'
    }
