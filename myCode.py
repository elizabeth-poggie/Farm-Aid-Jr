import io
import cv2
#import matplotlib as plt
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()
def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string

def localize_objects(path):
    """Localize objects in the local image.
        
        Args:
        path: The path to the local file.
        """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))


#cap = cv2.VideoCapture("http://192.168.43.215:8080/?action=stream")
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite(file,frame)

    # print OCR text
    #print(detect_text(file))
    localize_objects(file)
    #if (time.time() - start == 200):
    #    breaks
    
    # Display the resulting frame
    if frame is not None:
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.startWindowThread()
    #cv2.namedWindow("test")
    #plt.imshow(canvas, interpolation='nearest')
    #plt.show()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
