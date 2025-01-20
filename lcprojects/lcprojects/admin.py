from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse

class MyAdminSite(admin.AdminSite):
    site_header = "LC Projects Admin"
    site_title = "LC Projects Admin Portal"
    index_title = "Welcome to LC Projects Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.custom_index), name='index'),
        ]
        return custom_urls + urls

    def custom_index(self, request):
        context = dict(
            self.each_context(request),
            title=self.index_title,
        )
        return TemplateResponse(request, "admin/custom_index.html", context)

admin_site = MyAdminSite(name='myadmin')