import random

class SecurityAgent:
    def __init__(self, components):
        self.components = components
        self.patched = []

    def system_scan(self):
        print("Scanning System:")
        for component, status in self.components.items():
            if status == "Vulnerable":
                print(f"- {component}: Vulnerable (Warning: Needs patching)")
                self.patched.append(component)
            else:
                print(f"- {component}: Safe (Success: No issues)")

    def patch_vulnerabilities(self):
        print("\nPatching Vulnerabilities:")
        for component in self.patched:
            if self.components[component] == "Vulnerable":
                self.components[component] = "Safe"
                print(f"- Patching {component}: Safe")
        print("\nAll vulnerable components have been patched.\n")

    def final_check(self):
        print("Final System Check:")
        for component, status in self.components.items():
            print(f"{component}: {status}")
        if all(status == "Safe" for status in self.components.values()):
            print("\nAll components are now safe and secure. No vulnerabilities remain.")

def initialize_system():
    components = {
        'A': random.choice(['Safe', 'Vulnerable']),
        'B': random.choice(['Safe', 'Vulnerable']),
        'C': random.choice(['Safe', 'Vulnerable']),
        'D': random.choice(['Safe', 'Vulnerable']),
        'E': random.choice(['Safe', 'Vulnerable']),
        'F': random.choice(['Safe', 'Vulnerable']),
        'G': random.choice(['Safe', 'Vulnerable']),
        'H': random.choice(['Safe', 'Vulnerable']),
        'I': random.choice(['Safe', 'Vulnerable'])
    }
    return components

def main():
    print("Initializing the system...\n")
    components = initialize_system()
    
    print("Initial System Check:")
    for component, status in components.items():
        print(f"{component}: {status}")
    

    agent = SecurityAgent(components)

    print("\nSystem Scan:")
    agent.system_scan()

    agent.patch_vulnerabilities()

    agent.final_check()

if __name__ == "__main__":
    main()