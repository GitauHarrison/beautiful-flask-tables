# Beautiful and functional tables

I was quite worried about how I can create a table in [my personal blog]() and add table functionalities that will allow me to quickly access any particular data. In the case where the data in the tables is too large, the addition of pagination was extremely necessary. Also, loading the data in the table as efficiently as possible would help improve the experience of working with my blog application.

## Features

- [x] Pagination of data in rows
    * Choose the number of rows to be displayed in the table
- [x] Searching for data in the entire table 
    * The application can search the entire table for a specific word or phrase (slow and not efficient as seen the Basic Table example)
    * The application can search for a specific word or phrase per the paginated data (fast and efficient as seen the Ajax Table example)
- [x] Sorting of data in the entire table
    * The application can sort the entire table by a specific column (You can choose what column to sort by during development)

## Technologies Used

- [x] Flask framework
- [x] Python for programming (front-end and back-end)
- [x] SQLAlchemy for the database
- [x] [Bootstrap](https://getbootstrap.com/) for the beautiful table
- [x] jQuery for the front-end
- [x] [dataTables.js](https://datatables.net//) library to enhance the table
- [x] [Faker](https://faker.readthedocs.io/en/master/) to generate fake user data
- [x] AJAX for the front-end
- [x] Heroku for Deployment
- [x] Docker for Deployment

Additional technologies used:

- [x] Flask login for authentication
- [x] Flask-WTF for forms
- [x] Flask-Migrate for database migrations

### Basic Table

The basic table is a table that displays all the data in the database. I call it basic in the sense that it is quite good for the purposes of displaying short data. However, it is not very efficient as it is slow to load extremely large data. 

The biggest shortcoming of the basic table, which simply shows all the user data in our database, is that, for a few seconds on page load, this table will display the entire table before pagination kicks in. In the event that the data is too large, a user will have to patiently wait as the route 'does its thing' before the actual final table is displayed.

###### Table when the page is loading for the first few seconds:

![Table on Page Load](app/static/basic-table-on-page-load.png)

###### Table when the page is fully loaded:

![Table on Page Load](app/static/app.png)

### Ajax Table

The use of Ajax helps to solve this problem. The table is loaded in chunks of data, which is then displayed on the screen. Also, searching is conviniently done on the server side. This improves the performance of the application. A user can search for a specific word or phrase in the entire table in an instant, without waiting for several seconds for Python to load the searched data.

![Searching in Ajax Table](app/static/search_alex.png)

### Deployed Application

- [x] [Flask Table App](https://beautiful-flask-tables.herokuapp.com/) on Heroku
- [x] [Flask Table App](https://hub.docker.com/r/gitauharrison/table) on Docker

### Testing

If you are interested in testing the application, you can use the following commands to run the application:

1. Clone this repository:

`$ git clone git@github.com:GitauHarrison/beautiful-flask-tables.git`

2. Change directory to access the application:

`$ cd beautiful-flask-tables`

3. Create and activate the virtual environment:

`$ mkvirtualenv flask-tables`

4. Install dependencies:

`$ pip3 install -r requirements.txt`

5. Run the application:

`$ flask run`

6. Open the application in your browser running on local port 5000:

    - [x] [Chrome](http://127.0.0.1:5000/)
    - [x] [Firefox](http://127.0.0.1:5000/)
    - [x] [Safari](http://127.0.0.1:5000/)

### Reference

I have made tremendous changes to this application since the original version. The code here is not updated. However, I have an article that goes into greater detail about how this project can be redone in a more structured way. You can read about it [here](https://github.com/GitauHarrison/notes/blob/master/flask_tables.md).

- [Interactive Flask Templates](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates) - Miguel Grinberg