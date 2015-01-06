# Do OAuth2 stuff to create credentials object
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
import gdata.spreadsheet.service
from oauth2client.tools import run
from oauth2client import tools
import argparse
import gdata.spreadsheets.client
import gdata.gauth

parser = argparse.ArgumentParser(parents = [tools.argparser])
flags = parser.parse_args()
storage = Storage("creds.dat")
credentials = storage.get()
if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow_from_clientsecrets("client_secrets.json", scope = ["https://spreadsheets.google.com/feeds"],redirect_uri ='urn:ietf:wg:oauth:2.0:oob'),storage, flags)
gd_client = gdata.spreadsheets.client.SpreadsheetsClient()
gd_client.auth_token = gdata.gauth.OAuth2TokenFromCredentials(credentials)

spreadsheet_id='1GS3RW7SrJZWTooknqhIH52iIVhR0rLEZ5NSAI8YnLec'
worksheet_id='od6'
