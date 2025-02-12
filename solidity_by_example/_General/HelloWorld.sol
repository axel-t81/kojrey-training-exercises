// Lesson:
// pragma specifies the compiler version of Solidity.

// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.24 and less than 0.9.0
pragma solidity ^0.8.24;

// My notes:
// Look at this, it all starts with the 'contract' reserved word
contract HelloWorld {
    string public greet = "Hello World";
}
