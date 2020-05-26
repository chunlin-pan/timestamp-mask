[toc]


# Windows 安裝方式
1. 下載python3 (有python3 略過這一步)

    https://www.python.org/downloads/

    或是直接點這裡[下載](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)。

    Add Python 3.8 to Path 請打勾，其他配置請勿更動。
    ![](https://imgur.com/wjOad4R)

2. 下載imagemagick (有imagemagick 略過這一步)

    https://imagemagick.org/script/download.php

    或是直接點這裡[下載](https://imagemagick.org/download/binaries/ImageMagick-7.0.10-14-Q16-x64-dll.exe)。

    安裝配置請勿更動。

3. 下載本[專案](https://github.com/chunlin-pan/timestamp-mask/archive/master.zip)並解壓縮

    開啟CMD

    `$ cd C:\Users\user\Downloads\timestamp-mask` 後面的參數是解壓縮後的資料夾位置

    `$ python -m vnev timestamp-env` 開啟虛擬環境

    `$ timestamp-env\Scripts\activate.bat` 進入虛擬環境

    `$ pip install -r requirements.txt` 安裝必要套件

    安裝完後以WordPad開啟
    
    `timestamp-mask\timestamp-env\Lib\site-packages\moviepy\config_defaults.py` 
    
    將檔案最下面一行

    IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')

    改成

    IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"

    回到CMD輸入

    `$deactivate`

    完成安裝

# 使用方式



