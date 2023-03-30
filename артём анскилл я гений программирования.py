import csv

with open('schedule.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    new_rows = []

    for row in reader:
        if not (row[0].startswith("расписание") or row[0].startswith("Группа")):
            new_row = [cell.strip() for cell in row if cell.strip() != ""]
            new_rows.append(new_row)

with open('new_filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_rows)