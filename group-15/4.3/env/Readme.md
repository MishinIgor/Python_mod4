* Фреймворк (англ. framework) - это структура, набор инструментов, библиотек и правил, предназначенных для разработки программного обеспечения. Фреймворк определяет основные архитектурные компоненты приложения, его структуру и способы взаимодействия между различными компонентами. Идея фреймворков заключается в том, чтобы предоставить разработчикам готовые решения для распространенных задач и сфокусировать их на бизнес-логике приложения, вместо того чтобы начинать с нуля при каждом новом проекте.
* Веб-фреймворк - это фреймворк, разработанный специально для создания веб-приложений. Веб-фреймворк предоставляет инструменты и структуру для упрощения процесса разработки веб-приложений, включая обработку HTTP-запросов, маршрутизацию URL-адресов, взаимодействие с базами данных, управление сессиями и многие другие задачи, связанные с веб-разработкой.
* Веб-фреймворки помогают разработчикам следовать лучшим практикам, повышают безопасность, обеспечивают масштабируемость и снижают время разработки, предоставляя готовые решения и абстракции для множества веб-ориентированных задач. Они также способствуют структурированию кода, улучшают его поддерживаемость и позволяют командам разработчиков более эффективно сотрудничать над проектами.


* Django - это бесплатный и открытый фреймворк для разработки веб-приложений на языке программирования Python. Он был создан с целью упростить процесс создания веб-приложений, предоставляя разработчикам набор инструментов и шаблонов для решения распространенных задач, связанных с веб-разработкой. Вот некоторые ключевые особенности Django:

1) ORM (Object-Relational Mapping): Django включает в себя ORM, который позволяет разработчикам работать с базами данных, используя объектно-ориентированный подход, вместо написания SQL-запросов. Это упрощает взаимодействие с базой данных и делает код более читаемым.

2) Административная панель: Django предоставляет готовую административную панель, которую можно легко настроить для управления данными в приложении. Это позволяет администраторам легко добавлять, редактировать и удалять записи в базе данных без необходимости создания пользовательского интерфейса.

3) URL-маршрутизация: Django имеет мощную систему URL-маршрутизации, которая позволяет определить, какие функции или представления должны обрабатывать различные URL-адреса в приложении.

4) Шаблоны: Фреймворк предоставляет средства для создания шаблонов HTML, которые позволяют разделять логику приложения и представление.

5) Защита от типичных уязвимостей: Django включает в себя множество встроенных мер безопасности для защиты от типичных уязвимостей, таких как атаки CSRF (межсайтовая подделка запроса) и SQL-инъекции.

6) Многоразработчиковая поддержка: Django обеспечивает удобные средства для совместной разработки приложений, включая управление версиями, миграции базы данных и другие инструменты.

* Командная строка, также известная как командный интерфейс или консоль, представляет собой текстовый интерфейс, который позволяет пользователю взаимодействовать с операционной системой или компьютером с помощью команд. Командная строка позволяет выполнять разнообразные задачи, такие как управление файлами, установка программ, настройка системных параметров и многие другие операции, используя текстовые команды.

    Вот некоторые ключевые аспекты командной строки:

1) Промпт (приглашение): Когда вы открываете командную строку, вам обычно будет предложено ввести команду, и это место, где вы видите приглашение (prompt). Обычно оно состоит из имени пользователя, имени компьютера и текущей директории, например, user@mycomputer:~$.

2) Команды: Вы вводите команды, чтобы выполнять различные действия. Команды могут быть простыми, такими как ls (для просмотра списка файлов и папок в текущей директории) или более сложными, например, git commit -m "Изменения в коде" (для создания коммита в системе контроля версий Git).

3) Аргументы и опции: Команды могут иметь аргументы (параметры), которые передаются команде для указания дополнительной информации, и опции (флаги), которые изменяют поведение команды. Например, в ls -l опция -l используется для отображения списка файлов с подробной информацией.

