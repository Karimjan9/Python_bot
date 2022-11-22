import mysql.connector  
import pymysql
import pymysql.cursors
from var_dump import var_dump
from bs4 import BeautifulSoup
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='clinic')
def insertChar(mystring, position, chartoinsert ):
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring 
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 
def FetchOneAssoc(cursor):
    data = cursor.fetchone()
    if data == None:
        return None
    desc = cursor.description

    dict = {}

    for (name, value) in zip(desc, data):
        dict[name[0]] = value

    return dict
def FetchAssoc(cursor,cur):
    data = cursor
    if data == None:
        return None
    desc = cur.description

    dict = {}

    for (name, value) in zip(desc, data):
        dict[name[0]] = value

    return dict
# try:
#     id_number=84
#     cursor = cnx.cursor()
#     phone=+998914440449
#     ph=str(phone)
#     cursor.execute("""
#                select * from visit where """"user_id="+str(id_number))
#     result = cursor.fetchall()
#     data=result[0]
   
#     b=list(find_all(data[19],'</p>'))
#     l=len(b)
#     i=0
#     insert=data[19]
#     z=4
#     while i<l:
#         insert=insertChar(insert,b[i]+z,"<br>")
#         z=z+4
#         i=i+1
#     soup = BeautifulSoup(insert)
#     soup = BeautifulSoup(insert)
#     text=soup.get_text()
#     text=soup.get_text()
#     result1=data[18]+"\n"+text
#     print(text)
# finally:
#     cnx.close()


# from pprint import pprint
# id_number=84
# try:
#     cursor = cnx.cursor()
#     cursor.execute("""
#     select * from users where id="""+str(id_number))
#     result = cursor.fetchall()
#     if(not result or result==""):
#         # bot.send_message(message.chat.id, text="error number range")
#         print('error')
#     else:
#         data=result[0]
#         result1=data[5]+" "+data[6]+" "+data[7]+" "+str(data[8])+" "+data[9]+" "+str(data[14])
#         # bot.send_message(message.chat.id, text=result1)
# finally:
#     cnx.close()

# from fpdf import FPDF
 
# class CustomPDF(FPDF):
 
#     def header(self):
#         # Устанавливаем лого
#         self.image('logo.png', 10, 8, 33)
#         self.set_font('Arial', 'B', 15)
 
#         # Добавляем адрес
#         self.cell(100)
#         self.cell(0, 5, 'Ism:', ln=1)
#         self.cell(100)
#         self.cell(0, 5, 'Familiya:', ln=1)
#         self.cell(100)
#         self.cell(0, 5, 'Otchestvo:', ln=1)
 
#         # Разрыв линии
#         self.ln(20)
 
#     def footer(self):
#         self.set_y(-10)
 
#         self.set_font('Arial', 'I', 8)
 
#         # Добавляем номер страницы
#         page = 'Page ' + str(self.page_no()) + '/{nb}'
#         self.cell(0, 10, page, 0, 0, 'C')
 
# def create_pdf(pdf_path):
#     pdf = CustomPDF()
#     # Создаем особое значение {nb}
#     pdf.alias_nb_pages()
#     pdf.add_page()
#     pdf.set_font('Times', '', 12)
#     line_no = 1
#     for i in range(50):
#         pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
#         line_no += 1
#         i=i+1
#     pdf.output(pdf_path)
#     create_pdf('header_footer.pdf')


# pprint(+998913103298)
# print(vars(+998913103298))

# a=+998905109042
# b=str(a)
# if (type(b)==int):
#     print("int")
# elif(type(b)==str):
#     print("str")
# print(b)
# import textwrap
# from fpdf import FPDF

# def text_to_pdf(text, filename):
#     a4_width_mm = 210
#     pt_to_mm = 0.35
#     fontsize_pt = 10
#     fontsize_mm = fontsize_pt * pt_to_mm
#     margin_bottom_mm = 10
#     character_width_mm = 7 * pt_to_mm
#     width_text = a4_width_mm / character_width_mm

#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.set_auto_page_break(True, margin=margin_bottom_mm)
#     pdf.add_page()
#     pdf.set_font(family='Courier', size=fontsize_pt)
#     # splitted = text.np.array_split('\n')

