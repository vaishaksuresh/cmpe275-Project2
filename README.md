cmpe275-Project2
================

1. Download the Zip file in your local disk
2. Assuming that you have Django and mongodb installed
3. Navigate to downloaded project path
4. fire python manage.py shell
5. from gashproj2.models import *
>>> post = Post(
... title="CMPE275 Discussion!",
... coursename = "CMPE00275",
... slug="hello!!!!",
... body = "Welcome to CMPE275 Discussion!")
>>> post.save()

6.  To add comment

comment = Comment(
... author="Sowmya Ganesan",
... body="Discussion on project2")
>>> post.comments.append(comment)
>>> post.save()

7. Run python manage.py runserver
8. you should be able to see the discussion blog opening in http://localhost:8000
