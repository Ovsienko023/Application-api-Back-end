import psycopg2
import sys
sys.path.insert(0, 'Application/scripts')
from logic.core_logic import ConnectDB

info_bd = ConnectDB().config_app()['Data_Base']

def create_cards():
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            req = """CREATE TABLE Cards
            (
                user_name CHARACTER VARYING(50),
                times CHARACTER VARYING(50),
                title CHARACTER VARYING(50),
                board CHARACTER VARYING(50),
                status CHARACTER VARYING(50),
                description CHARACTER VARYING(150),
                assignee CHARACTER VARYING(50),
                estimation CHARACTER VARYING(10),
                last_update_at CHARACTER VARYING(50),
                last_update_by CHARACTER VARYING(50)
            )"""
            cursor.execute(req)
            records = cursor

def create_boards():
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            req = """CREATE TABLE Boards
            (
                user_name CHARACTER VARYING(30),
                times CHARACTER VARYING(30),
                title CHARACTER VARYING(50),
                columns CHARACTER VARYING(100)
                )"""
            cursor.execute(req)
            records = cursor
     
def create_users():
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            req = """CREATE TABLE Users
            (
                user_name CHARACTER VARYING(30),
                user_secret CHARACTER VARYING(30)
                
            )"""
            cursor.execute(req)
            records = cursor
    app_users()
   
def app_users():
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            req = """INSERT INTO Users (user_name, user_secret)
                VALUES ('Bob', '123')"""
            cursor.execute(req)
            records = cursor





def main():
    create_cards()
    create_boards()
    create_users()
    print('Ok')

main()
