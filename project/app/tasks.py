from django.db.models import Count
from .models import *
import pandas as pd
from celery import shared_task

@shared_task()
def report_generator_function():
    dataset_sheet1 = list()
    queryset_sheet1 = Area.objects.all() \
        .annotate(discipline_count=Count('discipline')) \
        .order_by('-discipline_count')
    map(lambda n: n * 2, [1, 2, 3, 4, 5])

    for query1 in queryset_sheet1:
        try:
            curator = Curator.objects.filter(area=query1)[0].name
        except:
            curator = None
        dataset_sheet1.append(['Area:'+str(query1.title),'Curator: '+str(curator)])

        for subquery1 in Discipline.objects.filter(area=query1):
            dataset_sheet1.append(['Discipline: ' + str(subquery1.title),''])

    data_frame_sheet1 = pd.DataFrame(dataset_sheet1)

    dataset_sheet2 = list()
    max_students_amount = 20
    queryset_sheet2 = Group.objects.all() \
        .annotate(student_count=Count('student')) \
        .order_by('-student_count')
    # print(queryset_sheet2)

    for query2 in queryset_sheet2:
        try:
            area = Area.objects.filter(group=query2)[0].title
        except:
            area = None
        dataset_sheet2.append([query2.title, 'Area: ' + str(area),
                               "free_spaces: " + str(max_students_amount - Student.objects.filter(group=query2).count()),
                               "males: " + str(Student.objects.filter(group=query2).filter(sex='male').count()),
                               "females: " + str(Student.objects.filter(group=query2).filter(sex='female').count())])

        for subquery2 in Student.objects.filter(group=query2):
            dataset_sheet2.append(['Student: ' + str(subquery2.name), '', '', '', ''])

    data_frame_sheet2 = pd.DataFrame(dataset_sheet2)

    with pd.ExcelWriter("report/report.xlsx") as writer:
        data_frame_sheet1.to_excel(writer, sheet_name="Sheet1", index=False)
        data_frame_sheet2.to_excel(writer, sheet_name="Sheet2", index=False)