#     for line in text:
#         lines = textwrap.wrap(line, width_text)

#         if len(lines) == 0:
#             pdf.ln()

#         for wrap in lines:
#             pdf.cell(0, fontsize_mm, wrap, ln=1)

#     pdf.output(filename, 'F') 
# text=[["abc","abc2","abc3"],[123,234,456],["bafo","Bafojon","Html"]]
# # input_filename = 'test.txt'
# output_filename = 'output.pdf'
# # file = open(input_filename)
# # file.close()
# text_to_pdf(text, output_filename)
# from fpdf import FPDF 
# pdf = FPDF() 
 
# pdf.add_page() 

# pdf.set_font("New Times Roman", size = 25) 

# # create a cell 
# pdf.cell(200, 10, txt = "JournalDev", 
# 		ln = 1, align = 'C') 

# pdf.cell(200, 10, txt = "Welcome to the world of technologies!", 
# 		ln = 2, align = 'C') 
# for line in text:
#     pdf.cell(200, 10, txt = line, 
# 		ln = 2, align = 'C') 
# pdf.output("data.pdf") 
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.units import inch
# from reportlab.lib.styles import getSampleStyleSheet
# data = [{"a": 1, "b": 2}, {"c": 3, "d":4}]
# def create_pdf():
   
#     story = []
    
#     # Initialise the simple document template
#     doc = SimpleDocTemplate(f"blog.pdf",
#                             page_size=letter,
#                             bottomMargin=.4 * inch,
#                             topMargin=.4 * inch,
#                             rightMargin=.8 * inch,
#                             leftMargin=.8 * inch)
    
#     # set the font style
#     styles = getSampleStyleSheet()
#     styleN = styles['Normal']
#     for count, d in enumerate(data, 1):
#         p_count = Paragraph(f" Data: {count} ")
#         story.append(Spacer(1, 12))
#         story.append(p_count)
#         for k, v in d.items():
#             # extract and add key value pairs to PDF
#             p = Paragraph(k + " : " + str(v), styleN)
#             story.append(p)
#             story.append(Spacer(1, 2))
#     # build PDF using the data
#     doc.build(story)
# create_pdf()


# from fpdf import FPDF
# text=[["abc","abc2","abc3"],[123,234,456],["bafo","Bafojon","Html"]]
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=20)
# pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
# for i in range(len(text[0])):
#     pdf.cell(200, 10, txt=text[0][i], ln=1, align="L")
# pdf.output("simple_demo1.pdf")

# from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         # Logo
#         self.image('logo.png', 10, 8, 33)
#         # Arial bold 15
#         self.set_font('Arial', 'B', 15)
#         # Move to the right
#         # self.cell(80)
#         self.ln(20)
#         # Title
#         self.cell(30, 10, 'Title', 1, 0, 'L')
#         # Line break
#         self.ln(20)

#     # Page footer
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Arial', 'I', 8)
#         # Page number
#         self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# # Instantiation of inherited class
# pdf = PDF()
# pdf.alias_nb_pages()
# pdf.add_page()
# pdf.set_font('Times', '', 12)

# pdf.output('tuto2.pdf', 'F')
def assocdb(result,quest):
    l=len(result)
    if(l>0):
        for row in result:
            if(row[0]==quest):
                return row[1]

#  b=list(find_all(data[19],'</p>'))
#                     l=len(b)
#                     i=0
#                     insert=data[19]
#                     x=4
#                     while i<l:
#                         insert=insertChar(insert,b[i]+x,"<br>")
#                         x=x+4
#                         i=i+1
#                     soup = BeautifulSoup(insert)
#                     text=soup.get_text()


# import ibm_db
# -*- coding: cp1251 -*-
import webbrowser

id=11101
def edit(text,word,swap):
    b=list(find_all(text,word))
    lenx=len(swap)
    x=lenx
    l=len(b)
    i=0
    while i<l:
        text=insertChar(text,b[i],swap)
        x=x+lenx
        i=i+1
    return text
