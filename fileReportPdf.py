from fpdf import FPDF
#import fpdf

class ReportPdf(FPDF):
    title = ""
    
    #def __init__(self):
    #    super().__init__()
       # self.title = title
    #    print('Rapport PDF')
    
    def header(self):
       # Arial bold 15
       self.set_font('Arial', 'B', 20)
       # Calculate width of title and position
       w = self.get_string_width(self.title) + 6
       #self.set_x((210 - w) / 2)
       # Colors of frame, background and text
       #self.set_draw_color(0, 80, 180)
       #self.set_fill_color(230, 230, 0)
       self.set_text_color(220, 50, 50)
       # Thickness of frame (1 mm)
       #self.set_line_width(1)
       # Title
       self.cell(w, 9, self.title, 1, 1, 'C', 1)
       # Line break
       self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Partie %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, data):
        print(data)
        # Read text file
        #with open(name, 'rb') as fh:
        #    txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        #self.multi_cell(0, 5, data.get('Nombre d\'items'))
        # Line break
        self.ln()
        # Mention in italics
        #self.set_font('Arial', 'I')
        #self.cell(0, 5, data['Statut_point_charge']['path_diag'])
       # self.image()

    def print_chapter(self, num, title_chapter, data):
        self.add_page()
        self.chapter_title(num, title_chapter)
        self.chapter_body(data)