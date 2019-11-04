import csv
headers = ['id', 'title', 'year', 'runtime', 'genre', 'director', 'cast', 'writer', 'language', 'country', 'awards', 'imdb_rating', 'imdb_votes', 'box_office']

class Filtering:

    def Filter(self, value, column):

        index_1 = headers.index(column)

        if column in ['awards'] and value in ['only_nominated']:
            with open('Movies_populated.csv', 'r', newline='') as f_input:
                csv_input = csv.DictReader(f_input)
                filtered = filter(lambda row: 'Oscar' in row[column], csv_input)
                filtered2 = filter(lambda row: 'Won' not in row[column], filtered)

                with open('output.csv', 'w', newline='') as f_output:
                    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
                    csv_output.writeheader()
                    csv_output.writerows(filtered2)

                with open('output.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        print(f'\t{row[1]} {row[index_1]}')
                        line_count += 1
                    print(f'Processed {line_count} lines.')

        elif column in ['awards'] and value in ['80_percent_won']:
            with open('Movies_populated.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    awards = row[10]
                    numbers = [int(s) for s in awards.split() if s.isdigit()]
                    nom_awa = numbers[-2:]
                    sum_nomi = sum(nom_awa)
                    wins = sum(nom_awa[0:1])
                    if sum_nomi != 0:
                        result = (wins / sum_nomi)
                        if result >= 0.30:
                            print(f'\t{row[1]}' " %.2f" % result)
                            # print("%.2f" % result)
                    else:
                        result = 0
                    line_count += 1

                print(f'Processed {line_count} lines.')

        elif column in ['box_office'] and value in ['money']:
            with open('Movies_populated.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    money = row[13]
                    if len(money) >= 11:
                        print(f'\t{row[1]} {row[13]}')
                        # print(len(money))

        else:
            with open('Movies_populated.csv', 'r', newline='') as f_input:
                csv_input = csv.DictReader(f_input)
                filtered = filter(lambda row: value in row[column], csv_input)

                with open('output.csv', 'w', newline='') as f_output:
                    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
                    csv_output.writeheader()
                    csv_output.writerows(filtered)

                with open('output.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        print(f'\t{row[1]} {row[index_1]}')
                        line_count += 1
                    print(f'Processed {line_count} lines.')




    #print(headers.index('year'))