from django.db import models


TYPE1 = 1
TYPE2 = 2
TYPE3 = 3
TYPE_CHOICES = (
    (TYPE1, 'type1'),
    (TYPE2, 'type2'),
    (TYPE3, 'type3'),
)


class GodModel(models.Model):
    my_type = models.IntegerField(choices=TYPE_CHOICES)
    for_type1 = models.TextField(blank=True, null=True)
    for_type2 = models.CharField(max_length=255, blank=True, null=True)
    for_type3 = models.IntegerField(blank=True, null=True)
