from validators import Validator
from models.club import Club
from ui.club_information_ui import ClubInformationUI

class ClubController:
    def __init__(self, db_controller):
        self.db_controller = db_controller
        self.validator = Validator(db_controller)
        self.club_info_ui = ClubInformationUI(db_controller)
    def create_club(self, club_name, description, club_leader):
        if self.validator.validate_club_name(club_name):
            new_club = Club(club_name, description, club_leader)
            self.db_controller.add_club(new_club)
            return True
        else:
            return False
    def retrieve_club(self, club_name):
        return self.db_controller.retrieve_club(club_name)
       