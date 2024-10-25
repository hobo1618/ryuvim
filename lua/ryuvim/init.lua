local config = require("ryuvim/config")
local marp = require("ryuvim/ryuvim")

local M = {}

M.setup = config.setup
M.start = marp.start
M.stop = marp.stop
M.status = marp.status
M.toggle = marp.toggle

-- create MarpStart command
vim.api.nvim_create_user_command("RyuStart", M.start, { desc = "Start Marp" })
vim.api.nvim_create_user_command("RyuStop", M.stop, { desc = "Stop Marp" })
vim.api.nvim_create_user_command("RyuStatus", M.status, { desc = "Show Marp status" })
vim.api.nvim_create_user_command("RyuToggle", M.toggle, { desc = "Toggle Marp (start/stop)" })

return M
