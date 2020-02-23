from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="aofDB117",  # your password
                     db="bookw14")        # name of the data base

# db = MySQLdb.connect(user="myadmin@mydatabaseforwebapp", 
#                      password="login_1234", 
#                      host="mydatabaseforwebapp.mariadb.database.azure.com", 
#                      port=3306, 
#                      database="BookInfo",
#                      ssl_ca='C:/ssl/BaltimoreCyberTrustRoot.crt.pem')      # name of the data base
cur = db.cursor()

# def index(request):
#     cur.execute("SELECT * FROM author")
#     return HttpResponse("Hello, world. You're at the polls index %s."% cur.fetchall()[0][1])

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def index(request):
    try:
        test_sql=request.POST['sql_code']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'books/Query.html')
    else:
        try:
            cur.execute(test_sql)
        except:
            context = {'code':test_sql}
            return render(request, 'books/Query.html',context)
        else:
            desc = cur.description
            query_list = cur.fetchall()
            context = {'query': query_list,'code':test_sql,'len_query':len(query_list),'desc':desc}
            return render(request, 'books/Query.html',context)
        # cur.execute(test_sql)
        # context = {'test':cur.fetchall(),'test2':test_sql}
        # context = {'test2':test_sql}
        # return render(request, 'books/555.html',context)

# def index(request):
#     try:
#         test_sql=request.POST['sql_code']
#     except (KeyError):
#         context = {'y':5555}
#         return render(request, 'books/666.html',context)
#     else:
#         context = {'y':test_sql}
#         return render(request, 'books/666.html',context)


# def index2(request):
#     test_sql=request.POST['sql_code']
#     context = {'y':test_sql}
#     return render(request, 'books/666.html',context)

def index2(request):
    context = {'gg':[1,2,3,4,5]}
    return render(request, 'books/index.html',context)

def test(request):
    return render(request, 'books/test.html')