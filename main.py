# the flask is a micro webframe  work it takes two modules such as render_template and Respose. render_template is for to render the HTTP file. respose is  to get HTTP response requests. FLask is based on Wrekzeg(this implements requests and responses), WSGI(Web server gate way interface) toolkit and jinga2 template engine that combines a template with specific data source to render a dynamic web page and alloes python varibles to get convert into html  file. flask provides a way to return the output in client browser using render_template. 

# Flask is written in  a very pythonic manner unlike Django. and it is easy to work with flask becasue it does not have a huge learning curve. and it is very readable and very eplicit. like to write a hello world  in a flask :
#    from flask import Flask
#       app = Flask(__name__)

#    @app.route('/')
#   def hello_world():
       #return 'Hello World!'

#   if __name__ == '__main__':
#    app.run()
# There are total 5 files in this projects: 1. camera file, mailn file, harcasscade text file, python ipynb file, index html file
# python ipynb file has trained data model, harcasscade is detecting the correct facial figures or parameters, index html file is creating a video template for flask app, camera file is taking the video, getting it in frame by frame, convert it into grayscale mode, then feed into trainded model, creating the predictiion from there, then creating a box aroung the face and tagging the emotion text over the box. then the flask app(main.py) work over the camera.py file which output the response of the video on the web interface which is working on the loaclhost which runs the port 5000(url)

from flask import Flask, render_template, Response
from camera import VideoCamera


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    # this is an HTML template for flask app.

def gen(camera):
    while True:
        frame = camera.get_frame()         # to get the video by frame by frame.
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),     # an the predicted image and get back to the web interface.
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)         # to run the app on a localhost which runs port 5000 (url)
