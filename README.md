# ROV ROS Workspace

Three-role structure:
- Path Planning: src/rov_path_planner
- System Parameters and Comms: src/rov_comms_params, src/rov_bringup
- Computer Vision and Data: src/rov_vision
- Shared Interfaces: src/rov_interfaces

## Interface Contracts (Draft)
- Vision -> Planner: /rov/vision/obstacles (occupancy or obstacle list + timestamp)
- Comms/Params -> All: /rov/system/mode and ROS parameters (grid resolution, safety margin, planner rate)
- Planner -> Comms/Control: /rov/planner/path (ordered waypoints + replan status)
