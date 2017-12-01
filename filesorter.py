import os
import re

files = [x for x in os.listdir() if os.path.isfile(x)]

# Image files re
imgre = re.compile(r'\.(jp(e)?g|png|svg|ico|xcf)$', re.I)


#zip files re
zipre = re.compile(r'\.(zip|rar|tar\.(gz|bz2))$', re.I)


#doc files re
docre = re.compile(r'\.(doc(x)?|pdf|ppt(x)?|xlsx|csv|json|txt|dat|odt)$', re.I)

#html files
webre = re.compile(r'\.(html|xml|css)$', re.I)

#scripts
scriptre = re.compile(r'\.(sh|jar|c)$', re.I)

#installer applications
appre = re.compile(r'\.(apk|exe|deb|pkg|AppImage|bin)$', re.I)

if not os.path.exists('doc_files'):
    os.makedirs('doc_files')
if not os.path.exists('image_files'):
    os.makedirs('image_files')
if not os.path.exists('zipped_files'):
    os.makedirs('zipped_files')
if not os.path.exists('script_files'):
    os.makedirs('script_files')
if not os.path.exists('application_files'):
    os.makedirs('application_files')
if not os.path.exists('web_files'):
    os.makedirs('web_files')

for i in files:
    if imgre.search(i):
        os.rename(i, 'image_files/'+i)
    elif zipre.search(i):
        os.rename(i, 'zipped_files/'+i)
    elif docre.search(i):
        os.rename(i, 'doc_files/'+i)
    elif scriptre.search(i):
        os.rename(i, 'script_files/'+i)
    elif appre.search(i):
        os.rename(i, 'application_files/'+i)
    elif webre.search(i):
        os.rename(i, 'web_files/'+i)
