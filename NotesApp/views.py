from django.shortcuts import render
from .models import NotesModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import NoteSerializer,NoteSerializerForGetPut
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import status
from rest_framework.generics import GenericAPIView


#---------------------- List and Create ApiView -----------------------
class NotesListView(GenericAPIView):
    serializer_class=NoteSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #-------------------- Get all Function ----------------
    def get(self,request,*args,**kwargs):
        notes=NotesModel.objects.filter(user=request.user.id)
        serializer=NoteSerializer(notes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #--------------------Post Function------------------
    def post(self,request,*args,**kwargs):
        
        data={
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'image':request.data.get('image'),
            'user':request.user.id,
            
        }
        serializer=NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#-----------------------Get-Update-delete ApiView--------------------
class NotesDetailView(GenericAPIView):
    serializer_class=NoteSerializerForGetPut
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #-------------------Get Function--------------
    def get_object(self,pk,user_id=None):
        try:
            if user_id is None:
                return NotesModel.objects.get(id=pk)
            else:
                return NotesModel.objects.get(id=pk,user=user_id)


        except NotesModel.DoesNotExist:
            return None

    def get(self,request,pk,*args, **kwargs):        
        if request.user.id==None:
            note_instance=self.get_object(pk)
        else:
            note_instance=self.get_object(pk,request.user.id)
        if not note_instance:
            return Response(
                {"res": "Notes does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer=NoteSerializer(note_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

    #--------------------Update Function------------------
    def put(self,request,pk ,*args,**kwargs):
        note_instance=self.get_object(pk,request.user.id)
        if not note_instance:
            return Response(
                {"res":"notes does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data={
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'image':request.data.get('image'),
            'user':request.user.id,
            
        }
        serializer=NoteSerializerForGetPut(instance=note_instance,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"updated successfully "},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #------------------Delete Function -----------------------
    def delete(self, request, pk, *args, **kwargs):
        note_instance = self.get_object(pk, request.user.id)
        if not note_instance:
            return Response(
                {"res": "Note does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        note_instance.delete()
        return Response(
            {"res": "Note has been deleted!"},
            status=status.HTTP_200_OK
        )