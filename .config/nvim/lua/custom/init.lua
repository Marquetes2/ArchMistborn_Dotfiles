local g = vim.g

-- Mapings local leader
g.maplocalleader = ","

-- Makes lines wrap
vim.o.wrap = true
vim.o.linebreak = true
vim.o.smartindent = true
vim.o.autoindent = true
vim.o.breakindent = true
vim.o.breakindentopt = "list:-1"
vim.o.formatlistpat = [[^\s*[-\*\~]\+[\.\)]*\s\+]]
