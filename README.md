# Плагин "List Rooms" для pyRevit

Пользовательское pyRevit-расширение для Autodesk Revit. Позволяет получить ID элемента, имя, номер и площадь (в м², округленную до 2 знаков после запятой) для всех помещений активного проекта в виде таблицы. Таблицу можно просмотреть в отдельном окне или сохранить в формате CSV.

Версия Autodesk Revit 2021.1.2

Версия pyRevit 5.2.0

## Установка

Установка выполняется вручную.

**1.** Скачать репозиторий (архив .zip)
![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/a41fa6c3715f9665ed6f178a98c96ac04abff7de/images/how-download-dir.png?raw=true "Скриншот кнопки скачивания архива репозитория с GitHub")

**2.** Извлечь папку List_Rooms.extension, вложенную в папку List_Rooms.extension-main, в предпочтительное место на устройстве. (например ` C:\Users\<username>\Documents\List_Rooms.extension-main\List_Rooms.extension `)

**3.** Запустить Revit и в первой панели вкладки pyRevit, в выпадающем меню открыть **Настройки**.

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/07a8eb35a52433afb58af0d97387c7edca120bc1/images/pyrevit-settings.png?raw=true "Скриншот местоположения настроек pyRevit")

**4.** Добавить папку List_Rooms.extension-main, содержащую папку List_Rooms.extension, в список каталогов пользовательских расширений.

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/07a8eb35a52433afb58af0d97387c7edca120bc1/images/add-extension-folder-path.png?raw=true "Скриншот меню добавления пути к папке с пользовательским расширением")

**5.** Перезапустить Revit

## Использование

После установки при следующем запуске Revit во вкладке "pyRevit" появится панель "Tools", на которой расположен выпадающий список "Rooms", содержащий одну кнопку "List Rooms".

![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/dropdown-button.PNG?raw=true "Скриншот выпадающего списка 'Rooms'")
![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/list-rooms-button.png?raw=true "Скриншот кнопки 'List Rooms'")

Нажатие на кнопку вызывает окно выбора действия с тремя вариантами работы с собранной информацией о помещениях:

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/90ca62228663ef92a6fc317b34a2f6e350f37920/images/output-options.PNG?raw=true "Скриншот диалогового окна с выбором из 3 вариантов представления собранной информации о помещениях")

### Опция _Показать таблицу в окне_
Вызовет окно вывода, в котором будет отображена таблица, содержащая 4 столбца: _ElementId_, _Name_, _Number_ и _Area_. 

- В _ElementId_ находятся уникальные идентификаторы объектов-помещений проекта,
- В _Name_ - задаваемое пользовательское имя помещения,
- В _Number_ - задаваемый пользовательский номер помещения,
- В _Area_ - рассчитанная Revit площадь помещения в квадратных метрах, округленная до 2 знаков после запятой.

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/34791f19183e702ba4e9ef422d5a5edcf0710a1e/images/ouput-table-start.PNG?raw=true "Скриншот таблицы в окне вывода")

### Опция _Сохранить в формате CSV_
- Если активный проект сохранен, то описанная в предыдущем пункте таблица с четырьмя столбцами будет сохранена в файле в формате CSV (comma-separated values) под именем ` <имя_проекта>_Rooms.csv ` в директории, содержащей файл проекта.
- Если файл ` <имя_проекта>_Rooms.csv ` уже существует в директории, будет открыто диалоговое окно сохранения файла с именем по умолчанию с временной меткой вида ` <имя_проекта>_Rooms_YYYYMMDD-HHMM.csv `.
- Если активный проект **не** сохранен, будет открыто диалоговое окно сохранения файла без предустановленных значений.

**Результат**: CSV-файл (разделитель ',', кодировка _utf-8_, десятичный разделитель '.', первая строка содержит заголовки столбцов). Некоторые десятичные числа могут быть некорректно интерпретированы как даты при открытии файла в Microsoft Excel или Google Таблицах. (Для корректного просмотра нужно импортировать файл в Excel/Таблицы с нужными настройками.)

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/12aec8013a62b5c513293ba005c49a249712e8c4/images/base-csv.PNG?raw=true "Скриншот CSV-файла, открытого в Google Таблицах")

### Опция _Сохранить в CSV для русскоязычного Excel_ 
Порядок сохранения идентичен предыдущему пункту.

**Результат**: CSV-файл (разделитель ';', кодировка _windows-1251_, десятичный разделитель ',', первая строка содержит заголовки столбцов). Соответствует параметрам по умолчанию в русскоязычном Microsoft Excel, предназначен для просмотра в нем.

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/12aec8013a62b5c513293ba005c49a249712e8c4/images/ru-excel-compatible-csv.PNG?raw=true "Скриншот CSV-файла, совместимого с русскоязычным Microsoft Excel, открытого в Google Таблицах")

### Особые случаи:

Если в текущем открытом проекте нет помещений, при нажатии на кнопку будет только показано соответствующее сообщение:

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/527698866fca1026216e2fe19069a2631e755e60/images/no-rooms-found.PNG?raw=true "Скриншот сообщения об отсутствии помещений в активном документе")

Если окно сохранения файла закрыто без сохранения, будет показано соответствующее предупреждение:

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/a724d10a97e20ed3e2cce9ab92d5b75432a9e026/images/no-file-name-given.PNG?raw=true "Скриншот сообщения о невыполненном сохранении")
