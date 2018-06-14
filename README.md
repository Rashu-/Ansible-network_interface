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
