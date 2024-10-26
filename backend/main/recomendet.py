import psycopg2  # Импорт адаптера базы данных PostgreSQL
import nechetk as nh  # Импорт библиотеки nechetk (предполагается, что это пользовательская библиотека)
import chat_rec as rc
import nechet_fri as fr
# Определение параметров подключения к базе данных
host = 'postgres81.1gb.ru'  # Хост базы данных
port = 5432  # Порт базы данных
database = 'xgb_web_coach'  # Имя базы данных
username = 'xgb_web_coach'  # Имя пользователя базы данных
password = 'R-A9KW9ynBRX'  # Пароль базы данных

# Установка соединения с базой данных
connection = psycopg2.connect(host=host, user=username, password=password, database=database)

# Создание объекта курсора для выполнения запросов
cur = connection.cursor()
user_id =0  

# Определение идентификатора пользователя, для которого нужно получить данные
def set_user_id(id):
    global user_id
    user_id = id
    stroke_ferst ={}
    stroke_two = {}
    # Инициализация пустых списков и словарей для хранения данных
    
    progress = {}
    progress1 = {}
    # Проверка, существует ли пользователь в базе данных
    cur.execute('SELECT * FROM xgb_web_coach."Users" WHERE user_id = %s', (user_id,))
    flag = cur.fetchall()

    if flag:
        print(f'Пользователь с ID {user_id} существует в базе данных')
        
        # Получение данных прогресса пользователя из базы данных
        cur.execute('SELECT progres, id_skills FROM xgb_web_coach.user_ferst_level WHERE user_id = %s', (user_id,))
        user_data = cur.fetchall()
        
        # Заполнение словаря прогресса данными пользователя
        for skill in user_data:
            progress[skill[1]] = skill[0]
        
        # Нормализация значений прогресса, чтобы они были между 0 и 1
        progress = {key: value / 100 for key, value in progress.items()}
        # Вывод ключей и значений словаря прогресса
        print("\nКлючи:")
        for key in progress.keys():
            print(key)
        print("\nЗначения:")
        for value in progress.values():
            print(value)
        print("------------------------------------")   
    #для третьего уровняя
        cur.execute('SELECT progres, id_skills FROM xgb_web_coach.user_second_level WHERE user_id = %s', (user_id,))
        user_data_1 = cur.fetchall()

        # Заполнение словаря прогресса данными пользователя
        for skill in user_data_1:
            progress1[skill[1]] = skill[0]
        # Нормализация значений прогресса, чтобы они были между 0 и 1
        progress1 = {key: value / 100 for key, value in progress1.items()}
        # Вывод ключей и значений словаря прогресса
        print("\nКлючи:")
        for key in progress.keys():
            print(key)
        print("\nЗначения:")
        for value in progress.values():
            print(value)
        print("------------------------------------")   
        # Закрытие соединения с базой данных
        connection.close()
        
        # Вызов функции nechetk.start с словарем прогресса
        mass_rec = nh.start(progress)
        print("------------------------------------")
        # print(mass_rec)
        #читает рекомендации из json 
        print("------------------------------------")
        outpute_info = rc.pces(mass_rec)
        # print(outpute_info)
        stroke_ferst = outpute_info
        print("------------------------------------")

        # Вызов функции nechet_fry.troi с словарем прогресса
        masss_rec = fr.troi(progress1)
        print("------------------------------------")
        # print(masss_rec)
        print("------------------------------------")
        outpute_info = rc.pcess(masss_rec)
        # print(outpute_info)
        print("------------------------------------")
        stroke_two = outpute_info
        return stroke_ferst, stroke_two
       
    else:
        print(f'Пользователь с ID {user_id} не существует в базе данных')
        connection.close()
        return {},{}
           

       
otvet_ferst, otvet_two = set_user_id(1)

# Вывод данных с переносом строки
for key, value in otvet_ferst.items():
    print(f"{key}: {value}\n")

# Вывод данных с переносом строки
for key, value in otvet_two.items():
    print(f"{key}: {value}\n")