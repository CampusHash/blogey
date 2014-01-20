from google.appengine.ext import ndb

class User(ndb.Model):
	"""
	A registered user
	"""

	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	email = ndb.StringProperty()
	joined = ndb.DateTimeProperty(auto_now_add=True)

class Post(ndb.Model):
	"""
	A blog post written by a registered user
	"""

	subject = ndb.StringProperty(required=True)
	content = ndb.TextProperty(required=True)
	author = ndb.KeyProperty(kind='User', required=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	modified = ndb.DateTimeProperty(auto_now=True)