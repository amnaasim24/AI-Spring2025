import random

components = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
vulnerability_states = ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"]

system_state = {component: random.choice(vulnerability_states) for component in components}

def display_system_state(state, message):
    print(f"\n{message}:")
    for component, status in state.items():
        print(f"{component}: {status}")

display_system_state(system_state, "Initial System State")

class UtilityBasedSecurityAgent:
    def __init__(self):
        self.resources = {
            "free_patches": 3,
            "premium_service": False
        }

    def calculate_utility(self, component, status):
        """
        Calculate the utility of patching a vulnerability.
        Utility is higher for High Risk Vulnerabilities but requires premium service.
        Low Risk Vulnerabilities have lower utility but are free to patch.
        """
        if status == "Low Risk Vulnerable":
            return 1
        elif status == "High Risk Vulnerable":
            return 10
        return 0

    def patch_vulnerability(self, component, status):
        """
        Patch a vulnerability based on its type and available resources.
        """
        if status == "Low Risk Vulnerable" and self.resources["free_patches"] > 0:
            system_state[component] = "Safe"
            self.resources["free_patches"] -= 1
            print(f"{component}: Low Risk Vulnerability patched. Free patches remaining: {self.resources['free_patches']}")
        elif status == "High Risk Vulnerable":
            if self.resources["premium_service"]:
                system_state[component] = "Safe"
                print(f"{component}: High Risk Vulnerability patched using premium service.")
            else:
                print(f"{component}: High Risk Vulnerability detected. Premium service required to patch.")
        else:
            print(f"{component}: No action taken.")

    def scan_and_patch(self, system_state):
        """
        Scan the system and patch vulnerabilities based on utility and available resources.
        """
        print("\nScanning the system and patching vulnerabilities...")
        sorted_components = sorted(
            system_state.keys(),
            key=lambda x: self.calculate_utility(x, system_state[x]),
            reverse=True
        )
        for component in sorted_components:
            status = system_state[component]
            if status != "Safe":
                self.patch_vulnerability(component, status)

agent = UtilityBasedSecurityAgent()
agent.scan_and_patch(system_state)

display_system_state(system_state, "Final System State")