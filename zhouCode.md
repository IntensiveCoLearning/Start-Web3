---
timezone: Asia/Shanghai
---

# zhouCode

1. zhouCode，web3新手，狠狠地学习！
2. 你认为你会完成本次残酷学习吗？会
3. 你的联系方式（[zhouG1n](https://t.me/zhouG1n)）

# Notes

<!-- Content_START -->

## 2025.03.03

阅读：[web3-general-manual/chapter2/2.3-layer1.md at main · lxdao-official/web3-general-manual](https://github.com/lxdao-official/web3-general-manual/blob/main/chapter2/2.3-layer1.md)

Layer1：

**概念**：所有区块链活动发生的地方，包括交易的处理、验证和记录。

**技术**：共识机制「工作量证明（PoW）、权益证明（PoS）」、网络结构：有的网络设计重视速度和效率，而有的则更加强调安全和去中心化。

### Layer1 的实际应用

**公链**：任何人都可以参与验证交易，加强了网络的去中心化和透明性。

**联盟链**：介于公链和私链之间的区块链形式，它在特定的组织群体之间建立起了信任和合作的桥梁。

**联盟链的应用**

R3 Corda：金融服务行业中的联盟链，旨在提高银行间交易的效率。

Hyperledger Fabric：由Linux基金会发起，用于企业级区块链解决方案。

Quorum：由摩根大通开发，是一个基于以太坊的企业焦点的区块链平台。

**联盟链优势**：高效率，低成本，更好的隐私保护。

**私链**：受限访问、更高的效率、定制化的控制

**私链应用场景**：企业数据管理、内部记录保持、供应链跟踪、私链的挑战、安全性考量

## 2025.03.04

阅读：[web3-general-manual/chapter2/2.4-layer2_and_cross-chain_bridge.md at main · lxdao-official/web3-general-manual](https://github.com/lxdao-official/web3-general-manual/blob/main/chapter2/2.4-layer2_and_cross-chain_bridge.md)

用户增多，为了提高区块链扩展性和效率，但是不改变底层结构，所以出现了Layer2

Layer2提供更快，更便宜的交易，解决区块链交易量激增导致网络拥堵和Gas增加的情况

分类：

**状态通道**：双方链下多次交易，最后把结果提交到主链。

**侧链**：与主链并行且独立，资产和数据可以在两者之间转移。

**Plasma**：一个框架，可以创建多个子链，每个子链与主链相互作用。

**Rollups**：通过链下交易，然后结果打包到主链提高效率。

> **疑问**：状态通道看起来和Rollups是一样的，有具体区别吗？
>
> GPT老师回答：
> **状态通道**特点在于点对点链下多次交易，需要固定参与者，加入新用户要重新打开通道。需要所有参与者保持在线，否则可能面临资金被作恶者盗取的风险。
>
> **Rollups**非点对点，分为**ZK-Rollups** 和 **Optimistic Rollups**
>
> 其中**ZK-Rollups**最终提交一个**零知识证明**到主链。主链只需要验证这个证明，不需要检查具体交易。交易验证速度快，但是生成零知识证明计算量大，对算力要求高。
>
> 而**Optimistic Rollups**交易默认有效，并批量提交到主链，设置挑战期（通常为7天），如果有人发现无效交易，可以提交欺诈证明。优点为计算成本比ZK-Rollups低，更容易兼容智能合约，但是由于有争议期，提款时间较长。

**跨链桥**

定义：允许在不同区块链之间转移资产和数据的技术。

为什么需要跨链桥？

区块链平台越来越多，急需相互操作性

种类：

**简单支付验证（SPV）桥**：通过验证另一个链上的交易来工作。

**联邦桥**：由一组验证者管理，负责在两个链之间转移资产。

**TSS（阈值签名方案）桥**：使用多方计算来创建垮链交易的签名。

**总结**

Layer2扩展链，分摊主链的压力

跨链桥实现不同区块链之间的资产和数据流动

<!-- Content_END -->
