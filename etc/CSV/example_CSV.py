import csv
import time

#CSV 파일 읽기
with open('file.csv', 'r') as f:
    reader_csv = csv.reader(f, delimiter=',')
    for row in reader_csv:
        print(row)

time.sleep(3)
print('open file.csv')
#CSV 파일 쓰기
with open('file.csv', 'w') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(['love']*3+['banana'])
    writer.writerow(['Spam','Lovely Spam', 'Wonderful Spam'])


#CSV 딕셔너리 형식으로 읽기
with open('solar_2014.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['월'], row['일'], row['시간(12h)'], row['시간(16h)'])


#CSV 딕셔너리 형식으로 쓰기
with open('solar_2014.csv', 'w') as f:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
