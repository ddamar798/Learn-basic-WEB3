// Versi compiler
pragma solidity ^0.8.0;

// Nama kontrak
contract HelloWorld {
    string public greet = "Hello, Web3!";

    function changeGreeting(string memory _newGreet) public {
        greet = _newGreet;
    }
}