# Code Snippets
This is just a list of interesting code snippets I've found and used. Unless otherwise noted, statements were ran on whatever version of MacOS I was on at the time of creation

## A lot of these utilize libraries downloaded from [HomeBrew](https://brew.sh), so install that first. 

What HomeBrew says to do: 
``` 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
```

What I did before finding their website :laugh: 
```
/usr/bin/ruby -e "$(curl -fsSL https:/raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Downloading and Converting different movie formats 

Utilizing [FFMPEG](https://www.ffmpeg.org):

```
brew install ffmpeg
```

To convert, for instance, an mkv to an mp4:

```
ffmpeg -i example.mkv -c copy example.mp4
```

To convert, for instance, an webm file from a url to an mp4: 

```
ffmpeg -i url<ending in .webm> name.mp4 (Conversion is saved in current folder)
```

## Converting images between weird icon formats (Specifically SVG)

Utilizing [librsvg](https://en.wikipedia.org/wiki/Librsvg):

```
brew install librsvg
```

To convert (where # indicates the height of the produced image, width is determined automatically) 

```
rsvg-convert -h # icon.svg > icon.png
```

## To download videos from a website

Utilizing [Youtube-DL](https://ytdl-org.github.io/youtube-dl/index.html): 

```
brew install youtube-dl
```

To download the video: 

```
youtube-dl url
```

## To parse HTML pages 

Checkout [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)! I used them for my senior project. You can find some examples from the GitHub project: [JackalopeSearchEngine](https://github.com/aarno97/JackalopeSearchEngine). 

Specifically: 

* Code that was written to pull images from web pages: [ImageRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/ImageRipper/ImageRipper.py)

* Code that was written to pull text from web pages: [TextRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/TextRipper/TextRipper.py)

* Code that was written to pull links from web pages: [LinkRipper](https://github.com/aarno97/JackalopeSearchEngine/blob/master/LinkRipper/LinkRipper.py) 

BeautifulSoup also has really great documentation to help you learn how to do this yourself!

## To keep an eye on prices of items at [Amazon](https://smile.amazon.com)

##### You will need to have installed [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [requests](https://requests.readthedocs.io/en/master/) to run this project: 
```
pip3 install bs4 requests
``` 

I have recently added a new project called [PriceChecker-GitHubVersion](https://github.com/aarno97/Code_Snippets/tree/master/PriceChecker-GitHubVersion). 

This project simply needs to be updated in a few spots and you'll be able to run a simple script to find and receive an email when a price drops during a search.

1. At line 48, enter the email to your gmail account that you can sign into. 
2. At line 49, enter an app-specific password so that your project can login. 
3. At line 51, write the email for the email address you are wanting to send it to and the email address it is coming from. 
4. At line 57, you will see the dictionary for items you are monitoring. 
    * insert the url and original price of the item (or the price you are wanting it to drop below) in the correct format

After that, you're all set! You can use a scheduler if your computer is always-on to run the script at specified intervals!  

## To use sherlock to find and open your user accounts

#### For reference I found this very useful to find a lot of records regarding your own usernames and decided to share how to do so 

I have uploaded a file called finder.sh this is a shell script that will take in an argument (a single username, feel free to update to where you could pass in multiple usernames at once) using the [sherlock](https://github.com/sherlock-project/sherlock) library. 

1. To begin follow the instructions using the above link to clone sherlock to your personal computer. I cloned mine into: 

    ```
    ~/Documents/GitHub/
    ```

2. Download the **finder.sh** file or just clone this entire repository: 
    
   ```
   git clone https://github.com/aarno97/Code_Snippets.git
   ```
   
3. In the **finder.sh** file change:
 
    a. (line 2) to `cd path/of/sherlock-repository`
    
4. I created an alias in **.zshrc** that allowed me to run the script from anywhere: 

    ```
   alias sherlock='cd /path/to/finder.sh && bash finder.sh'
   ```

Using this method you will be able to quickly call sherlock by `sherlock username` from anywhere and the returned list of URLs from Sherlock will all instantly open. 

## To color your zsh shell

Some helpful examples can be found [here](https://blog.balthazar-rouberol.com/customizing-your-shell) and [here](https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/).

I've added the code needed to get a simple colored zsh shell (Showing the Apple Unicode symbol and your name in cyan, path in purple) in a file called **.zshrc**

The simple way to do this would be to add all the color stuff (up to line 42) and just change line 44

Using [Visual Studios Code](https://code.visualstudio.com) or Vim or whatever, open the .zshrc file:

```
code ~/.zshrc
```

Add the entire contents of the supplied .zshrc file in and on line 42 change: 

```
export PROMPT='%F{cyan} Aaron%f%F{blue} 🏡 %~ ➤ %f'
```

To: 

```
export PROMPT='%F{COLOR} NAME%f%F{COLOR} 🏡 %~ ➤ %f'
```

The text inside each %F and %f will be the specified color. 

They accept a multitude of colors (red, purple, yellow, cyan, etc.)

It accepts unicode symbols that are available on your machine, if you don't see the Apple symbol, your machine doesn't support it and probably shows an empty box. 

The %~ specifies the directory you are in, and check the [first link](https://blog.balthazar-rouberol.com/customizing-your-shell) for more options. 

### Data Science Applications -- Serial Killers

Decided to look into specific numbers of active serial killers via decade after reading this [Why were there so many serial killers in the 1980s? - BBC News](https://www.bbc.com/news/world-us-canada-45324622) and decided to add some files on usage

To begin, I downloaded a .csv file containing all the data available on [List of serial killers in the United States - Wikipedia](https://en.wikipedia.org/wiki/List_of_serial_killers_in_the_United_States) using [Wiki Table to CSV online converter](https://wikitable2csv.ggor.de/)

I then used pyplot to get basic histograms displaying years active from, and years active to after scrubbing the data manually.

Then using a dictionary containing decades I wanted to look at, and creating a function called find_decade, I cycled through each record adding each decade a person was active to a set (to prevent duplication) and then incremented appropriately. 

Further applications could be made with more in-depth data science, as well as looking at other things you'd like to have data regarding activity across decades such as: 

[Lists of Pokémon episodes - Wikipedia](https://en.wikipedia.org/wiki/Lists_of_Pok%C3%A9mon_episodes) -- seeing overlap of dates in media production

[List of current monarchs of sovereign states - Wikipedia](https://en.wikipedia.org/wiki/List_of_current_monarchs_of_sovereign_states) -- seeing years of greatest over turn on monarchs



# Future stuff will be added below this marker. 
