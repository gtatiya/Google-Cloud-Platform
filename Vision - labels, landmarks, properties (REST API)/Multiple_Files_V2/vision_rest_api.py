from json import dumps, loads

from google.appengine.api import app_identity
from google.appengine.api.urlfetch import fetch, POST

api_key = "Your Key"

# It returns top 5 unique labels
def vision_api_label_detection(uri):
	"""This is the minimal code to accomplish a web detect request to the google vision api

	You don't need 56 MiB of python client code installing 'google-cloud-vision' to accomplish
	that task on google app engine, which does not even work.

	.. TODO:: you should have secured your api key before you deploy this code snippet.
	Please take a look at https://support.google.com/cloud/answer/6310037?hl=en

	:param uri: the complete uri to compare against the web
	:type uri: str
	:return: the result dictionary
	:rtype: dict
	"""

	payload = {
		"requests": [
			{
				"image": {
					"source": {
						"image_uri": uri
					}
				},
				"features": [
					{
						"type": "LABEL_DETECTION"
					}
				]
			}
		]
	}

	response = fetch(
		"https://vision.googleapis.com/v1/images:annotate?key=" + api_key,
		method=POST,
		payload=dumps(payload),
		headers={"Content-Type": "application/json"}
	)
	result = loads(response.content)

	#return len(result["responses"][0])

	if (len(result["responses"][0]) == 0):
		return []
	else:
		try:
			top_5_labels = []
			i = 0
			for label in result["responses"][0]["labelAnnotations"]:
				top_5_labels.append(label["description"])
				i += 1
				if (i == 5):
					break
			return set(top_5_labels)
		except:
			return []

# It returns top 5 unique landmarks
def vision_api_landmark_detection(uri):
	"""This is the minimal code to accomplish a web detect request to the google vision api

	You don't need 56 MiB of python client code installing 'google-cloud-vision' to accomplish
	that task on google app engine, which does not even work.

	.. TODO:: you should have secured your api key before you deploy this code snippet.
	Please take a look at https://support.google.com/cloud/answer/6310037?hl=en

	:param uri: the complete uri to compare against the web
	:type uri: str
	:return: the result dictionary
	:rtype: dict
	"""

	payload = {
		"requests": [
			{
				"image": {
					"source": {
						"image_uri": uri
					}
				},
				"features": [
					{
						"type": "LANDMARK_DETECTION"
					}
				]
			}
		]
	}

	response = fetch(
		"https://vision.googleapis.com/v1/images:annotate?key=" + api_key,
		method=POST,
		payload=dumps(payload),
		headers={"Content-Type": "application/json"}
	)
	result = loads(response.content)

	if (len(result["responses"][0]) == 0):
		return []
	else:
		try:
			top_5_landmarks = []
			i = 0
			for landmark in result["responses"][0]["landmarkAnnotations"]:
				top_5_landmarks.append(landmark["description"])
				i += 1
				if (i == 5):
					break
			return set(top_5_landmarks)
		except:
			return []

# It returns most dominant color
def vision_api_property_detection(uri):
	"""This is the minimal code to accomplish a web detect request to the google vision api

	You don't need 56 MiB of python client code installing 'google-cloud-vision' to accomplish
	that task on google app engine, which does not even work.

	.. TODO:: you should have secured your api key before you deploy this code snippet.
	Please take a look at https://support.google.com/cloud/answer/6310037?hl=en

	:param uri: the complete uri to compare against the web
	:type uri: str
	:return: the result dictionary
	:rtype: dict
	"""

	payload = {
		"requests": [
			{
				"image": {
					"source": {
						"image_uri": uri
					}
				},
				"features": [
					{
						"type": "IMAGE_PROPERTIES"
					}
				]
			}
		]
	}

	response = fetch(
		"https://vision.googleapis.com/v1/images:annotate?key=" + api_key,
		method=POST,
		payload=dumps(payload),
		headers={"Content-Type": "application/json"}
	)
	result = loads(response.content)

	try:
		r = result["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][0]["color"]["red"]
		g = result["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][0]["color"]["green"]
		b = result["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][0]["color"]["blue"]
		return (r, g, b)
	except:
		return (0, 0, 0)