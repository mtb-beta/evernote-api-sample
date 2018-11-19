import os
from dotenv import load_dotenv

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types


load_dotenv()
TOKEN = os.getenv("EVERNOTE_DEVELOPPER_TOKEN")
NOTEBOOK = "My Sample Notebook"

def main():
    client = EvernoteClient(token=TOKEN)
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    target_notebook = None
    for notebook in notebooks:
        if notebook.name == NOTEBOOK:
            target_notebook = notebook
            break

    if not notebook:
        print("Notebook {} Not Found.".format(NOTEBOOK))

    note = Types.Note()
    note.title = "This is my first note"
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>Hello, world!</en-note>'
    note.notebookGuid = target_notebook.guid
    note = note_store.createNote(note)

if __name__ == "__main__":
    main()
