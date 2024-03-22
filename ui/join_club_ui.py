from flask import render_template

class JoinClubUI:
    def __init__(self):
        pass
    
    def join_club(self):
        return render_template('join.html')