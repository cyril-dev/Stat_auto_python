from pyparsing import empty
from fileCalculStat import CalculStat
from fileReportPdf import ReportPdf
from lib import gestionArg
import  sys 


#----------------------------------
#              MAIN
#----------------------------------

if __name__ == '__main__':

    file_csv = gestionArg(sys.argv[1:])
    stat = CalculStat(file_csv)
    dist_data = stat.contenuFile()
    dist_data["moyenne general"] = stat.meanByItem("CodePostale")
    t = type(dist_data)
    print(t)
    pdf = ReportPdf()