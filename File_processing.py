import csv
import requests

class File_processing:

    def Save_file(self):

        def Get_titles():
            with open('Backend_Movies.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                headers = []
                movie_titles = []
                for row in csv_reader:
                    #if line_count == 69:
                        if line_count == 0:
                            headers = row
                            line_count += 1
                        else:
                            movie_titles.append(row[1])
                            line_count += 1

            return headers, movie_titles

        with open('Movies_populated.csv', 'w', newline='', encoding="utf-8") as csvfile:
            URL = "http://www.omdbapi.com/"
            API_KEY = "427836a0"
            headers, movie_titles = Get_titles()
            fieldnames = headers
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            j = 0

            writer.writeheader()
            for i in movie_titles:
                PARAMETERS = {'t': i, 'apikey': API_KEY}
                response = requests.get(URL, params=PARAMETERS)
                json_data = response.json()
                j += 1
                if json_data["Type"] == "series":
                    writer.writerow({headers[0]: j,
                                     headers[1]: json_data["Title"],
                                     headers[2]: json_data["Year"],
                                     headers[3]: json_data["Runtime"],
                                     headers[4]: json_data["Genre"],
                                     headers[5]: json_data["Director"],
                                     headers[6]: json_data["Actors"],
                                     headers[7]: json_data["Writer"],
                                     headers[8]: json_data["Language"],
                                     headers[9]: json_data["Country"],
                                     headers[10]: json_data["Awards"],
                                     headers[11]: json_data["imdbRating"],
                                     headers[12]: json_data["imdbVotes"],
                                     headers[13]: "N/A"
                                     })
                else:
                    writer.writerow({headers[0]: j,
                                     headers[1]: json_data["Title"],
                                     headers[2]: json_data["Year"],
                                     headers[3]: json_data["Runtime"],
                                     headers[4]: json_data["Genre"],
                                     headers[5]: json_data["Director"],
                                     headers[6]: json_data["Actors"],
                                     headers[7]: json_data["Writer"],
                                     headers[8]: json_data["Language"],
                                     headers[9]: json_data["Country"],
                                     headers[10]: json_data["Awards"],
                                     headers[11]: json_data["imdbRating"],
                                     headers[12]: json_data["imdbVotes"],
                                     headers[13]: json_data["BoxOffice"]
                                     })
