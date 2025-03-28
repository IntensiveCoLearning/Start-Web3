---
timezone: UTC+8
---

> 请在上边的 timezone 添加你的当地时区(UTC)，这会有助于你的打卡状态的自动化更新，如果没有添加，默认为北京时间 UTC+8 时区


# 你的名字
bulin
1. 自我介绍
  hello，我是bulin，希望加入这次残酷共学获得一点提升
2. 你认为你会完成本次残酷学习吗？
  我会尽力！
3. 你的联系方式（推荐 Telegram）
  @MadoMosel

## Notes

<!-- Content_START -->

### 2025.03.03
Chapter1：
Web3不是来替代web2，而是对web2的一种补充。

隐私也是资产，web3的核心在于：用户拥有自己数据隐私的所有权，不必再寄希望于平台的隐私保护，而是依赖于确定的代码逻辑来实现协议和功能。没有了第三方的隐私滥用，数据将更加公平公正，数据将由参与的节点来共同维护。同样，去除了作为中间商的第三方，消费者和生产者双方可以直接参加到交易之中，进行更贴合需求和成本更低的沟通。

web3和web2的最大区别就在于数据的中心化。用户可以决定自己的个人数据被如何使用，无需授权给第三方，只需要与特定的智能合约交互就可以满足自己的需求。


chapter2：
区块链技术：哈希函数，公私钥对，数字签名，零知识证明（ZCash币），多重签名
区块链的各项特性是由什么技术来实现的？
去中心化：分布式网络中，一个节点即是服务器，也是客户端，它接受其他节点的请求，同时也享受其他节点的服务。在分布式的网络中，数据的验证、传播等功能都不依赖于某一个中心节点，而是由参与整个网络的节点共同维护。
防篡改：由默克尔树和哈希指针来确保，当有人企图篡改某一个区块的数据时，变化的数据值会使敏感的哈希值一同改变，同时影响后续整条链的数据。若想篡改一笔交易，就必须篡改后续的所有哈希值，而这是一项巨大的工作量，除非你掌握超过一半节点的算力，攻击才可能成功。而在一个足够大的区块链网络中，掌握一半的算力几乎是不可能的。
透明性：区块一旦上链，数据将对所有人可见

共识算法的分类：
Pow（挖矿类算法）：节点完成难题获得记账权
  特点：1.难题具有难以解答，但却容易验证的特点。2.一个节点解决了难题这个消息的传播速度，大于其他节点计算难题的速度。3.资源浪费。
Po*：
  特点：减少了出块开销，但凭证是更加中心化的，有悖去中心化的思想。
BFT算法：节点协商选出能被所有节点认可的区块
  特点：1.安全性证明完备。2.应用规模小。3.通信开销较大。
可信执行环境(Trusted Execution Environment, TEE)的软硬件结合的共识算法：
  可信执行环境是指在这一类环境中的操作是绝对安全可信，外界无法干预修改的运行环境。其能访问的软硬件资源和Rich OS（普通操作系统）完全分离的。能较大程度的消除恶意节点的操作，能够大幅提升共识算法的性能。

智能合约：自动执行的计算机程序

### 2025.03.04
Layer1（构建去中心化网络的基础）：
  核心：共识机制
  实际应用：
    公链：Bitcoin，Ethereum，Litecoin等
    联盟链：特定组织内的区块链系统，如R3 Corda（金融），HyperLedger Fabric，Quorum
    私链：更加私密的区块链
      特点：高效，访问受限，定制化的控制
      
Layer2（建立在Layer1上，提高系统扩展性和效率的技术）
  分类：
    State Channels（状态通道）：双方在链下可以进行多次交易，最后将结果提交到主链。
    Sidechains（侧链）：与主链并行运行的独立链，资产和数据可以在两条链间转移。
    Plasma：一个框架，允许创建多条子链，每一个子链都和主链相互作用。
    Rollups：在链下处理交易并将结果打包到主链，以此提高效率
    
跨链桥：在不同的区块链之间转移资产的技术
  种类：
    简单支付验证桥（SPV）：通过验证另一个链上的交易来工作
    联邦桥：由一组验证者管理，负责在两条链之间转移资产
    阈值签名方案（TSS）桥：使用多方计算来创建跨链交易的签名

  Layer2使区块链可以处理更多的交易，满足日益增长的交易需求。
  跨链桥确保了不同区块链系统的互操作性，使得不同的链可以互相通信和互相支持

