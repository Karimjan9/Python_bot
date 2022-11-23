import telebot
from telebot import types
import mysql.connector  
import smtplib
from bs4 import BeautifulSoup
#bot stats
token=""
bot=telebot.TeleBot(token)
chat_id=
#mysql connect
cnx = mysql.connector.connect(user='', password='',
                              host='',
                              database='')
# function we need
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

def assocdb(result,quest):
    l=len(result)
    if(l>0):
        for row in result:
            if(row[0]==quest):
                return row[1]
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

# bot start code
result1=""
z=0
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋Ma'lumot  olish!")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!\n Добро пожаловать в клинику Химчан".format(message.from_user), reply_markup=markup)
@bot.message_handler(commands=["help"])
def welcome(message2):
    bot.reply_to(message2,"Nomer tel {}".format(message2.from_user.first_name))

@bot.message_handler(content_types=['text'])
def func(message):
  
    if(message.text == "👋Ma'lumot  olish!"):
        global control
        control=1
        keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)  
        bot.send_message(message.chat.id, text="Iltimos id raqamni kiriting\n Masalan:1234567",reply_markup=keyboard)
    elif(not message.text ):
        result1="error empty list"
        bot.send_message(message.chat.id, text=result1)
    elif(message.text.isdigit() and control==1):
        global id_number
        id_number=message.text
        z==1
        control=0
        bot.send_message(message.chat.id, text="Iltimos telefon raqamni kiriting\n Masalan:  99 123 45 67") 
    elif( (message.text.isdigit() or type(message.text)==str) and control==0):
            cursor = cnx.cursor()
            a=str(message.text)
            b = a.split()
            b = ''.join(b)
            if(b.find("+")==-1 and b.find("998")!=-1):
                cursor.execute("""select * from users where numberPhone="""+"+"+b+" and "+"id="+str(id_number))
            elif(b.find("+")==-1 and b.find("998")==-1):
                cursor.execute("""select * from users where numberPhone="""+"+998"+b+" and "+"id="+str(id_number))
            else:
                cursor.execute("""select * from users where numberPhone="""+b+" and "+"id="+str(id_number))
            result = cursor.fetchall()
            try:
                if(not result or result==""):
                    bot.send_message(message.chat.id, text="error number range")
                else:
                    bot.send_message(message.chat.id, text="iltimos kuting!")
                    id=id_number
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
                    pdf.output("./user_pdf/user_id_"+str(id)+".pdf")
                put="./user_pdf/user_id_"+str(id)+".pdf"
                file = open(put, 'rb')
                bot.send_document(message.chat.id, file)
            finally:
                return cnx

    else:
        bot.send_message(message.chat.id, text="error\n qaytadan kiriting")
bot.polling(none_stop=True)
