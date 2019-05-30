"""
NOTE: ノートブック一覧を取得するサンプル
"""
import os

from decouple import config

from evernote.api.client import EvernoteClient


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

    @property
    def all_notebooks(self):
        return self.note_store.listNotebooks()


def main():
    evernote_app = EvernoteApp(token=TOKEN, use_sandbox=USE_SANDBOX)
    for notebook in evernote_app.all_notebooks:
        print("id:{}, name:{}".format(notebook.guid, notebook.name))


if __name__ == "__main__":
    main()
