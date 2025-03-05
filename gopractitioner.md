---
timezone: UTC+13
---

> 请在上边的 timezone 添加你的当地时区(UTC)，这会有助于你的打卡状态的自动化更新，如果没有添加，默认为北京时间 UTC+8 时区


# Jasper
1. 自我介绍
A full-stack developer interested in both algorithm and project development...
Now I'm studying in Web3/Blockchain...
2. 你认为你会完成本次残酷学习吗？
会
3. 联系方式Telegram
@jasperz999
## Notes

<!-- Content_START -->
 L
### 2025.03.04

1. Unspending transaction output: maintain a set of all UTXOs, easy to implement CoinJoin or Zero-Knowledge-Proof
2. Solution techniques for the increasing UTXO set:
   (1) Improving technologies: More efficient data structures, such as Merkle Tree or some better ones. Let light clients don't need to store the complete UTXO set. Remove the UTXOs not in use for a long time.
   (2) Improving the protocols: Encourage merging UTXOs. Implement snapshots of UTXO set to speed up the synchronization of nodes. Implement layering and sharding to distrubute the UTXO storage burden.

To address UTXO scalability issues, several innovative solutions include:
Layer 2 Solutions: Utilizing second-layer solutions such as Lightning Network to reduce UTXO creation on the main chain
Hybrid Models: Combining the advantages of UTXO and account models (such as Cardano's EUTXO model)
Advanced Data Structures: Using more efficient data structures and compression techniques to store UTXOs
Sharding Techniques: Distributing the UTXO set across different nodes or shards

### 2025.03.05
PoW / BFT
Layer1 / Layer2

<!-- Content_END -->
