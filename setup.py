import os

def main():
    creat_env = 'python -m venv timestamp-env'
    venv_dir = 'timestamp-env\Scripts\activate.bat'
    install_require = 'pip install -r requirements.txt'
    os.popen(creat_env + ' && ' + venv_dir + ' && ' + install_require)
    root_path = r'timestamp-env\Lib\site-packages\moviepy\'
    config_defaults_path = os.path.realpath(root_path+'config_defaults.py')
    imagick_policy = open(config_defaults_path, mode = 'r')
    line = imagick_policy.readline()
    while line:
        if line = 'IMAGEMAGICK_BINARY = os.getenv(\'IMAGEMAGICK_BINARY\', \'auto-detect\')'
            line = 'IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"'
        tmp_path = os.path.realpath(path+'tmp.txt')
        tmp = open(tmp_path, 'a')
        tmp.write('\r\n'+line)
        tmp.close()
        line = imagick_policy.readline()
    imagick_policy.close()
    os.popen('del ' + config_defaults_path + ' && ' +'ren ' +  tmp_path +' '+ config_defaults_path)

if __name__ == '__main__':
    main()