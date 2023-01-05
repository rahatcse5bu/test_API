from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Importing Models 
from CSE.models import Student
from CSE.models import User
from CSE.models import Invoice
from CSE.models import Product
from CSE.models import Category
from CSE.models import Online_Payment
from CSE.models import Store
from CSE.models import Invoice_Product
from CSE.models import Notification
# Importing Serializers
from CSE.serializers import StudentSerializer
from CSE.serializers import UserSerializer
from CSE.serializers import InvoiceSerializer
from CSE.serializers import ProductSerializer
from CSE.serializers import CategorySerializer
from CSE.serializers import Online_PaymentSerializer
from CSE.serializers import StoreSerializer
from CSE.serializers import NotificationSerializer


from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

@csrf_exempt
def student_list(request):
 
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, roll):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.get(roll=roll)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@csrf_exempt
def user_list(request):
 
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create_user(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt
def user_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)
@csrf_exempt
def delete_user(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(id=id)
        if request.method == 'DELETE':
            snippet.delete()
            return JsonResponse(status=204)
    except Exception as e:
        return HttpResponse(status=404)


#partial Update..................
@api_view(["PUT"])
def UserUpdate(request, id):
    try:
        snippet = User.objects.get(id=id)
        serializer = UserSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    except Exception as e:
        return Response(status=404)



# class based view for Student
class ClassBasedStudentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassedBasedStudentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, roll):
        try:
            return Student.objects.get(roll=roll)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, roll, format=None):
        snippet = self.get_object(roll)
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, roll, format=None):
        snippet = self.get_object(roll)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, roll, format=None):
        snippet = self.get_object(roll)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentList1(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetail1(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Invoice Section Starts here
@csrf_exempt
def generate_invoice(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




# Invoice Section Ends Here


# Products Section Starts here 

@csrf_exempt
def product_list(request):
 
    if request.method == 'GET':
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create_product(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt
def single_product_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Product.objects.get(ID=id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(snippet)
        return JsonResponse(serializer.data)
@csrf_exempt
def delete_product(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Product.objects.get(ID=id)
        if request.method == 'DELETE':
            snippet.delete()
            res= {"message":"Product Deleted!",status:204}
            return JsonResponse(res)
    except Exception as e:
        res= {"message":"Product Deleted!",'status':404}
        return JsonResponse(res)


#partial Update..................
@api_view(["PUT"])
def update_product(request, id):
    try:
        snippet = Product.objects.get(ID=id)
        serializer = ProductSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    except Exception as e:
        return JsonResponse(status=404)


# Product Section Ends 



# Products Section Starts here 

@csrf_exempt
def category_list(request):
 
    if request.method == 'GET':
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create_category(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt
def single_category_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Category.objects.get(ID=id)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(snippet)
        return JsonResponse(serializer.data)
@csrf_exempt
def delete_category(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Category.objects.get(ID=id)
        if request.method == 'DELETE':
            snippet.delete()
            res= {"message":"Product Deleted!",status:204}
            return JsonResponse(res)
    except Exception as e:
        res= {"message":"Product Deleted!",'status':404}
        return JsonResponse(res)


#partial Update..................
@api_view(["PUT"])
def update_category(request, id):
    try:
        snippet = Category.objects.get(ID=id)
        serializer = CategorySerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    except Exception as e:
        return JsonResponse(status=404)


