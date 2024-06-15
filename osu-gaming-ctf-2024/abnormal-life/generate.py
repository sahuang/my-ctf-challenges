from osrparse import Replay
from osrparse.utils import LifeBarState

flag = "H1D3_UND3R"

r = Replay.from_path("replay.osr")
r.life_bar_graph = []
# H
r.life_bar_graph.append(LifeBarState(0, 0.5))
r.life_bar_graph.append(LifeBarState(0, 1.0))
r.life_bar_graph.append(LifeBarState(0, 0.75))
r.life_bar_graph.append(LifeBarState(10, 0.75))
r.life_bar_graph.append(LifeBarState(10, 0.5))
r.life_bar_graph.append(LifeBarState(10, 1.0))
# 1
r.life_bar_graph.append(LifeBarState(20, 0.7-0.5))
r.life_bar_graph.append(LifeBarState(23, 0.75-0.5))
r.life_bar_graph.append(LifeBarState(23, 0.4-0.5))
r.life_bar_graph.append(LifeBarState(20, 0.4-0.5))
r.life_bar_graph.append(LifeBarState(26, 0.4-0.5))
# D
r.life_bar_graph.append(LifeBarState(40, 0.6-1))
r.life_bar_graph.append(LifeBarState(40, 0.3-1))
r.life_bar_graph.append(LifeBarState(42, 0.34-1))
r.life_bar_graph.append(LifeBarState(44, 0.37-1))
r.life_bar_graph.append(LifeBarState(46, 0.42-1))
r.life_bar_graph.append(LifeBarState(48, 0.46-1))
r.life_bar_graph.append(LifeBarState(48, 0.49-1))
r.life_bar_graph.append(LifeBarState(46, 0.52-1))
r.life_bar_graph.append(LifeBarState(44, 0.56-1))
r.life_bar_graph.append(LifeBarState(42, 0.58-1))
r.life_bar_graph.append(LifeBarState(40, 0.6-1))
# 3
r.life_bar_graph.append(LifeBarState(60, 0.5-1.5))
r.life_bar_graph.append(LifeBarState(63, 0.46-1.5))
r.life_bar_graph.append(LifeBarState(66, 0.42-1.5))
r.life_bar_graph.append(LifeBarState(63, 0.38-1.5))
r.life_bar_graph.append(LifeBarState(60, 0.34-1.5))
r.life_bar_graph.append(LifeBarState(63, 0.3-1.5))
r.life_bar_graph.append(LifeBarState(66, 0.26-1.5))
r.life_bar_graph.append(LifeBarState(63, 0.22-1.5))
r.life_bar_graph.append(LifeBarState(60, 0.18-1.5))
# _
r.life_bar_graph.append(LifeBarState(80, 0.15-2))
r.life_bar_graph.append(LifeBarState(95, 0.15-2))
# U
r.life_bar_graph.append(LifeBarState(110, -0.3+0.35-2.5))
r.life_bar_graph.append(LifeBarState(110, -0.5+0.35-2.5))
r.life_bar_graph.append(LifeBarState(112, -0.52+0.35-2.5))
r.life_bar_graph.append(LifeBarState(114, -0.54+0.35-2.5))
r.life_bar_graph.append(LifeBarState(116, -0.56+0.35-2.5))
r.life_bar_graph.append(LifeBarState(118, -0.56+0.35-2.5))
r.life_bar_graph.append(LifeBarState(120, -0.54+0.35-2.5))
r.life_bar_graph.append(LifeBarState(122, -0.52+0.35-2.5))
r.life_bar_graph.append(LifeBarState(124, -0.5+0.35-2.5))
r.life_bar_graph.append(LifeBarState(124, -0.3+0.35-2.5))
# N
r.life_bar_graph.append(LifeBarState(140, -0.5+0.35-3))
r.life_bar_graph.append(LifeBarState(135, -0.7+0.35-3))
r.life_bar_graph.append(LifeBarState(140, -0.5+0.35-3))
r.life_bar_graph.append(LifeBarState(146, -0.7+0.35-3))
r.life_bar_graph.append(LifeBarState(152, -0.5+0.35-3))
# D
r.life_bar_graph.append(LifeBarState(170, -0.6+0.35-3.5))
r.life_bar_graph.append(LifeBarState(170, -0.9+0.35-3.5))
r.life_bar_graph.append(LifeBarState(173, -0.86+0.35-3.5))
r.life_bar_graph.append(LifeBarState(176, -0.83+0.35-3.5))
r.life_bar_graph.append(LifeBarState(179, -0.78+0.35-3.5))
r.life_bar_graph.append(LifeBarState(182, -0.74+0.35-3.5))
r.life_bar_graph.append(LifeBarState(182, -0.71+0.35-3.5))
r.life_bar_graph.append(LifeBarState(179, -0.68+0.35-3.5))
r.life_bar_graph.append(LifeBarState(176, -0.64+0.35-3.5))
r.life_bar_graph.append(LifeBarState(173, -0.62+0.35-3.5))
r.life_bar_graph.append(LifeBarState(170, -0.6+0.35-3.5))
# 3
r.life_bar_graph.append(LifeBarState(220-25, -0.7-0.22-4))
r.life_bar_graph.append(LifeBarState(223-25, -0.66-0.22-4))
r.life_bar_graph.append(LifeBarState(226-25, -0.62-0.22-4))
r.life_bar_graph.append(LifeBarState(223-25, -0.58-0.22-4))
r.life_bar_graph.append(LifeBarState(220-25, -0.54-0.22-4))
r.life_bar_graph.append(LifeBarState(223-25, -0.5-0.22-4))
r.life_bar_graph.append(LifeBarState(226-25, -0.46-0.22-4))
r.life_bar_graph.append(LifeBarState(223-25, -0.42-0.22-4))
r.life_bar_graph.append(LifeBarState(220-25, -0.38-0.22-4))
# R
r.life_bar_graph.append(LifeBarState(220, -0.85-4.5))
r.life_bar_graph.append(LifeBarState(220, -1.1-4.5))
r.life_bar_graph.append(LifeBarState(220, -0.85-4.5))
r.life_bar_graph.append(LifeBarState(230, -0.9-4.5))
r.life_bar_graph.append(LifeBarState(220, -0.95-4.5))
r.life_bar_graph.append(LifeBarState(229, -1.1-4.5))

r.write_path("abnormal.osr")

for x in range(len(r.life_bar_graph)):
    r.life_bar_graph[x] = LifeBarState(r.life_bar_graph[x].time, r.life_bar_graph[x].life + 5)
r.write_path("fixed.osr")