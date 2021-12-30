from django.http.response import JsonResponse
from backend.models import Article, ArticleSerializer, Source
from newsapi import NewsApiClient
import datetime as dt
from django.utils.dateparse import parse_datetime


# Made this query class to keep record of - data of which query is present in database
class Query:
    def __init__(self):
        self.q="sports"
    
    def get_present_q(self):
        return self.q
    
    def change_q(self,new_q):
        self.q=new_q

query=Query()

def get_data(q="sports"):
    Article.objects.all().delete()
    newsapi = NewsApiClient(api_key='<API_KEY>')
    data = newsapi.get_everything(q=q,from_param=f"{dt.date.today()}",language='en',sort_by='publishedAt',page_size=50,page=1)
    for article in data['articles']:
        if article['source']['id']!="": # if source id is not empty
            if len(Source.objects.filter(sid=article['source']['id']))==0: # checking if source doesn't already exists
                source=Source(sid=article['source']['id'],name=article['source']['name'])
                source.save()
            else:
                source=Source.objects.get(sid=article['source']['id'])
        else: # I have considered that one of id,name would not be empty
            if len(Source.objects.filter(name=article['source']['name']))==0:
                source=Source(sid=article['source']['id'],name=article['source']['name'])
                source.save()
            else:
                source=Source.objects.get(name=article['source']['name'])
        if len(Article.objects.filter(url=article['url']))==0: # taking url for every article to be unique
            art=Article(author=article['author'],title=article['title'],description=article['description'],content=article['content'],publishedAt=parse_datetime(article['publishedAt']),url=article['url'],source=source)
            art.save()
            source.articles.add(art)

def api(request):
    if 'q' in request.GET:
        if query.get_present_q()!=request.GET['q'] or len(Article.objects.all())==0: # checking if the data present in database is of query = q in get request, or not,  if it is same then no need to fetch the api again just return the data from database
            query.change_q(request.GET['q'])
            get_data(request.GET['q'])
    elif len(Article.objects.all())==0: # if the database is empty then also fetch the data
            get_data()
    maxResults=10
    if 'maxResults' in request.GET:
        maxResults=int(request.GET['maxResults'])
        if maxResults<0 or maxResults>50:
            maxResults=10
    data=Article.objects.order_by('-publishedAt')[:maxResults]
    serializer=ArticleSerializer(data, many = True)
    return JsonResponse(serializer.data,safe = False)
