call plug#begin()

Plug 'nvim-lualine/lualine.nvim'
Plug 'tanvirtin/monokai.nvim'
Plug 'maxboisvert/vim-simple-complete'
Plug 'nvim-tree/nvim-web-devicons'
Plug 'nvim-tree/nvim-tree.lua'
Plug 'bsuth/emacs-bindings.nvim'

call plug#end()

lua require'lualine'.setup()
lua require'monokai'.setup()

set number
set tabstop=4
set shiftwidth=4
set cindent
set expandtab
set showmatch
set ai
set si

set pastetoggle=<f5>
set mouse=a
set clipboard^=unnamed

set laststatus=2
set noshowmode

:nmap <c-s> :w<CR>
:imap <c-s> <Esc>:w<CR>a

syntax on
filetype indent on
