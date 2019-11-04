import csv
headers = ['id', 'title', 'year', 'runtime', 'genre', 'director', 'cast', 'writer', 'language', 'country', 'awards', 'imdb_rating', 'imdb_votes', 'box_office']

class Sorting:
    def Sort(self, column1):

        index_1 = headers.index(column1)
        #index_2 = headers.index(column2)

        with open('Movies_populated.csv', 'r', newline='') as f_input:
            csv_input = csv.DictReader(f_input)
            data = sorted(csv_input, key=lambda row: (row[column1]), reverse=True)

        with open('output.csv', 'w', newline='') as f_output:
            csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
            csv_output.writeheader()
            csv_output.writerows(data)

        with open('output.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print(f'\t{row[1]} {row[index_1]}')
                line_count += 1
            print(f'Processed {line_count} lines.')



