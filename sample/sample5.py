"""
あるノートをあるノートブックに入れる
"""
from decouple import config
from bs4 import BeautifulSoup

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)


class Note:
    def __init__(self, app, note_meta):
        self.app = app
        self.note_meta = note_meta

    @property
    def title(self):
        return self.note_meta.title

    @property
    def content(self):
        # ノートIDからノートを取得
        note = self.app.note_store.getNote(self.note_meta.guid, True, True, True, True)

        # ノートに含まれているXMLをパース
        content_soup = BeautifulSoup(note.content, 'html.parser')
        return content_soup.find('en-note').text

    @property
    def notebook(self):
        return self.note_meta.notebookGuid

    @notebook.setter
    def notebook(self, notebook):
        self.note_meta.notebookGuid = notebook.guid

    def save(self):
        self.app.note_store.updateNote(self.note_meta)


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

    def list_notes(self, notebook):
        # ノート検索条件を指定。ノートブックのIDを指定。更新日でソート
        note_filter = NoteFilter()
        note_filter.notebookGuid = notebook.guid
        note_filter.order = NoteSortOrder.UPDATED

        # ノート検索結果のフォーマットを指定。タイトルを含む
        result_format = NotesMetadataResultSpec()
        result_format.includeTitle = True

        # ノートのメタデータリストを取得
        note_meta_list = self.note_store.findNotesMetadata(note_filter, 0, 10, result_format)
        return [Note(self, note_meta) for note_meta in note_meta_list.notes]

    def get_notebook(self, notebook_name, offset=0):
        notebooks = self.filter_notebook(notebook_name)
        if notebooks:
            return notebooks[offset]

def main():
    from_notebook_name = "My Sample Notebook"
    to_notebook_name = "My Sample Notebook1"
    note_title = "This is my seccond note"

    app = EvernoteApp(token=TOKEN, use_sandbox=USE_SANDBOX)

    # 移動元のノートブックを探す
    from_notebook = app.get_notebook(from_notebook_name)
    if not from_notebook:
        print("Notebook {} Not Found.".format(from_notebook_name))
        exit()


    # 移動先のノートブックを探す
    to_notebook = app.get_notebook(to_notebook_name)
    if not to_notebook:
        print("Notebook {} Not Found.".format(to_notebook_name))
        exit()

    # 移動元のノートブックの先頭にあるノートを移動先のノートに移す
    notes = app.list_notes(from_notebook)
    notes[0].notebook = to_notebook
    notes[0].save()

if __name__ == "__main__":
    main()

