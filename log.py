#! /usr/bin/env python3

import psycopg2
DBNAME = "news"

# 1.What are the most popular three articles of all time?

query1 = "SELECT title, views FROM article_view_number LIMIT 3"

# 2.Who are the most popular article authors of all time?

query2 = """SELECT name, SUM(article_view_number.views) AS views FROM article_view_number, authors
 WHERE authors.id = article_view_number.author
GROUP BY authors.name ORDER BY views DESC"""

# 3.On which days did more than 1% of requests lead to errors?

query3 = "SELECT * from error_log WHERE Percent_Error > 1 "

# Store results

query1_result = dict()
query1_result['title'] = "\n1. The three most popular articles of all time ae:\n"

query2_result = dict()
query2_result['title'] = """\n2. The most popular article authors of all time are: \n"""

query3_result = dict()
query3_result['title'] = """\n3. Days with more than 1% of request that lead to an error: \n"""

def get_query_result(query):
  #"""Return all results of query"""
  db = psycopg2.connect(database = DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  return results

def print_query_results(query_result):
# """Print query's the results"""
  print (query_result['title'])
  for result in query_result['results']:
    print ('\t' + str(result[0]) + '--->' + str(result[1]) + ' views')

def print_error_query_results(query_result):
#"""Print error query's results"""
  print (query_result['title'])
  for result in query_result['results']:
    print ('\t' + str(result[0]) + '--->' + str(result[1]) + '%')

# Store query results
query1_result['results'] = get_query_result(query1)
query2_result['results'] = get_query_result(query2)
query3_result['results'] = get_query_result(query3)

# Print the formatted output
print_query_results(query1_result)
print_query_results(query2_result)
print_error_query_results(query3_result)
