from django.shortcuts import redirect

from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import FacadeForm
from .models import Location
from django.contrib import messages
import requests


API_key = '8f6f5609468ff4a8281eb49c77e9fde4'  # put a key of a weather API from openweathermap.org

class WeatherView(FormView):

    # CSC - city, state, country
    urls = {
        'CSC': 'https://api.openweathermap.org/data/2.5/weather?q={},{},{}&units=metric&lang=pt&appid=' + API_key
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
            r = requests.get(self.urls['CSC'].format(city, state, country)).json()

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
            Do not allow inputs of city, state and county like ''.
            """
            for place in places:
                if place == '':
                    return False
            return True

        locations = Location.objects.all()
        form = FacadeForm(request.POST)

        if form.is_valid():

            location = form.cleaned_data['location'].lower()
            location = location.split(',')

            if not_blank(location):

                location_obj = Location(None, *location)

                # if local searched doesn't exist
                if requests.get(self.urls['CSC'].format(location[0], location[1], location[2])).json()['cod'] != 200:
                    return self.form_invalid(form, message="Local inválido.")

                for obj in locations:

                    citys = [obj.city, location_obj.city]
                    states = [obj.state, location_obj.state]
                    countrys = [obj.country, location_obj.country]

                    # erase void strings in values
                    citys = [citys[0].replace(' ', ''), citys[1].replace(' ', '')]
                    states = [states[0].replace(' ', ''), states[1].replace(' ', '')]
                    countrys = [countrys[0].replace(' ', ''), countrys[1].replace(' ', '')]

                    # if the location sought alredy exist in Location
                    if citys[0] == citys[1] and states[0] == states[1] and countrys[0] == countrys[1]:
                        return self.form_invalid(form, message="Lugar procurado já pertence a lista de lugares.")

                location_obj.save()
                return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        form = FacadeForm()
        return super(WeatherView, self).form_valid(form)

    def form_invalid(self, form, message="Erro ao adicionar local."):
        messages.error(self.request, message)
        return super(WeatherView, self).form_invalid(form)


def delete_location(request, pk):
    Location.objects.get(pk=pk).delete()
    return redirect('index')

