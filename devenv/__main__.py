import pulumi
import pulumi_hcloud as hcloud

network = hcloud.Network("devenv", ip_range="10.0.0.0/16")
network_subnet = hcloud.NetworkSubnet(
    "devenv-main",
    type="cloud",
    network_id=network.id,
    network_zone="eu-central",
    ip_range="10.0.1.0/24",
)
for idx in range(3):
    server = hcloud.Server(
        f"node-{idx}",
        server_type="cx11",
        image="ubuntu-22.04",
        location="fsn1",
        ssh_keys=[],
        labels={
            "env": "dev",
            "id": f"{idx}",
            "group_docker": "",
        },
        networks=[
            hcloud.ServerNetworkArgs(
                network_id=network.id,
            )
        ],
        user_data="""#cloud-config
users:
  - name: ansible
    sudo: ALL=(ALL) NOPASSWD:ALL
    no_user_group: true
    shell: /bin/bash
    ssh_authorized_keys:
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINN6b1TpL87pWbJd9spaHlTNmIUCFKeH+xU5S2/yT2Gb
""",
        opts=pulumi.ResourceOptions(depends_on=[network_subnet]),
    )
