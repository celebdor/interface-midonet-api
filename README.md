# MidoNet API Interface

This interface handles the communictation between MidoNet API and its clients.

## Usage

### Provides

Charms providing MidoNet API make use of the provider interface. The events
are

* `{relation_name}.connected` The relation to a client has been established.
  Not that it does not indicate that the service is available yet. The provider
  charm should send its port for the clients using:
      * `send_port(port)`
* `{relation_name}.available` The API is ready for use


### Requires

A client charm can make use of the requires part of the interface to connect to
a charm that provides the MidoNet API.

The following states will be set:

* `{relation_name}.connected` The charm has connected to the API providing one.
  At the promp of this event, the interface waits for connection details
  (port, ip).
* `{relation_name}.available` The API is ready for use

### States

`{{name}}.available`

`{{name}}.connected`
