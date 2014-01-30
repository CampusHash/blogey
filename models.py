from google.appengine.ext import ndb

from utils import *

class Post(ndb.Model):
	"""
	A blog post written by a registered user
	"""

	title = ndb.StringProperty(required=True)
	content = ndb.TextProperty(required=True)
	author = ndb.UserProperty(required=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	modified = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def top_posts(cls):
		"""
		Returns the most recent 10 blog posts
		"""
		
		top_posts = cls.query().order(-cls.created).fetch(10)
		return list(top_posts)

	@classmethod
	def create_new(cls, title, content, user):
		"""
		Create a new blog post
		"""

		# if not title or content:
		# 	raise ValidationError("Title / content cannot be empty!")

		post = cls(title=title, content=content, author=user).put()

		return post.id()