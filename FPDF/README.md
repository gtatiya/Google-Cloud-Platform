# FPDF

pip install -t lib -r requirements.txt

pip uninstall google-cloud-storage


https://stackoverflow.com/questions/47721024/how-to-create-a-pdf-of-images-stored-in-google-cloud-storage


Yes, it says that, but when I am using:
`pdf.image("https://storage.googleapis.com/seventh-terrain-179700.appspot.com/excuses.jpg", 10, 10, 100, 100)`
I get error: `RuntimeError: FPDF error: Missing or incorrect image file: https://storage.googleapis.com/seventh-terrain-179700.appspot.com/excuses.jpg. error: [Errno 22] invalid mode ('rb') or filename: 'https://storage.googleapis.com/seventh-terrain-179700.appspot.com/excuses.jpg' `
So, I was using `urllib2.urlopen(image)` and storing it locally as mentioned here: https://stackoverflow.com/questions/3177716/fpdf-error-missing-or-incorrect-image-file
Do you know how to make it work?