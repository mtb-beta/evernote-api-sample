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


class EvernoteApp:
    def __init__(self, token, use_sandbox):
        self.token = token
        self.use_sandbox = use_sandbox
        self.client = EvernoteClient(token=self.token, sandbox=self.use_sandbox)
        self.note_store = self.client.get_note_store()

    def create_notebook(self, name):
        notebook = Types.Notebook()
        notebook.name = name
        self.note_store.createNotebook(notebook)

    @property
    def all_notebooks(self):
        return self.note_store.listNotebooks()

    def filter_notebook(self, keyword):
        notebooks = []
        for notebook in self.all_notebooks:
            if keyword in notebook.name:
                notebooks.append(notebook)
        return notebooks

    def create_note(self, notebook, title, content):
        note = Types.Note()
        note.title = title
        note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>{}</en-note>'.format(content)
        note.notebookGuid = notebook.guid
        return self.note_store.createNote(note)

def main():
    evernote_app = EvernoteApp(token=TOKEN, use_sandbox=USE_SANDBOX)
    notebooks = evernote_app.filter_notebook(NOTEBOOK)
    if not notebooks:
        print("Notebook {} Not Found.".format(NOTEBOOK))

    evernote_app.create_note(
        notebook=notebooks[0],
        title="This is my first note",
        content="Hello, world!"
    )

if __name__ == "__main__":
    main()
