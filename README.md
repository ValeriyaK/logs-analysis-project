# Log Analysis

### Project Overview
The project requires students to create and use SQL queries that would will results from a database of a news website. The objective is to extend the student's SQL database skills. The code requirements suggest the use of only one single query to answer each request. The answer code presented here does not change the original database but utilizes views to answer the questions.

### You will need:
Python3
Vagrant
VirtualBox


# Setup

Install Vagrant And VirtualBox

``` sh
# clone this repo
git clone https://github.com/ValeriyaK/logs-analysis-project

# clone Udacity's repo
git clone https://github.com/udacity/fullstack-nanodegree-vm

cd fullstack-nanodegree-vm/vagrant/

vagrant up

vagrant ssh

cd /vagrant
```
Download the data: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Move the newsdata.sql file into your vagrant directory, then run the following command:

``` sh
psql -d news -f newsdata.sql
```

Move the contents of this repo into the /vagrant folder.

Next, you need to create the views that are used to query the database.

### Create Views

``` sh
CREATE VIEW article_views AS SELECT articles.title, 
count(log.id) AS views FROM articles, log 
WHERE log.path = concat('/article/', articles.slug) 
GROUP BY articles.title;
```

``` sh
CREATE VIEW top_authors AS SELECT authors.name, count(*) 
FROM log, articles, authors WHERE log.path = concat('/article/', articles.slug) 
AND articles.author = authors.id 
GROUP BY authors.name ORDER BY count(*) DESC;
```

``` sh
CREATE VIEW errors AS SELECT date(time), 
round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status),2) 
AS percent FROM log GROUP BY date(time) 
ORDER BY percent DESC;
```


Once the views are created, run the following command to run the python program:

``` sh
python3 news-analysis.py
```


### Troubleshooting

Python3 might not come with psycopg2, in which case, run the following command:

``` sh
pip3 install psycopg2-binary --user
```
