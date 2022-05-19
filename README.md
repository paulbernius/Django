# InfraTie Solutions Demo

<a href="https://img.shields.io/badge/License-undefined-brightgreen"><img src="https://img.shields.io/badge/License-undefined-brightgreen"></a>
<a href="https://www.python.org/about/gettingstarted/"><img src="https://img.shields.io/badge/Language-Python-yellow"></a>
<a href="[https://www.python.org/about/gettingstarted/](https://www.djangoproject.com)"><img src="https://img.shields.io/badge/Framework-Django-green"></a>


## :book: Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Challenges](#challenges)
- [Usage](#usage)
- [Contact Information](#contact-information)

### Description
This project was created to demonstrate my skills within the Django framework for Python
<br/>
#### Project Requirements:
- Develop a web-based database application with Django
- Create login page
- Create page for Table 1 data (Displays after user logs in)
- Create page for Table 2 data (Displays data relating to the row selected in Table 1)
- Table 1 <table class="table table-hover align-middle">
            <thead>
            <tr>
                <th scope="col" style="text-align: center;">InspectionID</th>
                <th scope="col" style="text-align: center;">PipeID</th>
                <th scope="col" style="text-align: center;">Length</th>
                <th scope="col" style="text-align: center;">Width</th>
                <th scope="col" style="text-align: center;">Rating</th>
            </tr>
            </thead>
            <tbody>
                <tr>
                    <td scope="row" style="text-align: center;">1</a>
                    <td style="text-align: center;">UA1001</td>
                    <td style="text-align: center;">220</td>
                    <td style="text-align: center;">8</td>
                    <td style="text-align: center;">3</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">2</a>
                    <td style="text-align: center;">UA1001</td>
                    <td style="text-align: center;">220</td>
                    <td style="text-align: center;">8</td>
                    <td style="text-align: center;">5</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">3</a>
                    <td style="text-align: center;">UA1002</td>
                    <td style="text-align: center;">150</td>
                    <td style="text-align: center;">12</td>
                    <td style="text-align: center;">4</td>
                </tr>
            </tbody>
        </table>   
- Table 2 <table class="table table-hover align-middle">
            <thead>
            <tr>
                <th scope="col" style="text-align: center;">ConditionID</th>
                <th scope="col" style="text-align: center;">InspectionID</th>
                <th scope="col" style="text-align: center;">Distance</th>
                <th scope="col" style="text-align: center;">Code</th>
            </tr>
            </thead>
            <tbody>
                <tr>
                    <td scope="row" style="text-align: center;">1</a>
                    <td style="text-align: center;">1</td>
                    <td style="text-align: center;">0</td>
                    <td style="text-align: center;">AMH</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">2</a>
                    <td style="text-align: center;">1</td>
                    <td style="text-align: center;">25</td>
                    <td style="text-align: center;">CC</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">3</a>
                    <td style="text-align: center;">1</td>
                    <td style="text-align: center;">80</td>
                    <td style="text-align: center;">FL</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">4</a>
                    <td style="text-align: center;">1</td>
                    <td style="text-align: center;">130</td>
                    <td style="text-align: center;">MSA</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">5</a>
                    <td style="text-align: center;">2</td>
                    <td style="text-align: center;">0</td>
                    <td style="text-align: center;">AMH</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">6</a>
                    <td style="text-align: center;">2</td>
                    <td style="text-align: center;">80</td>
                    <td style="text-align: center;">CM</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">7</a>
                    <td style="text-align: center;">2</td>
                    <td style="text-align: center;">200</td>
                    <td style="text-align: center;">CC</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">8</a>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">0</td>
                    <td style="text-align: center;">AMH</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">9</a>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">65</td>
                    <td style="text-align: center;">SSS</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">10</a>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">110</td>
                    <td style="text-align: center;">FM</td>
                </tr>
                <tr>
                    <td scope="row" style="text-align: center;">11</a>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center;">150</td>
                    <td style="text-align: center;">AMH</td>
                </tr>
            </tbody>
        </table>



### Installation
- Step 1 (Optional) Install virtual environment: ```$ pip3 install virtualenv```
- Step 2 (Optional) Activate virtual environment: ```$ virtualenv 'name' source env/bin/activate```
- Step 3 Install Django: ```$ pip3 install Django```
- Step 4 Clone repo: ```$ git clone https://github.com/paulbernius/Django```
- Step 5 (May only apply to some users):
  - Make a demo project to copy *SECRET KEY*
  - Open CMD (Windows) or Terminal (Mac & Linux)
  - ```$ django-admin startproject demo```
  - Navigate to *settings.py*
  - Copy *SECRET KEY*
  - Navigate to cloned folder and open *settings.py*
  - Paste copied *SECRET KEY*
- Step 6: In the same folder from step 5, execute 
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
- Step 7 Create Superuser: ```$ python3 manage.py createsuperuser```
- Step 8 Run server: ```$ python3 manage.py runserver```

### Challenges
While developing this project I did encounter some problems.<br/><br/>

#### Challenge 1 (Presenting the InspectionID the user is viewing in Detail view (Table 2)):
To read data from a data model in Django, you must insert the data into a *context* dict. This allows the developer to dynamically create componenets.<br/><br/>
The challenge I faced with this is accessing a single value from the dictionary. While I could easily create a dynamic table with the data, I was having trouble accessing a single value (InspectionID). A better understanding of how Python's dictionaries work would've helped during the development.<br/><br/>
To overcome this challenege, I used the Django documentation to better understand the context dictionary. Initially, I had this single line to access the data model:
```python
context["dataset"] = Table2.objects.filter(InspectionID=InspectionID)
```
Adding this line allowed me to access to the requested InspectionID from the user:
```python
context["InspectionID"] = InspectionID
```
Now in the HTML code, I can use ```{{ InspectionID }}``` to access the requested InspectionID
<br/><br/>

#### Challenge 2 (While creating user 'Client' Django default auth api wouldn't allow usernames and passwords to be similar):
Django, by default, has APIs to handle password verification.<br/><br/>
```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```
<br/>The ```UserAttributeSimilarityValidator``` attribute prevents passwords being created that are too similar to the user name. Because of this attribute, I was initially unable to create the requested password for user 'Client'.<br/><br/>
To Fix this, I removed ```UserAttributeSimilarityValidator``` from ```AUTH_PASSWORD_VALIDATORS```, allowing users to create passwords that are similar to their usernames.
<br/><br/>


#### Challenge 3 (Application determining whether or not a user is currently logged in):
Django has libraries that handle many things, but specific to this challenge, it has an authentication library.
<br/><br/>
In early development of this project, when the user requested ```http://localhost:8000```, they could bypass the login page and access the data without authentication.
<br/><br/>
Upon reading Python documentation, I found how to use <a href="https://svn.python.org/projects/external/Jinja-2.1.1/docs/_build/html/api.html">Jinja</a> to create if-else statements inline with HTML code.
<br/><br/>
Adding this code in my home HTML file allowed me determine whether or not a user has been authenticated or not. If so, display the home page. If not, request the user to login.
```
{% if user.is_authenticated %}
{% else %}
{% endif %}
```


### Usage

After installation, the project should be running at http://localhost:8000
![Screen Shot 2022-05-18 at 8 59 43 PM](https://user-images.githubusercontent.com/100249266/169187718-e7abcfee-d1fc-476a-97cd-b019796f8067.png?raw=true)

Since this is the first time the user has visited the web-application, the user will not be logged in.<br/>
To log in, click the 'Log In' button. <br/>
The user will then be presented with a login form.
![Screen Shot 2022-05-18 at 9 01 57 PM](https://user-images.githubusercontent.com/100249266/169187851-713512e7-44d4-423b-98b6-c973e27c7a8a.png)

The default login credentials are:<br/>
Username: ```Client```<br/>
Password: ```Client1234!```
![Screen Shot 2022-05-18 at 9 03 48 PM](https://user-images.githubusercontent.com/100249266/169188041-1a8100a9-6b34-4b66-acbe-7d63e3d58247.png)

Once the user has logged in, they will presented with data from Table 1.
From this page the user can:
- Request data from Table 2
- Logout
![Screen Shot 2022-05-18 at 9 05 00 PM](https://user-images.githubusercontent.com/100249266/169188157-39366677-daec-42b9-a4d0-2d3f4305d98e.png)

If a user clicks on any row, the application will present data in Table 2 relating to the data selected in Table 1.
- InspectionID 1: ![Screen Shot 2022-05-18 at 9 05 58 PM](https://user-images.githubusercontent.com/100249266/169188265-132e19cd-959a-44b7-bba3-a6d0e4dc93c9.png)
- InspectionID 2: ![Screen Shot 2022-05-18 at 9 06 17 PM](https://user-images.githubusercontent.com/100249266/169188292-01f372c4-cee1-4c73-810b-f5732eef1393.png)
- InspectionID 3: ![Screen Shot 2022-05-18 at 9 06 34 PM](https://user-images.githubusercontent.com/100249266/169188324-e7dc3b53-4f42-4a80-aea8-4e8c6911eb3e.png)

If the user is viewing data from Table 2, they may press the 'Home' button or their username to return to the Home page.


### Contact-Information
[Github Profile](https://github.com/paulbernius)
<br/><br/>
paul.bernius@okstate.edu




