# Network interface configuration

Ansible role that configures the physical, layer 2 and layer 3 attributes for a network device interface. For more specific interface config like hsrp, mlag, ospf and so on use the other roles. 

The configuration of the role is done so that it shouldn't be necessary to modify the role for any configuration.
All settings can be configured by changing role parameters or by declaring new config as variable.

Please report any issues or send PR.

nxos specific: For nxos_interface - when you default a loopback int, the admin state toggles on certain versions. For vlan interface you need feature interface-vlan enabled. 
nxos_l2_interface - For layer2 ports, the VLANs have to exist on the device before the interfaces can be configured with a VLAN.
nxos_vrf_interface - vrf needs to exist on device before configured on a interface. Removing a vrf from an interface will remove all L3 attributes. vrf is not read from an interface until the IP is configured on the interface. 

## Examples

```yaml
---

- name: Example of how to configure an eth interface physical settings and sets mode to layer2
  hosts: switches
    vars:
      interfaces:
        Ethernet:
          1/1:
            description: "*** To server 1 ***"
            admin_state: up
            state: present
            duplex: full
            speed: 10000
            mode: layer2
  roles:
    - ansible-network_interface

- name: Example of how to configure an interface layer2 trunk
  hosts: switches
    vars:
      interfaces:
        port-channel:
          101:
            switchport:
              state: present
              mode: trunk
              trunk_allowed_vlans: 11-15
              native_vlan: 99
  roles:
    - ansible-network_interface
    
- name: Example of how to configure an interface as part of vrf
  hosts: switches
    vars:
      interfaces:
        Vlan:
          101:
            vrf:
              name: production
              state: present
  roles:
    - ansible-network_interface

- name: Example of how to configure an interface layer3 settings
  hosts: switches
    vars:
      interfaces:
        Vlan:
          101:
            ip:
              state: present
              address:
                ipv4_address: 192.0.2.1/24
                ipv6_address: 2001:DB8::1/64
  roles:
    - ansible-network_interface

- name: Example of how to configure an interface layer3 settings with dot1q
  hosts: switches
    vars:
      interfaces:
        Ethernet:
          1/1.23:
            ip:
              state: present
              address:
                ipv4_address: 192.0.2.1/24
              dot1q: 23
  roles:
    - ansible-network_interface

# Most of the options above can be combined

- name: Example of how to configure an loopback, port-channel and ethernet interface
  hosts: switches
    vars:
      interfaces:
        Ethernet:
          1/1.23:
            description: "*** uplink ***"
            admin_state: up
            state: present          
            ip:
              state: present
              address:
                ipv4_address: 192.0.2.1/25
              dot1q: 23
            vrf:
              name: staging
              state: present
        loopback:
          0:
            description: "*** ospf loopback ***"
            admin_state: up
            mode: layer3
            state: present
            vrf:
              name: prod
              state: present
            ip:
              address:
                ipv4_address: 192.0.2.128/32
        port-channel:
          11:
            description: "*** link to host A ***"
            admin_state: up
            mode: layer2
            state: present
            switchport:
              state: present
              mode: trunk
              trunk_allowed_vlans: 13-15
  roles:
    - ansible-network_interface

```

## Role variables

```yaml
# Define the attirbutes to be configured on interfaces (see README for examples)
interfaces: { }
```


## License

Apache


## Author

Dan Murarasu
