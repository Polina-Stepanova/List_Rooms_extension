# Расширение "List Rooms" для pyRevit

Пользовательское pyRevit-расширение для Autodesk Revit. Позволяет получить ID элемента, имя, номер и площадь (в м², округленную до 2 знаков после запятой) для всех помещений активного проекта в виде таблицы. Таблицу можно просмотреть в отдельном окне или сохранить в формате CSV.

Версия Autodesk Revit 2021.1.2

Версия pyRevit v5.2.0

## Установка

Установка выполняется из командной строки (cmd) командой

` pyrevit extend ui List_Rooms "https://github.com/Polina-Stepanova/List_Rooms.extension.git" --branch="main" `

По умолчанию расширение будет установлено в ` C:\Users\<username>\AppData\Roaming\pyRevit\Extensions `. Указать директорию для установки можно с помощью ` --dest="<dest_path>" `.

## Использование


После установки, при следующем запуске Revit в вкладке "pyRevit" появится панель "Tools", на которой расположен выпадающий список "Rooms", содержащий одну кнопку "List Rooms".

![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/dropdown-button.PNG?raw=true "Скриншот выпадающего списка 'Rooms'")
![Alt text](https://github.com/Polina-Stepanova/List_Rooms/blob/main/images/list-rooms-button.png?raw=true "Скриншот кнопки 'List Rooms'")

Нажатие на кнопку вызывает окно выбора действия с тремя вариантами работы с собранной информацией о помещениях:

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/90ca62228663ef92a6fc317b34a2f6e350f37920/images/output-options.PNG?raw=true "Скриншот диалогового окна с выбором из 3 вариантов представления собранной информации о помещениях")

Опция **Показать таблицу в окне** вызовет окно вывода, в котором будет отображена таблица, содержащая 4 столбца: _ElementId_, _Name_, _Number_ и _Area_. 
- В _ElementId_ находятся уникальные идентификаторы объектов-помещений проекта,
- В _Name_ - задаваемое имя помещения,
- В _Number_ - задаваемый номер помещения,
- В _Area_ - рассчитанная Revit площадь помещения в квадратных метрах, округленная до 2 знаков после запятой.

![Alt text](https://github.com/Polina-Stepanova/List_Rooms.extension/blob/34791f19183e702ba4e9ef422d5a5edcf0710a1e/images/ouput-table-start.PNG?raw=true "Скриншот таблицы в окне вывода")

Опция **Сохранить в формате CSV**

szx ячы SZX ЯЧЫ

Сохранение в CSV-файл происходит в директорию, содержащую файл текущего проекта, под именем 


Опция **Сохранить в CSV для русскоязычного Excel** 

В случае, если в текущем открытом документе нет помещений, при нажатии на кнопку будет только показано соответствующее сообщение.


