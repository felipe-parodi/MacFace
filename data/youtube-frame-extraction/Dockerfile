FROM ubuntu:20.04
LABEL maintainer="Jordan Matelsky <opensource@matelsky.com>"
ENV DEBIAN_FRONTEND noninteractive

# Install youtube-dl, ffmpeg:
RUN apt-get update
RUN apt-get install -y \
    ffmpeg \
    imagemagick \
    git \
    jq
RUN apt-get install -y python3-pip

# Install youtube-dl:
# RUN pip3 install youtube-dl
RUN pip3 install 'git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl'
RUN rm -rf /var/lib/apt/lists/*

COPY frameextract.sh /usr/local/bin/frameextract.sh
RUN chmod +x /usr/local/bin/frameextract.sh

ENTRYPOINT ["bash", "frameextract.sh"]