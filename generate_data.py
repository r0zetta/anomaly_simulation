from cyber_game import *
import time, os, sys, random

num_agents = 3000
step_out = 50

save_dir = "saves"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

episode = 1
while True:
    gs = game_space(num_agents)
    gs.compromised_modifier = random.uniform(1e-4, 1e-6)
    for step in range(2016):
        if step % step_out == 0:
            sys.stdout.write("\r")
            sys.stdout.flush()
            sys.stdout.write("Episode " + str(episode) + " " + "#"*int(step/step_out))
            sys.stdout.flush()
        gs.step()
    filename = os.path.join(save_dir, "episode" + "%04d"%episode + ".json")
    gs.save_events(filename)
    episode += 1


