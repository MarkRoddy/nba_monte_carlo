import pygsheets
import pandas as pd

def model(dbt, sess):

    #Authorization
    # gc = pygsheets.authorize(service_file='pygsheets.json')
    gc = pygsheets.authorize()
    sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1aSyqoJ6j2xkVFt4oRKZX2N36wyIFoR8Fbbny_hvCoTs/edit#gid=5328645")

    # grab the first sheet, can we do this by name for more clarity?
    worksheet = sheet[0]
    # data = worksheet.range("A8:J38")
    df = worksheet.get_as_df(has_header=True, start = "A8", end = "J38")
    return df

