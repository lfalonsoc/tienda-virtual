from flask import Blueprint, render_template

glogal_h=Blueprint('views',__name__)

@glogal_h.route('/home')
@glogal_h.route('/')
def home():
  return render_template('home.html')
