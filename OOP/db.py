import pymysql


def baglantiOlustur():
    db = pymysql.connect(host='localhost', user='root', password='', db='bitirmeprojesi',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    return db, cursor
