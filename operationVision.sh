# UPDATE COMPUTER BEFORE PERFORMING
echo "You should have updated your computer by now: softwareupdate -l"

# set up shell prompt
echo "export PROMPT='%F{cyan} Aaron%f%F{blue} 🏡 %~ ➤ %f'" >>~/.zshrc
echo "" >>~/.zshrc
echo "export PATH=$HOME/.local/bin:$PATH" >>~/.zshrc
echo "autoload bashcompinit && bashcompinit" >>~/.zshrc

# install xCode components
xcode-select --install

# install HomeBrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install cask
brew doctor
brew update

# install HomeBrew packages
brew install git
brew install visual-studio-code
brew install --cask jetbrains-toolbox
brew install --cask discord
brew install ffmpeg
brew install librsvg
brew install youtube-dl

# set up git config
git config --global user.email "yourEmail@wherever.com"
git config --global user.name "Your Name"
git config --global color.ui auto