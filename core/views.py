from django.shortcuts import redirect

from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import FacadeForm
from .models import Location
from django.contrib import messages
import requests


API_key = ''  # put a key of a weather API from openweathermap.org

class WeatherView(FormView):

    # C - city | CS - city, state | CSC - cidade, state, country
    urls = {
        'C': 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_key,
        'CS': 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid=' + API_key,
        'CSC': 'https://api.openweathermap.org/data/2.5/weather?q={},{},{}&units=metric&appid=' + API_key
    }

    template_name = 'weather.html'
    form_class = FacadeForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):

        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()

        locations = Location.objects.all()
        weather_data = []

        for location in locations:

            city = location.city
            state = location.state
            country = location.country

            # if the request will use, besides the city, state or state and country,
            if location.have_state():
                if location.have_country():
                    r = requests.get(self.urls['CSC'].format(city, state, country)).json()
                r = requests.get(self.urls['CS'].format(city, state)).json()
            else:
                r = requests.get(self.urls['C'].format(city)).json()

            weather_city = {
                'city': location.city,
                'pk': location.pk,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }

            weather_data.append(weather_city)

        kwargs['weather_data'] = weather_data

        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):

        def not_blank(places):
            """
            Não permitir entradas que deixam a entrada
            da cidade, estado ou país como ''.
            """
            for place in places:
                if place == '':
                    return False
            return True

        form = FacadeForm(request.POST)

        if form.is_valid():

            location = form.cleaned_data['location']
            location = location.split(',')

            if not_blank(location):
                location = Location(None, *location)
                location.save()
                return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        form = FacadeForm()
        messages.success(self.request, "Local adicionado com sucesso.")
        return super(WeatherView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao adicionar local.")
        return super(WeatherView, self).form_invalid(form)


def delete_location(request, pk):
    Location.objects.get(pk=pk).delete()
    return redirect('index')

