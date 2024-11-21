from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from .chat_bot import chat
import psycopg2
#from corsheaders.decorators import cors_policy_permissions
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import bcrypt


# Create your views here.


def main(request):
    print(request.method)
    if request.method == 'GET':
        print(request.GET.get('user_id'))
    #print('user', request.user.is_authenticated)
    # login_to_check = "user"
    # password_to_check = "12345"
    # host = 'postgres81.1gb.ru'
    # port = 5432
    # database = 'xgb_web_coach'
    # username = 'xgb_web_coach'
    # password = 'R-A9KW9ynBRX'


    # try:
    #     connection = psycopg2.connect(database=database, user=username, password=password, host=host, port=port  )
    #     cur = connection.cursor()
    #     cur.execute('SELECT password FROM xgb_web_coach."Users" WHERE login = %s', (login_to_check,))
    #     db_password = cur.fetchone()[0]
    #     print(db_password)
    #     cur.close()
    #     connection.close()
        # connection.close()
        # if user:
        #     return True
        # else:
        #     return False
        
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)

    return render(request, "./index.html", {'AAA':'aaa'})


def auth(request):
    print(request.method)
    if request.method == 'GET':
        print(request.GET.get('user_id'))


    return render(request, "./autorization.html", {'AAA':'aaa'})


def register(request):


    return render(request, "./registration.html", {'AAA':'aaa'})

class Chat(APIView):
    def post(self, request):
        data = request.data['zapros']
        otvet = chat.get_response_model(data)
        print('me', otvet)
        return Response({'title': otvet})
    

class Test(APIView):
    def get(self, request):
       return Response({'data':'Штирлиц всю ночь топил камин. Наутро камин утонул.'}) 
     
    def post(self, request):
        data = request.data['data']
        if data == '1':
            return Response({'data':'1111111'}) 
        if data == '2':
            return Response({'data':'222222'}) 
        else:
            return Response({'data':'0000000'}) 


class Autorization(APIView):
    def post(self,request):
        data = request.data
        input_name = data['name']
        input_password = data['password']

        host = 'postgres81.1gb.ru'
        port = 5432
        database = 'xgb_web_coach'
        username = 'xgb_web_coach'
        password = 'R-A9KW9ynBRX'
        connection = psycopg2.connect(host=host, user=username, password=password, database=database)
        cur = connection.cursor()

        # Get the stored hashed password for the user
        cur.execute('SELECT user_id, password FROM xgb_web_coach."Users" WHERE login = %s', (input_name,))
        stored_hash = cur.fetchone()
        connection.close()
        if (stored_hash):
            user_id = stored_hash[0]
            stored_hash = stored_hash[1]
            print(stored_hash)
        else:
            return Response({'request':'False'})

        # Hash the input password using Bcrypt
        stored_hash_bytes = bytes(stored_hash)
        if bcrypt.checkpw(input_password.encode('utf-8'), stored_hash_bytes):
            Response.set_cookie("user_id", user_id)
            return Response({'request':'True'})
        else:
            return Response({'request':'False'})


class Registration(APIView):
    def post(self,request):

        data = request.data
        input_login = data['login']
        first_name = data['f_name']
        last_name = data['l_name']
        othestvo  = data['otchestvo']
        password = data['password']
        host = 'postgres81.1gb.ru'
        port = 5432
        database = 'xgb_web_coach'
        username = 'xgb_web_coach'
        password = 'R-A9KW9ynBRX'
        connection = psycopg2.connect(host=host, user=username, password=password, database=database)
        cur = connection.cursor()

        cur.execute('SELECT user_id, password FROM xgb_web_coach."Users" WHERE login = %s', (input_login,))
        user = cur.fetchone()
        if (user):
            return Response({'request':'IS_USER'})
        
        # хешируем пароль
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # создаем нового пользователя
        cur.execute('SELECT * FROM xgb_web_coach."Users"')
        user_id = len(cur.fetchall())+1
        print(user_id)
        cur.execute('INSERT INTO xgb_web_coach."Users" (user_id, login,first_name,last_name,othectvo,password) VALUES (%s,%s,%s,%s,%s,%s)', (user_id,input_login,first_name,last_name,othestvo, hashed_password))
        connection.commit()
        connection.close()
        return Response({'request':'OK'})


class Nechetk(APIView):
    def post(self,request):
        data = request.data
        user_id = data['id']
        host = 'postgres81.1gb.ru'
        port = 5432
        database = 'xgb_web_coach'
        username = 'xgb_web_coach'
        password = 'R-A9KW9ynBRX'
        id_skills = []
        progress = {}
        connection = psycopg2.connect(host=host, user=username, password=password, database=database)
        cur = connection.cursor()
        cur.execute('SELECT user_id FROM xgb_web_coach."Users" WHERE login = %s', (user_id,))
        user_id = cur.fetchone()[0]

        if user_id:
            print(f'Пользователь с ID {user_id} существует в базе данных')
            
            # Получение данных прогресса пользователя из базы данных
            cur.execute('SELECT progres, id_skills FROM xgb_web_coach.user_ferst_level WHERE user_id = %s', (user_id,))
            user_data = cur.fetchall()
            
            # Заполнение словаря прогресса данными пользователя
            for skill in user_data:
                progress[skill[1]] = skill[0]
        return Response({'progress':progress})