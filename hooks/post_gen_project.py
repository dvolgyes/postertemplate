#!/usr/bin/env python3
import sys
import wget
import os
from pathlib import Path
from collections import defaultdict

def wget_as(url,filename):
    tempfile = Path(wget.download(url))
#    filename = Path(filename)
    if filename.endswith('/'):
        filename = Path(filename)
        if not filename.exists():
            filename.mkdir()
        filename = Path(filename) / tempfile.name
        print("x {filename}")
    if tempfile.exists():
        print(f'{tempfile} -> {filename}')
        tempfile.replace(filename)
    else:
        sys.exit(1)

if '{{cookiecutter.online_gitignore}}'.lower() == 'y':
    wget_as('https://github.com/github/gitignore/blob/master/TeX.gitignore','.gitignore')

#templates:
templates={
"uioposter": ("https://raw.githubusercontent.com/dvolgyes/uioposter/master/uioposter.cls",
             ("https://github.com/dvolgyes/uioposter/raw/master/uioposter-images/uioposter-apollon.pdf", 'uioposter-images/'),
             ("https://github.com/dvolgyes/uioposter/raw/master/uioposter-images/uioposter-logo-english.pdf", 'uioposter-images/'),
             ("https://github.com/dvolgyes/uioposter/raw/master/uioposter-images/uioposter-logo-norsk.pdf", 'uioposter-images/'),
             ("https://raw.githubusercontent.com/dvolgyes/uioposter/master/examples/uioposter-example-portrait.tex",'{{cookiecutter.poster_file}}.tex'),
             )
}


style = '{{cookiecutter.style}}'
if style in templates:
    urls = templates[style]
    if not isinstance(urls, tuple):
        urls = (urls,)
    for url in urls:
        if isinstance(url, tuple):
            wget_as(*url)
        else:
            wget.download(url)

os.system('git init .')
os.system('git add .')
os.system('git commit . -m "Initial commit."')
git_backend = '{{cookiecutter.git_backend}}'.lower()
if git_backend != 'none':
    git_server = None
    if git_backend == 'github':
        git_server = 'github.com'
    elif git_backend == 'bitbucket':
        git_server = 'bitbucket.org'
    elif git_backend == 'gitlab':
        git_server = 'gitlab.com'
    else:
        sys.exit(1)
    os.system('git remote add origin git@{git_server}:{{cookiecutter.username}}/{{cookiecutter.project_slug}}')
