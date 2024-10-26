import numpy as np  # Импорт библиотеки NumPy для работы с числами
from skfuzzy import control as ctrl  # Импорт библиотеки scikit-fuzzy для работы с нечеткой логикой
from skfuzzy import trimf  # Импорт функции trimf для создания треугольных функций принадлежности

# Определение входных переменных
c_sharp = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'c_sharp')  # Уровень знаний в C#
c_plus_plus = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'c_plus_plus')  # Уровень знаний в C++
python = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'python')  # Уровень знаний в Python
js = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'js')  # Уровень знаний в JavaScript
css_html = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'css_html')  # Уровень знаний в CSS/HTML
sql = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'sql')  # Уровень знаний в SQL
b_network = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'b_network')  # Уровень знаний в сетевых технологиях

# Определение функций принадлежности для каждой входной переменной
c_sharp['novice'] = trimf(c_sharp.universe, [0, 0, 0.3])  # Начальный уровень
c_sharp['intermediate'] = trimf(c_sharp.universe, [0, 0.3, 0.7])  # Средний уровень
c_sharp['advanced'] = trimf(c_sharp.universe, [0.3, 0.7, 1])  # Продвинутый уровень

# Аналогичные функции принадлежности для других входных переменных
c_plus_plus['novice'] = trimf(c_plus_plus.universe, [0, 0, 0.3])
c_plus_plus['intermediate'] = trimf(c_plus_plus.universe, [0, 0.3, 0.7])
c_plus_plus['advanced'] = trimf(c_plus_plus.universe, [0.3, 0.7, 1])

python['novice'] = trimf(python.universe, [0, 0, 0.3])
python['intermediate'] = trimf(python.universe, [0, 0.3, 0.7])
python['advanced'] = trimf(python.universe, [0.3, 0.7, 1])

js['novice'] = trimf(js.universe, [0, 0, 0.3])
js['intermediate'] = trimf(js.universe, [0, 0.3, 0.7])
js['advanced'] = trimf(js.universe, [0.3, 0.7, 1])

css_html['novice'] = trimf(css_html.universe, [0, 0, 0.3])
css_html['intermediate'] = trimf(css_html.universe, [0, 0.3, 0.7])
css_html['advanced'] = trimf(css_html.universe, [0.3, 0.7, 1])

sql['novice'] = trimf(sql.universe, [0, 0, 0.3])
sql['intermediate'] = trimf(sql.universe, [0, 0.3, 0.7])
sql['advanced'] = trimf(sql.universe, [0.3, 0.7, 1])

b_network['novice'] = trimf(b_network.universe, [0, 0, 0.3])
b_network['intermediate'] = trimf(b_network.universe, [0, 0.3, 0.7])
b_network['advanced'] = trimf(b_network.universe, [0.3, 0.7, 1])

# Определите выходные переменные
backend = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'backend')  # Выходная переменная для бэкенда
front_end = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'front_end')  # Выходная переменная для фронтен
linux = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'linux')
unity = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'unity')
subd = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'subd')
Unreal = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Unreal')
Scapy = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Scapy')

# Определите функции принадлежности для каждой выходной переменной.
backend['novice'] = trimf(backend.universe, [0, 0, 0.4])
backend['intermediate'] =trimf(backend.universe, [0.4, 0.6, 0.7])
backend['advanced'] = trimf(backend.universe, [0.8, 0.9, 1])

Scapy['novice'] = trimf(Scapy.universe, [0, 0, 0.3])
Scapy['intermediate'] =trimf(Scapy.universe, [0, 0.3, 0.7])
Scapy['advanced'] = trimf(Scapy.universe, [0.8, 0.9, 1])

front_end['novice'] = trimf(front_end.universe, [0, 0, 0.3])
front_end['intermediate'] = trimf(front_end.universe, [0, 0.3, 0.7])
front_end['advanced'] = trimf(front_end.universe, [0.3, 0.7, 1])

linux['novice'] = trimf(linux.universe, [0, 0, 0.3])
linux['intermediate'] = trimf(linux.universe, [0, 0.3, 0.7])
linux['advanced'] = trimf(linux.universe, [0.3, 0.7, 1])

unity['novice'] = trimf(unity.universe, [0, 0, 0.3])
unity['intermediate'] = trimf(unity.universe, [0, 0.3, 0.7])
unity['advanced'] = trimf(unity.universe, [0.3, 0.7, 1])

subd['novice'] = trimf(subd.universe, [0, 0, 0.3])
subd['intermediate'] = trimf(subd.universe, [0, 0.3, 0.7])
subd['advanced'] = trimf(subd.universe, [0.3, 0.7, 1])

Unreal['novice'] = trimf(Unreal.universe, [0, 0, 0.3])
Unreal['intermediate'] = trimf(Unreal.universe, [0, 0.3, 0.7])
Unreal['advanced'] = trimf(Unreal.universe, [0.3, 0.7, 1])
# Define the rules

rule9 = ctrl.Rule(c_sharp['advanced'], unity['advanced'])
rule26 = ctrl.Rule(c_sharp['novice'], unity['novice'])
rule27 = ctrl.Rule(c_sharp['intermediate'], unity['intermediate'])



rule28 = ctrl.Rule(c_plus_plus['advanced'], Unreal['advanced'])
rule29 = ctrl.Rule(c_plus_plus['novice'], Unreal['novice'])
rule30 = ctrl.Rule(c_plus_plus['intermediate'], Unreal['intermediate'])

rule31 = ctrl.Rule(python['advanced'], Scapy['advanced'])
rule32 = ctrl.Rule(python['novice'], Scapy['novice'])
rule33 = ctrl.Rule(python['intermediate'], Scapy['intermediate'])


