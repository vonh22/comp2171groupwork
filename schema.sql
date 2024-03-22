DROP DATABASE IF EXISTS Project2171;
CREATE DATABASE Project2171;

USE Project2171;

CREATE USER 'kraem'@'localhost' IDENTIFIED BY 'Custodian';

GRANT ALL PRIVILEGES ON Project2171.* TO 'kraem'@localhost;

-- Create the clubs table
CREATE TABLE clubs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clubName VARCHAR(255) ,
    description VARCHAR(255) ,
    clubLeader VARCHAR(255)
);

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    department VARCHAR(255)
);

CREATE TABLE membership (
    id INT AUTO_INCREMENT PRIMARY KEY,
    club_id INT,
    student_id INT,
    FOREIGN KEY (club_id) REFERENCES clubs(id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    UNIQUE (club_id, student_id)
);

INSERT INTO clubs (clubName, description, clubLeader) 
VALUES 
('Chess Club', 'A club for chess enthusiasts', 'John Doe'),
('Photography Club', 'Learn and practice photography skills', 'Alice Smith'),
('Debate Club', 'Engage in debates and discussions', 'Michael Johnson'),
('Music Club', 'Explore and create music together', 'Emily Brown'),
('Coding Club', 'Learn and practice coding skills', 'David Lee');

INSERT INTO student (name, email, department) 
VALUES
('John Doe', 'john@example.com', 'Computer Science'),
('Jane Smith', 'jane@example.com', 'Electrical Engineering'),
('Alice Johnson', 'alice@example.com', 'Mechanical Engineering');