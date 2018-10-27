from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

#@ask.intent('HelloIntent')
#def hello():
  #  return statement("Hello World!")   

@ask.launch
def launch():
    speech = "Welcome to Volume Calculator. Which object would you like me to calculate the volume of?"
    return get_dialog_state()

def get_dialog_state():
    return session['dialogState']
 
@ask.intent("BoxVolumeIntent", convert={'length': int, 'width': int, 'height': int})
def calculate_box_volume(length, width, height):
 
    dialog_state = get_dialog_state()
    if dialog_state != "COMPLETED":
        return delegate(speech=None)
 
    box_volume = length * width * height
    return statement("The volume of the box is {} cubic meters"
                     .format(box_volume))
if __name__ == '__main__':
   app.run(debug=True)
    #app.run(host="192.168.99.1",port=5000)
'''
@ask.intent("StatsIntent")
def stats():
    r = requests.get(ENDPOINT)
    repo_json = r.json()

    if r.status_code == 200:
        repo_name = ENDPOINT.split('/')[-1]
        keys = ['stargazers_count', 'subscribers_count', 'forks_count']
        stars, watchers, forks = itemgetter(*keys)(repo_json)
        speech = "{} has {} stars, {} watchers, and {} forks. " \
            .format(repo_name, stars, watchers, forks)
    else:
        message = repo_json['message']
        speech = "There was a problem calling the GitHub API: {}.".format(message)

    logger.info('speech = {}'.format(speech))
    return statement(speech)
    '''
