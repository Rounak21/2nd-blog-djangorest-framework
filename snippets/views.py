#from rest_framework import status
#from rest_framework import mixins
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer
#from django.http import Http404
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Snippetlist(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset=Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset= Snippet.objects.all()
    serializer_class= SnippetSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('UserList', request=request, format=format),
        'snippets': reverse('Snippetlist', request=request, format=format)
    })
'''
