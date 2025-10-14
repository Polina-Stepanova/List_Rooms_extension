# Расширение "List Rooms" для pyRevit

Пользовательское pyRevit-расширение для Autodesk Revit, представляющее собой одну кнопку "List Rooms" в выпадающем списке "Rooms" на панели "Tools" во вкладке "pyRevit".

Позволяет получить ID элемента, имя, номер и площадь (в м², округленную до 2 знаков после запятой) для всех помещений активного проекта в виде таблицы. Таблицу можно просмотреть в отдельном окне или сохранить в формате CSV.

Версия Autodesk Revit 2021.1.2

Версия pyRevit v5.2.0

## Установка

Установка выполняется из командной строки (cmd) командой

` pyrevit extend ui List_Rooms "https://github.com/Polina-Stepanova/List_Rooms.extension.git" --branch="main" `

По умолчанию расширение будет установлено в ` C:\Users\<username>\AppData\Roaming\pyRevit\Extensions `. Указать директорию для установки можно с помощью ` --dest="<dest_path>" `.

## Использование

szx ячы SZX ЯЧЫ

После установки, при следующем запуске Revit в вкладке pyRevit появится 

![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/dropdown-button.PNG?raw=true "Скриншот выпадающего списка 'Rooms'")
![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/list-rooms-button.png?raw=true "Скриншот кнопки 'List Rooms'")

Сохранение в CSV-файл происходит в директорию, содержащую файл текущего проекта, под именем 
