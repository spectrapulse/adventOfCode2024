---@diagnostic disable: lowercase-global

function file_exists(file)
	local f = io.open(file, "rb")
	if f then
		f:close()
	end
	return f ~= nil
end

function lines_from(file)
	if not file_exists(file) then
		return {}
	end
	local lines = {}
	for line in io.lines(file) do
		lines[#lines + 1] = line
	end
	return lines
end

local file = "input.txt"
local lines = lines_from(file)

local good_lines = 0

for _, line in pairs(lines) do
	local previous_number = tonumber(-1)
	local not_safe = 0
	local increasing = 0
	for str in line:gmatch("[^%s]+") do
		local current_num = tonumber(str)
		if previous_number == -1 then
			previous_number = current_num
		else
			local diff = previous_number - current_num
			local adiff = math.abs(diff)
			if increasing == 0 then
				if current_num > previous_number then
					increasing = 1
				else
					increasing = -1
				end
			end
			if adiff < 1 or adiff > 3 then
				not_safe = 1
				break
			end
			if previous_number < current_num and increasing == -1 then
				not_safe = 1
				break
			elseif previous_number > current_num and increasing == 1 then
				not_safe = 1
				break
			end
			previous_number = current_num
		end
	end
	if not_safe == 0 then
		good_lines = good_lines + 1
	end
end

print(good_lines)
