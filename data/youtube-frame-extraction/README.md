# YouTube Video Frame Extraction

```shell
podman build -t frameextractor .
# podman run -it --rm -v $(pwd)/frames:/out frameextractor [VIDEO ID] 100 512 /out
podman run -it --rm -v $(pwd)/frames:/out frameextractor QH2-TGUlwu4 100 512 /out
```

Arguments are:

* YouTube Video ID
* Frequency of frames to extract (1 = every second, 100 = one frame every 100 seconds)
* Size of extracted frames (height)
* Output directory (should be mounted as a volume)

To get video IDs from a YouTube playlist, use the following command:

```shell
podman run -it --rm -v $(pwd)/frames:/out frameextractor 'https://www.youtube.com/watch?v=0fts6x_EE_E&list=PL-M-cbWTCkAE5VQIt4Njwz63aAItXBY2S'
```

This will print all the video IDs in the playlist to stdout, one per line. To run the extraction on all the videos in the playlist in parallel, you can use the following `parallel` command:

```shell
podman run -it --rm -v $(pwd)/frames:/out frameextractor 'https://www.youtube.com/watch?v=0fts6x_EE_E&list=PL-M-cbWTCkAE5VQIt4Njwz63aAItXBY2S' | parallel -j 2 podman run -it --rm -v $(pwd)/frames:/out frameextractor {} 10 512 /out
podman run -it --rm -v $(pwd)/frames:/out frameextractor 'https://www.youtube.com/watch?v=b6uQmVjVjXM&list=PLh26pNSrrxvyKRwkD3PPIJg5ht_e57Esz' | parallel -j 2 podman run -it --rm -v $(pwd)/frames:/out frameextractor {} 10 512 /out
podman run -it --rm -v $(pwd)/frames:/out frameextractor 'https://www.youtube.com/watch?v=2M1BmfHlOEI&list=PLqGjS-l4Roj9P6H_BCXyRCEUJUo4SB0wV' | parallel -j 2 podman run -it --rm -v $(pwd)/frames:/out frameextractor {} 10 512 /out
```