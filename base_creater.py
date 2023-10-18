import csv

def replace_spaces_with_commas(file_path):
    if file_path.endswith('.csv'):
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = [','.join(row) for row in reader]
        
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([row.split(',') for row in rows])
    else:
        with open(file_path, 'r') as file:
            content = file.read()
            replaced_content = content.replace(' ', ',').replace('\t', ',')
        
        with open(file_path, 'w') as file:
            file.write(replaced_content)

file_path = 'C://Users//kruac//OneDrive//Документы//python//ZiYou2//src//DNSS_1_09_2022.csv'  # Укажите путь к вашему файлу
replace_spaces_with_commas(file_path)