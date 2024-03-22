from flask import render_template
from controllers.db_controller import DbController



class ClubInformationUI:
    def __init__(self, db_controller: DbController):
        self.db_controller = db_controller

    def display_club_info(self, club_name):
        club_list = self.db_controller.retrieve_club(club_name)
        if club_list:
            
            return render_template('club_info.html', club_list=club_list)
        else:
            return render_template('club_not_found.html')
