import os

import arabic_reshaper
import pandas as pd
import patoolib
from bidi.algorithm import get_display

Unrar_data_path = data_folder_path = Original_data_path = "/media/amirali/Data2/Data"

Citys = ["تهران", "قم", "قزوين", "مازندران", "البرز", "اصفهان", "آذربايجان شرقي", "خراسان رضوي", "خراسان شمالي",
         "خراسان جنوبي", "استان خوزستان",
         "فارس", "کرمان", "مرکزي", "گيلان", "آذربايجان غربي", "سيستان و بلوچستان", "هرمزگان", "زنجان", "کرمانشاه",
         "کردستان", "همدان", "چهارمحال و بختياري",
         "لرستان", "ايلام", "کهگيلويه و بويراحمد", "سمنان", "اردبيل", "يزد", "بوشهر", "گلستان"]
Years = ["1395", "1396", "1397", "1398", "1399", "1400", "1401", "1402"]
Month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def show_directory_contents(directory_path=data_folder_path):
    contents = []
    try:
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            contents.append(full_path)
    except FileNotFoundError:
        print("Directory does not exist.")

    return contents


def show_directory_contents_by_year_month(folder_path=data_folder_path, year='1395', month='1'):
    directory_path = os.path.join(folder_path, year, month)
    contents = []
    try:
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            contents.append(full_path)
    except FileNotFoundError:
        print(f"Directory {year}/{month} does not exist.")

    return contents


def extract_rar_file(rar_file, year, month):
    try:
        unrar_save_path = os.path.join(Unrar_data_path, year, month)
        patoolib.extract_archive(rar_file, outdir=unrar_save_path, )
    except Exception as e:
        print(f"Error occurred: {e}")


def extract_rar_folder(year, month):
    rar_files = show_directory_contents_by_year_month(
        Original_data_path, year, month)
    for item in rar_files:
        extract_rar_file(item, year, month)


def get_hourly_data_path_with_year_month_city(year, month, city):
    links = show_directory_contents_by_year_month(Unrar_data_path, year, month)
    folder_path = load_files_with_word(links, city)
    hourly_path = os.path.join(folder_path[0], "‫حجم تردد ساعتی‬")

    return show_directory_contents(hourly_path)


def get_dayly_data_path_with_year_month_city(year, month, city):
    links = show_directory_contents_by_year_month(Unrar_data_path, year, month)
    folder_path = load_files_with_word(links, city)
    hourly_path = os.path.join(folder_path[0], "‫حجم تردد روزانه‬")

    return show_directory_contents(hourly_path)


def load_files_with_word(file_paths, word):
    loaded_files = []
    for file_path in file_paths:
        if word in file_path:
            loaded_files.append(file_path)
    return loaded_files


def load_csv_file(csv_path):
    return pd.read_excel(csv_path, skiprows=1)


def getRoadAddress(year, month, city, code):
    all = get_dayly_data_path_with_year_month_city(year, month, city)
    for i in all:
        if code in i:
            return i
    return None


def getRoadName(city, code):
    pass


def getRoadCode():
    pass

def persian_fix(text):
    return get_display(
        arabic_reshaper.reshape(
            u'%s' % str(text)
        )
    )