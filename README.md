# timestamp-mask
[![Python](https://img.shields.io/badge/python-3.8.3-blue.svg?style=popout)](https://www.python.org/downloads/release/python-383/)
[![imagemagick](https://img.shields.io/badge/imagemagick-7.0.10--14-green])](https://github.com/ImageMagick/ImageMagick/tree/7.0.10-14)
[![moviepy](https://img.shields.io/badge/moviepy-1.0.3-yellow)](https://github.com/Zulko/moviepy/tree/v1.0.3)

timestamp-mask是一個幫影片增加時間戳記的工具，以下demo經過加速，實際輸出還是原來影片的速度。

![Alt Text](demo/input_gif.gif)
![Alt Text](demo/timestamp_gif.gif)
![Alt Text](demo/output_gif.gif)
# Windows 安裝方式
1. 下載python3 (有python3 略過這一步)

    https://www.python.org/downloads/

    或是直接點這裡[下載](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)。

    Add Python 3.8 to Path 請打勾，其他配置請勿更動。
    ![Imgur Image](https://imgur.com/wjOad4R.jpg)

2. 下載imagemagick (有imagemagick 略過這一步)

    https://imagemagick.org/script/download.php

    或是直接點這裡[下載](https://imagemagick.org/download/binaries/ImageMagick-7.0.10-14-Q16-x64-dll.exe)。

    安裝配置請勿更動。

3. 下載本[專案](https://github.com/chunlin-pan/timestamp-mask/archive/master.zip)並解壓縮

    開啟CMD(`$` 開頭表示要在CMD中輸入的指令，從`$`後面的內容開始輸入)

    `$ cd C:\Users\user\Downloads\timestamp-mask` 後面的參數是解壓縮後的資料夾位置

    `$ python -m vnev timestamp-env` 開啟虛擬環境

    `$ timestamp-env\Scripts\activate.bat` 進入虛擬環境

    `$ pip install -r requirements.txt` 安裝必要套件

    安裝完後以WordPad開啟以下檔案
    
    `timestamp-mask\timestamp-env\Lib\site-packages\moviepy\config_defaults.py` 
    
    將檔案最下面一行

    IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')

    改成

    IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"

    回到CMD輸入

    `$ deactivate`

    完成安裝

# 使用方式

1. 開啟CMD

2. 移到`timestamp-mask`目錄

    `$ cd C:\Users\user\Downloads\timestamp-mask`

3. 進入虛擬環境

    `$ timestamp-env\Scripts\activate.bat`

4. 增加時間浮水印

    如果你要加浮水印的影片、影片當下時間等等的規格如下:

        輸入檔名: input.mp4

        影片當下時間: 2020/05/26 06:23:00

        影片擷取起點: 第3秒

        影片持續時間: 10秒

        關閉聲音: 是

        輸出檔案: output.mp4

    就輸入:

    `$ python timestamp.py -f input.mp4 -t 2020,5,26,6,23,0 -s 3 -d 10 -audio-off -o output.mp4`

    如果要保留聲音則把`-audio-off`去掉，則輸入:

    `$ python timestamp.py -f input.mp4 -t 2020,5,26,6,23,0 -s 3 -d 10 -o output.mp4`

5. 離開虛擬環境

    `$ deactivate`

