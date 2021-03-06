# Vision - labels, landmarks, properties

This program takes in images located in 'resources' folder and does labels, landmarks, properties analysis using Vision API.
For each image it considers only top 5 unique labels, and landmarks, and the most dominant color.

After the analysis, it creates 3 dictionaries (label_dict, landmark_dict, dominant_color_dict).

## label_dict = {
Label1: [pic1, pic2, pic3, �],
Label2: [pic1, pic2, pic3, �],
Label3: [pic1, pic2, pic3, �],
�
}

## landmark_dict = {
Landmark1: [pic1, pic2, pic3, �],
Landmark2: [pic1, pic2, pic3, �],
Landmark3: [pic1, pic2, pic3, �],
�
}

## dominant = {
(R1, G1, B1): [pic1, pic2, pic3, �],
(R2, G2, B2): [pic1, pic2, pic3, �],
(R3, G3, B3): [pic1, pic2, pic3, �],
�
}

Finally, it prints each dictionary in a sorted way. So, for example, label that has highest number of pics will be at the top.

## To run:
python main.py

## Output:

(u'tourism', 11, ['2007.12.15  DSC00075.jpg', '2011.02.20 20022011082.jpg', '2011.02.20 20022011134.jpg', '2011.02.22 220220111590.jpg', '2011.02.22 22022011165.jpg', '2011.09.27 IMG (120).JPG', '2012.01.05 050120121826.jpg', '2014.03.12 DSCN2600.JPG', '2017.06.14 20170614_192952-01.jpg', '2017.07.22 IMG_20170722_155305.jpg', '2017.09.02 IMG_20170902_133309.jpg'])
(u'sky', 8, ['2011.02.20 20022011082.jpg', '2011.02.22 22022011165.jpg', '2011.09.27 IMG (120).JPG', '2012.01.05 050120121826.jpg', '2012.01.09 090120122101.jpg', '2014.03.12 DSCN2600.JPG', '2017.06.14 IMG_20170614_173138.jpg', '2017.09.02 IMG_20170902_133514.jpg'])
(u'fun', 7, ['2000s (25).jpg', '2010.10.19 19102010200.jpg', '2010.12.12 12122010200.jpg', '2011.02.21 21022011138.jpg', '2011.09.27 IMG (120).JPG', '2014.03.12 DSCN2622.JPG', '2017.06.14 20170614_192952-01.jpg'])
(u'travel', 6, ['2007.12.15  DSC00075.jpg', '2011.02.20 20022011134.jpg', '2011.02.22 220220111590.jpg', '2011.02.22 22022011165.jpg', '2014.03.12 DSCN2600.JPG', '2017.07.22 IMG_20170722_155305.jpg'])
(u'vacation', 6, ['2007.12.15  DSC00075.jpg', '2011.02.20 20022011134.jpg', '2011.02.22 22022011165.jpg', '2014.03.12 DSCN2600.JPG', '2017.06.14 20170614_192952-01.jpg', '2017.07.22 IMG_20170722_155305.jpg'])
(u'temple', 5, ['2011.02.20 20022011082.jpg', '2011.02.20 20022011134.jpg', '2011.02.22 22022011165.jpg', '2012.01.05 050120121826.jpg', '2014.03.12 DSCN2600.JPG'])
(u'recreation', 5, ['2000s (25).jpg', '2007.12.15  DSC00075.jpg', '2010.12.12 12122010200.jpg', '2011.02.20 20022011134.jpg', '2014.03.12 DSCN2622.JPG'])
(u'statue', 5, ['2012.01.09 090120122101.jpg', '2014.02.12 DSC_0074.jpg', '2017.06.14 IMG_20170614_173138.jpg', '2017.09.02 IMG_20170902_133309.jpg', '2017.09.02 IMG_20170902_133514.jpg'])
(u'monument', 5, ['2011.02.20 20022011082.jpg', '2012.01.09 090120122101.jpg', '2017.06.14 IMG_20170614_173138.jpg', '2017.09.02 IMG_20170902_133309.jpg', '2017.09.02 IMG_20170902_133514.jpg'])
(u'social group', 4, ['2007.12.20 DSC00099.jpg', '2010.12.12 12122010200.jpg', '2011.09.27 IMG (120).JPG', '2013.02.06 377765_501271499919187_1848268795_n.jpg'])
(u'landmark', 4, ['2008.06.11 DSCN0287.JPG', '2012.01.09 090120122101.jpg', '2017.06.14 IMG_20170614_173138.jpg', '2017.09.02 IMG_20170902_133514.jpg'])
(u'building', 4, ['2008.06.11 DSCN0287.JPG', '2008.06.11 DSCN0289.JPG', '2011.02.22 220220111590.jpg', '2012.01.05 050120121826.jpg'])
(u'tree', 4, ['2000s (15).jpg', '2008.06.09 DSCN0241.JPG', '2014.02.12 DSC_0074.jpg', '2017.09.02 IMG_20170902_133309.jpg'])
(u'historic site', 3, ['2008.06.11 DSCN0289.JPG', '2012.01.05 050120121826.jpg', '2012.05.25 25052012174.jpg'])
(u'youth', 3, ['2007.12.20 DSC00099.jpg', '2010.12.12 12122010200.jpg', '2013.02.06 377765_501271499919187_1848268795_n.jpg'])
(u'sculpture', 2, ['2014.02.12 DSC_0074.jpg', '2017.09.02 IMG_20170902_133514.jpg'])
(u'community', 2, ['2010.12.12 12122010200.jpg', '2013.02.06 377765_501271499919187_1848268795_n.jpg'])
(u'urban area', 2, ['2008.06.11 DSCN0287.JPG', '2011.02.22 220220111590.jpg'])
(u'art', 1, ['2011.02.21 21022011138.jpg'])
(u'crowd', 1, ['2017.06.14 20170614_192952-01.jpg'])
(u'headgear', 1, ['2017.09.02 IMG_20170902_133309.jpg'])
(u'plant', 1, ['2014.02.12 DSC_0074.jpg'])
(u'yellow', 1, ['2008.06.09 DSCN0241.JPG'])
(u'sign', 1, ['2008.06.09 DSCN0241.JPG'])
(u'triumphal arch', 1, ['2008.06.11 DSCN0289.JPG'])
(u'classical architecture', 1, ['2008.06.11 DSCN0289.JPG'])
(u'infrastructure', 1, ['2011.02.22 220220111590.jpg'])
(u'signage', 1, ['2008.06.09 DSCN0241.JPG'])
(u'event', 1, ['2013.02.06 377765_501271499919187_1848268795_n.jpg'])
(u'archaeological site', 1, ['2012.05.25 25052012174.jpg'])
(u'city', 1, ['2008.06.11 DSCN0287.JPG'])
(u'memorial', 1, ['2017.06.14 IMG_20170614_173138.jpg'])
(u'light', 1, ['2014.03.12 DSCN2622.JPG'])
(u'space', 1, ['2014.03.12 DSCN2622.JPG'])
(u'fortification', 1, ['2012.05.25 25052012174.jpg'])
(u'arch', 1, ['2011.02.20 20022011082.jpg'])
(u'ancient history', 1, ['2012.05.25 25052012174.jpg'])
(u'amusement park', 1, ['2000s (25).jpg'])
(u'team', 1, ['2011.09.27 IMG (120).JPG'])
(u'beach', 1, ['2017.07.22 IMG_20170722_155305.jpg'])
(u'ceremony', 1, ['2013.02.06 377765_501271499919187_1848268795_n.jpg'])
(u'product', 1, ['2011.02.21 21022011138.jpg'])
(u'tourist attraction', 1, ['2000s (25).jpg'])
(u'nature', 1, ['2000s (15).jpg'])
(u'mammal', 1, ['2014.02.12 DSC_0074.jpg'])
(u'suit', 1, ['2010.10.19 19102010200.jpg'])
(u'leisure', 1, ['2000s (25).jpg'])
(u'woody plant', 1, ['2000s (15).jpg'])
(u'adventure', 1, ['2007.12.15  DSC00075.jpg'])
(u'artwork', 1, ['2011.02.21 21022011138.jpg'])
(u'town square', 1, ['2008.06.11 DSCN0287.JPG'])
(u'cool', 1, ['2010.10.19 19102010200.jpg'])
(u'wood', 1, ['2014.03.12 DSCN2622.JPG'])
(u'photograph', 1, ['2000s (15).jpg'])
(u'medieval architecture', 1, ['2008.06.11 DSCN0289.JPG'])
(u'column', 1, ['2012.01.09 090120122101.jpg'])
(u'ruins', 1, ['2012.05.25 25052012174.jpg'])
(u'mural', 1, ['2011.02.21 21022011138.jpg'])
(u'person', 1, ['2007.12.20 DSC00099.jpg'])
(u'sand', 1, ['2017.07.22 IMG_20170722_155305.jpg'])
(u'green', 1, ['2000s (15).jpg'])
(u'advertising', 1, ['2008.06.09 DSCN0241.JPG'])
(u'professional', 1, ['2010.10.19 19102010200.jpg'])
(u'male', 1, ['2007.12.20 DSC00099.jpg'])
(u'friendship', 1, ['2007.12.20 DSC00099.jpg'])
(u'water', 1, ['2017.06.14 20170614_192952-01.jpg'])

