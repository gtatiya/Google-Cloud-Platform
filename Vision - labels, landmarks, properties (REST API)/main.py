import webapp2

import vision_rest_api

class MainPage(webapp2.RequestHandler):
    def get(self):
        url = "gs://seventh-terrain-179700.appspot.com/RedFort.jpg"
        
        url = "gs://seventh-terrain-179700.appspot.com/2000s (15).jpg"

        output = vision_rest_api.vision_api_label_detection(url)

        self.response.write("LABEL_DETECTION<br>")
        self.response.write(output)

        self.response.write("<br>")

        output = vision_rest_api.vision_api_landmark_detection(url)
        self.response.write("LANDMARK_DETECTION<br>")
        self.response.write(output)

        self.response.write("<br>")

        output = vision_rest_api.vision_api_property_detection(url)
        self.response.write("IMAGE_PROPERTIES<br>")
        self.response.write(output)

application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)
