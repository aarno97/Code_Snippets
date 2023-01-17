# UPDATE COMPUTER BEFORE PERFORMING
echo "You should have updated your computer by now: softwareupdate -l"

# set up shell prompt
echo "export PROMPT='%F{cyan} Aaron%f%F{blue} 🏡 %~ ➤ %f'" >> ~/.zshrc
echo "" >> ~/.zshrc
#echo "alias python=/usr/local/bin/python3.8" >> ~/.zshrc
#echo "alias sherlock='cd ~/Documents/GitHub/Code_Snippets && bash finder.sh'" >> ~/.zshrc
#echo "echoed sherlock into ~/.zshrc, please clone project before using"
#echo "" >> ~/.zshrc
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.zshrc
echo "autoload bashcompinit && bashcompinit" >> ~/.zshrc

# install xCode components
xcode-select --install

# install HomeBrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install cask
brew doctor
brew update

# install HomeBrew packages
# brew install node
brew install git
brew install visual-studio-code
brew install --cask jetbrains-toolbox
brew install --cask discord
brew install ffmpeg
brew install librsvg
brew install youtube-dl
brew tap adoptopenjdk/openjdk
brew cask install adoptopenjdk11
brew install python3 pipenv
python3 --version
pip3 --version

# set up git config
git config --global user.email "yourEmail@wherever.com"
git config --global user.name "Your Name"
git config --global color.ui auto


# install node related things
# nvm install stable
# npm install -g npm

# npm install -g tldr
# npm install -g typescript
# npm install -g @vue/cli
# npm install -g vuepress
# npm install -g @angular/cli
# npm install -g eslint
# npm install -g gitbook-cli
# npm install -g lodash