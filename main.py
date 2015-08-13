#!/usr/bin/env python
#
form = """
<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="">
          </td>
          <td class="error">
            %(one)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(two)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(three)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="">
          </td>
          <td class="error">
            %(four)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

welcomeForm = """
<form> method="get" action="/welcome">
	<p name="username" ><b>Welcome, %s !</b>.</p>
</form>

"""

import webapp2
import re

class MainHandler(webapp2.RequestHandler):

	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	PASSWORD_RE = re.compile(r"^.{3,20}$")
	EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

	errorMsg = {"one": "",
                "two": "",
                "three": "",
                "four": ""}

	def get(self):
		self.writeForm(self.errorMsg)


	def writeForm(self, message):
		self.response.write(form % message)

	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		verify = self.request.get('verify')
		email = self.request.get('email')

		if(self.verifyUsername(username) and
			self.verifyPass(password) and
			self.verifyEmail(email) and
			password == verify):
			
			self.redirect("/welcome?username=%s" % username)

		else:
			if(self.verifyUsername(username) == "None"):
				self.errorMsg['one'] = "That's not a valid username"
			
			if(self.verifyPass(password) == "None"):
				self.errorMsg['two'] = "That's not a valid password"

			if(password != verify):
				self.errorMsg['three'] = "Your passwords didn't match"

			if(self.verifyEmail(email) == "None"):
				self.errorMsg['four'] = "That's not a valid email."	

			self.writeForm(self.errorMsg)


	def verifyUsername(self, username):
		return self.USER_RE.match(username)

	def verifyPass(self, password):
		return self.PASSWORD_RE.match(password)

	def verifyEmail(self, email):
		return self.EMAIL_RE.match(email)


class WelcomeHandler(webapp2.RequestHandler): 
	def get(self):
		verifiedUserName = self.request.get('username')
		self.response.write("<b>Welcome, %s!<b>" % verifiedUserName)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome',WelcomeHandler)
], debug=True)
