import mysql.connector 
from models.club import Club
class DbController:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="kraem",
            password="Custodian",
            database="Project2171"
        )
        self.cursor = self.connection.cursor()

    def add_club(self, club):
        query = "INSERT INTO clubs (clubName, description, clubLeader) VALUES (%s, %s, %s)"
        values = (club.club_name, club.description, club.club_leader)
        self.cursor.execute(query, values)
        self.connection.commit()

    def retrieve_club(self, club_name):
        query = "SELECT * FROM clubs WHERE clubName = %s"
        self.cursor.execute(query, (club_name,))
        club_row = self.cursor.fetchone()  
        if club_row:
            club_info_list = ['Club Name: {}'.format(club_row[1]), 'Description: {}'.format(club_row[2]), 'Club Leader: {}'.format(club_row[3])]
            return club_info_list
        else:
            return None
        
  
    def retrieve_club_by_id(self, club_id):
        query = "SELECT * FROM clubs WHERE Id = %s"
        self.cursor.execute(query, (club_id,))
        club_row = self.cursor.fetchone()  
        if club_row:
            club_name = club_row[0]
            description = club_row[1]
            club_leader = club_row[2]
            # Assuming Club class has the constructor: Club(club_name, description, club_leader)
            club = Club(club_name, description, club_leader)
            return club
        else:
            return None
  
    def add_member(self, club_id, student_id):
        query = "INSERT INTO membership (club_id, student_id) VALUES (%s, %s)"
        values = (club_id, student_id)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("random")
        except mysql.connector.Error as err:
            print(f"Error adding member: {err}")

    def check_membership(self, student_id, club_id):
        query = "SELECT * FROM membership WHERE student_id = %s AND club_id = %s"
        self.cursor.execute(query, (student_id, club_id))
        result = self.cursor.fetchone()
        return result is not None

    def close_connection(self):
        self.cursor.close()
        self.connection.close()