cmpe275-Project2
================

Complete Details: http://docs.mongodb.org/manual/tutorial/write-a-tumblelog-application-with-django-mongodb-engine/



* Download the Zip file in your local disk
* Assuming that you have Django and mongodb installed
* Navigate to downloaded project path
* fire python manage.py shell

    `from gashproj2.models import *`

    `post = Post(title="CMPE275 Discussion!",  coursename = "CMPE00275", slug="hello!!!!",  body = "Welcome to CMPE275 Discussion!")`

    `post.save()`


* To add comment

    `comment = Comment(author="Sowmya Ganesan",body="Discussion on Project2")`

    `post.comments.append(comment)`
  
  `post.save()`

* Run python manage.py runserver
* you should be able to see the discussion blog opening in `http://localhost:8000`
