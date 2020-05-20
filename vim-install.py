import os
from git import Repo
from shutil import copyfile
from shutil import rmtree

#All the plugin git
utils = "https://github.com/xrex110/utils.git"
pathogen = "https://github.com/tpope/vim-pathogen.git"
nerd_tree = "https://github.com/scrooloose/nerdtree.git"
nerd_comm = "https://github.com/scrooloose/nerdcommenter.git"
airline = "https://github.com/vim-airline/vim-airline.git"
airline_themes = "https://github.com/vim-airline/vim-airline-themes.git"
color_schemes = "https://github.com/rafi/awesome-vim-colorschemes.git"


print("Make sure you install the gitpython module before running this script")
print("Create a .vim folder in your ~ directory")

vim_folder_path = input("Enter the full path (including .vim/) of your .vim folder: ");
vimrc_path = input("Enter the full path (including .vimrc) of your .vimrc file: ")

vim_bundle_path = vim_folder_path + "bundle/"
vim_autoload_path = vim_folder_path + "autoload/"

print(".vim folder path: " + vim_folder_path)
print(".vimrc path: " + vimrc_path)
print("bundle path: " + vim_bundle_path)
print("autoload path: " + vim_autoload_path)


#We clone all the files into ~/.vim/bundle
print("Switching to " + vim_bundle_path)
os.chdir(vim_bundle_path);
print("Cloning required repositories")
Repo.clone_from(nerd_tree, "nerdtree")
Repo.clone_from(nerd_comm, "nerdcommenter")
Repo.clone_from(airline, "vim-airline")
Repo.clone_from(airline_themes, "vim-airline-themes")
Repo.clone_from(color_schemes, "awesome-vim-colorschemes")
print ("finished cloning all repositories")

print("Switching to " + vim_folder_path)
os.chdir(vim_folder_path)
Repo.clone_from(utils, "tempfolder")
Repo.clone_from(pathogen, "tempfolder2")
copyfile(vim_folder_path + "tempfolder2/autoload/pathogen.vim", vim_autoload_path + "pathogen.vim");
copyfile(vim_folder_path + "tempfolder/vimrc", vimrc_path)
print("vimrc and pathogen.vim loaded")

print("Removing temporary directories")
rmtree(vim_folder_path + "tempfolder/");
rmtree(vim_folder_path + "tempfolder2/");
print("Finish execution")
