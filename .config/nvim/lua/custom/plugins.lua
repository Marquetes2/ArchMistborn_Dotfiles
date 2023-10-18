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

        -- norg (Neorg)
        "norg"
      },
      indent = {
          enable = true,
          -- Godot autoindent having problems
          disable = {"gdscript"}
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
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-treesitter/nvim-treesitter", { "nvim-telescope/telescope-fzf-native.nvim", build = "make" } },
    cmd = "Telescope",
     config = function()
        require "custom.configs.telescope"
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
  },
  {
    "folke/zen-mode.nvim",
    opts = {
      -- your configuration comes here
      -- or leave it empty to use the default settings
      -- refer to the configuration section below
    },
    lazy=false
  },
  {
    "nvim-neorg/neorg",
    build = ":Neorg sync-parsers",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      require("neorg").setup {
        load = {
          ["core.defaults"] = {}, -- Loads default behaviour
          ["core.concealer"] = { -- Adds pretty icons to your documents
            config = {
              icon_preset = "diamond"
            }
          },
          ["core.keybinds"] = { -- Keybinds
              config = {
                  hook = function(keybinds)
                      -- Keybind for toggling the todo list
                      -- keybinds.remap_event("norg", "n", "<C-j>", "core.qol.todo_items.todo.task_cycle")
                  end,
              }
          },
          ["core.dirman"] = { -- Manages Neorg workspaces
            config = {
              workspaces = {
                notes = "~/Notes",
              },
              default_workspace = "notes"
            },
          },
          ["core.summary"] = {}, -- Creation of summaries
          ["core.presenter"] = {
            config = {
              zen_mode = "zen-mode"
            }
          }, -- Allows zen mode
          -- ["core.ui.calendar"] = {}, -- Calendar
        },
      }
      vim.wo.foldlevel = 99
      vim.wo.conceallevel = 2
    end,
    lazy=false
  }
}

return plugins
