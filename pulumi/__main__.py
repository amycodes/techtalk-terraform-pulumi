import pulumi
import pulumi_digitalocean as digitalocean

# Create a new Web Droplet in the nyc2 region
pulumi_droplet = digitalocean.Droplet("techtalk-pulumi",
    image="ubuntu-22-04-x64",
    region="sfo3",
    size="s-4vcpu-8gb")
web_firewall = digitalocean.Firewall("webFirewall",
    droplet_ids=[pulumi_droplet.id],
    inbound_rules=[
        digitalocean.FirewallInboundRuleArgs(
            protocol="tcp",
            port_range="22",
            source_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
    ],
    outbound_rules=[
        digitalocean.FirewallOutboundRuleArgs(
            protocol="tcp",
            port_range="53",
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
        digitalocean.FirewallOutboundRuleArgs(
            protocol="udp",
            port_range="53",
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
        digitalocean.FirewallOutboundRuleArgs(
            protocol="icmp",
            destination_addresses=[
                "0.0.0.0/0",
                "::/0",
            ],
        ),
    ])