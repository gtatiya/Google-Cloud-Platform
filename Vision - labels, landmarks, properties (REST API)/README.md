# Vision - labels, landmarks, properties (REST API)

This code takes an image stored in Cloud Storage and uses REST API to labels, landmarks, properties analysis using Vision API.
It returns top 5 unique labels, and landmarks, and the most dominant color of the image.

## Requirement:
- API key
- url of image in Cloud Storage

## Source
https://gist.github.com/skoegl/a322a3b66f997ef0591c5a48f5da872c
https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate
https://cloud.google.com/vision/docs/quickstart
https://cloud.google.com/vision/docs/using-curl
https://cloud.google.com/vision/docs/detecting-labels#vision-label-detection-protocol
https://cloud.google.com/vision/docs/detecting-landmarks#vision-landmark-detection-gcs-protocol


## Multiple_Files_V2

This program takes in images located in Cloud Storage and does labels, landmarks, properties analysis using Vision API.
For each image it considers only top 5 unique labels, and landmarks, and the most dominant color.

After the analysis, it creates 3 dictionaries (label_dict, landmark_dict, dominant_color_dict).

## label_dict = {
Label1: [pic1, pic2, pic3, …],
Label2: [pic1, pic2, pic3, …],
Label3: [pic1, pic2, pic3, …],
…
}

## landmark_dict = {
Landmark1: [pic1, pic2, pic3, …],
Landmark2: [pic1, pic2, pic3, …],
Landmark3: [pic1, pic2, pic3, …],
…
}

## dominant = {
(R1, G1, B1): [pic1, pic2, pic3, …],
(R2, G2, B2): [pic1, pic2, pic3, …],
(R3, G3, B3): [pic1, pic2, pic3, …],
…
}

Finally, it prints each dictionary in a sorted way. So, for example, label that has highest number of pics will be at the top.

## Output:

LABEL_DETECTION
[u'tourism', u'sky', u'fun', u'travel', u'vacation', u'statue', u'temple', u'recreation', u'monument', u'social group', u'landmark', u'tree', u'building', u'historic site', u'youth', u'community', u'sculpture', u'urban area', u'leisure', u'arch', u'product', u'tourist attraction', u'infrastructure', u'nature', u'space', u'town square', u'cool', u'woody plant', u'artwork', u'adventure', u'fortification', u'ceremony', u'memorial', u'archaeological site', u'city', u'headgear', u'plant', u'male', u'beach', u'ancient history', u'amusement park', u'water', u'yellow', u'sign', u'mural', u'suit', u'crowd', u'art', u'mammal', u'event', u'classical architecture', u'triumphal arch', u'signage', u'column', u'light', u'ruins', u'photograph', u'medieval architecture', u'team', u'professional', u'friendship', u'sand', u'wood', u'person', u'green', u'advertising']

LANDMARK_DETECTION
[u'Gateway of India', u'The Red Fort', u'India Gate', u'Red Fort', u'Lotus Temple', u'Qutb Minar', u'Taj Mahal Palace & Tower', u'New Delhi railway station', u'Mehrangarh Fort', u'Public Garden']

IMAGE_PROPERTIES
[(215, 251, 254), (126, 119, 110), (229, 228, 231), (62, 50, 46), (94, 82, 55), (189, 195, 214), (126, 118, 111), (241, 242, 244), (132, 110, 86), (140, 194, 248), (225, 182, 86), (75, 83, 111), (167, 202, 235), (197, 202, 208), (226, 228, 234), (198, 157, 11), (130, 124, 120), (135, 154, 209), (158, 115, 57), (184, 187, 164), (116, 73, 58), (177, 150, 123), (155, 108, 85), (156, 34, 26), (80, 127, 193), (0, 0, 0), (52, 48, 52), (198, 73, 72)]