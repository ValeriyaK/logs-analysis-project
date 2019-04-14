popular articles: create view article_views as select articles.title, count(log.id) as views from articles, log where log.path = concat('/article/', articles.slug) group by articles.title;


top authors: create view top_authors as select authors.name, count(*) from log, articles, authors where log.path = concat('/article/', articles.slug) and articles.author = authors.id group by authors.name order by count(*) desc;


errors: create view errors as select date(time), round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status),2) as percent from log group by date(time) order by percent desc;
