import webapp2

from google.appengine.api import users

from utils import *
from models import Post

class BaseHandler(webapp2.RequestHandler):
	"""
	Base class for view functions, which provides basic rendering 
	funtionalities
	"""

	def render(self, template, **kw):
		"""
		Render a template with the given keyword arguments
		"""

		self.response.out.write(render_str(template, **kw))

	def initialize(self, *a, **kw):
		"""
		Override the constuctor for adding user information
		when a request comes
		"""

		webapp2.RequestHandler.initialize(self, *a, **kw)
		self.user = users.get_current_user()

class Home(BaseHandler):
	"""
	Handle the homepage, which shows the 10 most recent blog posts
	"""

	def get(self):
		"""
		For a GET request, return the homepage
		"""

		top_posts = Post.top_posts()

		self.render("home.html", posts=top_posts, user=self.user, permalink=False)

class Permalink(BaseHandler):
	"""
	Handle permalink for the posts
	"""

	def get(self, post_id):
		"""
		For a GET request with a valid post_id, return the post
		Else, return a 404 error
		"""

		post = Post.get_by_id(int(post_id))
		if post:
			self.render("home.html", user=self.user, posts=[post], permalink=True)
		else:
			self.abort(404)

class Login(BaseHandler):
	"""
	Handle login to the blog
	"""

	def get(self):
		"""
		For a GET request, render the login page
		"""

		if self.user:
			self.redirect('/')
		else:
			self.redirect(users.create_login_url('/'))

class Logout(BaseHandler):
	"""
	Log out a user
	"""

	def get(self):
		"""
		Log out the user and redirect her to homepage
		"""

		self.redirect(users.create_logout_url('/'))

class NewPost(BaseHandler):
	"""
	Create a new post
	"""

	def get(self):
		"""
		Render the form for adding new post
		"""

		if not self.user:
			self.redirect('/login')

		self.render('newpost.html', user=self.user)

	def post(self):
		"""
		Add a new post, and redirect to the permalink page
		"""

		title = self.request.get('title')
		content = self.request.get('content')
		user = self.user

		if not user:
			self.abort(403)

		try:
			post_id = Post.create_new(title=title, content=content, user=user)
			self.redirect('/post/%s' % str(post_id))

		except Exception, e:
			self.render('newpost.html', 
						post={'title' : title, 'content' : content},
						user=self.user,
						error=e)