#company title
cursor1 = cnx.cursor(buffered=True)
cursor1.execute("""SELECT * FROM company_constants """)
result1 =cursor1.fetchall()
#reports query
cursor2=cnx.cursor(buffered=True)
cursor2.execute("SELECT  us.first_name,us.last_name,us.father_name, vs.add_date, vs.completed,ds.is_document, vs.user_id, vs.parent_id, vs.service_id, us.dateBith, vs.accept_date  FROM visit vs LEFT JOIN users us ON(us.id=vs.user_id) LEFT JOIN service sc ON(sc.id=vs.service_id) LEFT JOIN division ds ON(ds.id = sc.division_id) WHERE  vs.report_title IS NOT NULL AND  vs.report IS NOT NULL AND  vs.user_id="+str(id))
result2=FetchOneAssoc(cursor2)
result22=cursor2.fetchall()
#reports and repport_titles name 
cursor3=cnx.cursor(buffered=True)
cursor3.execute("SELECT DISTINCT vs.division_id, ds.name, ds.title ,vs.report_title, vs.report FROM visit vs LEFT JOIN division ds ON(ds.id=vs.division_id) WHERE ds.level NOT IN (12, 13) AND  vs.completed IS NOT NULL AND  vs.laboratory IS NULL AND vs.service_id != 1 AND  vs.user_id="+str(id))
result3=cursor3.fetchall()
cursor6=cnx.cursor(buffered=True)
cursor6.execute("SELECT sc.name FROM visit vs LEFT JOIN service sc ON(sc.id=vs.service_id) WHERE vs.id="+str(id))
result6=cursor6.fetchall()
#service-id
if(result2!=None):
    cursor4=cnx.cursor(buffered=True)
    cursor4.execute("SELECT vs.id, sc.id 'serv_id', sc.name FROM visit vs LEFT JOIN service sc ON(sc.id=vs.service_id) WHERE  vs.completed IS NOT NULL AND vs.laboratory IS NOT NULL AND vs.direction IS NOT NULL AND vs.user_id="+str(result2["user_id"]))
    result4=cursor4.fetchall()
from fpdf import FPDF
pdf = FPDF()
effective_page_width = pdf.w - 1*pdf.l_margin
pdf.add_page()
pdf.image('./logo/logo.png', x=10, y=8, w=75)
pdf.set_font("Arial", size=12)
pdf.set_draw_color(0, 0, 0)
pdf.line(0, 40, 220, 40)
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)
pdf.ln(3)
pdf.cell(100)
pdf.cell(200, 5, txt=assocdb(result1,'print_header_title'), ln=1,align="L")
pdf.cell(100)
pdf.cell(200, 5, txt=assocdb(result1,'print_header_address'), ln=1,align="L")
pdf.cell(100)
pdf.cell(200, 5, txt=assocdb(result1,'print_header_phones'), ln=1,align="L")
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)
pdf.ln(20)
if(result2!=None):
    pdf.cell(100, 8, txt='Ф.И.О.:'+str(result2["first_name"])+" "+str(result2["last_name"])+" "+str(result2["father_name"]), ln=1,align="L")
    pdf.cell(10)
    pdf.ln(0)
    pdf.cell(100, 8, txt='ID Пациента:'+str(result2["user_id"]), ln=1,align="L")
    pdf.cell(10)
    pdf.ln(0)
    pdf.cell(100, 8, txt='Дата рождения:'+str(result2['dateBith']), ln=1,align="L")
    pdf.ln(0)
    pdf.cell(10)
    pdf.ln(0)
    pdf.cell(100, 8, txt='Дата поступления:'+str(result2['add_date']), ln=1,align="L")
    pdf.cell(10)
    pdf.ln(0)
    pdf.cell(100, 8, txt='Дата выписки:'+str(result2['completed']), ln=1,align="L")
    for (report_one,resultdate) in zip(result3, result22):
        resultdate=FetchAssoc(resultdate,cursor2)
        report_one=FetchAssoc(report_one,cursor3)
        pdf.ln(10)
        pdf.cell(50)
        pdf.add_font('DejaVu', 'B','DejaVuSansCondensed-Bold.ttf', uni=True)
        pdf.set_font('DejaVu', 'B', 14)
        pdf.cell(50, 8, txt='Дата исследования:  ',align="L")
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 12)
        pdf.cell(50, 8, txt="  "+str(resultdate['accept_date']),ln=1,align="L")
        pdf.ln(10)
        pdf.cell(50)
        pdf.ln(3)
        soup = BeautifulSoup(str(report_one['report']), features="html.parser")
        text=soup.get_text()
        pdf.add_font('DejaVu', 'B','DejaVuSansCondensed-Bold.ttf', uni=True)
        pdf.set_font('DejaVu', 'B', 14)
        pdf.cell(20)
        pdf.multi_cell(180,5,(str(report_one['report_title'])),0,0)
        pdf.ln(3)
        text=edit(text,'Диагноз',"\n")
        text=edit(text,'Рекомендация',"\n")
        pdf.add_font('DejaVu', 'I','DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', 'I', 12)
        pdf.multi_cell(200,5,("    "+text),0,0)
        pdf.ln(3)   
