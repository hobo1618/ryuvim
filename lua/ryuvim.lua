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
	print("Starting")
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
	print("Stopping")
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
	print("Status")
end

return M
