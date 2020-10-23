from django.db import models

class Location(models.Model):

    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100, blank=True, default='')
    country = models.CharField('País', max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return '{}, {}, {}'.format(str(self.city), str(self.state), str(self.country))

    def have_city(self):
        if self.city != '':
            return True
        return False

    def have_state(self):
        if self.state != '':
            return True
        return False

    def have_country(self):
        if self.country != '':
            return True
        return False