# Code Snippets
This is just a list of interesting code snippets I've found and used. Unless otherwise noted, statements were ran on whatever version of MacOS I was on at the time of creation

## A lot of these utilize libraries downloaded from [HomeBrew](https://brew.sh), so install that first. 

What HomeBrew says to do: 
``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" ```

What I did before finding their website :laugh: 
```/usr/bin/ruby -e "$(curl -fsSL https:/raw.githubusercontent.com/Homebrew/install/master/install)"```

## Downloading and Converting different movie formats 

Utilizing [FFMPEG](https://www.ffmpeg.org):

```brew install ffmpeg```

To convert, for instance, an mkv to an mp4:

```ffmpeg -i example.mkv -c copy example.mp4```

To convert, for instance, an webm file from a url to an mp4: 

```ffmpeg -i url<ending in .webm> name.mp4``` (Conversion is saved in current folder) 

## Converting images between weird icon formats (Specifically SVG)

Utilizing [librsvg](https://en.wikipedia.org/wiki/Librsvg):

```brew install librsvg```

To convert (where # indicates the height of the produced image, width is determined automatically) 

```rsvg-convert -h # icon.svg > icon.png```

## To download videos from a website

Utilizing [Youtube-DL](https://ytdl-org.github.io/youtube-dl/index.html): 

```brew install youtube-dl```

To download the video: 

```youtube-dl url```

## To parse HTML pages 

Checkout [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)! I used them for my senior project. You can find some examples from the GitHub project from the project: [JackalopeSearchEngine](https://github.com/aarno97/JackalopeSearchEngine). 

Specifically: 

* Code that was written to pull images from web pages: [ImageRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/ImageRipper/ImageRipper.py)

* Code that was written to pull text from web pages: [TextRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/TextRipper/TextRipper.py)

* Code that was written to pull links from web pages: [LinkRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/LinkRipper/LinkRipper.py) 

BeautifulSoup also has really great documentation to help you learn how to do this yourself!

# Future stuff will be added below this marker. 
