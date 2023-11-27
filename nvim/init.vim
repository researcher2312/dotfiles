call plug#begin()

Plug 'nvim-lualine/lualine.nvim'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'tanvirtin/monokai.nvim'

call plug#end()

set termguicolors
lua require'colorizer'.setup()
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

syntax on
filetype indent on
