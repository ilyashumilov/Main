from .tasks import report_generator_function
from rest_framework.response import Response
from rest_framework.views import APIView
from celery.result import AsyncResult
from django.http import FileResponse
from rest_framework import status
from project.celery import app
from .serializers import *
from .models import *

# Create your views here.

class AreaAPIView(APIView):
    def get(self, request):
        queryset = Area.objects.all()
        serializer = AreaSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The new Area instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Area.objects.get(pk=request.query_params['id'])
            print(instance)
            instance.delete()
            return Response({"message": f"The Area instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Area instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class CuratorAPIView(APIView):
    def get(self, request):
        queryset = Curator.objects.all()
        serializer = CuratorSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):

        # cheking if Area instance with passed id exists
        try:
            Area.objects.get(pk=request.data['area_id'])
        except ObjectDoesNotExist:
            return Response({'error': 'Area instance with that id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CuratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The new Curator instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Curator.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response({"message": f"The Curator instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Curator instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class DisciplineAPIView(APIView):
    def get(self, request):
        queryset = Discipline.objects.all()
        serializer = DisciplineSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):

        # cheking if Area instance with passed id exists
        try:
            Area.objects.get(pk=request.data['area_id'])
        except ObjectDoesNotExist:
            return Response({'error': 'Area instance with that id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The new Discipline instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Discipline.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response(
                {"message": f"The Discipline instance with id {request.query_params['id']} has been deleted"},
                status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Discipline instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class GroupAPIView(APIView):
    def get(self, request):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):

        # cheking if Area instance with passed id exists
        try:
            Area.objects.get(pk=request.data['area_id'])
        except ObjectDoesNotExist:
            return Response({'error': 'Area instance with that id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The new Group instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Group.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response({"message": f"The Group instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Group instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):

        # cheking if Group instance with passed id exists
        try:
            Group.objects.get(pk=request.data['group_id'])
        except ObjectDoesNotExist:
            return Response({'error': 'Group instance with that id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The new Student instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Student.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response({"message": f"The Student instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Student instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

class ReportCreateAPIView(APIView):
    def post(self, request):
        res=report_generator_function.delay()
        return Response({'message': 'The report has been scheduled to be generated',
                         'task_id':res.id}, status=status.HTTP_200_OK)

def retrieve_report(request):
    return FileResponse(open('project/report/report.xlsx', 'rb'), as_attachment=True, filename="report.xlsx")

class task_status_checkAPIView(APIView):
    def post(self, request):
        res = AsyncResult(request.data['task_id'], app=app)
        return Response({"Task's status": res.status}, status=status.HTTP_200_OK)