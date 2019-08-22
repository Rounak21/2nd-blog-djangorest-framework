from django.urls import path,include
#from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)
'''
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
'''
urlpatterns=[
    path('',include(router.urls)),
    ]
'''
    path('snippets/', snippet_list.as_view(),name='snippet-list'),
    path('snippets/<int:pk>', snippet_detail,name='snippet-detail'),
    path('users/', user_list,name='user-list'),
    path('users/<int:pk>/', user_detail,name='user-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight,name='snippet-highlight'),
    #path('', views.api_root),
    ]
#urlpatterns = format_suffix_patterns(urlpatterns)
'''
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
