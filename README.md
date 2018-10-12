## EUMETSAT IR Opacity daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/eumetsatd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/eumetsatd)

Part of the observatory software for the Warwick La Palma telescopes.

`eumetsatd` is a Pyro frontend that estimates the IR opacity from the EUMETSAT image published by sat24.com

`eumetsat` is a commandline utility that shows the current status.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

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
