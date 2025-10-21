# -*- coding: utf-8 -*-

import csv
import os.path
from datetime import datetime
from System import Math,MidpointRounding
from System.Globalization import CultureInfo
from Autodesk.Revit import DB
from pyrevit import forms

def fill_room_table(room_list):
    """Формирует таблицу (список списков) параметров (ElementId, Name, Number и Area (площадь, в кв.м округленная до 2 знаков)) помещений (элементов типа OST_Rooms) из списка room_list"""
    room_table = []
    for room in room_list:
        room_id_int = room.Id.IntegerValue # 'ElementId'
        room_name = room.Parameter[DB.BuiltInParameter.ROOM_NAME].AsString() # 'Name'
        room_numb = room.Parameter[DB.BuiltInParameter.ROOM_NUMBER].AsString() # 'Number'
        room_area = Math.Round(DB.UnitUtils.Convert(room.Area, DB.UnitTypeId.SquareFeet, DB.UnitTypeId.SquareMeters),2, MidpointRounding.AwayFromZero) # 'Area' (м², округлён до 2 знаков)
        room_table.append([room_id_int, room_name, room_numb, room_area])
    return room_table

def determine_save_file_name(project_file_dir_address = ""):
    """Составляет имя CSV-файла по полному пути до и имени файла проекта. В случае отсутствия имени проекта (по пустой строке) или существования созданного имени - запрашивает имя через диалоговое окно"""
    if project_file_dir_address:
        # по умолчанию - сохранение рядом с проектом, под именем "<имя_проекта>_Rooms.csv"
        file_for_csv = project_file_dir_address[:project_file_dir_address.rfind(".")] + "_Rooms.csv"
        if os.path.exists(file_for_csv):
            # добавление временной метки к имени по умолчанию, вызов диалогового окна для сохранения
            date_time = datetime.today()
            file_for_csv_name = file_for_csv[project_file_dir_address.rfind("\\")+1 : project_file_dir_address.rfind(".")] + "_Rooms_" + datetime.now().strftime("%Y%m%d-%H%M") + ".csv"
            dir_for_csv = file_for_csv[:project_file_dir_address.rfind("\\")]
            file_for_csv = forms.save_file(file_ext = "csv", init_dir = dir_for_csv, default_name = file_for_csv_name, title = "Выберите или укажите имя CSV-файла для повторного сохранения")
        return file_for_csv
    else:
        return forms.save_file(file_ext = "csv", title = "Выберите или укажите имя CSV-файла для сохранения")

def write_table_to_csv(target_csv_file, room_table, delimiter_symbol=',', text_encoding='utf-8', decimal_culture=CultureInfo.InvariantCulture):
    """Выполняет сохранение таблицы параметров помещений room_table в CSV-файл target_csv_file"""
    tablewriter = csv.writer(target_csv_file, delimiter=delimiter_symbol, quotechar='"', quoting=csv.QUOTE_MINIMAL) # значения параметров quotechar и quoting равны значениям по умолчанию
    tablewriter.writerow(["ElementId", "Name", "Number", "Area"])
    for row in room_table:
        tablewriter.writerow([row[0], row[1].encode(text_encoding), row[2].encode(text_encoding), row[3].ToString(decimal_culture)])