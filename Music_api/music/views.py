from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .serializers import MusicSerializer
from .models import Music
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# class MusicListView(APIView):
#     def get(self, request):
#         queryset = Music.objects.all()
#         paginator = LimitOffsetPagination()
#         result = paginator.paginate_queryset(queryset=queryset, request=request)
#         serializer = MusicSerializer(instance=result, many=True, context={"request": request})
#         return Response(serializer.data)
#
#
# class MusicDetailView(APIView):
#     def get(self, request, pk):
#         instance = Music.objects.get(id=pk)
#         serializer = MusicSerializer(instance=instance)
#         return Response(serializer.data)
#
#
# class AddMusicView(APIView):
#
#     def post(self, request):
#         serializer = MusicSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.validated_data['user'] = request.user
#             serializer.save()
#             return Response({"response": "Added"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UpdateMusicView(APIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]
#
#     def put(self, request, pk):
#         instance = Music.objects.get(id=pk)
#         serializer = MusicSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.update(instance=instance, validated_data=serializer.validated_data)
#             return Response({"Response": "Updated"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         instance = Music.objects.get(id=pk)
#         instance.delete()
#         return Response({"Response": "Deleted"})
#
#
# class MusicCommentsView(APIView):
#     def get(self,request, pk):
#         comments = Music.objects.get(id=pk).comments.all()
#         serializer = CommentSerializer(instance=comments, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)





class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)