from moviepy.editor import *
from datetime import datetime as dt
import argparse

def timestamp(filename, time, duration, output_name, start_time=0, color='white', audio='on'):
    ''''2020/05/20 06:43:' time格式'''
    time = time
    second_range = range(duration)
    text_list=[]
    for i in second_range:
        text_clip = TextClip(set_time(time, i),fontsize=70,color=color).set_duration(1)
        
        text_list.append(text_clip)
    if type(start_time) in [tuple, list]:
        start = (start_time[0],start_time[1]+i)
        end = (start_time[0],start_time[1]+i+1)
        video = VideoFileClip(filename).subclip(start,end)
    else:
        video = VideoFileClip(filename).subclip(start_time, start_time + duration)
    if audio == 'off':
        video = video.without_audio()
    final_text_clip = concatenate_videoclips(text_list).set_position((0.05,0.85), relative=True)
    final_clip = CompositeVideoClip([video, final_text_clip])
    final_clip.write_videofile(output_name, fps = 60)

def set_time(time, second):
    mod_second = (second) % 60 
    carry_second = second // 60
    
    minute = time[4] + carry_second
    mod_minute = minute % 60
    carry_minute = minute // 60
    
    hour = time[3] + carry_minute
    mod_hour = hour % 60
    carry_hour = hour // 60
    
    day = time[2] + carry_hour
    return dt(time[0], time[1], day, mod_hour, mod_minute, mod_second).strftime("%Y/%m/%d %H:%M:%S")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='input xxx.mp4', type = str)
    parser.add_argument('-t', '--time', help='year, month, day, minute', type = str) #year, month, day, hour, minute
    parser.add_argument('-s', '--starttime', help='input an integer', type = int)
    parser.add_argument('-d', '--duration', help='input an integer', type = int)
    parser.add_argument('-aud-off', '--audio-off', help='turn off audio', action='store_true')
    parser.add_argument('-o', '--outputname', help='input xxx.mp4', type = str)
    args = parser.parse_args()
    
    filename = args.filename
    time = list(map(int, args.time.split(',')))[:5] #[year, month, day, hour, minute]
    start_time = args.starttime
    duration = args.duration
    audio = 'off' if arg.audio_off else 'on'
    output_name = args.outputname
    timestamp(filename=filename, time=time, duration=duration, output_name=output_name, start_time=start_time, audio = audio, color='white')