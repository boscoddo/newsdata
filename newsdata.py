# Udacity Project 1: Log Analysis
# By Bosco Do

import psycopg2


# To Execute Queries
def execute_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def newsdata():
    """
      - Query 1 for What are the most popular three articles of all time?
      - Execute query 1 to get results 
      - prints sorted list with the most popular article at the top.
    """
    query1 = ("""
        select title, art_total_views from
            (select substr(path, 10), count(*) as art_total_views from log
            where path !='/' group by path)
        as hits, articles where substr = slug order by art_total_views desc limit 3;
        """)
    results = execute_query(query1)
    print('1. What are the most popular three articles of all time?')
    for title, art_total_views in results:
        print('{} - {} views'.format(title, art_total_views))
    print ""

    """
      - Query 2 Who are the most popular article authors of all time?
      - Execute query 2 to get results 
      - prints sorted list with the most popular author at the top.
    """
    query2 = ("""
        select name, sum(views) as aut_total_views from
            (select name, author, title, views from
                (select substr(path, 10), count(*) as views from log
                    where path !='/' group by path)
                as hits, articles, authors
                where substr = slug and author = authors.id
                order by views desc)
            as threetables group by name order by aut_total_views desc;
        """)
    results = execute_query(query2)
    print('2. Who are the most popular article authors of all time?')
    for name, aut_total_views in results:
        print('{} - {} views'.format(name, aut_total_views))
    print ""

    """
      - Query 3 - On which days did more than 1% of requests lead to errors?
      - Execute query 3 to get results 
      - prints results
    """
    query3 = ("""
        select error_date, http_requests, error_404,
        error_404 * 100 / http_requests as error_percent from
            (select date_trunc('day', time) as date_request, count(*)
            as http_requests from log group by date_request)
            as requests,
            (select date_trunc('day', time) as error_date, count(*)
            as error_404 from log where status = '404 NOT FOUND'
            group by error_date)
            as errors
        where date_request = error_date
        and errors.error_404 > 0.01 * requests.http_requests
        order by error_date desc;
        """)
    results = execute_query(query3)
    print('3. On which days did more than 1% of requests lead to errors?')
    for error_date, http_requests, error_404, error_percent in results:
        print("{:%B %d, %Y} - {:.2f}% errors".format(error_date, error_percent))
    print ""


if __name__ == "__main__":
    newsdata()
