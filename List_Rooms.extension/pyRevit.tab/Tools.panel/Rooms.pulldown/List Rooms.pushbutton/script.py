# -*- coding: utf-8 -*-

from System.IO import IOException
from System.Globalization import CultureInfo
from Autodesk.Revit import DB
from pyrevit import forms, script
import lib.ListRoomsFunctions

active_doc = __revit__.ActiveUIDocument.Document
room_list = DB.FilteredElementCollector(active_doc).OfCategory(DB.BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()
if room_list.Count == 0:
    forms.alert("В документе не найдено помещений.", title="Сообщение")
else:
    room_table = lib.ListRoomsFunctions.fill_room_table(room_list) # получение таблицы параметров помещений
    action_choice = forms.alert("Выберите формат вывода результата:",options=["Показать таблицу в окне",
                                                                            "Сохранить в формате CSV",
                                                                            "Сохранить в CSV для русскоязычного Excel"]) # если окно выбора закрыто без выбора одной из опций, то ничего не происходит
    if (action_choice == "Показать таблицу в окне"):
        output = script.get_output()
        output.print_table(table_data=room_table, title="Помещения активного проекта", columns=["ElementId", "Name", "Number", "Area"])
    elif (action_choice in ["Сохранить в формате CSV", "Сохранить в CSV для русскоязычного Excel"]):
        file_for_csv = lib.ListRoomsFunctions.determine_save_file_name(active_doc.PathName) # имя CSV файла для сохранения, параметр - полный путь до и имя файла проекта если активный проект сохранен, в противном случае пустая строка
        if file_for_csv:
            # запись в CSV файл
            try:
                csvfile=open(file_for_csv, 'wb')
            except IOException as ioex_inst:
                forms.alert(ioex_inst.Message, title = "Ошибка при попытке записи в файл")
            else:
                with csvfile:
                    if action_choice == "Сохранить в формате CSV":
                        lib.ListRoomsFunctions.write_table_to_csv(csvfile, room_table, delimiter_symbol=',', text_encoding='utf-8', decimal_culture=CultureInfo.InvariantCulture) # значения параметров delimiter_symbol, text_encoding и decimal_culture равны значениям по умолчанию, десятичный разделитель '.'
                    else: # опция "Сохранить в CSV для русскоязычного Excel"
                        lib.ListRoomsFunctions.write_table_to_csv(csvfile, room_table, delimiter_symbol=';', text_encoding='windows-1251', decimal_culture=CultureInfo("ru-RU")) # десятичный разделитель ','
        else:
            # если окно выбора файла для сохранения закрыто, или нажато "Отмена"
            forms.alert("Не задано имя файла. Сохранение не выполнено.", title="Ошибка при попытке записи в файл")