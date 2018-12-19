# RED судя по всему имеет один метод принимающий multipart запрос, загружающий изображения.
# И возвращающий число от 0 до 1.0 в качестве ответа.
#
# Пример:
#
# <<< POST https://red.example.com/api/red_upload
#
# files = {
#     'file_for_analyze': open('image.jpg', 'rb')
# }
#
# >>> 0.9341
#
#
# Добавление сервиса RED_STATS влечет за собой добавление сущности "Клиент", и соответсвующих параметров в RED:
#
# <<< POST https://red.example.com/api/red_upload
#
# files = {
#     'file_for_analyze': open('image.jpg', 'rb')
# }
#
# data = {
#     'login': 'Edward',
#     'password': '1234',
# }
#
# >>> 0.9341
#
# Для простоты авторизация будет производится по логину/паролю клиента,
# в будущем можно использовать какой-нибудь более надежный способ: OAuth, сессионные токены, jwt.
#
# API RED_STATS содержит три метода:
#
# // Добавление измерения, методом пользуется только сервис RED
#
# >>> POST https://redstat.example.com/api/add_measure
# <<< Success 200
#
# // Метод получения статистики. Указывается начало и конец временного промежутка в формате unix timestamp (start_timestamp и end_timestamp соответсвенно), а также значение выше которого должна выдаваться статистика (red_limit_more_than)
#
# >>> GET https://redstat.example.com/api/all_measurements
#   ?start_timestamp=1540722150
#   &end_timestamp=1540822150
#   &red_limit_more_than=0.34
#
# <<< 120
#
# // Метод подписки на определенные замеры красного выше заданного
# // Для простоты, метод реализует паттерн long-polling,
# // но в будущем можно реализовать на базе WebSockets
# // (пример реализации long-poll: http://blog.fanout.io/2016/11/21/moving-from-polling-to-long-polling/)
#
# GET https://redstat.example.com/api/subscribe_measurements
#   ?red_limit_more_than=0.34
#
# В качестве базы можно взять любую современную БД: Postgresql, MySQL, SQLServer.
# Добавить таблицу Measurements:
#
# | measurement_id | measurement_time | measurement_user | measurement_result |
# | 1         | 1540722150    | 'Edward'       | 0.532        |
# | 2         | 1540722250    | 'Edward'       | 0.432        |
#
# В условии не сказано, но может появиться необходимость делать запросы по конкретным пользователям,
# предварительно уточнить вероятность возникновения такой задачи и добавить поле measurement_user, чтобы не потерять
# потенциально полезную информацию.
# Масштабировать можно путем добавления запущенных инстансов RED_STATS, единая база будет являться source of true.