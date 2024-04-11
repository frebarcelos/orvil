from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from ..dao.BookDAO import BookDAO
from ..dao.ReportDAO import ReportDAO
from ..dao.UserDAO import UserDAO

@csrf_exempt
def createReport(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            bookId = data['IdDoLivro']
            userId = data['IdDoUsuario']
            report = data['Resumo']
            summary = data['Nota']
            if BookDAO.getBookById(bookId):
                if UserDAO.getUserById(userId):
                    ReportDAO.createReport(bookId,userId,report,summary)
                    returnedData = {'IdDoLivro':bookId,'IdDoUsuario':userId,'Resumo':report,'Nota':summary, 'Message' : 'Avaliado com sucesso!'}
                    return JsonResponse(returnedData, safe=False, status=201)
                return JsonResponse({'Error': 'Usuario inexistente'}, safe=False, status=400)
            return JsonResponse({'Erro': 'Livro inexistente'}, safe=False, status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def getReportFromId(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            report = ReportDAO.getReportById(id)
            if report:
                return JsonResponse({'Id' : report.id, 'Id do usuario' : report.userId, 'Id do Livro' : report.bookId, 'Resumo' : report.report, 'Avaliação': report.summary}, safe=False,status=200)
            return JsonResponse({'Error' : 'Report not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def editReport(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            report = data['Resumo']
            summary = data['Nota']
            reportObject = ReportDAO.getReportById(id)
            if reportObject:
                reportObject = ReportDAO.editReport(id,report, summary)
                if reportObject:
                    return JsonResponse({'Message' : 'Report edited successfully'}, safe=False,status=200)
            return JsonResponse({'Error' : 'Report not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def deleteReport(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            id = data['id']
            report = ReportDAO.getReportById(id)
            if report:
                deletedReport = ReportDAO.deleteReport(id)
                if deletedReport:
                    return JsonResponse({'Message' : 'Report deleted successfully'}, safe=False,status=200)
            return JsonResponse({'Error' : 'Report not found'}, safe=False, status=404)
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def listReports(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            bookId = data['idDoLivro']
            reports = ReportDAO.getAllReportsFromABooks(bookId)
            allReports =[]
            if reports:
                for report in reports:
                    allReports.append({'Id': report.id, 'Id do Livro': report.bookId, 'Id do Usuario': report.userId,
                                       'Resumo': report.report, 'Nota': report.summary})
                return JsonResponse(allReports, safe=False, status=200)

            return HttpResponse(status=404)

    else:
        return HttpResponse(status=405)



