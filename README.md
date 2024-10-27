# Домашнее задание по Системному программному обеспечению (СПО)
## Автор
Корпусев Владислав Дмитриевич
Группа: Фт-320007
## Метод создания готового исполняемого файла
Так как программа написана на языке Python, будем использовать pyinstaller.
PyInstaller собирает в один пакет Python-приложение и все необходимые ему библиотеки следующим образом:
1. Считывает файл скрипта.
2. Анализирует код для выявления всех зависимостей, необходимых для работы.
3. Создает файл spec, который содержит название скрипта, библиотеки-зависимости, любые файлы, включая те параметры, которые были переданы в команду PyInstaller.
4. Собирает копии всех библиотек и файлов вместе с активным интерпретатором Python.
5. Создает папку BUILD в папке со скриптом и записывает логи вместе с рабочими файлами в BUILD.
6. Создает папку DIST в папке со скриптом, если она еще не существует.
7. Записывает все необходимые файлы вместе со скриптом или в одну папку, или в один исполняемый файл.
