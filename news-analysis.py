#! /usr/bin/env python3

import psycopg2

DBNAME = 'news'

question_one = ("What are the most popular three articles of all time?")
question_two = ("What are the most popular three articles of all time?")
question_three = ("What are the most popular three articles of all time?")

article_query = """SELECT * from article_views
                order by views desc
                limit 3;"""

author_query = """SELECT * from top_authors;"""

error_query = """SELECT * from errors limit 1;"""


def connect_to_database(query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.OperationalError as e:
        print('Unable to connect!')
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def get_top_articles():
    results = connect_to_database(article_query)
    print(question_one)
    for (title, count) in results:
        print("    {} - {} views".format(title, count))


def get_top_authors():
    results = connect_to_database(author_query)
    print(question_two)
    for (title, count) in results:
        print("    {} - {} views".format(title, count))


def get_day_with_most_errors():
    results = connect_to_database(error_query)
    print(question_three)
    for (day, percent) in results:
        print("    {} - {}%".format(day, percent))


if __name__ == '__main__':
    get_top_articles()
    get_top_authors()
    get_day_with_most_errors()
