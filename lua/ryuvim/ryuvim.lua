local M = {}

--[[
    Toggles the Marp server.
    @usage
    ```lua
    local marp = require("marp")
    marp.toggle()
    ```
]]
function M.toggle()
	print("Toggles")
end

--[[
    Starts the Marp server.
    @usage
    ```lua
    local marp = require("marp")
    marp.start()
    ```
]]
function M.start()
	print("./main.py")
	-- Construct the command to execute Python with the passed keywords
	-- local command = "python ../../backend/main.py" .. keywords
	-- local command = "python ../../backend/main.py"
	local command = "python ./main.py"

	-- Execute the Python script and capture the output
	local output = vim.fn.system(command)

	-- Print or return the output (for debugging)
	print(output)
end

--[[
    Stops the Marp server.
    @usage
    ```lua
    local marp = require("marp")
    marp.stop()
    ```
]]
function M.stop()
	print("../main.py")
	-- Construct the command to execute Python with the passed keywords
	-- local command = "python ../../backend/main.py" .. keywords
	-- local command = "python ../../backend/main.py"
	local command = "python ../main.py"

	-- Execute the Python script and capture the output
	local output = vim.fn.system(command)

	-- Print or return the output (for debugging)
	print(output)
end

--[[
    Logs the status of the Marp server.
    @usage
    ```lua
    local marp = require("marp")
    marp.status()
    ```
]]
function M.status()
	print("../../main.py")
	-- Construct the command to execute Python with the passed keywords
	-- local command = "python ../../backend/main.py" .. keywords
	-- local command = "python ../../backend/main.py"
	local command = "python ../../main.py"

	-- Execute the Python script and capture the output
	local output = vim.fn.system(command)

	-- Print or return the output (for debugging)
	print(output)
end

return M
