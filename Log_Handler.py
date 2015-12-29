#!/usr/bin/env python3.4
from flask import Flask,request,render_template
res = {}
def Log(file): 
    with open('nginx_access.log') as f:
	for l in f:
	    arr = l.split(' ')
	    ip = arr[-1].rstrip().rstrip('\"').lstrip('\"')
	    url = arr[6]
	    status = arr[8]
	    res[(ip,url,status)] = res.get((ip,url,status),0) + 1

app = Flask(__name__)
@app.route('/')
def index():
	res_list = [(i[0],i[1],i[2],v) for i,v in res.items()]
	table = '<table border="10">'
	for s in sorted(res_list,key=lambda s:s[3],reverse=True)[:10]:
		table += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %s
	table += "</table>"
	return table

if __name__ == '__main__':
    Log('/usr/DaoKe/Python/haproxy.log')
    app.run(host='localhost',port=1028)
		
