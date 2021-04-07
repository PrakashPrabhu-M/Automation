from pathlib import Path
import shutil,os,pyperclip
cwd=Path('.')
files=[]
folders=[]
for i in cwd.iterdir():
    if i.is_file():
        files.append(i)
    else:
        folders.append(i)

#print(type(files[0].name))
#print(type(Path('.')))
image_formats=['bmp','jpeg','gif']
video_formats=['mp4','3gp','avi','mkv']
torrent_formats=['torrent']
audio_formats=['mp3','wav','ogg']
runnable_formats=['exe']
document_formats=['txt','docx','pdf','doc','xml']
compressed_formats=['zip','rar']

images=[]
videos=[]
audios=[]
runnables=[]
torrents=[]
documents=[]
compresses=[]

images_=[]
videos_=[]
audios_=[]
runnables_=[]
torrents_=[]
documents_=[]
compresses_=[]

img_path=[]
vdo_path=[]
aud_path=[]
run_path=[]
tor_path=[]
doc_path=[]
com_path=[]

for i in files:
    for image_format in image_formats:
        if image_format == i.name[-len(image_format):]:
            images.append(image_format)
            images_.append(i)
            img_path.append(f'Images/{image_format}')

    for video_format in video_formats:
        if video_format ==i.name[-len(video_format):]:
            videos.append(video_format)
            videos_.append(i)
            vdo_path.append(f'Videos/{video_format}')

    for audio_format in audio_formats:
        if audio_format==i.name[-len(audio_format):]:
            audios.append(audio_format)
            audios_.append(j)
            aud_path.append(f'Videos/{audio_format}')

    for document_format in document_formats:
        if document_format==i.name[-len(document_format):]:
            documents.append(document_format)
            documents_.append(i)
            doc_path.append(f'Documents/{document_format}')

    for runnable_format in runnable_formats:
        if runnable_format==i.name[-len(runnable_format):]:
            runnables.append(runnable_format)    
            runnables_.append(i)    
            run_path.append(f'Runnables/{runnable_format}')

    for torrent_format in torrent_formats:
        if torrent_format==i.name[-len(torrent_format):]:
            torrents.append(torrent_format)
            torrents_.append(i)
            tor_path.append(f'Torrents/{torrent_format}')

    for compressed_format in compressed_formats:
        if compressed_format==i.name[-len(compressed_format):]:
            compresses.append(compressed_format)
            compresses_.append(i)
            com_path.append(f'Compressed Files/{compressed_format}')

print(Path.cwd())
print(images)
print(videos)
print(audios)

for image in images:
    Path(f'./Images/{image}').mkdir(exist_ok=True, parents=True)
for video in videos:
    Path(f'./Videos/{video}').mkdir(exist_ok=True, parents=True)
for document in documents:
    Path(f'./Documents/{document}').mkdir(exist_ok=True, parents=True)
for audio in audios:
    Path(f'./Audios/{audio}').mkdir(exist_ok=True, parents=True)
for torrent in torrents:
    Path(f'./Torrents/{torrent}').mkdir(exist_ok=True, parents=True)
for runnable in runnables:
    Path(f'./Runnables/{runnable}').mkdir(exist_ok=True, parents=True)
for compressed in compresses:
    Path(f'./Compressed Files/{compressed}').mkdir(exist_ok=True, parents=True)

images=list(set(images))
videos=list(set(videos))
audios=list(set(audios))
runnables=list(set(runnables))
torrents=list(set(torrents))
documents=list(set(documents))
compressed=list(set(compressed))


# img_path=list(set(img_path))
# vdo_path=list(set(vdo_path))
# aud_path=list(set(aud_path))
# run_path=list(set(run_path))
# tor_path=list(set(tor_path))
# doc_path=list(set(doc_path))

for img in images_:
    for i in images:
        if i==img.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),img.name)
            shutil.move(os.path.join(os.getcwd(),img.name),os.path.join(os.getcwd(),'Images',i,img.name))

for vdo in videos_:
    for i in videos:
        if i==vdo.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),vdo.name)
            shutil.move(os.path.join(os.getcwd(),vdo.name),os.path.join(os.getcwd(),'Videos',i,vdo.name))

for ado in audios_:
    for i in audios:
        if i==ado.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),ado.name)
            shutil.move(os.path.join(os.getcwd(),ado.name),os.path.join(os.getcwd(),'Audios',i,ado.name))

for run in runnables_:
    for i in runnables:
        if i==run.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),run.name)
            shutil.move(os.path.join(os.getcwd(),run.name),os.path.join(os.getcwd(),'Runnables',i,run.name))

for doc in documents_:
    for i in documents:
        if i==doc.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),doc.name)
            shutil.move(os.path.join(os.getcwd(),doc.name),os.path.join(os.getcwd(),'Documents',i,doc.name))

for tor in torrents_:
    for i in torrents:
        if i==tor.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),tor.name)
            shutil.move(os.path.join(os.getcwd(),tor.name),os.path.join(os.getcwd(),'Torrents',i,tor.name))

for com in compresses_:
    for i in compresses:
        if i==com.name[-len(i):]:
            print(Path.cwd)
            # print(type(os.getcwd()))
            # print(os.path.join([os.getcwd()]))
            # print(os.getcwd(),com.name)
            shutil.move(os.path.join(os.getcwd(),com.name),os.path.join(os.getcwd(),'Compressed Files',i,com.name))


# print(type(files[0]))
# print(dir(shutil))
#print(help(Path.mkdir))