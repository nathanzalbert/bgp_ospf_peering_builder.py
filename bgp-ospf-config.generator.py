import ipaddress


def get_positive_number(prompt):
    """Ask the user for a positive whole number."""

    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def generate_ip_sequence(starting_ip, number_of_neighbors):
    """
    Generate sequential IP addresses.

    Example:
    Starting IP: 10.0.0.2
    Results:
    10.0.0.2
    10.0.0.3
    10.0.0.4
    """

    start_ip = ipaddress.ip_address(starting_ip)

    return [
        str(start_ip + number)
        for number in range(number_of_neighbors)
    ]


def build_bgp_config():
    """Create a Cisco BGP configuration with multiple neighbors."""

    print("\n--- BGP Neighbor Configuration Builder ---")

    local_as = input("Enter the local AS number: ").strip()

    starting_neighbor_ip = input(
        "Enter the first neighbor IP address: "
    ).strip()

    number_of_neighbors = get_positive_number(
        "How many BGP neighbors do you want to create? "
    )

    same_remote_as = input(
        "Will all neighbors use the same remote AS? (yes/no): "
    ).strip().lower()

    neighbors = generate_ip_sequence(
        starting_neighbor_ip,
        number_of_neighbors
    )

    configuration = [
        f"router bgp {local_as}",
        " bgp log-neighbor-changes"
    ]

    if same_remote_as in ["yes", "y"]:
        remote_as = input(
            "Enter the remote AS number for all neighbors: "
        ).strip()

        for neighbor_ip in neighbors:
            configuration.append(
                f" neighbor {neighbor_ip} remote-as {remote_as}"
            )

    else:
        starting_remote_as = get_positive_number(
            "Enter the first remote AS number: "
        )

        for index, neighbor_ip in enumerate(neighbors):
            remote_as = starting_remote_as + index

            configuration.append(
                f" neighbor {neighbor_ip} remote-as {remote_as}"
            )

    print("\nAdd a network that BGP should advertise.")

    network_address = input(
        "Enter the network address, or press Enter to skip: "
    ).strip()

    if network_address:
        subnet_mask = input("Enter the subnet mask: ").strip()

        configuration.append(
            f" network {network_address} mask {subnet_mask}"
        )

    return "\n".join(configuration)


def build_ospf_config():
    """Create a Cisco OSPF configuration with multiple networks."""

    print("\n--- OSPF Network Configuration Builder ---")

    process_id = input("Enter the OSPF process ID: ").strip()
    router_id = input("Enter the router ID: ").strip()
    area = input("Enter the OSPF area number: ").strip()

    number_of_networks = get_positive_number(
        "How many OSPF-connected networks do you want to add? "
    )

    configuration = [
        f"router ospf {process_id}",
        f" router-id {router_id}"
    ]

    for number in range(1, number_of_networks + 1):
        print(f"\nOSPF network {number}")

        network_address = input(
            "Enter the network address: "
        ).strip()

        wildcard_mask = input(
            "Enter the wildcard mask: "
        ).strip()

        configuration.append(
            f" network {network_address} "
            f"{wildcard_mask} area {area}"
        )

    return "\n".join(configuration)


def save_configuration(configuration, protocol):
    """Save the generated configuration to a text file."""

    save_choice = input(
        "\nSave the configuration to a text file? (yes/no): "
    ).strip().lower()

    if save_choice not in ["yes", "y"]:
        return

    filename = f"{protocol.lower()}_neighbor_configuration.txt"

    try:
        with open(filename, "w", encoding="utf-8") as config_file:
            config_file.write(configuration)

        print(f"\nConfiguration saved as {filename}")

    except OSError as error:
        print(f"\nThe file could not be saved: {error}")


def main():
    """Run the routing configuration builder."""

    print("=" * 50)
    print(" Cisco BGP and OSPF Neighbor Configuration Builder")
    print("=" * 50)

    print("\nChoose a routing protocol:")
    print("1. BGP")
    print("2. OSPF")

    choice = input("\nEnter 1 or 2: ").strip()

    try:
        if choice == "1":
            protocol = "BGP"
            configuration = build_bgp_config()

        elif choice == "2":
            protocol = "OSPF"
            configuration = build_ospf_config()

        else:
            print("\nInvalid selection. Please enter 1 or 2.")
            return

    except ValueError as error:
        print(f"\nInvalid IP address: {error}")
        return

    print(f"\n--- Generated {protocol} Configuration ---")
    print(configuration)

    save_configuration(configuration, protocol)


if __name__ == "__main__":
    main()