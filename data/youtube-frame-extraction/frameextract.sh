# Given a YouTube Video URL (such as https://www.youtube.com/watch?v=QH2-TGUlwu4),
# this script will download the video, extract the frames to a directory at a
# user-specified interval, delete the video, and then downsample each frame to
# a user-specified min-size (while maintaining aspect ratio).

# This script requires ffmpeg and ImageMagick to be installed, and it requires
# the user to have write access to the current directory.

# Everything is wrapped in a function so that we can use the "return" command
# to exit the script with a non-zero exit code if something goes wrong.

# This script is intended to be run from the command line, but it can also be
# run from a shell script by sourcing it.

# Populate variables from command line arguments
youtube_url=$1

# Try to extract youtube IDs from the URL (if the URL is a playlist).
# If not, fail gracefully by continuing. Otherwise, print the IDs and exit.

# Check to see if "list" is in the URL:
if [[ "$youtube_url" == *"list"* ]]; then
    # If so, extract the playlist ID:
    playlist_id=$(echo "$youtube_url" | sed 's/.*list=\([^&]*\).*/\1/')
    # Use youtube-dl to extract the video IDs from the playlist:
    youtube-dl -j --flat-playlist "https://www.youtube.com/playlist?list=$playlist_id" | jq -r .url > playlist_ids.txt
    # Print the IDs to the screen:
    cat playlist_ids.txt
    # Exit the script:
    exit 0
fi

frame_interval=$2
frame_min_height=$3
output_dir=$4

youtube_id=$(echo "$youtube_url" | sed 's/.*v=\([^&]*\).*/\1/')

youtube-dl -f 'best[height <=? 720]' -o "$youtube_id".mp4 "https://www.youtube.com/watch?v=$youtube_id"
# ffmpeg -i "$youtube_id".mp4 -vf fps=1/$frame_interval -s $frame_min_height "$output_dir"/"$youtube_id"_%04d.jpg
ffmpeg -i "$youtube_id".mp4 -vf "fps=1/$frame_interval, scale=$frame_min_height:-1" "$output_dir"/"$youtube_id"_%04d.jpg


exit 0