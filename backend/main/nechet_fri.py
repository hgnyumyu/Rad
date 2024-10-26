#третий уровень
import numpy as np  # Импорт библиотеки NumPy для работы с числами
from skfuzzy import control as ctrl  # Импорт библиотеки scikit-fuzzy для работы с нечеткой логикой
from skfuzzy import trimf  # Импорт функции trimf для создания треугольных функций принадлежности
# Определение входных переменных
front_end = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'front_end')  
backend = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'backend')  
subd = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'subd')  
linux = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'linux') 
unity = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'unity')  
Unreal = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Unreal') 
Scapy = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'Scapy')  


front_end['novice'] = trimf(front_end.universe, [0, 0, 0.3])
front_end['intermediate'] = trimf(front_end.universe, [0, 0.3, 0.69])
front_end['advanced'] = trimf(front_end.universe, [0.7, 0.8, 1])
# Определение функций принадлежности для каждой входной переменной
backend['novice'] = trimf(backend.universe, [0, 0, 0.3])  # Начальный уровень
backend['intermediate'] = trimf(backend.universe, [0, 0.3, 0.69])  # Средний уровень
backend['advanced'] = trimf(backend.universe, [0.7, 0.8, 1])  # Продвинутый уровень

subd['novice'] = trimf(subd.universe, [0, 0, 0.3])
subd['intermediate'] = trimf(subd.universe, [0, 0.3, 0.69])
subd['advanced'] = trimf(subd.universe, [0.7, 0.8, 1])

linux['novice'] = trimf(linux.universe, [0, 0, 0.3])
linux['intermediate'] = trimf(linux.universe, [0, 0.3, 0.69])
linux['advanced'] = trimf(linux.universe, [0.7, 0.8, 1])

unity['novice'] = trimf(unity.universe, [0, 0, 0.3])
unity['intermediate'] = trimf(unity.universe, [0, 0.3, 0.69])
unity['advanced'] = trimf(unity.universe, [0.7, 0.8, 1])

Unreal['novice'] = trimf(Unreal.universe, [0, 0, 0.3])
Unreal['intermediate'] = trimf(Unreal.universe, [0, 0.3, 0.69])
Unreal['advanced'] = trimf(Unreal.universe, [0.7, 0.8, 1])

# Аналогичные функции принадлежности для других входных переменных
Scapy['novice'] = trimf(Scapy.universe, [0, 0, 0.3])
Scapy['intermediate'] = trimf(Scapy.universe, [0, 0.3, 0.69])
Scapy['advanced'] = trimf(Scapy.universe, [0.7, 0.8, 1])


# Определите выходные переменные
fulstek = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'fulstek')  # Выходная переменная для бэкенда
data_sience = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'data_sience')  # Выходная переменная для фронтен
kiber_sequrity = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'kiber_sequrity')
game = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'game')


# Определите функции принадлежности для каждой выходной переменной.
fulstek['novice'] = trimf(fulstek.universe, [0, 0, 0.4])
fulstek['intermediate'] =trimf(fulstek.universe, [0, 0.3, 0.69])
fulstek['advanced'] = trimf(fulstek.universe, [0.7, 0.8, 1])

data_sience['novice'] = trimf(data_sience.universe, [0, 0, 0.3])
data_sience['intermediate'] =trimf(data_sience.universe, [0, 0.3, 0.69])
data_sience['advanced'] = trimf(data_sience.universe, [0.7, 0.8, 1])

kiber_sequrity['novice'] = trimf(kiber_sequrity.universe, [0, 0, 0.3])
kiber_sequrity['intermediate'] = trimf(kiber_sequrity.universe, [0, 0.3, 0.69])
kiber_sequrity['advanced'] = trimf(kiber_sequrity.universe, [0.7, 0.8, 1])

game['novice'] = trimf(game.universe, [0, 0, 0.3])
game['intermediate'] = trimf(game.universe, [0, 0.3, 0.69])
game['advanced'] = trimf(game.universe, [0.7, 0.8, 1])

rule101 = ctrl.Rule(backend['novice'] & front_end['novice'] , fulstek['novice'])
rule102 = ctrl.Rule(backend['novice'] & front_end['intermediate'] , fulstek['novice'])
rule103 = ctrl.Rule(backend['intermediate'] & front_end['intermediate'] , fulstek['intermediate'])
rule104 = ctrl.Rule(backend['intermediate'] & front_end['advanced'] , fulstek['intermediate'])
rule105 = ctrl.Rule(backend['advanced'] & front_end['intermediate'] , fulstek['intermediate'])
rule106 = ctrl.Rule(backend['advanced'] & front_end['novice'] , fulstek['intermediate'])
rule107 = ctrl.Rule(backend['novice'] & front_end['advanced'] , fulstek['intermediate'])
rule108 = ctrl.Rule(backend['advanced'] & front_end['advanced'] , fulstek['advanced'])
rule109 = ctrl.Rule(backend['intermediate'] & front_end['novice'] , fulstek['novice'])