### 2025.03.05
chapter3：
数字资产：照片，电子邮件，比特币……
  特点：稀缺，去中心化，安全
  种类：
    加密货币
    NFT
    数字证券
    其他：数字收藏品，虚拟商品，数字身份等

### 2025.03.06
比特币（数字时代的黄金）
以太坊：智能合约
区块链钱包：
  软件钱包（热钱包）
  硬件钱包（冷钱包）
  在纸张上记录的公私钥对
账户模型：
  传统账号模型（Ethereum）：
    原子性
    一致性
    隔离性
    持久性
  UTXO模型（bitcoin）

以太坊的账户类型：
  EOA普通账户：公私钥对控制
  CA合约账户：智能合约代码控制

多种类型的加密货币：
  Meme币（Dogecoin，Shiba）：缺乏具体功能，通常依靠趣味性和营销来吸引观众，价格波动大
  公链原生代币（TRX，XRP）：支付交易费用，反应公链的功能和价值
  项目代币：应用在DAPP中，可以代表债券，权益，治理权
  稳定币：与美元挂钩，维护市场稳定


### 2025.03.07
AMA：Ask Me Anything，项目方举办的问答活动
AMA：自动做市商
Alpha：早期的、内部的投资建议或情报
空投：将一个项目的加密货币或数字资产发送给满足特定要求人的钱包，空投有助于项目的增长和提升价值

### 2025.03.08
Avatar：VR，互联网中的虚拟实体
Avatar项目：包含数千个NFT头像的收藏品
ATH：代币的历史最高价格
Arbitrum：一个以太坊第二层的扩展解决方案
Apeing in：不经过调研和了解，盲目购买NFT

Beta收益：一般指大盘指数收益或市场平均收益
燃烧：从市场收回币
BTD：逢低买入
Bagholder：持有价值已大幅贬值投资者的资产价值
抵押品：可以是实物资产（房地产），也可以是数字资产（比特币）
吃肉：一般指购买的藏品有利可图

DD/DYOR：在购买货币之前对项目进行充分的调查
Diamond Hands：钻石手，表面你对这个币的上涨有信心，无论如何也不愿意抛售
二级市场：玩家间的市场

FOMO：害怕错失利益的焦虑心理
Fiat：法币

ICO：首次代币发行
IEO：首次交易所发行
Kovan：一个权威认证，可以公开访问的以太坊测试网
L3：layer3，客户端应用层，是我们作为消费者交互的UI平台
Liquidity Pool：流动性池。提供用户的资金合集，锁定在一个智能合约中，以促进 DeFi 平台上的交易
Mempool：矿池，在挖矿前存储待处理的交易
铸造：验证信息的过程，执行该过程的参与者被成为矿工
Moonboy：看好某一资产的人
MEV：矿工可提取价值
NGMI：不会成功
Oracle：为智能合约提供来自外部世界的数据的服务
OTC：场外交易或法币交易

Paper hands：在货币下跌时卖出，通常会有损失
PFP：个人资料图片，“个人资料图片”的缩写，通常指一张NFT的照片
抽水和倾倒：炒作一个项目让许多人买入，提高其价格。进行炒作的人在价格短时间快速上涨时卖出他们持有的资产。导致市场立即抛售，没有卖出的人遭受了损失

Queued Pool：排队的池子，队列池时mempool中的交易池，这些交易因为“失序”而尚未准备好被处理
Rugged：被诈骗
Rekt：一个人遭受了巨大的损失
Rug：加密行业中出现的参与潜逃的事件
削减：砍价、烧毁或重新分配验证者的加密货币过程，作为批准欺诈性收费或其他方式破坏网络的惩罚
滑点：报价与实际交易价格的差异

测试网：模仿主网区块链的软件环境，用于测试网络升级和智能合约，然后再部署到主网
TVL：Total Value Locked，锁定的总价值。锁定在dapp智能合约中的资产的数量度
Vaporware：蒸发产品，宣布和特斯拉的产品或项目，但从未真正实现

### 2025.03.09
XR：扩展现实，指通过将真实与虚拟相结合，打造一个可人机交互的虚拟环境
X2E：X to Earn：指一切能够在web3中获得收益的行为
YOLO：You Only Live Once，通常指在单一资产上投入过多的资金
Your Bags：你的背包，意指NFT钱包地址

