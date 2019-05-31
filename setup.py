from setuptools import setup


setup(
    name='pyevernote',
    version='0.0.1',
    description='Pythonic Evernote API Wrapper',
    author='Tatsuya Matoba',
    author_email='tatsuya.matoa.wk.jp@gmail.com',
    packages = ['pyevernote'],
    include_package_data=True,
    install_requires=[
        'bs4',
        'evernote3',
    ],
)
