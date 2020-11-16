from flask import Flask, render_template
app = Flask(__name__)

soundList = {
  'Creak': 'doorCreak',
  'Ghoul Laugh': 'ghoul',
  'Cat Yowl': 'yowl',
  'Snake': 'rattlesnake',
  'Bite': 'bite',
  'Heartbeat' : 'heartbeat',
  'Howl' : 'howl',
  'Owl Hoot': 'owlhoot',
  'Mad Cat' : 'crabbycat',
  'Witch' : 'witch',
  'Spooky Laugh': 'spookylaugh',
  'Weird Sound' : 'weirdsound',
}

@app.route('/')
def index():
  return render_template("index.html", soundList=soundList)

if __name__=="__main__":
  app.run(host='127.0.0.1', port=8080, debug=True)
