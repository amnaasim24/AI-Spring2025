import random

class LoadBalancerAgent:
    def __init__(self, servers):
        self.servers = servers

    def scan_and_balance(self):
        overloaded_servers = [server for server, load in self.servers.items() if load == "Overloaded"]
        underloaded_servers = [server for server, load in self.servers.items() if load == "Underloaded"]
        
        if overloaded_servers and underloaded_servers:
            print("\nBalancing the load...")
            for i in range(min(len(overloaded_servers), len(underloaded_servers))):
                overloaded_server = overloaded_servers[i]
                underloaded_server = underloaded_servers[i]
                self.servers[overloaded_server] = "Balanced"
                self.servers[underloaded_server] = "Balanced"
                print(f"Moved tasks from {overloaded_server} to {underloaded_server}")
        else:
            print("\nNo balancing needed, either no overloaded or no underloaded servers.")

    def display_system_state(self):
        print("\nUpdated System Load Status:")
        for server, load in self.servers.items():
            print(f"{server}: {load}")

def initialize_system():
    servers = {
        'Server 1': random.choice(['Underloaded', 'Balanced', 'Overloaded']),
        'Server 2': random.choice(['Underloaded', 'Balanced', 'Overloaded']),
        'Server 3': random.choice(['Underloaded', 'Balanced', 'Overloaded']),
        'Server 4': random.choice(['Underloaded', 'Balanced', 'Overloaded']),
        'Server 5': random.choice(['Underloaded', 'Balanced', 'Overloaded'])
    }
    return servers

def main():
    print("Initializing the system...\n")
    servers = initialize_system()
    
    print("Initial System Load Status:")
    for server, load in servers.items():
        print(f"{server}: {load}")
    
    agent = LoadBalancerAgent(servers)

    agent.scan_and_balance()

    agent.display_system_state()

if __name__ == "__main__":
    main()