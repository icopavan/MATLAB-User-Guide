from django.conf.urls import patterns, url
import api_docs.views

urlpatterns = patterns(
   '',
    url("(?P<user_guide_chapter>line-and-scatter-plots-tutorial)/$", api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>introduction)/$", api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>user-guide)/$", api_docs.views.user_guide_template),
    url("(?P<user_guide_chapter>overview)/$", api_docs.views.user_guide_template)
)
