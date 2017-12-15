import detect
import os

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

##################################################
# path = r"resources"

# photos = ['2011.02.20 20022011082.jpg', '2011.02.20 20022011134.jpg']

# ## Labels
# labels = detect.detect_labels_GT(path+os.sep+photos[1])
# print(labels)
# update_label_dict(labels, photos[1])
# print(label_dict)


# # Landmarks
# landmarks = detect.detect_landmarks_GT(path+os.sep+photos[1])
# print(landmarks)
# update_landmark_dict(landmarks, photos[1])
# print(landmark_dict)

# # dominant_color
# dominant_color = detect.detect_properties_GT(path+os.sep+'2011.02.22 22022011165.jpg')
# print(dominant_color)
# update_dominant_color_dict(dominant_color, '2011.02.22 22022011165.jpg')
# print(dominant_color_dict)
# # dominant_color
# dominant_color = detect.detect_properties_GT(path+os.sep+'2016.08.27 IMG_20160827_104641.jpg')
# print(dominant_color)
# update_dominant_color_dict(dominant_color, '2016.08.27 IMG_20160827_104641.jpg')
# print(dominant_color_dict)



#########################################
path = r"resources"

photonames = next(os.walk(path))[2] #  get only list of files 

for a_photo in photonames:
    labels = detect.detect_labels_GT(path+os.sep+a_photo)
    update_label_dict(labels, a_photo)
    landmarks = detect.detect_landmarks_GT(path+os.sep+a_photo)
    update_landmark_dict(landmarks, a_photo)
    dominant_color = detect.detect_properties_GT(path+os.sep+a_photo)
    update_dominant_color_dict(dominant_color, a_photo)

# print(label_dict)
# print(landmark_dict)
# print(dominant_color_dict)

for k in sorted(label_dict, key=lambda k: len(label_dict[k]), reverse=True):
        print(k, len(label_dict[k]), label_dict[k])

for k in sorted(landmark_dict, key=lambda k: len(landmark_dict[k]), reverse=True):
        print(k, len(landmark_dict[k]), landmark_dict[k])

for k in sorted(dominant_color_dict, key=lambda k: len(dominant_color_dict[k]), reverse=True):
        print(k, len(dominant_color_dict[k]), dominant_color_dict[k])
