## Basic REST API Built with Flask

I created this simple CRUD API to learn a little about how creating API's with Flask works.  

# The Process

I created a Flask project by first creating a Flask environment by following the [installation](https://flask.palletsprojects.com/en/1.1.x/installation/#installation) and [quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#) guides in the Flask documentation.

I first tried to get server side variables to be modified by calls from Postman, but decided quickly after that I should try to just get some kind of database functionality implemented.  I searched for the best way to do this and came across [Psycopg2](https://www.psycopg.org/docs/).  I did quite a bit of reading on their docs along with some Googling and finally figured out what I needed to be doing.

For a while my calls to my database were connecting but my queries weren't being executed.  My post was even iterating my ids in the table I was trying to insert into but the values weren't being saved.  The lst piece of that puzzle was `conn.commit()`, which is weird but seems to commit the changes made in the queries.

Everything works as intended although what I'm getting back in Postman for responses is a little different than what I'm expecting.  GET, POST, PUT, and DELETE all work as they should.