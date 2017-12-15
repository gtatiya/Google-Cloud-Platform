import webapp2
from fpdf import FPDF
import urllib2
import os
from cStringIO import StringIO

import snippets

pdf = FPDF()
pdfFile = StringIO()

class MainPage(webapp2.RequestHandler):
    def get(self):
        #imagelist = ["https://storage.googleapis.com/seventh-terrain-179700.appspot.com/L2FwcGhvc3RpbmdfdXMtZWFzdDQvYmxvYnMvQUVuQjJVclRWX29DNFJoVTJ3MjdIVm1LTUdaRzlqTnhENTlYMld5V3ctbU54N1h1bzNkckJ0alRvYXNmWEc4Y2tlT1lFd2FMZnhKT0lVQ2ZwbjJvZnVmM1lsODdZV3BLU0EucDBYMlpTWVlmZjBZaERYSQ", "https://storage.googleapis.com/seventh-terrain-179700.appspot.com/23915524_10159795172600226_2298623785197372860_n.jpg"]
        imagelist = ["https://storage.googleapis.com/scene-maker.appspot.com/excuses.jpg", "https://storage.googleapis.com/scene-maker.appspot.com/excuses2.jpg"]

        pdf = FPDF()
        i = 0
        for image in imagelist:
            buketName = image.split('/')[3]
            blobName = image.split('/')[4]

            snippets.rename_blob_GT(buketName, blobName, 'image'+str(i)+'.jpg')

            #image = urllib2.urlopen(image)

            image = urllib2.urlopen("https://storage.googleapis.com/"+buketName+"/"+'image'+str(i)+'.jpg')

            filename = os.path.basename(urllib2.urlparse.urlparse(image.url).path)
            self.response.write(filename+"<br>")

            # with open('image'+str(i)+'.jpg','wb') as output:
            #     output.write(image.read())

            pdf.add_page()
            #pdf.image('image'+str(i)+'.jpg', 10, 10, 100, 100) # pdf.image(image,x,y,w,h)

            pdf.image(image, 10, 10, 100, 100) # pdf.image(image,x,y,w,h)

            #os.remove('image'+str(i)+'.jpg')
            i += 1

        pdf.output("yourfile.pdf", "F")

application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)
