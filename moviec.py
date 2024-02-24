#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import argparse
import subprocess
import sys


def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def extract_audio(input_file, output_file):
    try:
        from moviepy.editor import VideoFileClip
    except ImportError:
        print("MoviePy is not installed. Installing...")
        install_package("moviepy")
        from moviepy.editor import VideoFileClip

    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

    video.close()
    audio.close()


def main():
    parser = argparse.ArgumentParser(description='Export audio from a video file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input video file path')
    parser.add_argument('-o', '--output', type=str, default='output.wav', help='Output audio file path')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    extract_audio(input_file, output_file)
    print("Audio exported successfully!")


"""
$ pip install moviepy
$ pip install pyinstaller

$ python moviec.py -i unravel.mp4 -o unravel.wav
$ python moviec.py -i input.mp4 -o input.wav

$ moviec -i input.mp4 -o input_c.wav

"""
if __name__ == "__main__":
    main()
