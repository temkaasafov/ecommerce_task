import zipfile
import os

class Extract_From_Zip:
    def extract(self):
        for _ in range(50):
            file_zip = zipfile.ZipFile(f'./data/events_week_{_ + 1}.zip')
            file_zip.extractall('./new_data')

        list = os.listdir("./new_data")
        i = 0
        for file in list:
            i += 1
            file_zip = zipfile.ZipFile(f'./new_data/{file}')
            file_zip.extractall(f'./all_json/json{i}') 
        for _ in range(350):
            json_list = os.listdir(f"./all_json/json{_ + 1}")
            
