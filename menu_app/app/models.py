from django.db import models


# Create your models here.


class TreeMenuCategory(models.Model):
    TAG = {
        'name': 'Name',
        'expanded_name': 'Expanded name'
    }

    name = models.CharField(TAG['name'], max_length=250, blank=True, null=False)
    expanded_name = models.CharField(TAG['expanded_name'], max_length=250, blank=True, null=False)

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.expanded_name


class TreeMenu(models.Model):
    TAG = {
        'name': 'Name',
        'category': 'Category',
        'path': 'Link',
        'parent': 'Parent element'
    }

    name = models.CharField(TAG['name'], max_length=250, blank=True, null=False)

    category = models.ForeignKey(
        TreeMenuCategory,
        verbose_name=TAG['category'],
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField(TAG['path'], max_length=500, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=TAG['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.name