### 2025.03.10
DAO：去中心化自治组织，以分布式、透明和信任最小化的方式来进行集体决策
  DAO利用了区块链智能合约，将部分或全部流程写入合约代码中，以执行决策并分配所有权。智能合约的出现为创新奠定了基础，因为智能合约可以让DAO的治理规则完全透明化，而且无法被任何DAO成员或外部方篡改
  优势：
    规定写在智能合约中，活动对社会公开。任何人都可以审计
    任何成员都可以提交提案、对别人的提案发起挑战或进行投票
    旦达成共识，任何一方或小团体都无法篡改治理流程

### 2025.03.11
DeFi:去中心化金融，指建立在区块链（Ethereum为主）上的数字资产、金融智能合约、协议和去中心化应用（DApps）。主要应用包括交易所、稳定币、存借贷、理财、金融衍生品、支付、期货合约、跨链支付、预言机等业务，更新兴的还有彩票、拍卖、预测等等

### 2025.03.12
Web3生态：
  协议层：
    区块链网络
    跨链桥：连接不同区块链网络的技术或协议，允许数字资产或数据在这些不同的区块链之间传输和互操作
  基础设施：
    节点服务：节点服务是连接区块链网络和 DApp 的桥梁，可以为一个提供读和写数据到区块链网络的服务器
    网络存储：提供去中心化存储的服务商
    数据服务：区块链上有大量的原始数据是无法直接使用的，有一些平台提供将链上数据进行索引、分析、归档等处理，提供开放 API
  应用层：直接面向用户的
    治理 & DAO （Govern）
    钱包
    金融
    游戏
    NFT
    社交
    创作&内容
    ……
  
### 2025.03.13
钓鱼攻击：
  1.0：Transfer 转账
      SafeTransferFrom 转NFT
  2.0：Approve 授权额度
      Increase Allowance 提升额度
      SetApproveForAll 授权NFT
  防范方法：
    警惕链接
    推特搜索或者谷歌搜索都不一定安全
    用官方查找：DeFiLiama，coinmarketcap
    安全工具：Scam Sniffer
              Rabby Wallet
    资金隔离：大资金用冷钱包
             小资金用热钱包
             未知项目用新钱包 

### 2025.03.14
GameFi：Game+Finance 链游
  为玩家提供经济激励，可以边玩边赚的区块链游戏
  生态：
    Axie Infinity是一款数字宠物世界形式的去中心化游戏。 玩家通过虚拟货币购买三只小宠物（Axie），使用它们繁殖出新的宠物进行战斗，并且与其他玩家战斗赚取加密代币，或将自己多余的宠物卖给他人获取收益，此外玩家也可以在游戏中购买虚拟地产。

  BigTime玩法类似于《暗黑破坏神》。与此前的现象级链游Axie Infinity相似，Big Time设立了打金机制，玩家刷副本、打怪可获得游戏代币BIGTIME

  
### 2025.03.15
恶意签名攻击：链下签名无需手续费
  permit（）
  流程：owner先授权给Uniswap permit2/Opensea seaport合约，owner进行一个链下签名，Receiver合法取得签名后的文本，把文本交给Permit2等合约检验，然后就可以转走代币。
  Hacker诱导授权一个恶意的签名：允许xx转走我的所有代币，允许xx免费购买我的NFT
  防范：
    仔细检查签名内容，仔细检查签名内容是否包含spender等可疑字眼
    工具：Scam Sniffer

### 2025.03.16
铭文：随着Ordinals协议的诞生，其为比特币提供了编号和铭文的功能，从而拓宽了比特币生态系统的产品范围
  
### 2025.03.17
盗取私钥攻击：伪装客服，发送钓鱼网站
  病毒软件：exe，pdf，mp4，jpg
  
### 2025.03.18
虚假地址攻击：
  原理：近似地址粉尘（小金额）转账，让粗心用户误转
        剪切板木马
  防范方式：复制时少复制一点
           粘贴时检查中部
           将历史信任记录转为信任地址薄
           Rabby钱包白名单转账

### 2025.03.19
貔貅盘/蜜罐代币：能买不能卖
  特点：合约不开源；起名怪异，可读性差
### 2025.07.12
<!-- Content_END -->
