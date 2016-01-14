
import webapp2
from app.handler import MainPage

app = webapp2.WSGIApplication(
	[('/', MainPage)],
	debug=True
	)