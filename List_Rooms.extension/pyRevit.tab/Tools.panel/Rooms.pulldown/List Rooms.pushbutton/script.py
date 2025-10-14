# -*- coding: utf-8 -*-

import csv
import os.path
from datetime import datetime
from System import Math,MidpointRounding
from System.IO import IOException
from System.Globalization import CultureInfo
from Autodesk.Revit import DB
from pyrevit import forms, script

active_doc = __revit__.ActiveUIDocument.Document
room_list = DB.FilteredElementCollector(active_doc).OfCategory(DB.BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()
if room_list.Count == 0:
    forms.alert("В документе не найдено помещений.", title="Сообщение")
else:
    room_table = []
    for room in room_list:
        room_id_int = room.Id.IntegerValue # 'ElementId'
        room_name = room.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString() # 'Name'
        room_numb = room.Parameter[DB.BuiltInParameter.ROOM_NUMBER].AsString() # 'Number'
        room_area = Math.Round(DB.UnitUtils.Convert(room.Area, DB.UnitTypeId.SquareFeet, DB.UnitTypeId.SquareMeters),2, MidpointRounding.AwayFromZero) # 'Area' (м², округлён до 2 знаков)
        room_table.append([room_id_int, room_name, room_numb, room_area])

    action_choice = forms.alert("Выберите формат вывода результата:",options=["Показать таблицу в окне",
                                                                            "Сохранить в формате CSV",
                                                                            "Сохранить в CSV для русскоязычного Excel"]) # если окно выбора закрыто без выбора одной из опций, то ничего не происходит
    if (action_choice == "Показать таблицу в окне"):
        output = script.get_output()
        output.print_table(table_data=room_table, title="Помещения активного проекта", columns=["ElementId", "Name", "Number", "Area"])
    elif (action_choice in ["Сохранить в формате CSV", "Сохранить в CSV для русскоязычного Excel"]):
        project_file_dir_address = active_doc.PathName # полный путь до и имя файла проекта если активный проект сохранен, в противном случае пустая строка
        if project_file_dir_address:
            # по умолчанию - сохранение рядом с проектом, под именем "<имя_проекта>_Rooms.csv"
            file_for_csv = project_file_dir_address[:project_file_dir_address.rfind(".")] + "_Rooms.csv"
            if os.path.exists(file_for_csv):
                # добавление временной метки к имени по умолчанию, вызов диалогового окна для сохранения
                date_time = datetime.today()
                file_for_csv_name = file_for_csv[project_file_dir_address.rfind("\\")+1 : project_file_dir_address.rfind(".")] + "_Rooms_" + datetime.now().strftime("%Y%m%d-%H%M") + ".csv"
                dir_for_csv = file_for_csv[:project_file_dir_address.rfind("\\")]
                file_for_csv = forms.save_file(file_ext = "csv", init_dir = dir_for_csv, default_name = file_for_csv_name, title = "Выберите или укажите имя CSV-файла для повторного сохранения")
        else:
            file_for_csv = forms.save_file(file_ext = "csv", title = "Выберите или укажите имя CSV-файла для сохранения")
        
        if file_for_csv:
            # запись в CSV файл
            try:
                csvfile=open(file_for_csv, 'wb')
            except IOException as ioex_inst:
                forms.alert(ioex_inst.Message, title = "Ошибка при попытке записи в файл")
            else:
                with csvfile:
                    if action_choice == "Сохранить в формате CSV":
                        tablewriter = csv.writer(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL) # значения параметров delimiter, quotechar и quoting равны значениям по умолчанию
                        tablewriter.writerow(["ElementId","Name","Number","Area"])
                        for row in room_table:
                            tablewriter.writerow([row[0], row[1].encode('utf-8'), row[2].encode('utf-8'), row[3].ToString(CultureInfo.InvariantCulture)]) # десятичный разделитель '.'
                    else: # опция "Сохранить в CSV для русскоязычного Excel"
                        tablewriter = csv.writer(csvfile, delimiter = ';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                        tablewriter.writerow(["ElementId", "Name", "Number", "Area"])
                        for row in room_table:
                            tablewriter.writerow([row[0], row[1].encode('windows-1251'), row[2].encode('windows-1251'), row[3].ToString(CultureInfo("ru-RU"))]) # десятичный разделитель ','
        else:
            # если окно выбора файла для сохранения закрыто, или нажато "Отмена"
            forms.alert("Не задано имя файла. Сохранение не выполнено.", title="Ошибка при попытке записи в файл")
