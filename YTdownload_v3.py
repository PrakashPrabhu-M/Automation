from pytube import YouTube
from pytube import Playlist
import pyperclip
import sys
import os

#getting the link from the user via clipboard or argument
link=sys.argv[-1] if len(sys.argv)>1 else pyperclip.paste()
#print(link)


def progress_func(stream,chunk,bytes_remaining):
    remaining=bytes_remaining/1024/1024
    print(f'Remaining: {round(remaining,2)} MB',end='\r')
def complete_func(stream,filepath):
    print(f'Done at {filepath}')

#checking wether it is a youtube link
if "https://youtu.be" not in link:
    if "https://youtube.com" not in link:
        print("URL error!")
    #if the link is a playlist
    else:
        playlist=Playlist(link)
        res_avail=[]
        print(playlist.title)
        for vdo in playlist.videos:
            name=vdo.title.replace("|","")

            chosen=vdo.streams.order_by("resolution").last()
            #checking wether the file contains audio
            #if there is no audio, it meanse the resolution is < 1028p and audio must be downloaded seperately and merged via ffmpeg
            if chosen.abr is None:
                #reference https://python-pytube.readthedocs.io/en/latest/user/streams.html#filtering-streams, filtering only audio and picking the highest available audio
                ado=vdo.streams.filter(only_audio=True).order_by("abr").last()
                
                #storing the formats of audio and video
                ado_format=ado.mime_type.split('/')[1]
                vdo_format=chosen.mime_type.split('/')[1]
                
                #changing the directory so the download must go into the required folder
                os.chdir(name)
                chosen.download(filename=name+"_vdo",output_path=os.getcwd()+"/"+name)
                ado.download(filename=name+"_ado",output_path=os.getcwd()+"/"+name)

                #merge audio and video
                if "mp4" in chosen.mime_type:
                    os.system(f'ffmpeg -i "{name}_vdo.{vdo_format}" -i "{name}_ado.{ado_format}" -strict -2 -c:v copy -c:a copy "{name}".{vdo_format}')
                os.system(f'ffmpeg -i "{name}_vdo.{vdo_format}" -i "{name}_ado.{ado_format}" -c:v copy -c:a copy "{name}".{vdo_format}')
                #removing audio and video files (unmerged)
                print(os.getcwd())
                temp_vdo="{0}_vdo.{1}".format(name,vdo_format)
                temp_ado="{0}_ado.{1}".format(name,ado_format)
                os.remove(temp_vdo)
                os.remove(temp_ado)

else:
    yt=YouTube(link,on_progress_callback=progress_func,on_complete_callback=complete_func)
    #yt=YouTube(link)
    
    print(yt.title,end='\n\n')
    #print(yt.thumbnail_url)

    #picking all the available formats of the youtube file
    formats=yt.streams
    choice_vdo=[]
    
    #displaying all the available formats for user to pick
    for i,j in enumerate(formats):
        #print(dir(j))
        #break
        choice_vdo.append(j)
        size=round(j.filesize/1024/1024,2)
        print(f"{i} - FPS: {j.fps} Resolution: {j.resolution} Type: {j.mime_type} File size: {size} MB Audio: {j.abr}")
    
    #selecting the user choice
    selection_vdo=choice_vdo[int(input("Type your choice: "))]
    #print(choice_vdo)

    #renaming the file name so that it works in ffmpeg
    name=yt.title.replace("|","")

    #checking wether the file contains audio
    #if there is no audio, it meanse the resolution is < 1028p and audio must be downloaded seperately and merged via ffmpeg
    if selection_vdo.abr is None:
        choice_ado=[]
        print("Choose your audio: ")
        choice_vdo=filter(lambda a:a.type=="audio",choice_vdo)
        for i,j in enumerate(choice_vdo):
            print(i,j.abr)
            choice_ado.append(j)
        selection_ado=choice_ado[int(input("Type your choice: "))]

        #proceeding to download after audio is selected
        print("Downloading")
        selection_vdo.download(filename=name+'_vdo',output_path=os.getcwd()+f"/{name}")
        selection_ado.download(filename=name+'_ado',output_path=os.getcwd()+f"/{name}")
        print("Done")
        vdo_format=selection_vdo.mime_type.split('/')[1]
        ado_format=selection_ado.mime_type.split('/')[1]
        print(vdo_format,ado_format)
        #input()
        os.chdir(name)
        #below command refered from https://kwizzu.com/construct.html
        if "mp4" in selection_vdo.mime_type:
            os.system(f'ffmpeg -i "{name}_vdo.{vdo_format}" -i "{name}_ado.{ado_format}" -strict -2 -c:v copy -c:a copy "{name}".{vdo_format}')
        else:
            os.system(f'ffmpeg -i "{name}_vdo.{vdo_format}" -i "{name}_ado.{ado_format}" -c:v copy -c:a copy "{name}".{vdo_format}')
        temp_vdo="{0}_vdo.{1}".format(name,vdo_format)
        temp_ado="{0}_ado.{1}".format(name,ado_format)
        os.remove(temp_vdo)
        os.remove(temp_ado)
   
    else:
        print("Downloading")
        selection_vdo.download(filename=name,output_path=os.getcwd()+f"/{name}")
        print("Done")     

    #checking if there is any subtitles in english to download
    caption=yt.captions.get_by_language_code('en')
    if caption:
        srt_file=caption.generate_srt_captions()

        with open(name+'.srt','w') as f:
            f.write(srt_file)
        print('Captions downloaded',os.getcwd())
    else:
        print("No Captions")
