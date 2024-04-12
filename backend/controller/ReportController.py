from django.urls import path
from ..view.ReportView import createReport, editReport, deleteReport, listReports,getReportFromId

urlpatterns = [
    path('criar/', createReport, name='createReport'),
    path('editar/', editReport, name='editReport'),
    path('remover/', deleteReport, name='removeReport'),
    path('listar/', listReports, name='getAllReportsFromABook'),
    path('id/', getReportFromId, name='getAReport'),
]