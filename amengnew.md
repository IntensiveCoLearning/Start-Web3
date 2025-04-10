---
timezone: UTC+8
---




# amengnew

1. 自我介绍
    985本科 英硕 转码选手 英文尚可 目前普通苦逼残废打工人 啥也不是厂flutter开发实习中
    会点Java Python 懂点点AI 主打横向发展
    对web3感兴趣 想要入行 **梦想**远程开发
    希望认识大家 进入圈子 为技术以及梦想奋斗
   
3. 你认为你会完成本次残酷学习吗？
   了解一些web3内容但是有限 看过北大肖老师课程有个基础概念
   春招中可能时间有限但是本着兴趣出发会 完美完成相信自己 
5. 你的联系方式（推荐 Telegram）:
   https://t.me/Benson_meng

## Notes

<!-- Content_START -->

### 2025.03.03

#### web3核心概念

- web3主要采用去中心化的交互方式，无需中心化服务器掌管数据传输而是p to p的对象传输。 
- web3交易以及数据安全依靠**共识机制**默认大多数节点是诚实节点
- 智能合约的引入使得web3能够允许用户与程序直接交互，增加了多种可能👍，例如去中心化应用以及金融
- web3采用多样化商业模型，加密货币代币化微支付等让用户为真实需求买单

#### 数字资产

##### 数字资产种类

- 加密货币
  - Meme币：基于文化以及营销策略，缺乏具体功能 例如狗狗币 狐狸币
  - 公链原生代币：维护网络安全，支付交易费用 例如 XRP TRX
  - 项目代币：应用与去中心化应用， 用于治理和收益分配 LXDAO代币
  - 稳定币：与实际货币挂钩 USDT等
- 非同质化代币(NFTs)， 代表独特东西如艺术品等
- 数字证券：传统金融资产数字版本
- 其他：虚拟身份，数字收藏品等

### 2025.03.04

#### 私钥与助记词

##### 私钥

- 256位0与1组成
- 计算收币地址， 授权交易， 恢复资产
- 非对称加密 公钥加密私钥解密
- 通过加入用户端信号、声音图像增加随机性

##### 助记词

- 12个单词
- 与私钥功能上一致
- 不区分大小写
- 主要目的是方便私钥被记住
- 一组助记词可以派生出多个私钥 用于多个币的存储

### 2025.03.05

#### 钱包

储存加密货币

##### 种类

- 软件钱包：metamask
- 硬件钱包：冷钱包
- 纸钱包

#### 账户模型

传统交易模型采用关系型数据库

UTXO模型未消费的输入输出

#### 以太坊账户

分为外部所有账户和**合约账户**

- 两账户都能接受持有发送ETH及通证
- 与已经部署的智能合约交互
- 外部账户免费 仅能进行ETH和通证交易
- 外部账户由地址、公钥、私钥组成
- 合约账户存在成本 但可以执行多种操作代码如代币转移或创建新合约 只能在接收到交易时发送交易
- 合约账户由智能合约控制

### 2025.03.06

#### 黑话

- bridge:允许独立的区块链通信的协议
- CeFi:中心化金融集中式金融
- DeFi:去中心化金融缩短，在公共区块链上构建无边界、无信任、点对点金融工具的生态系统
- DAO:去中心化自治组织

### 2025.03.07

- 分叉：区块链协议改变，变化较小软分叉。较大硬分叉形成不同规则的区块链

### 2025.03.08

- gameFi:游戏玩家通过视频游戏，了解加密货币趋势
- HFSP:快乐的贫困，不相信加密货币的人

### 2025.03.09

### 2025.03.10

#### 区块链

区块链是分布式账本，对任何人开放，使用哈希算法链接区块

区块链基础技术包括：哈希运算、数字签名、p2p网络、共识算法以及智能合约等

### 2025.03.11

#### 区块链

区块链发送交易需要其他节点的确认，对于签名进行验证。每当发送交易的时候会传给随机临近节点验证

交易完成会进行传递，直到所有区块收到消息

矿工挖出区块获得记账权会广播网络

##### 区块链透明以及不变性

- 如果要篡改一个交易就需要篡改其父节点所有，需要庞大计算

- 或者拥有全网50%算力利用共识机制篡改，当有足够多的节点参与是不可能的

- 默克尔树：通过多个交易计算哈希，两个合成一个，单个继续向上，最后合成根节点，即为一棵默克尔树

