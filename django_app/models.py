from django.db import models

NULLABLE = {'null': True, 'blank': True, }


class Menu(models.Model):
    """модель Menu позволяет хранить информацию о пунктах меню и их иерархии"""
    menu_item_name = models.CharField(max_length=50, verbose_name='название пункта меню')
    menu_item_reference = models.CharField(max_length=100, **NULLABLE, verbose_name='ссылка на пункт меню')
    parent_menu_item = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, **NULLABLE,
                               verbose_name='родительский пункт меню')

    def __str__(self):
        return self.menu_item_name

