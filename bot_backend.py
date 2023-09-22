import sqlite3 # noqa
import json
import os
from datetime import date
from PIL import Image


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
with open(DIR_PATH+"/valid_names.json") as jsonfile:
    VALID_NAMES = json.load(jsonfile)
con = sqlite3.connect("notesdb.db")
cur = con.cursor()


def get_image_index(imgdir=DIR_PATH+'/images'):
    """Return the number of files in a directory."""
    return len(next(os.walk(imgdir))[2])


def valid_name(lesson_name: str):
    """Check if the lesson name is valid."""
    return lesson_name in VALID_NAMES.keys()


def full_name(lesson_name: str):
    """Return the full name of the lesson."""
    assert lesson_name in VALID_NAMES.values()
    return VALID_NAMES[lesson_name]


def create_table():
    """Create a table if it doesnt exist."""
    global cur, con
    cur.execute("CREATE TABLE IF NOT EXISTS notestable(image, lesson_name,\
                 lesson_date, upload_date, uploader_user, uploader_userid,\
                 uploader_studentid)")
    con.commit()


def close_connection():
    """Closes the connection."""
    global cur, con
    con.close()


def save_note(image: Image, uploader_user: str, uploader_userid: str,
              uploader_studentid: int, upload_date: date, lesson_date: date,
              lesson_name: str):
    """Save a note to the database."""  # TODO: check lesson name
    global cur, con
    image_index = get_image_index()

    # Save image
    image.save(f"{DIR_PATH}/images/{image_index}.png")

    # Save into database
    data = (f"{image_index}.png", lesson_name, lesson_date, upload_date,
            uploader_user, uploader_userid, uploader_studentid)
    cur.execute("INSERT INTO notestable VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()


def get_note(known_values: dict):
    """Return a list of notes that match the known values."""
    where_clause = ' AND '.join([f'{k} = ?' for k in known_values.keys()])
    sql_query = f'SELECT * FROM notestable WHERE {where_clause}'
    cur.execute(sql_query, tuple(known_values.values()))
    rows = cur.fetchall()
    result_rows = []
    for row in rows:
        result_rows.append([Image.open(f'{DIR_PATH}/images/{row[0]}'), *row[1:]])
    return result_rows
