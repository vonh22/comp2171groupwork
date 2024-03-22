from flask import render_template

class RegisterClubUI:
    def __init__(self):
        pass

    def create_new_club(self):
        return render_template('index.html')