"""
NOTE:指定したノートブックにノートを作成するサンプル
"""
import os
from decouple import config

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)
NOTEBOOK = "My Sample Notebook"

def main():
    client = EvernoteClient(token=TOKEN, sandbox=USE_SANDBOX)
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
