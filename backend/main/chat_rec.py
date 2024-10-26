import json


# try:
#     with open('recomend.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     print
# except json.JSONDecodeError as e:
#     print("Ошибка при чтении JSON:", e)
# except FileNotFoundError:
#     print("Файл не найден. Проверьте путь.")
# Исходный словарь

# data = {
#     '1': 55,
#     '0': 43,
#     '3': 34,
#     '4': 32,
#     '2': 32,
#     '5': 32,
#     '6': 27
# }
# def set_user_id(mass):
#     global data
#     data = mass
def pces(data):
    # Чтение рекомендаций из JSON-файла
    with open('recomend.json', 'r', encoding='utf-8') as file:
        recommendations_data = json.load(file)

    # Создание словаря с рекомендациями на основе значений
    recommendations = {}
    for id, value in data.items():
        if id in recommendations_data['recommendations']:
            for level, params in recommendations_data['recommendations'][id].items():
                if params['min'] <= value <= params['max']:
                    recommendations[id] = params['text']
                    break
        else:
            recommendations[id] = ""

    # Преобразование словаря с рекомендациями в JSON
    # json_output = json.dumps(recommendations, indent=4, ensure_ascii=False)

    # Вывод JSON
    # print(json_output)
    return recommendations
def pcess(data):
    # Чтение рекомендаций из JSON-файла
    with open('recomend23.json', 'r', encoding='utf-8') as file:
        recommendations_data = json.load(file)

    # Создание словаря с рекомендациями на основе значений
    recommendations = {}
    for id, value in data.items():
        if id in recommendations_data['recommendations']:
            for level, params in recommendations_data['recommendations'][id].items():
                if params['min'] <= value <= params['max']:
                    recommendations[id] = params['text']
                    break
        else:
            recommendations[id] = ""

    # Преобразование словаря с рекомендациями в JSON
    # json_output = json.dumps(recommendations, indent=4, ensure_ascii=False)

    # Вывод JSON
    # print(json_output)
    return recommendations