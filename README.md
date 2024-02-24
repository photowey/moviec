# `moviec`

A small project using python's `moviepy` library to extract audio from video.

## 1.`Install`

```shell
$ pip install moviepy
```

## 2.`Usage`

### 2.1.`Python`

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

## 3.`Release`

### 3.1.`bin`

#### 3.1.1.`win`

[moviec](./bin/win/moviec.exe)

#### 3.1.2.`linux`

#### 3.1.3.`macOS`

> Binary executable files can be easily built on `Linux` and `macOS` systems. This project does not provide executable
> files for the time being.

