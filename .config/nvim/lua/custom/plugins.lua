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
        "norg",

        -- 
        "sql",

        --
        "rust",

        --
        "markdown",
      },
      indent = {
          enable = true,
          -- Godot autoindent having problems
          disable = {"gdscript"}
      },
      highlight = {
        enable = true,
      },
    },
  },
  -- {
  --   "MeanderingProgrammer/render-markdown.nvim",
  --   opts = { },
  --   dependencies = { 'nvim-treesitter/nvim-treesitter', 'echasnovski/mini.nvim' },
  -- },
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
          "gdtoolkit",
          "sqlls",
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
    dependencies = { { "nvim-lua/plenary.nvim" }, { "nvim-neorg/neorg-telescope" } },
    config = function()
      require("neorg").setup {
        load = {
          ["core.defaults"] = {}, -- Loads default behaviour
          ["core.journal"] = {
            config = {
              strategy = "flat"
            }
          },
          ["core.concealer"] = { -- Adds pretty icons to your documents
            config = {
              icon_preset = "diamond"
            }
          },
          ["core.keybinds"] = { -- Keybinds
              config = {
                  hook = function(keybinds)
                      -- Keybind for toggling the todo list
                      keybinds.remap_event("norg", "n", "<C-q>", "core.qol.todo_items.todo.task_cycle")
                  end,
              }
          },
          ["core.dirman"] = { -- Manages Neorg workspaces
            config = {
              workspaces = {
                notes = "~/notes",
              },
              default_workspace = "notes"
            },
          },
          ["core.summary"] = {}, -- Creation of summaries
          ["core.ui.calendar"] = {}, -- Calendar
          ["core.integrations.telescope"] = {},
        },
      }
      vim.wo.foldlevel = 99
      vim.wo.conceallevel = 2
    end,
    lazy=false
  },
  {
    "rust-lang/rust.vim",
    ft = "rust",
    init = function ()
      -- Auto format rust, once its saved
      vim.g.rustfmt_autosave = 1
    end
  },
  {
    "simrat39/rust-tools.nvim",
    ft = "rust",
    dependencies = "neovim/nvim-lspconfig",
    opts = function ()
      return require "custom.configs.rust-tools"
    end,
    config = function(_, opts)
      require('rust-tools').setup(opts)
    end
  },
  {
    "mfussenegger/nvim-dap"
  },
  {
    "saecki/crates.nvim",
    ft = {"rust", "toml"},
    config = function(_, opts)
      local crates = require('crates')
      crates.setup(opts)
      crates.show()
    end,
  },
  {
    "hrsh7th/nvim-cmp",
    opts = function()
      local M = require "plugins.configs.cmp"
      table.insert(M.sources, {name = "crates"})
    end
  },
  {
    "epwalsh/obsidian.nvim",
    version = "*",  -- recommended, use latest release instead of latest commit
    lazy = true,
    ft = "markdown",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "hrsh7th/nvim-cmp",
      "nvim-telescope/telescope.nvim",
    },
    opts = {
      workspaces = {
        {
          name = "What is life?",
          path = "~/Desktop/vaults/WhatIsLife/",
        },
      },
      ui = { enable = false },
      -- Optional, customize how note IDs are generated given an optional title.
      ---@param title string|?
      ---@return string
      note_id_func = function(title)
        if title ~= nil then
          return title
        else
          local new_title = ""
          for _ = 1, 8 do
            new_title = new_title .. string.char(math.random(65, 90))
          end
          return new_title
        end
      end,
      daily_notes = {
        -- Optional, if you keep daily notes in a separate directory.
        folder = "journal/",
        -- Optional, if you want to change the date format for the ID of daily notes.
        date_format = "%Y-%m-%d",
        -- Optional, default tags to add to each new daily note created.
        default_tags = { "daily-notes" },
        -- Optional, if you want to automatically insert a template from your template directory like 'daily.md'
        template = nil
      },
    },
  }
}

return plugins
