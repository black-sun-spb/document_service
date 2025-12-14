from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Document Service Administration"
    site_title = "Панель администратора"
    index_title = "Добро пожаловать, администратор"

admin_site = MyAdminSite(name='myadmin')
