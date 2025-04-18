// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeviceAuth {
    mapping(address => bool) public registeredDevices;

    event DeviceRegistered(address deviceAddr);
    event DeviceDeregistered(address deviceAddr);

    function registerDevice(address deviceAddr) public {
        registeredDevices[deviceAddr] = true;
        emit DeviceRegistered(deviceAddr);
    }

    function deregisterDevice(address deviceAddr) public {
        registeredDevices[deviceAddr] = false;
        emit DeviceDeregistered(deviceAddr);
    }

    function isDeviceRegistered(address deviceAddr) public view returns (bool) {
        return registeredDevices[deviceAddr];
    }
    
}
