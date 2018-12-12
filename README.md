# Project 1: Logs Analysis
## Description
Task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

* 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
* 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
* 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## How to run
In a terminal window type:
`python newsdata.py`

## Design
The newsdata.py is a Python Reporting Tool Program using the psycopg2 module to connect to the database.  The newsdata.py script runs 3 seperate queries and prints the results on the command line.

## Output
Query 1 - List the top 3 article by highest total views.
Query 2 - List the most popular author from highest number of views to lowest.
Query 3 - Totals the amount of request and 404 in a day to calculate to see which days had more than 1% of errors.