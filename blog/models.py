from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Neighborhood(models.Model):
    name = models.CharField(db_column='Neighborhood', max_length=100)
    cluster_label_com = models.IntegerField(db_column='Cluster Label Common', blank=True, null=True)
    cluster_label_pop = models.IntegerField(db_column='Cluster Label Popular', blank=True, null=True)
    zillow_value = models.IntegerField(db_column='Zillow Home Value Index', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Mostcommon(models.Model):
    neigh = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, related_name='comRest')
    number_1st_most_common_venue = models.CharField(db_column='1st Most Common Venue', max_length=100, blank=True, null=True)
    number_2nd_most_common_venue = models.CharField(db_column='2nd Most Common Venue', max_length=100, blank=True, null=True)
    number_3rd_most_common_venue = models.CharField(db_column='3rd Most Common Venue', max_length=100, blank=True, null=True)
    number_4th_most_common_venue = models.CharField(db_column='4th Most Common Venue', max_length=100, blank=True, null=True)
    number_5th_most_common_venue = models.CharField(db_column='5th Most Common Venue', max_length=100, blank=True, null=True)
    number_6th_most_common_venue = models.CharField(db_column='6th Most Common Venue', max_length=100, blank=True, null=True)
    number_7th_most_common_venue = models.CharField(db_column='7th Most Common Venue', max_length=100, blank=True, null=True)
    number_8th_most_common_venue = models.CharField(db_column='8th Most Common Venue', max_length=100, blank=True, null=True)
    number_9th_most_common_venue = models.CharField(db_column='9th Most Common Venue', max_length=100, blank=True, null=True)
    number_10th_most_common_venue = models.CharField(db_column='10th Most Common Venue', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.neigh.name)

class Mostpopular(models.Model):
    neigh = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, related_name='popRest')
    number_1st_most_popular_venue = models.CharField(db_column='1st Most Common Venue', max_length=100, blank=True, null=True)
    number_2nd_most_popular_venue = models.CharField(db_column='2nd Most Common Venue', max_length=100, blank=True, null=True)
    number_3rd_most_popular_venue = models.CharField(db_column='3rd Most Common Venue', max_length=100, blank=True, null=True)
    number_4th_most_popular_venue = models.CharField(db_column='4th Most Common Venue', max_length=100, blank=True, null=True)
    number_5th_most_popular_venue = models.CharField(db_column='5th Most Common Venue', max_length=100, blank=True, null=True)
    number_6th_most_popular_venue = models.CharField(db_column='6th Most Common Venue', max_length=100, blank=True, null=True)
    number_7th_most_popular_venue = models.CharField(db_column='7th Most Common Venue', max_length=100, blank=True, null=True)
    number_8th_most_popular_venue = models.CharField(db_column='8th Most Common Venue', max_length=100, blank=True, null=True)
    number_9th_most_popular_venue = models.CharField(db_column='9th Most Common Venue', max_length=100, blank=True, null=True)
    number_10th_most_popular_venue = models.CharField(db_column='10th Most Common Venue', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.neigh.name)


class Both(models.Model):
    neigh = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, related_name='popComRest')
    first_most_popular_venue = models.CharField(max_length=100, blank=True, null=True)
    first_most_common_venue = models.CharField(max_length=100, blank=True, null=True)
    second_most_popular_venue = models.CharField(max_length=100, blank=True, null=True)
    second_most_common_venue = models.CharField(max_length=100, blank=True, null=True)
    third_most_popular_venue = models.CharField(max_length=100, blank=True, null=True)
    third_most_common_venue = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.neigh.name)