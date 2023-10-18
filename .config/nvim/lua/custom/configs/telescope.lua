local telescope = require "telescope"
local actions = require "telescope.actions"

local opts = require "plugins.configs.telescope"
opts.defaults.mappings.i = {
  ["<Esc>"] = actions.close,
  ["<C-c>"] = function()
    vim.cmd [[stopinsert]]
  end,
}

opts.defaults.mappings.n = {
  ["<C-c>"] = actions.close,
  ["q"] = actions.close
}

-- set up telescope
dofile(vim.g.base46_cache .. "telescope")
telescope.setup(opts)

-- load extensions
for _, ext in ipairs(opts.extensions_list) do
  telescope.load_extension(ext)
end
