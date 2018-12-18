# Project 1: Logs Analysis
## Description
Task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

* What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## How to run
* 1. To excute this code you'll need to setup a Linux virtual machine.  Installing Virtual Box and Vagrant is recommended.
* 2. You will need to bring the virtual machine online with vagrant up, Then log into it with vagrant ssh.
* 3. Within the Linux virtual machine, please install PostgreSQL and copy newsdata.sql database (link below) and this logs analysis project to the same directory.
* 4. To load the data, cd into the directory and use the command psql -d news -f newsdata.sql
* 5. To excute the code, In a terminal window type: `python newsdata.py`

## Link to Download the newsdata database
[Please, click here!](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Design
The newsdata.py is a Python Reporting Tool Program using the psycopg2 module to connect to the database.  The newsdata.py script runs 3 seperate queries and prints the results on the command line.
* Query 1 - From log it calculates the top 3 articles views then sorts by highest total views.
* Query 2 - List the most popular author from highest number of views to lowest.
* Query 3 - Totals the amount of request and 404 in a day to calculate which days had more than 1% of errors.
