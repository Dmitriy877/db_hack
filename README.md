# Набор скриптов для корректировки записей электронного дневника школы

Данный репозиторий содержит крипты для:

* `check_name(name)` - скрипт для получения записи модели Schoolkid запрашиваемого ученика, а также  проверки уникальности имени ученика и правильности его ввода. Принимает аргумент `name` - ФИО ученика, возвращает запись модели Schoolkid запрашиваемого ученика. Если имя ученика не является уникальным или введено с ошибкой выводится соответствующее сообщение;
* `check_subject(subject)` - скрипт для получения записи модели Subject запрашиваемого предмета, а также проверки правильности указания предмета. Принимает аргумент `subject` - название предмета. Возвращает запись модели запрашиваено предмета. Если введено некорректное название предмета или такой предмет отсутствует в базе выводится сообщение об этом;
* `fix_marks(schoolkid)` - скрипт для корректировки оценок конкретного ученика в электронном дневнике. Изменяет все оценки 2, 3 ученика на 5. Принимает аргумент `schoolkid` - объект модели Schoolkid конкретного ученика, полученный в результате запуска функции `check_name(name)`;
* `remove_chastiments(schoolkid)`- скрипт для удаления из электронного дневника всех замечаний конкретного ученика. ППринимает аргумент `schoolkid` - объект модели Schoolkid конкретного ученика, полученный в результате запуска функции `check_name(name)`;
`create_commendation(schoolkid, subject)` - скрипт для добавления в элекронный дневник хвалебной записи для конкретного ученика по конкретному предмету за последний урок. Текст похвалы выбирается случайнм образом. Принимает аргумент `schoolkid` - объект модели Schoolkid конкретного ученика, полученный в результате запуска функции `check_name(name)`, аргумент `subject` - объект модели Subject конкретного предмета, полученный в результате запуска функции `check_subject(subject)`.

### Внимание: для данного проекта необходимо использовать Python версии 3.10 (работоспособность на других версиях Python может быть некорректной).

### Как установить

Используйте "pip" (или "pip3", есть конфлик с python2) для устанвки зависимостей (Python3 должен быть установлен):
```python
pip install -r requerements.txt
```

Для работы необходим сайт электронного дневника и файл базы данных, помещенный в папку проекта электронного дневника.


### Запуск сайта электронного дневника

Перед запуском сервера убедитесь что задали для проекта требуемые переменные

* Откройте консоль
* Перейдите в консоли в папку с проектом , например:

```python
cd ./Documents/GitHub/ediary
```

* введите в консоль команду запуска проекта на сервер с локальным адресом сервера как аргументом:

```python
python manage.py runserver 0.0.0.0:8000
```

* Произойдет запуск сервера. Для просмотра страницы со своего окомпьютера откоройте браузер и перейдите по адресу http://127.0.0.1:8000

Рекомендуется использовать [vitrualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.


### Как запустить

* Скопируйте файл scripts.py в папку с файлом manage.py проекта электронного дневника;
* Откройте консоль PowerShell;
* С помощю команды `cd` консоли перейти в папку с проектом, где расположени файл manage.py, например:

```
cd ./Documents/GitHub/ediary
```

* Откройте Django Shell командой:

```
python .\manage.py shell
```

* Импортируйте модели дневника командой:

```
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation
```

* Импортируйте функции `check_name(name)`, `check_subject(subject)`, `fix_marks(schoolkid)`, `remove_chastiments(schoolkid)` из файла scripts.py:

```
from scripts import check_name, check_subject, fix_marks, remove_chastiments, create_commendation
```
* Присвоить переменной schoolkid запись редактируемого ученика следующей командой:
```
schoolkid = check_name("ФИО ученика")
``` 
* Проверить корректность введенного имени командой (Если имя ученика не является уникальным или введено с ошибкой выводится соответствующее сообщение):
```
print(schoolkid)
``` 
* Задать название редактируемого предмета для добавления хвалебной записи:
```
subject = check_subject("Название предмета")
```
* Проверить правильность указания названия предмета командой (Если введено некорректное название предмета или такой предмет отсутствует в базе выводится сообщение об этом):
```
print(subject) 
```
* Откорректируйте оценки ранее выбранного ученика командой:
```
fix_marks(schoolkid)
```
* Удалите замечания выбранного ранее ученика командой:
```
remove_chastiments(schoolkid)
```
Добавьте случайную похвалу для ранее выбранного ученика и предмета (последнего проведенного урока) командой:
```
create_commendation(schoolkid, subject)
```

### Редактирование профиля другого ученика.

Для редактирования профиля другого ученика выполните описанные выше действия, привоив переменным schoolkid (ФИО ученика) и subject (название предмета) желаемые значения.


 ### Многократное использование

 Для повторного использования повторите действия, описанные в разделе "Как запустить"


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)