4) Работа с файлами и директориями: Командная строка позволяет перемещаться между директориями, создавать, копировать, перемещать и удалять файлы и директории.

5) Сценарии и автоматизация: Вы можете создавать сценарии (скрипты) с использованием командной строки, чтобы автоматизировать повторяющиеся задачи.

6) Перенаправление ввода и вывода: Вы можете перенаправлять вывод команд в файлы или использовать его как ввод для других команд.

7) Работа с переменными окружения: Вы можете устанавливать и изменять переменные окружения, которые влияют на поведение системы и программ.


Командная строка (CMD)

Эти команды позволяют вам выполнять разнообразные задачи, такие как управление файлами и папками, работу с сетью, настройку системы и многое другое. Обратите внимание, что некоторые из этих команд могут потребовать прав администратора для выполнения.

```
dir: Отображает список файлов и папок в текущей директории.


Пример: dir
```

```
cd: Перемещение между директориями (папками).
Пример:
cd C:\Users\YourUsername\Documents
```

```
mkdir: Создание новой директории (папки).
Пример:mkdir NewFolder
```

```
rmdir (или del): Удаление файлов и папок. Команда rmdir используется для удаления папок, а del - для файлов.

Пример:rmdir OldFolder / del OldFile.txt
```

```
copy: Копирование файлов.
Пример: copy File1.txt File2.txt


move: Перемещение или переименование файлов и папок.
Примеры:

move File1.txt C:\NewLocation\
move OldFolder NewName
```

```
ren: Переименование файлов и папок.
Пример:


ren File1.txt NewName.txt
```

```
ipconfig: Отображение информации о сетевых настройках, включая IP-адреса.
Пример:


ipconfig
```

```
ping: Проверка доступности других устройств в сети по их IP-адресу.
Пример:


ping google.com
```

```
tasklist: Отображение списка выполняющихся процессов.
Пример:


tasklist

taskkill: Завершение процесса по его имени или идентификатору.
Пример:


taskkill /IM notepad.exe
```

```
systeminfo: Отображение подробной информации о вашей операционной системе.
Пример:


systeminfo
```

```
shutdown: Выключение или перезагрузка компьютера.
Пример:



shutdown /s /t 0  // Выключить; Время указывается в секундах
shutdown /r /t 0  // Перезагрузить; Время указывается в секундах
```

VENV
* venv (сокращение от "virtual environment") - это инструмент в языке программирования Python, который позволяет создавать изолированные окружения для управления зависимостями и пакетами Python в ваших проектах. Он предоставляет возможность создавать отдельные виртуальные окружения для каждого проекта, что позволяет изолировать зависимости проекта от глобальных библиотек и библиотек других проектов.

Основные преимущества использования venv:

1) Изоляция зависимостей: Каждое виртуальное окружение имеет свою собственную копию интерпретатора Python и установленных пакетов. Это позволяет избежать конфликтов между версиями пакетов и обеспечивает надежную изоляцию зависимостей для каждого проекта.

2) Легкость управления зависимостями: Вы можете легко устанавливать, обновлять и удалять пакеты внутри виртуального окружения, не затрагивая глобальное окружение Python на вашей системе.

3) Чистота проектов: Используя виртуальные окружения, вы можете создавать проекты, которые содержат только те зависимости, которые действительно необходимы для работы этого проекта. Это способствует более чистому и управляемому коду.

Процесс создания и активации виртуального окружения с помощью venv в Python обычно выглядит следующим образом:

Создание виртуального окружения:
```
python -m venv myenv
```

 Эта команда создаст новое виртуальное окружение с именем myenv. Вы можете выбрать любое имя для вашего окружения.

```
Активация виртуального окружения:
В Windows:
myenv\Scripts\activate

В macOS и Linux:
source myenv/bin/activate
```

