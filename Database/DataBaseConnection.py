import mysql.connector


def CreateConnection():
    db = mysql.connector.connect(host='localhost', user='root', password='', db='bitirmeprojesi')
    cursor = db.cursor(buffered=True)
    return db, cursor



