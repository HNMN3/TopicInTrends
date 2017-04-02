**Topic In Trends**

This project is created using Django Restful Framework. 
In this project user can create their own topic, can get list of 
available topics and topics created by them.

They can also comment on a particular topic and do a reply on the comment.

****
**Technologies Used**

`Python`, `Django`, `REST`, `SQLite`

****
**Pre-requirements**
    
    Python >= 3.4.3
    Django >= 1.10
    Django Restful Framework
    
****
**Start the server**

- Open the terminal/command prompt.
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py runserver
- !! Server started. 
- Now note the URL of server.

****
**Usage**

- To create a new user run python manage.py createsuperuser
- You have to provide login credentials along with the url in headers.
- To see list of all topics do a GET request on server_url/topics/topic_list.
- To create new topic do a POST request on server_url/topics/topic_list along with the name of topic in JSON format
  with key `topic_name`.
- To see list of topics created by the the logged in user do a GET request on server_url/topics/my_topics.
- To comment on a particular topic do a post request on server_url/topics/comment/[topic_id] where topic_id is id of
  topic on which you have to comment.
- To Update comment do a PUT request on server_url/topics/comment_update