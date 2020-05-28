from cyber_game import *
import time, os, sys

num_agents = 3000

gs = game_space(num_agents)
for n in range(10000):
    os.system("clear")
    msg = "\n"
    msg += gs.print_whole_network()
    msg += "\n"
    msg += " " + gs.print_chrono() + "\n"
    msg += " Total anomalies: " + str(gs.total_anomalies) + "\n"
    top_inter = gs.get_top_interactions()
    #for x, c in top_inter.most_common(20):
    #    msg += " " + gs.print_node_status(x) + ": " + str(c) + " " + gs.print_interactions(x) + "\n"
    msg += " Admins: " + " ".join([gs.print_user_status(x) for x in gs.admin_ids]) + "\n"
    msg += " Servers: " + " ".join([gs.print_node_status(x) for x in gs.servers]) + "\n"
    msg += " Compromised nodes: " + " ".join([gs.print_node_status(x) for x in gs.get_compromised_nodes()]) + "\n"
    msg += " Compromised users: " + " ".join([gs.print_user_status(x) for x in gs.get_compromised_users()]) + "\n"
    msg += " All interactions: " + str(len(gs.all_interactions)) + "\n"
    msg += " Attacker interactions:\n"
    #msg += " " + gs.print_attacker_interactions()
    print(msg)
    if n > 0 and n % 50 == 0:
        gs.save_interactions("interactions.csv")
        gs.save_events("events.json")
    gs.step()
    time.sleep(0.1)

# Notes on additional things to add:
#
# Track infection vector such that we can compare it to graphs extracted by each host
# Add "attacker" intent
# Different attack patterns, such as APT, ransomware, etc
# Bias toward lateral movement
# Bias toward owning a server
# Incident reports from cert organizations

# Logon type: local interactive login versus remote
# Outgoing connections are always via a proxy
# If compromised, the RAT may attempt to directly contact external addresses, which would fail
# Workstation machine logging into a workstation machine should be really rare
# Jumpbox == VPN entry point. This would look like a server. More connections from this machine to other machines, and admin activities, etc.
# One web proxy, VPN entry point, etc. per region
# Subnets may be segregated for security reasons (DMZ, test network, orange network, etc.)
# User profiles - developer, office workers
# Server profiling - developers connect to git, jira, etc. financial users connect to financial system
# Incoming connections should only come from a few machines (DC, security provider, etc.)
# Servers should have different user scheme

# User behaviour modelling, countercept
