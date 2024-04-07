from file_handler import *

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


tehran_95_1 = get_dayly_data_path_with_year_month_city("1396", "1", "تهران")
print(len(tehran_95_1))
tehran = load_csv_file(tehran_95_1[0])
print(tehran.head(10))

tehran.describe()

tehran.info()


"""
Select a 
"""