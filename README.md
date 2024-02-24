# `moviec`

A small project using python's `moviepy` library to extract audio from video.

## 1.`Install`

```shell
$ pip install moviepy
```

## 2.`Usage`

### 2.1.`python`

```shell
$ python moviec.py -i input.mp4 -o input.wav
```

### 2.2.`Executable`

```shell
# install pyinstaller
$ pip install pyinstaller
$ pyinstaller --onefile moviec.py

$ moviec -i input.mp4 -o input_c.wav
```

