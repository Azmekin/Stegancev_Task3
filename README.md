# Stegancev_Task3
Homework to fintechhub on Django Framework.

Задание сделано в рамках программы Машинное обучение: No code кластеризация текстов.

Реализованы модели, необходимые для хранения всей необходимой информации о задачах, пользователях с используемой дополнительной моделью, рабочих пространствах, багрепортах.

Использована библиотека DjangoRestFramework: написаны сериализаторы для каждого класса, в app/urls.py dockstring описывает назначение каждого адреса и необходимые входные параметры (при наличии).

Использованны методы авторизации библиотеки simpleJWT, установлены дополнительные правила для вывода списка всех задач (IsAdmin), метод регистрации доступен для всех.

Список методов по просьбе фронтендеров (поля для заполнения отобразятся при открытии ссылки на бэкэнде с указанным режимом доступа):

What we have:

get_all/ - take all tasks from table (only for authorized admin)

change_task/<int:pk> - update or delete task

create_task/ - create task

profile/?login=<int> - get addicted info about user with equal id

user/?login=<int> - get main info about user with equal id

workspace/?workplace_id=<int>  - get all tasks in the workspace with equal id

register/ - create new user

bugreport/ - send bugreport

