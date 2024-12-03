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

local file = "day02.txt"
local lines = lines_from(file)

local good_lines = 0

function compute_diffs(nums)
	local diffs = {}
	local previous_num = -1
	for _, v in pairs(nums) do
		if previous_num ~= -1 then
			table.insert(diffs, previous_num - v)
		end
		previous_num = v
	end
	return diffs
end

function table.copy(t)
	local u = {}
	for k, v in pairs(t) do
		u[k] = v
	end
	return setmetatable(u, getmetatable(t))
end

function gen_one(og_diff, idx)
	local new_diff = table.copy(og_diff)
	table.remove(new_diff, idx)
	return compute_diffs(new_diff)
end

function gen_all(og_diff)
	local size = #og_diff
	local diffs = {}
	table.insert(diffs, compute_diffs(og_diff))
	for i = 1, size + 1, 1 do
		table.insert(diffs, gen_one(og_diff, i))
	end
	return diffs
end

function is_diff_safe(diff)
	local is_increasing = diff[1] > 0
	for _, i in pairs(diff) do
		local a = math.abs(i)
		if a > 3 or a == 0 then
			return false
		end
		if i > 0 and is_increasing == false then
			return false
		elseif i < 0 and is_increasing == true then
			return false
		end
	end
	return true
end

function are_diffs_safe(diffs)
	for _, i in pairs(diffs) do
		if is_diff_safe(i) then
			return true
		end
	end
	return false
end

for _, line in pairs(lines) do
	local nums = {}
	for str in line:gmatch("[^%s]+") do
		local current_num = tonumber(str)
		table.insert(nums, current_num)
	end

	if are_diffs_safe(gen_all(nums)) then
		good_lines = good_lines + 1
	end
end

print(good_lines)
