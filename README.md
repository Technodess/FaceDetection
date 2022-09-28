# Face Detection 
EYE FOR BLIND system is proposed for any kind of visual impaired persons: blind, partially sighted, and people with progressive loss of vision. This system can help the visually impaired individuals to travel through familiar or unfamiliar corridor by using the Kinect sensor that mounted on the head or holding into hand. This chapter consists of four parts. The four parts can be divided into problem statements, project introduction, previous related work, and conclusion.

How it works?

Our Face Recognition module works as follows-
1. Firstly the sample images of people to be recognized are given to the Python script for checking against the real time feed.
2. When the user wants to recognize a person he would have to say the hot word to awaken the virtual assistant and then say scan or recognize.
3. Then the face recognition script would run and check the person in the frame against the sample images provided.
4. Every sample image would be associated with a name. So when the program would find a match, the AI would tell the user the name of that person through the Earphones. 5. The object recognition module can only detect and recognize a handful of objects. For this purpose the OpenCV software contains the HaarCascade files of certain objects which are a combination of features and attributes extracted from around a million of samples.
6. To detect and recognize an object, the script would check if the features and attributes of the object match to the collective features and attributes of the particular object’s HaarCascade file.