rule110 = ctrl.Rule(linux['novice'] & Scapy['novice'] , kiber_sequrity['novice'])
rule111 = ctrl.Rule(linux['novice'] & Scapy['intermediate'] , kiber_sequrity['novice'])
rule112 = ctrl.Rule(linux['intermediate'] & Scapy['intermediate'] , kiber_sequrity['intermediate'])
rule113 = ctrl.Rule(linux['intermediate'] & Scapy['advanced'] , kiber_sequrity['advanced'])
rule114 = ctrl.Rule(linux['advanced'] & Scapy['intermediate'] , kiber_sequrity['advanced'])
rule115 = ctrl.Rule(linux['advanced'] & Scapy['novice'] , kiber_sequrity['intermediate'])
rule116 = ctrl.Rule(linux['novice'] & Scapy['advanced'] , kiber_sequrity['intermediate'])
rule117 = ctrl.Rule(linux['advanced'] & Scapy['advanced'] , kiber_sequrity['advanced'])
rule118 = ctrl.Rule(linux['intermediate'] & Scapy['novice'] , kiber_sequrity['novice'])

rule119 = ctrl.Rule(backend['novice'] & subd['novice'] , data_sience['novice'])
rule120 = ctrl.Rule(backend['novice'] & subd['intermediate'] , data_sience['novice'])
rule121 = ctrl.Rule(backend['intermediate'] & subd['intermediate'] , data_sience['intermediate'])
rule122 = ctrl.Rule(backend['intermediate'] & subd['advanced'] , data_sience['intermediate'])
rule123 = ctrl.Rule(backend['advanced'] & subd['intermediate'] , data_sience['intermediate'])
rule124 = ctrl.Rule(backend['advanced'] & subd['novice'] , data_sience['intermediate'])
rule125 = ctrl.Rule(backend['novice'] & subd['advanced'] , data_sience['intermediate'])
rule126 = ctrl.Rule(backend['advanced'] & subd['advanced'] , data_sience['advanced'])
rule127 = ctrl.Rule(backend['intermediate'] & subd['novice'] , data_sience['novice'])

rule128 = ctrl.Rule(Unreal['novice'] & unity['novice'] , game['novice'])
rule129 = ctrl.Rule(Unreal['novice'] & unity['intermediate'] , game['novice'])
rule130 = ctrl.Rule(Unreal['intermediate'] & unity['intermediate'] , game['intermediate'])
rule131 = ctrl.Rule(Unreal['intermediate'] & unity['advanced'] , game['intermediate'])
rule132 = ctrl.Rule(Unreal['advanced'] & unity['intermediate'] , game['intermediate'])
rule133 = ctrl.Rule(Unreal['advanced'] & unity['novice'] , game['intermediate'])
rule134 = ctrl.Rule(Unreal['novice'] & unity['advanced'] , game['intermediate'])
rule135 = ctrl.Rule(Unreal['advanced'] & unity['advanced'] , game['advanced'])
rule136 = ctrl.Rule(Unreal['intermediate'] & unity['novice'] , game['novice'])

syste = ctrl.ControlSystem([rule101,rule102,rule103,rule104,
                             rule105,rule106,rule107,rule108,rule109,rule110,rule111,
                             rule112,rule113,rule114,rule115,rule116,rule117,rule118, rule119, 
                             rule120, rule121, rule122, rule123,rule124,rule125,rule126,rule127,rule128,rule129,
                             rule130,rule131,rule132,rule133,rule134,rule135,rule136])
# Create a control system simulation
simm = ctrl.ControlSystemSimulation(syste)
def troi(val_dict):
    # Устанавливаем входные значения для симуляции из словаря val_dict
    print(val_dict)
    # Устанавливаем входные значения для симуляции из словаря val_dict
    simm.input['front_end'] = val_dict.get(0, 0)  # Используем правильное имя
    simm.input['backend'] = val_dict.get(1, 0)
    simm.input['subd'] = val_dict.get(2, 0)
    simm.input['linux'] = val_dict.get(3, 0)
    simm.input['unity'] = val_dict.get(4, 0)
    simm.input['Unreal'] = val_dict.get(5, 0)
    simm.input['Scapy'] = val_dict.get(6, 0)

    # Запускаем симуляцию
    simm.compute()
    # Получаем выходные значения
    output_values = simm.output
    print("fulstek:", output_values['fulstek'])  # Выводим значение для бэкенда
    print("data_sience :", output_values['data_sience'])  # Выводим значение для фронтенда
    print("kiber_sequrity:", output_values['kiber_sequrity'])  # Выводим значение для Linux
    print("game:", output_values['game'])  # Выводим значение для Unity

    procent = {}  # Словарь для хранения процентных значений
    procent = {key: int(value * 100) for key, value in output_values.items()}

    return procent # Возвращаем массив индексов и словарь процентных значений

# val_map={0:0. , 1:0. , 2:0. , 3:0.9 , 4:0. , 5:0. , 6:0.9}
# rezz= troi(val_map)
# print (rezz)