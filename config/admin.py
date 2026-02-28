from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    """
    Кастомный класс админ-сайта для приложения Document Service.

    Атрибуты:
    - site_header: заголовок верхней панели сайта администрирования.
    - site_title: заголовок окна браузера для админки.
    - index_title: заголовок главной страницы админки.
    """

    site_header = "Document Service Administration"
    site_title = "Панель администратора"
    index_title = "Добро пожаловать, администратор"


# Экземпляр кастомного админ-сайта, который можно использовать вместо стандартного admin.site
admin_site = MyAdminSite(name="myadmin")
