"""
NOTE: 指定したノートブックのノート一覧を取得するサンプル
"""
import os

from decouple import config
from bs4 import BeautifulSoup

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)
NOTEBOOK = "My Sample Notebook"

def main():
    client = EvernoteClient(token=TOKEN, sandbox=USE_SANDBOX)
    note_store = client.get_note_store()

    # ノートブック一覧を取得し、目当てのノートブックを探す
    notebooks = note_store.listNotebooks()
    target_notebook = None
    for notebook in notebooks:
        if notebook.name == NOTEBOOK:
            target_notebook = notebook
            break

    if not target_notebook:
        print("Notebook {} Not Found.".format(NOTEBOOK))

    # 検索条件を指定。ノートブックのIDを指定。更新日でソート
    note_filter = NoteFilter()
    note_filter.notebookGuid = target_notebook.guid
    note_filter.order = NoteSortOrder.UPDATED

    # 検索結果のフォーマットを指定。タイトルを含む
    result_format = NotesMetadataResultSpec()
    result_format.includeTitle = True

    # メタデータリストを取得
    note_meta_list = note_store.findNotesMetadata(note_filter, 0, 10, result_format)
    
    # メタデータリストからノートそのものを取得
    for note_meta in note_meta_list.notes:
        print(note_meta.title)
        # ノートIDからノートを取得
        note = note_store.getNote(note_meta.guid, True, True, True, True)

        # ノートに含まれているXMLをパース
        content_soup = BeautifulSoup(note.content, 'html.parser')
        content = content_soup.find('en-note').text
        print(content)




if __name__ == "__main__":
    main()


