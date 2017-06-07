from flask import Flask, render_template
from flask import request, redirect 
from flask import session

import os 
from datetime import datetime
#from arxiv import scrapeNewFeed

app = Flask(__name__)

@app.route('/')
def astrocoffee():
    author = "ChangHoon Hahn"
    return render_template('index.html')#, author=author, name=name)

#@app.route('/signup', methods = ['POST'])
#def signup(): 
#    email = request.form['email']
#    email_addresses.append(email)
#    session['email'] = email
#    print(email_addresses)
#    return redirect('/')

#@app.route('/emails.html')
#def emails():
        #    return render_template('emails.html', email_addresses=email_addresses)

#@app.route('/arxiv.html')
#def arxiv():
#    entries = scrapeNewFeed()
#    return render_template('arxiv.html', entries=entries) 

#@app.route('/unregister')
#def unregister():
#    # Make sure they've already registered an email address
#    if 'email' not in session:
#        return "You haven't submitted an email!"
#    email = session['email']
#    # Make sure it was already in our address list
#    if email not in email_addresses:
#        return "That address isn't on our list"
#    email_addresses.remove(email)
#    del session['email'] # Make sure to remove it from the session
#    return 'We have removed ' + email + ' from the list!'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
