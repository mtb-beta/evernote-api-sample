"""
NOTE: ノートブックを作成するサンプル
"""
import os

from decouple import config

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)

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

def main():
    evernote_app = EvernoteApp(token=TOKEN, use_sandbox=USE_SANDBOX)
    evernote_app.create_notebook("My Sample Notebook")

if __name__ == "__main__":
    main()
