A RESTful API written in Django to get user activity log details.

Setting up
This project was built with python +3.8 and mongodb 4.2

$ pip3 install -r requirements.txt <br> 
cd UserActivityApp

To run the application<br>
$ python manage.py runserver

Then head to

To generate dummy user data using following custom command<br>
python manage.py populate_user_activity_log_data

To get all user activity log (get request)<br>
http://127.0.0.1:8000/user_activity_log

in your browser to get started.
