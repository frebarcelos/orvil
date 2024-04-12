from backend.model.ReportModel import Report
class ReportDAO():

    @staticmethod
    def createReport(bookId,userId,report,summary):
        try:
            Report.objects.create(bookId=bookId,userId=userId,report=report,summary=summary)
        except Exception as e:
            print(e)


    @staticmethod
    def getReportById(id):
        try:
            return Report.objects.get(id=id)
        except:
            return None

    @staticmethod
    def getAllReportsFromABooks(bookId):
        try:
            return Report.objects.filter(bookId=bookId)
        except:
            return None

    @staticmethod
    def editReport(reportId,report,summary):
        dbreport = ReportDAO.getReportById(id=reportId)
        if dbreport:
            if report:
                dbreport.report= report
            if summary:
                dbreport.summary= summary
            dbreport.save()
            return dbreport
        return None

    @staticmethod
    def deleteReport(id):
        report = ReportDAO.getReportById(id)
        if report:
            report.delete()
            return True
        return False






