from django.shortcuts import render
import pyodbc

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=SAI;DATABASE=company;UID=me;PWD=pass')
    cursor = cnxn.cursor()
    cursor.execute("select user_id, user_name from users")
    rows = cursor.fetchall()
 #   for row in rows:
 #      print row.user_id, row.user_name

    
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me please e-mail me','harshvyas1214@gmail.com']})
