from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  serializers

from staff.models import Doctor


# Create your views here.

class DoctorCreateListView(APIView):
  
  def get(self,request):
    
    qs = Doctor.objects.all().values()
    
    doctors_list = list(qs)
    
    return Response(data=doctors_list)
  
  def post(self,request):
    
    form_data = request.data
    
    specialization = form_data.get("specialization")
    
    flat = [tp[0] for tp in Doctor.SPECIALIZATION_OPTIONS]
        
    if specialization not in flat:
      
      raise serializers.ValidationError(specialization+"is invalid choice")
    
    fee = form_data.get("fee")
    
    if fee > 1500:
      
      raise serializers.ValidationError("fee is invalid , it should be below 1500")
    
    Doctor.objects.create(**form_data)
    
    response_data = {"message":"Doctor Added.."}
    
    return Response(response_data)
  
class DoctorRetrieveUpdateDeleteView(APIView):
  
  def get(self,request,pk=None):
    
    qs = Doctor.objects.filter(id=pk).values()
    
    doctor_list = list(qs)
    
    return Response(data=doctor_list)
  
  def put(self,request,pk=None):
    
    form_data = request.data
    
    specialization = form_data.get("specialization")
      
    flat = [tp[0] for tp in Doctor.SPECIALIZATION_OPTIONS]
        
    if specialization not in flat:
      
      raise serializers.ValidationError(specialization+"is invalid choice")
    
    fee = form_data.get("fee")
    
    if fee > 1500:
      
      raise serializers.ValidationError("fee is invalid , it should be below 1500")
    
    Doctor.objects.filter(id=pk).update(**form_data)
    
    return Response(data={"message":"doctor data updated"})
  
  def delete(self,request,pk=None):
    
    Doctor.objects.filter(id=pk).delete()
    
    return Response({"message":"Doctor deleted"})