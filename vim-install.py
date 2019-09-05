import os
from git import Repo
from shutil import copyfile

nerd_tree = "https://github.com/scrooloose/nerdtree.git"
nerd_comm = "https://github.com/scrooloose/nerdcommenter.git"
airline = "https://github.com/vim-airline/vim-airline.git"
airline_themes = "https://github.com/vim-airline/vim-airline-themes.git"
color_schemes = "https://github.com/rafi/awesome-vim-colorschemes.git"

#We clone all the files into ~/.vim/bundle
os.chdir("~/.vim/bundle")

Repo.clone_from(nerd_tree, "nerdtree")
Repo.clone_from(nerd_comm, "nerdcommenter")
Repo.clone_from(airline, "vim-airline")
Repo.clone_from(airline_themes, "vim-airline-themes")
Repo.clone_from(color_schemes, "awesome-vim-colorschemes")

os.chdir("~/.vim/")
Repo.clone_from("https://github.com/xrex110/utils.git", "tempfolder")
copyfile("~/.vim/tempfolder/vimrc", "~/.vim/.vimrc")