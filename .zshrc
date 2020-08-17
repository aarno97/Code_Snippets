#Color Vars
# Foreground
black="$(tput setaf 0)"
red="$(tput setaf 1)"
green="$(tput setaf 2)"
yellow="$(tput setaf 3)"
blue="$(tput setaf 4)"
purple="$(tput setaf 5)"
cyan="$(tput setaf 6)"
white="$(tput setaf 7)"
bblack="$(tput setaf 8)"
bred="$(tput setaf 9)"
bgreen="$(tput setaf 10)"
byellow="$(tput setaf 11)"
bblue="$(tput setaf 12)"
bpurple="$(tput setaf 13)"
bcyan="$(tput setaf 14)"
bwhite="$(tput setaf 15)"
# Background
oblack="$(tput setab 0)"
ored="$(tput setab 1)"
ogreen="$(tput setab 2)"
oyellow="$(tput setab 3)"
oblue="$(tput setab 4)"
opurple="$(tput setab 5)"
ocyan="$(tput setab 6)"
owhite="$(tput setab 7)"
obblack="$(tput setab 8)"
obred="$(tput setab 9)"
obgreen="$(tput setab 10)"
obyellow="$(tput setab 11)"
obblue="$(tput setab 12)"
obpurple="$(tput setab 13)"
obcyan="$(tput setab 14)"
obwhite="$(tput setab 15)"
# Utility
bold="\[$(tput bold)\]"
dim="\[$(tput dim)\]"
# reset"\[$(tput sgr0)\]"
# Custom prompt
# export PS1=“[${bblue}\] Aaron\[${black}\] 🏡\[${bpurple}\] \w \[${white}\]➤ ”

export PROMPT='%F{cyan} Aaron%f%F{blue} 🏡 %~ ➤ %f'

export PATH=~/.node/bin:$PATH