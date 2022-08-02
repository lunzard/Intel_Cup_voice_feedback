import glob
import vlc

# if the address is got directly from windows file explorer
# format the backslash
def format_playlist_address(address):
    address.replace("\\" , "/")
    address += "/*"
    return address


address = "D:/NUS/project codes/Intel_Cup_voice_feedback/musiclist/*"
inst = vlc.Instance()
player = inst.media_list_player_new()
playlist = []
for song in glob.glob(address):
    playlist.append(song)

media_list = inst.media_list_new(playlist)
# media_list = inst.media_list_new(["D:/NUS/project codes/Intel_Cup_voice_feedback/musiclist/Lyn - Last Surprise.mp3"])
player.set_media_list(media_list)
player.play()

player.get_media_player().audio_set_volume(50)

is_playing = True
while is_playing:
    volume = input("set Volume: ")
    # exit/stop
    if volume == '-1':
        is_playing = False
        print('exiting...')
        break
    # pause
    elif volume == '-2':
        player.set_pause(1)
    # resume/play
    elif volume == '-3':
        player.set_pause(0)
    # change volume
    else:
        print('set volume to ', volume)
        player.get_media_player().audio_set_volume(int(volume))

print('finished play all sound')
    