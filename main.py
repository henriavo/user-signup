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

import webapp2

class MainHandler(webapp2.RequestHandler):

	errorMsg = {"one": "That's not a valid username",
                "two": "That's not a valid password",
                "three": "Your passwords didn't match",
                "four": "That's not a valid email."}

	emptyMsg = {"one": "",
            	"two": "",
            	"three": "",
            	"four": ""}


	def get(self):
		self.writeForm()
		#below prints error msg with form
		#self.writeForm(self.emptyMsg)

	def writeForm(self, message=emptyMsg):
		self.response.write(form % message)

	def post(self):
		username = self.request.get('username')
		password = self.request.get('pass')
		verify = self.request.get('verify')
		email = self.request.get('email')

		#TODO:
		#veryfiy all user input




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
