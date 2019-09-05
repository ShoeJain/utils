execute pathogen#infect()

syntax enable
colorscheme desert
filetype plugin indent on
set number
set autoindent
set tabstop=2
set softtabstop=2
set expandtab
set mouse=a
set wildmenu	"a wild search menu for vim commands
set showmatch	"Paranthesis matching
set lazyredraw	"Redraws are reduced to when needed
set incsearch	"Search as you type
set hlsearch	"highlight search results

"Leader key
let mapleader = "\<Space>"

"Natural splitting
set splitright
set splitbelow 

"Quick save exit
noremap <leader>s :update<CR>
noremap <leader>q :quit<CR>

"Enter/Exit out of insert faster
inoremap jk <esc>
inoremap kj <esc>

"Below maps ctrl c to norm, for commenting/uncommenting
"Usage: ctrl c -> i// for commenting, and ctrl c -> xx for uncommenting
vnoremap <C-c> :norm 

"Remapping arrows keys to learn using hjkl, no matter how bizzarre that sounds
"lol
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>

"Split navigation remaps
nnoremap <C-J> <C-W><C-J>
nnoremap <C-H> <C-W><C-H>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>

"ctrl j/k alt j/k for adding and deleting newlines above and below cursor
nnoremap <silent><A-j> :set paste<CR>m`o<Esc>``:set nopaste<CR>
nnoremap <silent><A-k> :set paste<CR>m`O<Esc>``:set nopaste<CR>

"noh remaps...
nnoremap <CR> :noh<CR><CR>

"Tab navigation
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

"Keybinds for NERDTree
map <C-n> :NERDTreeToggle<CR>
let NERDTreeQuitOnOpen = 1
"let NERDTreeMinimalUI = 1
let NERDTreeDirArrows  = 1 

"Airline stuff
let g:airline_theme='raven'

"NERDComment stuff
let g:NERDCompactSexyComs = 1
let g:NERDAltDelims_java = 1

