from time import perf_counter

import numpy as np
import scipy.spatial.distance as sp_dist
from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def _get_routes_from_solution(solution, routing, manager):
    """Get vehicle routes from a solution and store them in an array."""
    # Get vehicle routes and store them in a two dimensional array whose
    # i,j entry is the jth location visited by vehicle i along its route.
    routes = []
    route_length = []
    for route_nbr in range(routing.vehicles()):
        route_distance = 0
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, route_nbr)
            route.append(manager.IndexToNode(index))
        routes.append(route)
        route_length.append(route_distance)

    return routes, route_length


def solve_ortools(m: int,  # Number of salesmen
                  n: int = None,  # Number of cities - including the depot
                  coords: np.ndarray = None,  # Depot and cities positions [ 1 + #.cities x 2]
                  time_limit: int = -1,  # seconds
                  solution_limit: int = -1,  # Max. number of initial feasible solution search trials.
                  seed: int = None):  # random seed for generating city positions

    # For supporting the or-tools initial solution heuristics
    # scale the coordinates become integers
    scaler = 100000

    if seed is not None:
        np.random.seed(seed)

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        coords = np.random.uniform(size=(n, 2))
    if coords is not None:
        n = coords.shape[0]  # including the depot

    distance_matrix = sp_dist.cdist(coords, coords, metric='euclidean')
    distance_matrix = (distance_matrix * scaler).round().astype(int)

    # inputs: num_nodes, num_vehicles, depot_node_id
    # Set the first city as the depot, following the tsp convention
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), m, 0)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    # Define cost of each arc.
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(transit_callback_index,
                         slack_max=0,  # no slack
                         capacity=int(1e12),  # vehicle maximum travel distance
                         fix_start_cumul_to_zero=True,  # start cumul to zero
                         name=dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(10000)

    start_time = perf_counter()
    # Setting the first solution heuristics.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.AUTOMATIC
    if time_limit != -1:
        search_parameters.time_limit.seconds = time_limit
    if solution_limit != -1:
        search_parameters.solution_limit = solution_limit

    # Solve the MSTP problem.
    solution = routing.SolveWithParameters(search_parameters)
    end_time = perf_counter()

    routes = None
    route_length = None
    if solution:
        # print_solution(data, manager, routing, solution)
        routes, route_length = _get_routes_from_solution(solution, routing, manager)
        route_length = [el / scaler for el in route_length]

    amplitude = np.amax(route_length) - np.amin(route_length)
    route_length_dict = dict((str(w_id), route_l) for w_id, route_l in enumerate(route_length))
    total_length = np.sum(route_length)
    makespan = np.amax(route_length)

    info = dict()

    # meta info
    info['solution_method'] = 'OR-tools'
    info['n'] = n
    info['m'] = m
    info['coords'] = coords

    # solution and solver conditions
    info['solve'] = True if routing.status() == 1 else False
    info['obj_val'] = makespan  # minmax objective val.
    info['tours'] = {_m: route for _m, route in zip(range(m), routes)}
    info['run_time'] = end_time - start_time

    # additional performance metrics
    info['amplitude'] = amplitude
    info['total_length'] = total_length  # minsum objective val.
    info['tour_length'] = route_length_dict

    n_inactive = 0
    for tl in info['tour_length'].values():
        if tl <= 0.0:
            n_inactive += 1
    info['n_inactive'] = n_inactive
    info['utilization'] = (m - n_inactive) / m

    return info
