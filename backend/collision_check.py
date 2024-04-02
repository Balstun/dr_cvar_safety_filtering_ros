from backend.dynamic_vehicles import RectangularKinematicBicycle

def distance_to_collision(ego_veh: RectangularKinematicBicycle, obst_veh: RectangularKinematicBicycle):
    # Collect vehicle geometry data
    ego_center = ego_veh.center
    ego_width = ego_veh.width
    ego_height = ego_veh.height
    obst_center = obst_veh.center
    obst_width = obst_veh.width
    obst_height = obst_veh.height

    # Calculate axial distance to collision
    distance = max(abs(ego_center[0] - obst_center[0]) - (ego_width + obst_width)/2,
                   abs(ego_center[1] - obst_center[1]) - (ego_height + obst_height)/2)

    return distance
