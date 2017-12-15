import jinja2
import logging
import MySQLdb
import os
import re
import webapp2

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

def get_db():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, port=3307)
    return db

class MainPage(webapp2.RequestHandler):
    def get(self):
        guilds = []
        db = get_db()
        # http://mysql-python.sourceforge.net/MySQLdb.html#mysqldb
        try:
            cursor = db.cursor()
            cursor.execute('USE mmorpg;')
            cursor.execute('SELECT id, title, created_date, min_level FROM guild;')
            for (id, title, create_date, min_level) in cursor.fetchall():
                guilds.append({
                    'id':id,
                    'title':title,
                    'create_date':create_date,
                    'min_level':min_level
                    })
        finally:
            db.close()

        template = template_env.get_template('home.html')
        context = {
            'guilds': guilds,
        }
        self.response.out.write(template.render(context))

    def post(self):
        title = self.request.get('title').strip()
        min_level_str = self.request.get('min_level').strip()

        db = get_db()

        try:
            assert len(title) > 0
            min_level = int(min_level_str)

            key = re.sub(r'\W', '_', title.lower())

            cursor = db.cursor()
            cursor.execute('USE mmorpg;')
            cursor.execute('INSERT INTO guild VALUES (%s, %s, NOW(), %s);',(key, title, min_level_str))
            db.commit()
        except (AssertionError, ValueError), e:
            logging.info('Invalid value from user: title-%r min_level=%r', title, min_level_str)
        finally:
            db.close()

        self.redirect('/')

application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)
