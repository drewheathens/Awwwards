# Awwwards Application.

This application is an awwward clone. It aims for professional web design and development competition body. It aims to recognize and promote the best of innovative web design for different users. It then make other users compit amongest each other.
 

## Description
This web-app allows a user to create a Profile and post Projects all under his/her username allowing other users to vote for them and visit the particular projects site. 

## User Stories

As a user I would like:
> to view posted projects and their details.
> to post a project to be rated/reviewed
> to search for projects
> to view my profile page.
> rate/ review other users' projects


## Behaviour Driven Development
* The program should return all projects on the directories page<br>
Given:All projects<br>
When: Url is changed to directory page<br>
Then: All projects are displayed<br>

* Program should show the project with the highest number of votes on the caraousel on the home page<br>
Given:A Project with the highest votes<br>
When: Home page is accessed <br>
Then: Project with highest votes is displayed.<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>


## TECHNOLOGIES USED

-HTML

-Sublime text editor

-Django

-css, Bootstrap

-postgresql for database

-github storing online repositories

-Heroku  for deploying live site

## Prerequisites

 * Internet access
 
## To install a virtual environment

 * python3.6 -m venv virtual 
 * source virtual/bin/activate

## To install all dependencies

 * python3.6 -m pip install -r requirements.txt


 * Run python3.6 manage.py runserver to get the app running  navigate to http://127.0.0.1:8000/ and it will open in your browser


## contibution & Known Bugs

When contributing to this repository, please first discuss the change you wish to make via issue. 

> It does not have bugs.But if any inquiries and concerns, email me at mudavadie@gmail.com


## **LICENSING**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
