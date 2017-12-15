import webapp2

import models

# update the tz_offset values of current user in the UserPrefs model

class PrefsPage(webapp2.RequestHandler):
    def post(self):
        userprefs = models.get_userprefs() # Retrieves information associated with the user that is making a request
        try:
            tz_offset = int(self.request.get('tz_offset'))
            userprefs.tz_offset = tz_offset
            userprefs.put()
        except ValueError:
            # User entered a value that wasn't an integer.  Ignore for now.
            pass

        self.redirect('/')

application = webapp2.WSGIApplication([('/prefs', PrefsPage)],
                                      debug=True)
