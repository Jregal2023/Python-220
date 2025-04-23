# DJango Girls Tutorial

This is an application writtena as a tutorial for Django Girls

## Getting started 

To get started first go to the project Github URL and then open VSCode

Click File -> New Windows 
Click on CLone Git Repository in the Main Screen
Paste the URL of the Github Repo

## Running the application

First you need to make a virtual enviornment
Type this in your preferrre dterminal( Powershell or anything else)

```Console
> python - m venv myvenv
> myvenv\Scripts\activate
```
Then you want to install everything from the requirements.txt file

```console
>python manage.py migrate
```

Then you can run the server
```Console
> python manage.py runserver
```

Python Example Code

```python
x = 9
y = int(input("Give me another number"))
sum = x + y
```