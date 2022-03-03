from pyparsing import empty
from fileCalculStat import CalculStat
from fileReportPdf import ReportPdf
import lib
import  sys 


#----------------------------------
#              MAIN
#----------------------------------

if __name__ == '__main__':

    file_csv = lib.gestionArg(sys.argv[1:])
    stat = CalculStat(file_csv)
    dist_data = stat.contenuFile()
    dist_data["moyenne general"] = stat.meanByItem("CodePostale")
    dist_data["Statut_point_charge"] = {}
    dist_data["Statut_point_charge"]["path_diag"]=stat.diaCirculaire('Statut du point de recharge')
    dist_data["Statut_point_charge"]["resume"] = stat.resumeItem('Statut du point de recharge')
    # Création du fichier data.json 
    lib.fichierData(dist_data)
   
    #Création du rapport
    pdf = ReportPdf()
    #pdf.set_author('Jules Verne')
    pdf.title = 'Rapport annuel des bornes autolib Paris'
    pdf.print_chapter(1, 'VUE GENERALE', dist_data)
    pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
    pdf.output('Rapport_annuel.pdf', 'F')

    