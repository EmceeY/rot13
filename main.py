
import webapp2

import caesar

import cgi

def buildpage(textareacontent):
	rot_label = "<label> Rotate by how much: </label>"
	message_label = "<label> Type a message: </label>"
	rotation_input = "<input name='rotation' type='number'/>"
	textarea = "<textarea name='message'>" +  textareacontent + "</textarea>"
	submit = "<input type='submit'/>"
		
	header = "<h2> Web Caesar </h2>"

	form = "<form method='post'>" + rot_label + rotation_input + "<br>" + message_label + textarea + "<br>" + submit + "</form>" + "<br>"
	
	return header + form		

class MainHandler(webapp2.RequestHandler):
	def get(self):
		content = buildpage(" ")
		self.response.write(content)		

	def post(self):
		message = self.request.get("message")
		encrypt_number = self.request.get("rotation")
		encrypted_message = caesar.encrypt(message, encrypt_number)
		escaped_message = cgi.escape(encrypted_message)
		content = buildpage(escaped_message)
		self.response.write(content)
		

app = webapp2.WSGIApplication([
	('/', MainHandler),
], debug=True)
