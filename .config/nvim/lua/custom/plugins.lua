local plugins = {

  -- this opts will extend the default opts 
  {
    "christoomey/vim-tmux-navigator",
    lazy = false,
  },
  {
    "nvim-treesitter/nvim-treesitter",
    opts = {
      ensure_installed = {
        -- defaults
        "vim",
        "lua",

        -- web dev
        "html",
        "css",
        "javascript",
        "typescript",
        "json",

        -- low level
        "c",

        -- python
        "python",

        -- gdscript (Godot)
        "gdscript",
      },
    },
  },
  {
    "neovim/nvim-lspconfig",
     config = function()
        require "plugins.configs.lspconfig"
        require "custom.configs.lspconfig"
     end
  },
  {
    "williamboman/mason.nvim",
     opts = {
        ensure_installed = {
          "lua-language-server",
          "clangd",
          "pyright",
          "typescript-language-server",
          "css-lsp",
          "html-lsp",
          "emmet-language-server",
          "gdtoolkit"
        },
      },
  },
  {
    "habamax/vim-godot",
    lazy=false
  }
}

return plugins
