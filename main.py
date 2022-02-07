from pyparsing import empty
from fileCalculStat import CalculStat
from fileReportPdf import ReportPdf
import  sys , getopt


def gestionArg(argv):
    """Description 
    fonction servant à la gestion et au controle 
    des arguments 

    Args:
        argv (liste): Liste d'arguments passé en paramétre de l'application 
    """
    if not argv:
        print("le nombre d'argument est manquant")
        exit()
    
    try:                                
        opts, args = getopt.getopt(argv, "h", ["help", "path="])
    except getopt.GetoptError as err:
        print(err)          
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            print("Usage : main [OPTION] \n")
            print("-h --help : Cette aide\n") 
            print("--path : doit comporter un chemin valide d'un fichier au format csv \n")                
            sys.exit()                  
        elif opt in ("--path"): 
            path_csv = arg
            if "csv" in path_csv:
                return path_csv
            else:
                print("l'extention du fichier est non valide")
                sys.exit(2)
                           

    
    
   


#----------------------------------
#              MAIN
#----------------------------------

if __name__ == '__main__':

    file_csv = gestionArg(sys.argv[1:])
    stat = CalculStat(file_csv)
    pdf = ReportPdf()