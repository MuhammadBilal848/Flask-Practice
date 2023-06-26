from flask import Flask, render_template,Response
import cv2 as cv


app = Flask(__name__)

cam = cv.VideoCapture(1)
FaceCascade = cv.CascadeClassifier('haarcascade\haarcascade_frontalcatface.xml')

def detect_face(img):
    cop_img = img.copy()
    face_rects = FaceCascade.detectMultiScale(cop_img)

    for (x,y,w,h) in face_rects:
        cv.rectangle(cop_img,(x,y),(x+w,y+h),(255,255,255),10)

    return cop_img

def generate():
    while True:
        ret,frame = cam.read()
        if ret:
            frame = detect_face(frame)

            retb,buffer = cv.imencode('.png',frame) 

            frame = buffer.tobytes()
        else:
            break

        yield (b'--frame\r\n' 
        b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('face.html')

@app.route('/video')
def video():
    return Response(generate(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True)
