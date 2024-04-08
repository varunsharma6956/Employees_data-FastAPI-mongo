from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Sarthak'}}

@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog')
def index(limit=10, published: bool= True, sort: Optional[str] =  None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}



@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}



@app.get('/blog/{id}/comments')
def about(id: int):
    return {'data': {'1', '2'}}