rule34 = ctrl.Rule(python['advanced'], backend['novice'])
# rule35 = ctrl.Rule(python['novice'], backend['novice'])
rule36 = ctrl.Rule(python['intermediate'], backend['novice'])

rule1 = ctrl.Rule(c_sharp['intermediate'], backend['novice'])
rule10 = ctrl.Rule(c_sharp['intermediate'] & c_plus_plus['intermediate'] & python['intermediate'], backend['advanced'])
rule5 = ctrl.Rule(c_sharp['intermediate'] | c_plus_plus['intermediate'] | python['intermediate'], backend['novice'])
rule11 = ctrl.Rule(c_sharp['advanced'] & c_plus_plus['advanced'] & python['advanced'], backend['advanced'])
rule20 = ctrl.Rule(c_sharp['novice'] & c_plus_plus['novice'] & python['novice'], backend['intermediate'])

rule21 = ctrl.Rule(c_sharp['advanced'] & c_plus_plus['advanced'], backend['intermediate'])
rule25 = ctrl.Rule(c_sharp['intermediate'] & c_plus_plus['intermediate'], backend['intermediate'])
rule22 = ctrl.Rule(c_sharp['novice'] & c_plus_plus['novice'] , backend['novice'])
rule23 = ctrl.Rule(c_sharp['novice'] & c_plus_plus['intermediate'] , backend['novice'])
rule24 = ctrl.Rule(c_sharp['intermediate'] & c_plus_plus['novice'] , backend['novice'])

rule2 = ctrl.Rule(c_plus_plus['intermediate'], backend['novice'])
rule18 = ctrl.Rule(c_plus_plus['novice'], backend['novice'])
rule19 = ctrl.Rule(c_plus_plus['advanced'], backend['novice'])

rule3 = ctrl.Rule(python['intermediate'], backend['novice'])
rule4 = ctrl.Rule(js['advanced'] | css_html['advanced'], front_end['advanced'])
rule5 = ctrl.Rule(c_sharp['intermediate'] | c_plus_plus['intermediate'] | python['intermediate'], backend['intermediate'])
rule6 = ctrl.Rule(js['advanced'] & css_html['advanced'], front_end['advanced'])
rule7 = ctrl.Rule(sql['advanced'], subd['advanced'])
rule14 = ctrl.Rule(sql['novice'], subd['novice'])
rule15 = ctrl.Rule(sql['intermediate'], subd['intermediate'])
rule8 = ctrl.Rule(b_network['advanced'], linux['advanced'])

rule12 = ctrl.Rule(b_network['novice'], linux['novice'])
rule13 = ctrl.Rule(b_network['intermediate'], linux['intermediate'])
rule16 = ctrl.Rule(js['novice'] & css_html['novice'], front_end['novice'])
rule17 = ctrl.Rule(js['intermediate'] & css_html['intermediate'], front_end['intermediate'])
# Create a control system
system = ctrl.ControlSystem([rule36,rule34,rule33,rule32,
                             rule31,rule28,rule29,rule30,rule27,rule26,rule24,
                             rule23,rule22,rule21,rule20,rule18,rule19,rule1, rule2, 
                             rule3, rule4, rule5, rule6,rule7,rule8,rule9,rule10,rule11,rule12,
                             rule13,rule14,rule15,rule16,rule17])
# Create a control system simulation
sim = ctrl.ControlSystemSimulation(system)

def start(val_dict):
    # Устанавливаем входные значения для симуляции из словаря val_dict
    sim.input['c_sharp'] = val_dict[4]  # Уровень знаний в C#
    sim.input['c_plus_plus'] = val_dict[3]  # Уровень знаний в C++
    sim.input['python'] = val_dict[2]  # Уровень знаний в Python
    sim.input['js'] = val_dict[1]  # Уровень знаний в JavaScript
    sim.input['css_html'] = val_dict[0]  # Уровень знаний в CSS/HTML
    sim.input['sql'] = val_dict[5]  # Уровень знаний в SQL
    sim.input['b_network'] = val_dict[6]  # Уровень знаний в сетевых технологиях

    # Запускаем симуляцию
    sim.compute()

    # Получаем выходные значения
    output_values = sim.output
    print("Backend:", output_values['backend'])  # Выводим значение для бэкенда
    print("Front End:", output_values['front_end'])  # Выводим значение для фронтенда
    print("Linux:", output_values['linux'])  # Выводим значение для Linux
    print("Unity:", output_values['unity'])  # Выводим значение для Unity
    print("Subd:", output_values['subd'])  # Выводим значение для СУБД
    print("Unreal:", output_values['Unreal'])  # Выводим значение для Unreal
    print("Scapy:", output_values['Scapy'])  # Выводим значение для Unreal
    procent = {}  # Словарь для хранения процентных значений
    procent = output_values
    procent = {key: int(value * 100) for key, value in procent.items()}
    return procent # Возвращаем массив индексов и словарь процентных значений




output_values = sim.output
# Get the output values
# output_values = sim.output
# print("Backend:", output_values['backend'])
# print("Output values:")
# if 'backend' in output_values:
#     print("Backend:", output_values['backend'])
# else:
#     print("Backend: Not available")

# if 'front_end' in output_values:
#     print("Front End:", output_values['front_end'])
# else:
#     print("Front End: Not available")

# if 'linux' in output_values:
#     print("Linux:", output_values['linux'])
# else:
#     print("Linux: Not available")

# if 'unity' in output_values:
#     print("Unity:", output_values['unity'])
# else:
#     print("Unity: Not available")

# if 'subd' in output_values:
#     print("Subd:", output_values['subd'])
# else:
#     print("Subd: Not available")

#третий уровень