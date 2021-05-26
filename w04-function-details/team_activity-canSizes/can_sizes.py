import math


def main():
	print()
	can_list_names = ['#1 Picnic', '#1 Tall', '#2 Canny', '#2.5 Can', '#3 Cylinder',
					  '#5 Canny', '#6Z Can', '#8Z short', '#10 Canny', '#211 Can', '#300 Can', '#303 Can']
	can_list_radius = [6.83, 7.78, 8.73, 10.32, 10.79,
					   13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
	can_list_height = [10.16, 11.91, 11.59, 11.91, 17.78,
					   14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
	can_list_cost = [0.28, 0.43, 0.45, 0.61, 0.86,
					 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

	can_list = make_can_list(
		can_list_names, can_list_radius, can_list_height, can_list_cost)

	volumes = cylinder_volume(can_list_radius, can_list_height)
	surface_areas = cylinder_surface_area(can_list_radius, can_list_height)
	storage_efficiencies = can_storage_efficiency(volumes, surface_areas)
	cost_efficiencies = can_cost_efficiency(volumes, can_list_cost)

	best_se = 0.0
	best_ce = 10000.0
	for j in range(len(can_list)):
		for k in range(len(can_list[j])):
			if k == 0:
				name = can_list[j][k]
			elif k == 1:
				radius = can_list[j][k]
			elif k == 2:
				height = can_list[j][k]
			elif k == 3:
				cost = can_list[j][k]
		volume = math.pi * radius ** 2 * height
		area = 2 * math.pi * radius * (radius + height)
		cost_eff = volume / cost
		storage_eff = volume / area

		if storage_eff > best_se:
			best_se = storage_eff
			best_se_name = name

		if cost_eff < best_ce:
			best_ce = cost_eff
			best_ce_name = name
	
	print(f'BEST se: {best_se:.2} from {best_se_name}')
	print(f'BEST ce: {best_ce:.6} from {best_ce_name}')

	print('\n> SECOND FOR <')
	for name, radius, height, cost in can_list:
		print (name, radius, height, cost)

	print('\n> PRINT RESULTS <')
	print("Can Name \tSE \tCE")
	for i in range(len(can_list_names)):
		print(
			f'{can_list_names[i]} \t{storage_efficiencies[i]:.2} \t{cost_efficiencies[i]:.6}')

def make_can_list(can_list_names, can_list_radius, can_list_height, can_list_cost) -> list:
	can_list = []
	can = []
	for i in range(len(can_list_names)):
		can.append(can_list_names[i])
		can.append(can_list_radius[i])
		can.append(can_list_height[i])
		can.append(can_list_cost[i])
		can_list.append(list(can))
		can.clear()
	return can_list


def cylinder_volume(radiuses, heights):
	i = 0
	volumes = []
	while i < len(radiuses):
		volume = math.pi * radiuses[i] ** 2 * heights[i]
		volumes.append(volume)
		i = i + 1
	return volumes


def cylinder_surface_area(radiuses, heights):
	i = 0
	areas = []
	while i < len(radiuses):
		area = 2 * math.pi * radiuses[i] * (radiuses[i] + heights[i])
		areas.append(area)
		i = i + 1
	return areas


def can_cost_efficiency(can_volumes, can_list_cost):
	i = 0
	cost_efficiencies = []
	while i < len(can_volumes):
		ce = can_volumes[i] / can_list_cost[i]
		cost_efficiencies.append(ce)
		i = i + 1
	return cost_efficiencies


def can_storage_efficiency(volumes, surface_areas):
	i = 0
	storage_efficiencies = []
	while i < len(volumes):
		se = volumes[i] / surface_areas[i]
		storage_efficiencies.append(se)
		i = i + 1
	return storage_efficiencies


main()
