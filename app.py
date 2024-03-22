from flask import Flask, render_template, request, redirect, url_for
from controllers.club_controller import ClubController
from controllers.db_controller import DbController
from ui.register_club_ui import RegisterClubUI
from ui.join_club_ui import JoinClubUI
from ui.club_information_ui import ClubInformationUI
from controllers.membership_controller import MembershipController
app = Flask(__name__)

# Initialize controllers
db_controller = DbController()
club_controller = ClubController(db_controller)
register_ui = RegisterClubUI()
join_ui = JoinClubUI()
club_info_ui = ClubInformationUI(club_controller)
membership_controller = MembershipController(db_controller)
# Render the HTML form
@app.route('/register_club')
def index():
    return register_ui.create_new_club()

@app.route('/')
def main_page():
    return render_template('main.html')

# Handle form submission and create the club
@app.route('/create_club', methods=['POST'])
def create_club():
    club_name = request.form['clubName']
    description = request.form['description']
    club_leader = request.form['clubLeader']


    
    if club_controller.create_club(club_name, description, club_leader):
        return redirect(url_for('club_info', club_name=club_name))
    else:
        return 'Club Already Exists'
    
@app.route('/submit_student', methods=['POST'])
def submit_student():
    # Get data from the form
    id_number = request.form['id']
    name = request.form['name']
    email = request.form['email']
    department = request.form['department']
    club = request.form['clubid']

    if membership_controller.create_member(club, id_number):

          return 'Student Added Successfully'
    
    else:  
        return 'Failed to add student'
  
@app.route('/club_info/<club_name>')
def club_info(club_name):
    return club_info_ui.display_club_info(club_name)

@app.route('/join_club')
def join():
    return join_ui.join_club()

if __name__ == '__main__':
    app.run(debug=True)

