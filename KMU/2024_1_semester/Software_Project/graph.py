import matplotlib
matplotlib.use('Agg')

from urllib import parse
import matplotlib.pyplot as plt

def application(environ, start_response):
    if environ['PATH_INFO']=='/graph.png':
        try:
            with open('graph.png','rb') as fp:
                response_body=fp.read()
        except:
            response_body=''.encode('utf-8')
        start_response('200 OK',
                [('Content-Type', 'image/png'),
                    ('Content-Length', str(len(response_body)))])
        return [response_body]
    else:
        d = parse.parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
        c = d.get('c', [''])[0]
        
        if '' not in (a,b,c):
            a,b,c=int(a),int(b),int(c)
            x=[i/10 for i in range(-40,41)]
            y=[a*i**2+b*i+c for i in x]
            
            fig=plt.figure()
            graph=plt.plot(x,y)
            plt.grid()
            fig.savefig('graph.png')
            
        with open('template.html','r') as fp:
            response_body=fp.read().encode('utf-8')
            
        start_response('200 OK',
                    [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))])
        return [response_body]