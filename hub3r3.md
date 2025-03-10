---
timezone: UTC+8
---

# hub3r3

1. 小白一枚
2. 努力学习ing
3. hub3r3

## Notes

<!-- Content_START -->
### 2025.03.03
    学习区块链知识，第一个要先了解的肯定是比特币，比特币要先了解的特点之一就是UTXO账户。UTXO（Unspent Transaction Output）是比特币等区块链系
统中用于管理交易的核心模型，代表未被使用的交易输出。其本质是记录交易后剩余的、可被后续交易引用的资金单元。例如，当用户A向用户B转账时，系统会
消耗A的某个UTXO作为输入，并生成新的UTXO分配给B（作为输出）和可能的找零地址（若存在剩余金额）。UTXO的集合构成了全网用户的可用余额，并通过加密
算法确保交易不可篡改。
    说人话就是，每个UTXO必须作为整体被使用。例如，若某UTXO包含5个比特币，而用户仅需支付3个，则需将整个UTXO作为输入，生成两个新UTXO：3个比特币给
收款方，2个比特币作为找零返回原地址。这种设计异于我们日常所理解的银行账户，所以要先理解比特币的这个特点，才会更好理解比特币的创新之处。

### 2025.03.04
   目前的web2时代，各大互联网大厂垄断了绝大多数的数据，用户生产的数据，所有权却是各个大厂的，他们可以从中获取超额利益，用户却无法从中获益。
但到了Web 3.0时代(数据去中心化时代)，基于区块链技术，互联网变得更加开放和透明。用户将真正拥有数据所有权，不再依赖中心化平台，用户之间的协作
价值创造将更加分散。这才是互联网理想主义的初心，网络的发展方向将更人性化。相信Web3.0是互联网的下一阶段，它将带来更多的创新、更高的安全性、
更大的自由度和更深层次的普惠性。

### 2025.03.05
   在区块链世界，做为普通用户，接触最多的应该是dapp。去中心化应用（DApp）是基于区块链技术构建的新型应用程序，其核心特征为‌无中心化控制节
点‌ ，通过智能合约与分布式账本实现自治化运行。
‌1.去中心化运行机制‌。DApp不依赖中心化服务器，数据存储和计算分散在区块链网络的多个节点中，通过共识算法（如PoW、PoS）保障数据一致性‌。这种架构有
效避免了单点故障风险，提升了系统的抗攻击能力‌。
2.智能合约驱动‌。业务逻辑通过智能合约自动执行，代码开源且不可篡改。例如以太坊的Solidity语言编写的合约，可自动完成交易清算、投票治理等操作‌。
3.数据透明与不可篡改‌。所有交易记录和操作均存储在区块链上，用户可通过区块浏览器追溯完整历史，确保公开透明性‌。
4.开源与社区自治‌。DApp代码通常开源，允许开发者参与迭代优化。治理模式多采用DAO（去中心化自治组织），用户通过代币投票决定协议升级或资金分配。
### 2025.03.06
私钥是本质是256位的随机数，那么私钥生成的总数为2的256次方。所以想通过暴力碰撞去获取特定地址的私钥，难度超级大，概率接近0。虽然私钥可生成范围足够大，但是如果生成私钥的算法有问题，那也会有隐患。
比如一个钱包的随机数生成不够随机，那么是有可能给两个用户生成同一组私钥的，所以算法很关键，要保证真随机。助记词本质也是一串随机数（128—256位），不过因为随机数形式和私钥形式都不方便使用，所以比特币社区通过了BIP39协议，来允许将随机数通过特定编码转化为词库中的单词。私钥和助记词请不要存放在联网设备中。
### 2025.03.07
区块链钱包和普通钱包是不一样的。普通人可能觉得钱包就是装钱的，但区块链钱包其实不是装币的，而是管理密钥的工具。
昨天提到私钥，是由用户自己控制，‌而钱包只是显示作用，地址才是放钱的地方。所以需要强调的是钱包不存钱，而是管理密钥和地址。
钱包通过密钥能生成地址、签名交易。钱包有热钱包和冷钱包的区别，还有托管和非托管的区别。热钱包像手机里的支付宝（会联网），冷钱包像保险箱（不联网）。
我们绝对要保管好私钥，就像银行卡密码一样，不能泄露。而且真丢了私钥/助记词，神仙也找不回你的资产‌。
区块链就像银行金库，钱包就是你的钥匙串——金库里存着你的黄金（数字资产），钥匙串上有开锁密码（私钥）和保险柜编号（地址）‌。
### 2025.03.08
‌NFT是区块链世界的「数字身份证」‌
‌1. 什么是NFT？‌
‌本质‌：NFT是区块链上的“唯一编号证书”‌，就像现实中的房产证或身份证，每个NFT都有独一无二的编码，无法被复制或冒用‌。
‌和普通加密货币的区别‌：比特币这类加密货币像“钞票”，每张价值相同且可拆分；NFT更像“带编号的限量版球鞋”，每双都是孤品且不可分割‌。
‌2. 三大核心特点‌
‌唯一性‌：每个NFT对应特定数字内容（比如一张图、一段视频），区块链记录永久可查‌。
‌不可拆分‌：不能像比特币拆成0.1个，必须整体交易‌。
‌所有权透明‌：谁买了NFT，区块链上清清楚楚，但原创者可能保留版权（比如你买了NFT画作，能证明它是你的，但作者仍能用原图）‌。

