from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.fermata import Fermata


def getAllEdges():
    conn = DBConnect.get_connection()
    result = []
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM connessione c"
    cursor.execute(query)
    for row in cursor:
        result.append(Connessione(**row))
    cursor.close()
    conn.close()
    return result


class DAO:

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

