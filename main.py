from flask import Flask
import soundcloud
app = Flask(__name__)

@app.route('/soundcloud/recent')
def show_blog():
   return soundcloud.get5()

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()