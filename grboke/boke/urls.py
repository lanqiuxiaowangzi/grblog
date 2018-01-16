from django.conf.urls import url
from boke import views
urlpatterns=[
    # url(r'^$',views.index_view),
    url(r'^$',views.PostPage),
    url(r'^index/$',views.PostPage),
    url(r'^index/(\d*)$',views.PostPage),
    # url(r'^category/(\d*)$',views.PostPage),
    url(r'^boke/details/(\d+)$',views.post_details_view),
    url(r'^guidang/$',views.index_guidang),
    url(r'^category/(\d+)$',views.category_details_view),
    url(r'^archive/(\d+)/(\d+)$',views.date_details_view),

]