if(result2!=None and result2!="" and result4!=[]):
    if(result4!=None and result4!=[]):
        pdf.add_font('DejaVu', 'B','DejaVuSansCondensed-Bold.ttf', uni=True)
        pdf.set_font('DejaVu', 'B', 14)
        pdf.multi_cell(180,5,('   Результаты лабораторных и инструментальных исследований:'),0,0)
        pdf.ln(5)
        pdf.set_font('DejaVu', '', 12)
        for s_name in result6:
            s_name=FetchAssoc(s_name,cursor6)
            pdf.cell(30)
            pdf.add_font('DejaVu', 'B','DejaVuSansCondensed-Bold.ttf', uni=True)
            pdf.set_font('DejaVu', 'B', 12)
            pdf.cell(100, 8, txt=s_name['name'], ln=1,align="L")
            pdf.add_font('DejaVu', 'I','DejaVuSansCondensed.ttf', uni=True)
            pdf.set_font('DejaVu', 'I', 12)
            pdf.cell(10, 8, txt="№",align="L")
            pdf.cell(90, 8, txt="Анализ",align="L")
            pdf.cell(30, 8, txt="Норма",align="L")
            pdf.cell(30, 8, txt="  Ед",align="L")
            pdf.cell(30, 8, txt="Результат",ln=1,align="L")
            ind=1
            for one in result4:
                one=FetchAssoc(one,cursor4)
                #analyze
                cursor5=cnx.cursor(buffered=True)
                cursor5.execute("SELECT scl.name, vl.result,scl.name, scl.code, scl.standart,vl.deviation,scl.unit FROM visit_analyze vl LEFT JOIN service_analyze scl ON(scl.id=vl.analyze_id) WHERE vl.visit_id = "+str(one['id']) +" AND vl.service_id ="+str(one['serv_id']))
                res=cursor5.fetchall()
                for result5 in res:
                    resul=FetchAssoc(result5,cursor5)
                    # print(resul)
                    pdf.add_font('DejaVu', 'I','DejaVuSansCondensed.ttf', uni=True)
                    pdf.set_font('DejaVu', 'I', 12)
                    top = pdf.y
                    offset = pdf.x 
                    pdf.set_xy(offset,top)
                    pdf.multi_cell(10,8,(str(ind)+":"),0,0)
                    top = pdf.y
                    offset = pdf.x
                    offset=offset+10
                    pdf.set_xy(offset,top-8)
                    pdf.multi_cell(90,8,(str(resul['name'])+":"),0,0)
                    top = pdf.y
                    offset = pdf.x 
                    offset=offset+90+10
                    pdf.set_xy(offset,top-8)
                    pdf.multi_cell(30,8,(str(resul['standart'])+":"),0,0)
                    top = pdf.y
                    offset = pdf.x
                    offset=offset+30+90+10
                    pdf.set_xy(offset,top-8)
                    pdf.multi_cell(30,8,(str(resul['unit'])+":"),0,0)
                    top = pdf.y
                    offset = pdf.x 
                    offset=offset+30+30+90+10
                    pdf.set_xy(offset,top-8)
                    pdf.multi_cell(30,8,(str(resul['result'])+":"),0,0)
                    ind=1+ind
# pdf.output("./user_pdf/user_id_"+str(id)+".pdf")
# print(len(res))
a= 61 
print(str(a))

    
