from django.urls import path
from . import views
from django.conf.urls.static import static, settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.race_list, name='start_page'),
    path('prof_pick/', views.prof_list, name='prof_list',),
    path('stats/', views.stat_pick, name='stat_pick'),
    path('skills/', views.skill_pick, name="skill_pick"),
    path('character/', views.character_sheet, name='character_sheet'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
