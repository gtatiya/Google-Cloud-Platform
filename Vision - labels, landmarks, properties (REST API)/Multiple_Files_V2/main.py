import webapp2

import vision_rest_api

label_dict = dict()
landmark_dict = dict()
dominant_color_dict = dict()

def update_label_dict(labels, image):
    for label in labels:
        if label in label_dict:
            label_dict[label].append(image)
        else:
            label_dict[label] = []
            label_dict[label].append(image)

def update_landmark_dict(landmarks, image):
    for landmark in landmarks:
        if landmark in landmark_dict:
            landmark_dict[landmark].append(image)
        else:
            landmark_dict[landmark] = []
            landmark_dict[landmark].append(image)

def update_dominant_color_dict(dominant_color, image):
    # When image size is more than 4MB, detect_properties_GT returns empty list
    # which creates list index out of range error, so I am skipping it
    if (len(dominant_color)>1):
        if (len(dominant_color_dict) == 0):
            dominant_color_dict[dominant_color] = [image]
        else:
            range = 30
            for key in dominant_color_dict.keys():
                diff_r = abs(key[0] - dominant_color[0])
                diff_g = abs(key[1] - dominant_color[2])
                diff_b = abs(key[2] - dominant_color[2])
                if (diff_r <= range):
                    if (diff_g <= range):
                        if (diff_b <= range):
                            dominant_color_dict[key].append(image)
                        else:
                            dominant_color_dict[dominant_color] = []
                            dominant_color_dict[dominant_color].append(image)
                    else:
                        dominant_color_dict[dominant_color] = []
                        dominant_color_dict[dominant_color].append(image)
                else:
                    dominant_color_dict[dominant_color] = []
                    dominant_color_dict[dominant_color].append(image)

class MainPage(webapp2.RequestHandler):
    def get(self):

        photonames = ['2000s (15).jpg', '2000s (25).jpg', '2007.12.15  DSC00075.jpg', '2007.12.20 DSC00099.jpg', '2008.06.09 DSCN0241.JPG', '2008.06.11 DSCN0287.JPG', '2008.06.11 DSCN0289.JPG', '2010.10.19 19102010200.jpg', '2010.12.12 12122010200.jpg', '2011.02.20 20022011082.jpg', '2011.02.20 20022011134.jpg', '2011.02.21 21022011138.jpg', '2011.02.22 220220111590.jpg', '2011.02.22 22022011165.jpg', '2011.09.27 IMG (120).JPG', '2012.01.05 050120121826.jpg', '2012.01.09 090120122101.jpg', '2012.05.25 25052012174.jpg', '2013.02.06 377765_501271499919187_1848268795_n.jpg', '2014.02.12 DSC_0074.jpg', '2014.03.12 DSCN2600.JPG', '2014.03.12 DSCN2622.JPG', '2016.08.27 IMG_20160827_104641.jpg', '2017.06.14 20170614_192952-01.jpg', '2017.06.14 IMG_20170614_173138.jpg', '2017.07.22 IMG_20170722_155305.jpg', '2017.09.02 IMG_20170902_133309.jpg', '2017.09.02 IMG_20170902_133514.jpg']
        #photonames = ['2000s (15).jpg', '2000s (25).jpg', '2007.12.15  DSC00075.jpg']
        #photonames = ['2000s (15).jpg']

        url_base = "gs://seventh-terrain-179700.appspot.com/"


        for a_photo in photonames:
            labels = vision_rest_api.vision_api_label_detection(url_base+a_photo)
            update_label_dict(labels, a_photo)
            landmarks = vision_rest_api.vision_api_landmark_detection(url_base+a_photo)
            update_landmark_dict(landmarks, a_photo)
            dominant_color = vision_rest_api.vision_api_property_detection(url_base+a_photo)
            update_dominant_color_dict(dominant_color, a_photo)

        # label_dict_sorted = sorted(label_dict, key=lambda k: len(label_dict[k]), reverse=True)
        # self.response.write("LABEL_DETECTION<br>")
        # self.response.write(label_dict_sorted)
        # self.response.write("<br>")

        # landmark_dict_sorted =  sorted(landmark_dict, key=lambda k: len(landmark_dict[k]), reverse=True)
        # self.response.write("LANDMARK_DETECTION<br>")
        # self.response.write(landmark_dict_sorted)
        # self.response.write("<br>")

        # dominant_color_dict_sorted = sorted(dominant_color_dict, key=lambda k: len(dominant_color_dict[k]), reverse=True)
        # self.response.write("IMAGE_PROPERTIES<br>")
        # self.response.write(dominant_color_dict_sorted)
        # self.response.write("<br>")

        self.response.write("LABEL_DETECTION<br>")
        for k in sorted(label_dict, key=lambda k: len(label_dict[k]), reverse=True):
            self.response.write(k)
            self.response.write(", ")
            self.response.write(len(label_dict[k]))
            self.response.write(", ")
            self.response.write(label_dict[k])
            self.response.write("<br>")

        self.response.write("<br>")
        self.response.write("LANDMARK_DETECTION<br>")
        for k in sorted(landmark_dict, key=lambda k: len(landmark_dict[k]), reverse=True):
            self.response.write(k)
            self.response.write(", ")
            self.response.write(len(landmark_dict[k]))
            self.response.write(", ")
            self.response.write(landmark_dict[k])
            self.response.write("<br>")

        self.response.write("<br>")
        self.response.write("IMAGE_PROPERTIES<br>")
        for k in sorted(dominant_color_dict, key=lambda k: len(dominant_color_dict[k]), reverse=True):
            self.response.write(k)
            self.response.write(", ")
            self.response.write(len(dominant_color_dict[k]))
            self.response.write(", ")
            self.response.write(dominant_color_dict[k])
            self.response.write("<br>")

application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)
