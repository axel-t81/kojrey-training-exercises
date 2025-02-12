// Title: First App
// Lesson:
// Here is a simple contract that you can get, increment and decrement the count store in this contract.

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Counter {
    // the count variable
    uint256 public count;

    // function to get the current count
    function get() public view returns (uint256) {
        return count;
    }

    // function to increment by 1
    function inc() public {
        count += 1;
    }

    // function to decrement by 1
    function dec() public {
        // Note: This function will fail if count = 0
        // Because uint can't be negative, only int can. A common feature in 'typed langauges'
        // uint = unsigned integer, and int = signed integer
        count -= 1;
    }
}
