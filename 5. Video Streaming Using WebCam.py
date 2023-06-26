from flask import Flask, render_template,Response
import cv2 as cv


app = Flask(__name__)

cam = cv.VideoCapture(1)

def generate():
    while True:
        ret,frame = cam.read()
        if ret:
            retb,buffer = cv.imencode('.png',frame) 
            # This encoded image data can then be used for various purposes, 
            # such as storing it in a file, transmitting it over a network, or further processing it in
            #  your computer vision pipeline.
            frame = buffer.tobytes()

            # return cant be used as it will only return one frame and the loop will be terminated
            # b'--frame\r\n': This is a bytes literal that represents a delimiter or boundary marker.
            # It seems to be used to separate different frames in the generated sequence.

            # b'Content-Type: image/jpeg\r\n\r\n': This is another bytes literal that represents the content 
            # type of the frame, specifically indicating that it is an image in JPEG format. It is typically used
            # in HTTP headers to specify the media type of the content being transmitted.

            # + frame + b'\r\n': This concatenates the frame variable, which represents the actual
            # image data, with the previous bytes literals. The + operator is used to concatenate bytes
            # literals together.
        else:
            break

        yield (b'--frame\r\n' 
        b'Content-Type: image/PNG\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('vid.html')

@app.route('/video')
def video():
    return Response(generate(),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True)
