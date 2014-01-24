import webapp2

from config import *

app = webapp2.WSGIApplication([
								('/?', 'views.Home'),
								('/post/([0-9]+)/?', 'views.Permalink'),
								('/login/?', 'views.Login'),
								('/logout/?', 'views.Logout'),
								('/signup/?', 'views.Signup'),
								('/newpost/?', 'views.NewPost')
							], debug=True)