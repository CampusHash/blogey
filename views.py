import webapp2

from utils import *

class BaseHandler(webapp2.RequestHandler):
	"""
	Base class for view functions, which provides
	basic rendering funtionalities
	"""

	def render(self, template, **kw):
		"""
		Render a template with the given keyword arguments
		"""

		self.response.out.write(render_str(template, **kw))

	def write(self, *a, **kw):
		"""
		Write a string to the response
		"""

		self.response.out.write(*a, **kw)