(u'Gateway of India', 3, ['2008.06.11 DSCN0287.JPG', '2008.06.11 DSCN0289.JPG', '2012.01.05 050120121826.jpg'])
(u'The Red Fort', 2, ['2011.02.22 220220111590.jpg', '2011.02.22 22022011165.jpg'])
(u'India Gate', 2, ['2011.02.20 20022011082.jpg', '2014.03.12 DSCN2622.JPG'])
(u'Red Fort', 2, ['2011.02.22 220220111590.jpg', '2011.02.22 22022011165.jpg'])
(u'New Delhi railway station', 1, ['2014.03.12 DSCN2600.JPG'])
(u'Mehrangarh Fort', 1, ['2012.05.25 25052012174.jpg'])
(u'Lotus Temple', 1, ['2011.02.20 20022011134.jpg'])
(u'Taj Mahal Palace & Tower', 1, ['2008.06.11 DSCN0287.JPG'])
(u'Qutb Minar', 1, ['2014.03.12 DSCN2600.JPG'])
(u'Public Garden', 1, ['2017.06.14 IMG_20170614_173138.jpg'])

((215, 251, 254), 4, ['2007.12.15  DSC00075.jpg', '2011.02.20 20022011134.jpg', '2011.09.27 IMG (120).JPG', '2017.07.22 IMG_20170722_155305.jpg'])
((126, 119, 110), 3, ['2008.06.11 DSCN0287.JPG', '2008.06.11 DSCN0289.JPG', '2010.12.12 12122010200.jpg'])
((229, 228, 231), 3, ['2011.02.20 20022011134.jpg', '2011.09.27 IMG (120).JPG', '2017.07.22 IMG_20170722_155305.jpg'])
((62, 50, 46), 2, ['2012.01.05 050120121826.jpg', '2017.06.14 20170614_192952-01.jpg'])
((94, 82, 55), 2, ['2000s (15).jpg', '2011.02.22 220220111590.jpg'])
((189, 195, 214), 2, ['2012.01.09 090120122101.jpg', '2014.03.12 DSCN2600.JPG'])
((126, 118, 111), 2, ['2008.06.11 DSCN0289.JPG', '2010.12.12 12122010200.jpg'])
((241, 242, 244), 2, ['2011.09.27 IMG (120).JPG', '2017.07.22 IMG_20170722_155305.jpg'])
((132, 110, 86), 2, ['2011.02.20 20022011082.jpg', '2011.02.22 22022011165.jpg'])
((140, 194, 248), 1, ['2017.09.02 IMG_20170902_133309.jpg'])
((225, 182, 86), 1, ['2000s (25).jpg'])
((75, 83, 111), 1, ['2007.12.20 DSC00099.jpg'])
((167, 202, 235), 1, ['2017.06.14 IMG_20170614_173138.jpg'])
((197, 202, 208), 1, ['2014.03.12 DSCN2600.JPG'])
((226, 228, 234), 1, ['2017.07.22 IMG_20170722_155305.jpg'])
((198, 157, 11), 1, ['2008.06.09 DSCN0241.JPG'])
((130, 124, 120), 1, ['2010.12.12 12122010200.jpg'])
((135, 154, 209), 1, ['2013.02.06 377765_501271499919187_1848268795_n.jpg'])
((158, 115, 57), 1, ['2014.03.12 DSCN2622.JPG'])
((184, 187, 164), 1, ['2010.10.19 19102010200.jpg'])
((116, 73, 58), 1, ['2011.02.22 220220111590.jpg'])
((177, 150, 123), 1, ['2012.05.25 25052012174.jpg'])
((155, 108, 85), 1, ['2011.02.22 22022011165.jpg'])
((156, 34, 26), 1, ['2011.02.21 21022011138.jpg'])
((80, 127, 193), 1, ['2017.09.02 IMG_20170902_133514.jpg'])
((52, 48, 52), 1, ['2017.06.14 20170614_192952-01.jpg'])
((198, 73, 72), 1, ['2014.02.12 DSC_0074.jpg'])