‌3. 常见应用场景‌
‌数字艺术品‌：艺术家把作品变成NFT出售，买家获得“数字收藏证书”‌。
‌游戏道具‌：比如一把虚拟宝剑变成NFT，玩家真正拥有它，甚至能跨游戏使用‌。
‌虚拟房产/门票‌：元宇宙里的一块地、演唱会电子票，用NFT锁定归属权。
‌4. 举个接地气的例子‌
你花100块买了一张数字猫咪图片，如果是普通图片，别人能随便复制；但如果是NFT猫咪，区块链会给它盖个“全球唯一钢印”（哈希值），所有人都能查到这只猫归你‌。
‌5. 特别注意‌
NFT不等于实物：买NFT艺术品 ≠ 买下版权，可能只买了“收藏权”‌。
价格波动大：NFT可能被炒作，今天值10万，明天可能变泡沫‌。
总结：NFT就是用区块链技术给数字内容发“防伪身份证”，让虚拟世界的东西也能像实物一样被拥有和交易‌。

### 2025.03.09
‌1. 什么是DeFi？‌
‌核心定义‌：DeFi（去中心化金融）是用区块链技术重构的金融系统，把银行、交易所这些中间商全砍掉，让普通人直接用代码和智能合约完成借贷、交易、理财等操作‌。
‌类比理解‌：就像用支付宝转账，但不需要支付宝公司参与，资金流动由全网计算机共同记账验证‌。
‌2. 四大核心特点‌
‌去中介化‌：借钱不用找银行，交易不用找交易所，所有操作由智能合约自动执行。
‌透明可信‌：每一笔交易都写在区块链上，连黑客都改不了账本‌。
‌7×24小时服务‌：没有银行下班时间，全球随时随地操作‌。
‌资产自管‌：钱存在自己的区块链钱包里，不像支付宝存在阿里账户‌。
‌3. 常见应用场景‌
‌抵押借贷‌：抵押1个比特币，立刻借出等值的美元稳定币，利息由算法实时调整‌。
‌去中心化交易所（DEX）‌：像Uniswap这类平台，用户直接兑换加密货币，没有中间商赚差价‌。
‌生息理财‌：存数字货币进智能合约，自动赚取利息，收益率常高于银行定期‌。
‌4. 举个接地气的例子‌
你想借5000块钱急用，传统流程是：查征信→找银行→签合同→等放款。
用DeFi的话：
把价值1万的数字货币抵押到智能合约,10分钟后自动收到5000块稳定币（利息按秒计算）
还钱时连本带利打回合约，自动拿回抵押的币‌。

‌5. 特别注意‌
‌智能合约风险‌：代码漏洞可能导致资金被盗（比如2023年某DeFi项目被黑损失2亿美元）‌。
‌高波动性‌：抵押数字货币若暴跌，可能触发强制平仓。
‌使用门槛高‌：需自己管理私钥、gas费（类似手续费）等概念。
总结：DeFi相当于用区块链技术搭了个“金融乐高”，把银行柜台变成手机APP里的几行代码，但玩得转需要先学规则‌。

### 2025.03.10
‌Web3未来发展趋势展望    
一、‌核心技术突破方向‌
‌去中心化架构普及‌：区块链底层技术将支撑90%以上Web3平台，实现数据分布式存储与用户自主控权‌。
‌智能合约智能化‌：AI驱动的智能合约将实现动态风险预判，大幅降低DeFi领域的系统性风险。
‌跨链技术成熟‌：区块链互操作性协议将突破孤岛效应，实现比特币网络与以太坊生态的资产无缝流转‌。
二、‌主流应用场景深化‌
‌金融基建重构‌：
DeFi市场渗透率将超过传统证券市场，实现日均万亿美元级链上交易‌。基于NFT的房产、股票等实物资产代币化规模加大。
‌元宇宙经济崛起‌：
虚拟土地交易通过NFT确权，形成与现实地产评估体系接轨的估值模型‌。
XBIT等去中心化交易所将成为元宇宙资产流通的核心枢纽‌。
‌ 
三、‌关键挑战与破局路径‌
‌安全防护升级‌：
量子加密技术将应用于钱包系统，抵御预期的量子计算攻击‌ 
AI风控引擎实时监测链上交易，异常行为拦截 
‌‌用户体验革新‌：
  生物特征钱包登陆普及，Gas费支付实现「刷脸秒确认」
 
‌人才需求爆发‌：
智能合约审计师、DAO治理顾问等新型职业薪酬将超过传统投行分析师 
 

### 2025.07.11

笔记内容

### 2025.07.12

<!-- Content_END -->
