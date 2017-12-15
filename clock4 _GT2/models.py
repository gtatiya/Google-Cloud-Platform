from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs(db.Model):
    tz_offset = db.IntegerProperty(default=0)
    user = db.UserProperty(auto_current_user_add=True)

# Fetch instance of UserPrefs model of current user
def get_userprefs(user_id=None):
    if not user_id:
        user = users.get_current_user() # user will store None or email ID
        if not user:
            return None
        user_id = user.user_id() # Obtains the user ID of the user

    key = db.Key.from_path('UserPrefs', user_id) # Unique key for this entity
    userprefs = db.get(key) # Fetch instance from the datastore of a specific Model type using key
    if not userprefs:
        userprefs = UserPrefs(key_name=user_id)
    return userprefs
