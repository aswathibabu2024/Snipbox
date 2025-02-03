from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.shortcuts import render, get_object_or_404

from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer

# Create your views here.


class SnippetViewSet(viewsets.ModelViewSet):
    """Snippet view for create and retrieve snippets"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagListViewset(viewsets.ModelViewSet):
    """viewset for listing snippets"""

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tag = get_object_or_404(Tag, pk=pk)
        snippets = tag.snippet_set.filter(created_by=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
