// SPDX-License-Identifier: MIT\n// Beta Power placeholder
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BetaPower is ERC20 {
    mapping(address => mapping(string => uint256)) public reputation;

    constructor() ERC20("BetaPower", "BETA") {
        _mint(msg.sender, 1500000000 * 10 ** decimals()); // 1.5B supply
    }

    function addReputation(address user, string memory category, uint256 score) external {
        reputation[user][category] += score; // e.g., "family" for age votes
    }

    function rewardUser(address user, string memory category, uint256 amount) external {
        reputation[user][category] += amount;
        _mint(user, amount * 10 ** decimals());
    }
}
