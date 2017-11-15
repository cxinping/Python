import requests

key= '2684a869977e50e76d6fab6739415927'
rep = requests.get('http://v.juhe.cn/toutiao/index?type=top&key='+key)
#rep.encoding = 'utf-8'

#print( rep.json() ) 

news =  rep.json()['result']['data']

count = len( news )
print('count=',count  )

def showNew(dic):
    print('title=', dic['title'])
    print('date=', dic['date'] )
    print('category=', dic['category'] )
    print('author_name=', dic['author_name'] )
    print('url=', dic['url'] )
    
for i in news:
    print( i )
    showNew( i )
    print('\n')
    