Если столкнётесь с подобной ошибкой
```
env\Scripts\activate : Невозможно загрузить файл E:\synergy\Python\4mod\group-9\4.3\env\Scripts\Activate.ps1, так как выполнение сце
нариев отключено в этой системе. Для получения дополнительных сведений см. about_Execution_Policies по адресу https:/go.microsoft.co
m/fwlink/?LinkID=135170.
строка:1 знак:1
+ env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Ошибка безопасности: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
Воспользуйтесь Windows Power Shell, и введите следующую команду:

```
Set-ExecutionPolicy Unrestricted - активирует работу со сценариями(вводить эту при ошибки выше)
Set-ExecutionPolicy Restricted - деактивирует работу со сценариями
```

* После активации виртуального окружения ваша командная строка будет указывать на имя вашего окружения, и вы будете работать в изолированном окружении.
* Установка зависимостей: После активации вы можете использовать pip для установки необходимых пакетов и зависимостей для вашего проекта.

Деактивация виртуального окружения: Когда вы закончите работу над проектом, вы можете деактивировать виртуальное окружение следующей командой:
```
deactivate
```

venv является стандартным инструментом для управления виртуальными окружениями в Python и обычно поставляется с Python. В более старых версиях Python (до Python 3.3) вы также можете использовать сторонние инструменты, такие как virtualenv, для создания виртуальных окружений.

* Когда виртуальное окружение активировано, вы увидите его имя в приглашении командной строки.

Установите Django в виртуальное окружение: Теперь, когда виртуальное окружение активировано, установите Django в него с помощью pip:

```
pip install Django
```

Создайте Django проект: Теперь вы можете создать Django проект с использованием команды django-admin:
```
django-admin startproject website
```
Здесь projectname - это имя вашего Django проекта.

Здесь projectname - это имя вашего Django проекта.
Процесс настройки и разработки: Продолжайте разрабатывать свой проект, как указано в предыдущих ответах, например, настройте базу данных, создайте приложения, настройте URL-пути, создайте представления и шаблоны.

Запустим наш сайт для проверки что мы все сделали правильно с помощью команды
```
python manage.py runserver
```
```
и перейдем по ссылке http://127.0.0.1:8000/
Нас должна встретить стартовая страница.
Для остановки работы хоста нужно нажать ctrl+c
```

Далее создадим приложение с помощью комманды 
```
django-admin startapp APP
```

Переходим в папку с проектом и открываем settings.py
Добавляем в list INSTALLED_APPS 'APP'(установленое приложение)

В папке с приложением находим файл views.py для написания функции
```py
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')
```

Далее создадим путь к ней в urls.py(в папке проекта)
(APP - имя приложения, если у вас другое нужно написать ИМЯ.views)
```py
from APP.views import *

добавим в list url новый path
path('',index)
```

Home Work

1) Создать views-функцию, которая будет выводить 3 случайных числа от 0 до 3.
2) Создать условия:

a) Если все числа равны-функция возвращает HTTPResponse с выводом чисел и надписью “Победа, все 3 числа равны!”

b) Если не выпадает одинаковых чисел возвращает HTTPResponse с выводом чисел и надписью “Повезет в следующий раз!”

3) Создать адрес для этой страницы: http://127.0.0.1:8000/game

Переходим в приложении в файл views.py и напишем функцию:
```py
import random

def gen_numbers(request):
    #Генерация трех случай чисел от 0 до 3
    num1 = random.randint(0,3)
    num2 = random.randint(0,3)
    num3 = random.randint(0,3)
    
    #Проверка на равенство всех чисел
    if num1 == num2 == num3:
        response = f'Победа, все 3 числа равны {num1}!'
    else:
        response = f'Повезет в следующий раз! Числа: {num1}, {num2}, {num3}'
    
    return HttpResponse(response)
```

Переходим в папке проекта в файл urls.py
```py
добавляем в list url новый path

path('game/',gen_numbers,name='game')
game/ - доб. адрес
gen_numbers - название функции
```