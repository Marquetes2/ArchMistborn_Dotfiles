-- If nvim is running in the Notes directory, then apply some changes
local M = {}
  
local function check_notes()
  local directory = os.getenv("PWD")
  return string.find(directory, "/Notes")
end

local function update_chadrc(M)
  if check_notes() then
    M.ui.tabufline = {
      enabled = false
    }
  end
  return M
end

M.update_chadrc = update_chadrc

return M
