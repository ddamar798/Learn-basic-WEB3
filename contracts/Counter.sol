// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    uint public count = 0;

    function increment() public {
        count += 1;
    }

    function decrement() public {
        count -= 1; 
    }

    function reset() public {
        count = 0;
    }
}
