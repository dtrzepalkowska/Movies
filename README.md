<h1>Backend task</h1>

<ol>
<li>Sorting Movies by every column

Available commands:

python main.py --sort_by column_name

Example:

python main.py --sort_by year


<b>Column name must be exactly the same as in Backend_movies.csv file.</b>
</li>





<li>Filtering by:

python main.py --filter_by value_to_be_filtered_out column_name

Example inputs:
<ul>

  <li>Director</li>
  python main.py --filter_by Frank director
  </li>
  <li>Actor</li>
  python main.py --filter_by Barbara cast
  
  <li>Movies that was nominated  for Oscar but did not win any.</li>
  python main.py --filter_by only_nominated awards
  
  <li>Movies that won more than 80% of nominations</li>
  python main.py --filter_by 80_percent_won awards
  
  <li>Movies that earned more than 100,000,000 $</li>
  python main.py --filter_by big_money box_office
  
  <li>Only movies in certain Language</li>
  python main.py --filter_by Spanish language
</ul>

<b>Filtering is case sensitive.</b>

<li>Comparing by</li>
  Unavailable


<li> Adding movies to data source:</li>
  Unavailable

<li>Showing current highscores in:</li>
  Unavailable
  
</ol>
