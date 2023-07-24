local plugins = {
  {
    "neovim/nvim-lspconfig",
     config = function()
        require "plugins.configs.lspconfig"
        require "custom.configs.lspconfig"
     end,
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
          "html-lsp"
        },
      },
  },
}
return plugins