- 共识算法是一种用于在分布式进程或系统之间达成关于单个数据值的协议的技术，其主要是用来解决区块链的全民记账信任问题。常见的共识算法有

  - 工作量证明的共识算法：这类算法主要通过节点进行大量计算才能够解答，为了保证节点愿意在如此的计算中延续区块的成长会进行一定的奖励如比特币
  - P O的凭证类共识算法：由于工作量证明的公式算法在延续区块链成长的操作上耗费了庞大的计算资源，同时并没有任何意义，所以出现了工作量证明算法的替代者PO类算法。其主要思想是根据节点的某个属性提供某种凭证来进行节点的初始化。
  - 拜占庭容错类算法：相比于前面两种算法拜占庭容错算法更加倾向于协商处一个新的区块进行验证，而并不是进行一个竞争。其主要的思想是选出一个领导者来接收和排序区块链提示中的交易，并产生区块，以递交其他节点进行验证，通过举手表决的形式来产生现在区块。其主要需要具有完备的**安全性证明**，以保证群体中恶意节点数量不超过三分之一诚实节点的账本保持一致。
  - 结合可信执行环境的共识算法：上述三种算法都使用了纯软件的固执算法，除此以外还有一些结石结合硬件的公式算法，例如利用可信执行环境的软硬件结合的公式算法

  

### 2025.03.12

#### layer1

如果区块链是城市，那么layer1就是它的地基和基础设施

其包括交易的处理、验证和记录

从数字货币开始流行的时候人们就开始探索如何在没有中央权威的情况下安全的记录交易

技术核心是：**共识机制**

主要的共识机制包括：pow, pos

网络结构：构建数字交通系统

##### layer1实际应用

公链：就像给所有人开放的大道，任何人都可以在这里交易

公链代表：比特币，以太坊， 莱特币

公链挑战：可扩展性，能源消耗

---

联盟链：介于公链和私链的区块链，用于特定群体信任与合作的桥梁

应用：R3 Corda：金融服务中的联盟链

Quorum摩根大通开发，基于以太坊的企业焦点区块链平台

优势：高效率低成本，隐私保护

---

私链：被高墙围绕的私人领地，访问参与得到了严格控制

特点：受限访问、效率更高、定制化控制

应用场景：企业数据管理，内部纪录保持，供应链跟踪

### 2025.03.13

#### layer2

主要解决区块链的普及状态下交易量激增、网络拥堵以及交易费用上升的问题，提供更快更便宜的交易。

种类：

- 状态通道：允许两方在纞下进行多次交易，然后将结果提交到主链
- 侧链：与主链并行运行的独立链，允许资产和数据在两者之间转移
- Plasma:是一个框架允许创建多个子链，每个子链都与主链相互作用
- Rollups:通过在链下处理交易，并将其结果打包的主链来提高效率

#### 跨链桥

允许在不同区块链之间转移资产和数据的技术

多个区块链平台的出现，互操作性成为问题

种类：

- 简单支付验证桥：验证另一个链上的交易
- 联邦桥：由验证者管理，负责转移资产
- TSS:使用多方计算来创建跨链交易的签名

#### 重要性

提供扩展以及误操作以及创新的性能，为区块链的基础叠加了一层新型的层级

### 2025.03.16

Layer2进阶

增加传输效率有两种方法

- 增加区块容量
- 减少出块时间，提供更多区块

当时有些方法比较具有危险性

- 减少父节点数量：可能违背去中心化初衷
- 使用特殊机制提升

### 2025.03.17

不可能三角：去中心化、安全性、可拓展性

去中心化需要所有父节点存储所有数据到区块中，但这违背了可拓展性。这三种需要权衡

可以通过引入额外的层进行业务接触耦合并减轻原有层的负担

layer2可以分担第一层网络的负载并实现可拓展性

### 2025.03.18

#### DAO 去中心化组织

规定写在智能合约中

任何成员都可以提交提案，对别人的提案发起挑战或投票

共识机制以及落地执行机制都被写入了开源智能合约中，而智能合约被部署在的攻略上，一旦达成共识，任何一方或小团体无法篡改治理流程

具体工作：调整D pp参数提交体验，并进行讨论管理协议的资金，决定协议的长期路线图，制定协议的分成

#### NFT

非同质化代币，同比特币以太坊不同的是

每个NFT都不可分割，万物皆可，完全控制权、确权成本低，无限想象空间

DYOR - Do you own research

决定购买前需要考虑清楚为什么购买

尽可能了解这一切，评估当前价格是否合理

### 2025.03.20

#### 协议层

区块链网网络

包括链基础以及layer2

跨链桥

链接不同区块链网络的协议

Synapse protocol

#### 基础设施

##### 节点服务

链接区块和DAPP的桥梁，提供读或写到区块链网络的服务器

##### 网络存储

其中心化存储服务商 IPFS Areave Filecoin

##### 数据服务

原始数据索引分析归档

etherscan

#### 应用层

##### DAO

##### 钱包

##### 金融

##### 游戏

##### NFT

##### 社交

#### 其他领域

智能合约 应用协议 质押等ß

### 2025.03.21

Web3 安全问题

钓鱼攻击

恶意签名攻击

盗取私钥

虚拟地址攻击 剪贴板木马 历史交易 假地址

貔貅盘 蜜罐代币

### 2025.03.22

meme币

Dogecoin shiba inu

被网络流行趋势所影响，依靠于区块链技术，许多的meme币是纯粹的交易币种没有实际价值。

它们是非常脆弱的，没有实际依靠，基本都是价值炒作

一些国家已经将其进行规范化，





<!-- Content_END -->
