# news_app
News app which takes the preference (sports, tech) and gives a feed of articles fetching data from news APIs

## Requirements
All the requirements have been specified in ```requirements.txt``` file

## How to run
- ```cd``` to the directory where this code is present.
- Install reuirements by running ```pip install -r requirements.txt```
- Run ```python manage.py makemigrations``` to make migrations
- Run ```python manage.py migrate``` to apply migrations
- Enter API Key in views.py
- Run ```python manage.py runserver``` to run the server
- API is available at ```http://127.0.0.1:8000/``` _(Optional Parameters - __q__(default="sports"),__maxResults__(default="10"))_