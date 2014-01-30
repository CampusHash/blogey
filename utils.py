from config import *

def render_str(template, **params):
	"""
	Return a string rendered by a Jinja2 template
	"""

	t = JINJA_ENV.get_template(template)
	return t.render(params)