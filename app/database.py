import couchdb
import json
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField
from datetime import datetime

server = couchdb.Server()
    
db = server['eventstest1']

content = []

for i in db:
    doc = db[i]
	#print(doc['title'])
	#print(doc['start'])
    information = ['Title: ' + doc['title'], 'Start: ' + doc['start']]
    for j in range(len(information)):
		information[j] = information[j].encode('UTF-8')
    #content.append('    '.join(information))
    information = []

#print(content)

class Booking(Document):
	title = TextField()
	start = TextField()
	start = str(start)
	start = start[:9]
	

for k in db:
    booking = Booking.load(db, k)
    forEachDoc = [booking.title, booking.start]
    content.append(forEachDoc)
    
print(content)
