## EUMETSAT daemon

`eumetsatd` is a Pyro frontend that crops and estimates the IR opacity from the EUMETSAT images.

`eumetsat` is a commandline utility that shows the current status.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-eumetsat-server`, the `eumetsatd` must be enabled using:
```
sudo systemctl enable eumetsatd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start eumetsatd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9013/tcp --permanent
sudo firewall-cmd --reload
```
