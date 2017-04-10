**Topic In Trends**

This project is created using Django Restful Framework. In this project, the user can create their own topic, get a list of available topics and topics created by them.

They can also comment on a particular topic and send a reply on the comment.

****
**Technologies Used**

`Python`, `Django`, `REST`, `SQLite`

****cd 
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

- Replace the **server_url** in following points with the url you get when you start the server.
- To create a new user run python manage.py createsuperuser.
- To Authorize you have to get token from server & for that send a POST request with username and password to
  `server_url/topics/token/`.
- Now send this token in header with key name **Authorize** and key value as **Token `tokenvalue`** each time you talk to server. 
- To see list of all topics send a GET request on `server_url/topics/topic_list/`.
- To create new topic send a POST request on `server_url/topics/topic_list/` along with the name of topic in JSON format
  with key `topic_name`.
- To see list of topics created by the the logged in user send a GET request on `server_url/topics/my_topics/`.
- To comment on a particular topic send a POST request on `server_url/topics/comment/[topic_id]/` where topic_id is id of
  topic on which you have to comment along with your comment in JSON format with key `comment`.
- To Update comment send a PUT request on `server_url/topics/comment_update/[comment_id]/` where comment id is
  primary key(pk) of the comment along with your comment in JSON format with key `comment`.
- To send a reply on a particular comment send a PUT request on `server_url/topics/do_relpy/[comment_id]/` where comment id is
  primary key(pk) of the comment along with your reply in JSON format with key `reply`.
- To get list of all comments on a particular topic send a GET request on `server_url/topics/comment/[topic_id]/` 
  where topic_id is id of topic. 