---
timezone: UTC+8
---


# Zaki

1. 自我介绍
  自己為一位小碼農，希望能跟大家一起進步
2. 你认为你会完成本次残酷学习吗？
  yes~

## Notes

<!-- Content_START -->

### 2025.03.05

從網際網路誕生至今，已經歷三次重要的變革，每次都深刻影響了我們的生活方式和社會結構。

### 1. Web 1.0時代（only讀網路）

這是網路的早期階段，網站只提供靜態資訊，使用者只能瀏覽和閱讀，無法參與互動。  
內容多為文字與圖片，網站由少數管理者控制，使用者純粹是「資訊接收者」。  
這就像一本電子版百科全書，網際網路是單純的知識來源。

---

### 2. Web 2.0時代（讀寫網路）

Web 2.0讓使用者能夠產生內容，開啟了雙向互動的新時代。  
部落格、社交媒體、影音平台興起，每個人都可以發布內容、留言互動、分享轉發。  
網路從單向資訊流，變成一個全球社群。但這些平台多數是中心化的，資料和流量掌握在少數科技巨頭手中，使用者的資料隱私和數據主權也因此受到威脅。

---

### 3. Web 3.0時代（去中心化網路）

Web 3.0以區塊鏈為基礎，強調去中心化與資料自主權。  
使用者真正擁有自己的數據，不再依賴單一平台。  
這個時代，網路上的價值傳遞不再需要中介，點對點的協作和創新將成為主流。  
Web 3.0被視為回歸網際網路的初衷：開放、自由、民主化。

---

### Web 2.0與Web 3.0的主要差異

| 項目 | Web 2.0 | Web 3.0 |
|---|---|---|
| **控制權** | 中心化，平台掌握一切 | 去中心化，使用者掌握資料 |
| **數據所有權** | 平台所有 | 使用者所有 |
| **互動模式** | 內容互動 | 透過智能合約直接互動 |
| **安全性** | 容易成為攻擊目標 | 分散式架構更安全透明 |
| **商業模式** | 廣告為主，賣數據 | 加密貨幣、代幣經濟、直接支付 |

---

### Web 3.0的額外補充與想像空間

1. **個人數位身份**  
   每個人在Web3.0中擁有獨一無二的去中心化身份（DID），登入、交易、簽署、社交，都不再需要依賴Google或Facebook。

2. **去中心化金融（DeFi）**  
   不再依賴銀行和金融機構，每個人都可以直接借貸、投資、交易。

3. **數位資產與NFT**  
   創作者的每件作品，都能在區塊鏈上紀錄來源與版權，價值可由市場透明定價。

4. **自治組織（DAO）**  
   每個人都可以參與或創建去中心化自治組織，透過代幣治理，社群一起決策發展方向。

5. **元宇宙融合**  
   Web3.0還可能與元宇宙深度結合，虛擬世界中的每筆資產、每次互動、甚至每場活動都將上鏈，形成真正屬於用戶的數位空間。


### 2025.03.06

#### 助記詞與私鑰的關係
助記詞和私鑰的本質都是「隨機數」，它們在功能上是一致的，都是用來掌控你的加密貨幣資產。

助記詞本質上也是一段 128～256 位的隨機數。由於直接使用隨機數或私鑰都太不方便，為了改善使用體驗，比特幣社群制定了 **BIP39** 協議，將隨機數透過特定的編碼方式，轉換為一組由詞庫中單詞組成的助記詞。

助記詞因為是常見的單詞，不區分大小寫，使用上比私鑰方便許多。這也是為什麼近年來，**助記詞錢包**已逐漸成為主流。

#### 助記詞的優勢
助記詞錢包還有一個重要優點：  
**一組助記詞可以派生出無數個私鑰，每個私鑰可以對應不同幣種。**  
換句話說，如果你持有 30 種加密貨幣（如 BTC、ETH、LTC、EOS等），只要保存一組助記詞，就能掌控所有資產，不需要每種幣都單獨備份私鑰。

像「比特派錢包」，會同時展示助記詞和私鑰給用戶，但一般情況下，**只要妥善備份助記詞**就足夠了。

#### 助記詞是否通用？
只要各個錢包都遵循 **BIP32、BIP39、BIP44** 標準協議，助記詞就是通用的，理論上可以在不同錢包之間導入和恢復資產。  
**但要注意，不同錢包的安全性和實作細節有所不同，所以不建議頻繁跨錢包導入助記詞。**

---

### BIP 協議詳細介紹

#### BIP32：分層確定性錢包（Hierarchical Deterministic Wallet）
- BIP32 定義了一種「分層結構」的錢包，讓一組「主私鑰」可以派生出無限多個子私鑰，這樣你可以為每個幣種、每筆交易生成不同的地址，提升隱私性。
- BIP32 還允許透過「公開鍵」直接推算子地址（觀察錢包的概念），讓第三方（如會計師或稅務機構）可以監控地址資金流動，卻無法掌控資產。

#### BIP39：助記詞生成與管理（Mnemonic Phrase）
- BIP39 定義了如何把隨機數轉換成一組「助記詞」，並確保這組助記詞可以轉回原始隨機數。
- 助記詞來自固定的詞庫（如 2048 個英文單詞），加上校驗機制，讓輸入錯誤時較容易發現。
- BIP39 讓助記詞成為一種「跨錢包通用的備份格式」。

#### BIP44：多幣種支持（Multi-Account Hierarchy）
- BIP44 基於 BIP32 和 BIP43，定義了一種多幣種錢包的規範。
- 它設計了「5層路徑結構」，讓一組助記詞可以管理多個幣種、多個帳戶，每個帳戶下又能擁有無數地址。
- 標準格式：`m / purpose' / coin_type' / account' / change / address_index`
    - `purpose'`: 固定為 44，代表使用 BIP44
    - `coin_type'`: 不同幣種有不同編號（如 BTC=0, ETH=60）
    - `account'`: 帳戶編號（0 開始）
    - `change`: 0 表示外部地址（收款地址），1 表示內部地址（找零地址）
    - `address_index`: 具體地址序號

### 2025.03.07

## BIP32, BIP39, BIP44
BIP（Bitcoin Improvement Proposal，Bitcoin改進提案）是提出Bitcoin新功能或改進的技術文件。任何人都可以提出BIP，經過社群審核並在bitcoin/bips上公佈。BIP就像Internet上的RFC（Request for Comments）一樣，是協議和技術進步的基礎文件。

BIP32、BIP39和BIP44是共同定義了目前廣泛使用的HD Wallet（層級確定性錢包，Hierarchical Deterministic Wallet）。它們不僅規範了錢包如何生成和管理密鑰，還包括設計理念、實作方式和具體實例。這些BIP的作用是提供一個標準化的方法來生成和管理加密貨幣錢包，方便使用者備份、恢復和管理多個密鑰。

### BIP32: Hierarchical Deterministic Wallet (HD Wallet)
BIP32定義了所謂的層級確定性錢包（Hierarchical Deterministic Wallet，簡稱“HD Wallet”），該系統允許從一個單一的“seed”（種子）生成一個樹狀結構，其中包含多組密鑰對（包括公鑰和私鑰）。這樣的設計使得用戶只需要記住一個單獨的seed即可管理多個密鑰對。

**優點**
- **方便備份和恢復**：用戶只需記住一個seed，而無需分別備份每個密鑰對。
- **遷移性**：可以將整個錢包的所有密鑰對安全地轉移到任何其他兼容裝置上，只需要提供這個seed。
- **層級權限控制**：可以將不同的密鑰對映射到樹結構的不同層級，從而實現多層的權限管理。

<img src="https://github.com/user-attachments/assets/17a1db46-8fa0-4420-8641-43c6cb2ec3c7" width="500" />

### BIP39: Mnemonic Code（助記詞）
BIP39提供了一個方便記憶的方式來表示BIP32中的seed。BIP39將原本的seed轉換成一組易於記憶的單詞，這組單詞通常由12個或24個單字組成，稱為助記詞（Mnemonic Phrase）。這樣的設計大大降低了用戶記憶和書寫的難度，並且更容易傳遞和備份。

**舉例**
假設助記詞是：
```
rose rocket invest real refuse margin festival danger anger border idle brown
```
這一組單詞就代表了某個特定的私鑰的生成seed。使用這些單詞可以推算出相對應的密鑰對。

#### 生成助記詞

- 一：生成128位隨機數
生成一個128位的隨機數。這個隨機數的目的是作為助記詞生成的基礎，確保每次生成的助記詞都是唯一且不可預測的。

  128位隨機數是一個長度為128位（即16字節）的數字，可以是0和1的隨機排列。例如：  
`1011001000110010101011001110110010011110100101101100100011010101`（這是一個範例，實際情況中會是完全隨機的）。

- 二：計算校驗碼
生成128位隨機數後，會基於該隨機數計算一個4位的校驗碼。這個校驗碼的計算方式是將隨機數的哈希值（使用SHA-256算法）進行處理，然後取哈希結果的前面4個位作為校驗碼。

  這個校驗碼的作用是增加錯誤檢查的機制。這樣，即使在存儲和輸入助記詞時發生錯誤，也可以檢查是否有錯誤發生。

- 三：合併隨機數與校驗碼
將128位的隨機數和4位的校驗碼組合在一起，這樣總長度是132位（128位隨機數 + 4位校驗碼）。

- 四：切分為11位長的區塊
將132位的數字按每11位切分。這樣就會得到12個11位的二進位數字。這些數字代表了在BIP39單詞表中對應的單詞。

- 五：查表生成助記詞
每個11位長的二進位數都對應一個BIP39單詞表中的單詞。BIP39單詞表通常包含2048個單詞。每個11位的二進位數字都會轉換為一個範圍在0到2047之間的數字，然後用這個數字查找BIP39單詞表中的單詞。

   例如，假設某個11位的二進位數字是`00000000001`，對應的數字是1，查表後可能對應的單詞是「abandon」等。

- 六：生成12個助記詞

  你會得到12個單詞，這些單詞是根據隨機數生成的，並且包含了加強錯誤檢查的校驗碼。這12個單詞就是你所說的助記詞（Mnemonic Phrase），通常用於恢復錢包或保存私鑰。

![image](https://github.com/user-attachments/assets/077a9315-6854-41ad-ba95-b41b83741c97)


### BIP44: 多幣種、多帳戶支持
BIP44基於BIP32的設計，為HD Wallet的樹狀結構定義了每一層的特殊意義。這樣用戶可以使用同一個seed生成多個加密貨幣的錢包，支持多幣種和多帳戶管理。BIP44明確規範了錢包的路徑結構，將每一層的數字（稱為“硬分隔符”）賦予特定的意義。

**BIP44路徑結構：**
```
m / purpose' / coin_type' / account' / change / address_index
```
- **purpose'**：固定為44'，表明該路徑遵循BIP44標準。
- **coin_type'**：表示加密貨幣的類型。每個加密貨幣都有一個唯一的coin_type代碼。例如，比特幣的coin_type是0'，以太坊是60'。
- **account'**：表示錢包中的帳戶。每個帳戶可以有自己的密鑰對。
- **change**：用於區分普通地址和變更地址（通常是0和1，分別代表外部和內部地址）。
- **address_index**：表示具體的地址索引，每個地址對應一個唯一的索引。

### 以太坊的HD Wallet
以太坊的HD Wallet結構遵循BIP32和BIP44標準，並將coin_type設為60'，表示這個錢包是用來管理以太坊（ETH）資產的。在這種結構中，第一個帳戶的第一組密鑰對的路徑會是：
```
m/44'/60'/0'/0/0
```
這代表這是一個符合BIP44標準的以太坊錢包，並且是該錢包中第一個帳戶（account 0）下的第一個地址（address 0）。

### 創建以太坊HD Wallet的實作
在實現上，可以使用一些JavaScript庫來創建和管理以太坊的HD Wallet。常用的JavaScript套件包括：

- **bip39**：這個庫實現了BIP39標準，負責根據用戶提供的助記詞生成二進位的seed，並支持從seed生成對應的私鑰和公鑰。
  
- **ethereumjs-wallet**：這個庫提供了生成和管理以太坊密鑰對的功能，並且包含一個`hdkey`子套件來創建符合BIP32/BIP44標準的HD Wallet。

- **ethereumjs-util**（目前不需要）：這個庫包含許多以太坊特有的實用函數，例如加解密功能等。

參考：

[【加密貨幣錢包】從 BIP32、BIP39、BIP44 到 Ethereum HD Wallet](https://medium.com/taipei-ethereum-meetup/%E8%99%9B%E6%93%AC%E8%B2%A8%E5%B9%A3%E9%8C%A2%E5%8C%85-%E5%BE%9E-bip32-bip39-bip44-%E5%88%B0-ethereum-hd-%EF%BD%97allet-a40b1c87c1f7)

[2-Party BIP32：更安全的 HD-Wallet](https://blog.amis.com/2-party-bip32-%E6%9B%B4%E5%AE%89%E5%85%A8%E7%9A%84-hd-wallet-2d53a5f71545)

[DAY 28- BIP32- HD wallet](https://ithelp.ithome.com.tw/articles/10279944)

[HD Wallet](https://medium.com/@bun919tw/hd-wallet-970096a6d72f)

### 2025.03.08

### **什麼是哈希函數？**  
哈希函數會將 **任意長度的數據（訊息）** 轉換成 **固定長度的摘要（digest）**，這個摘要就像是訊息的「指紋」。在 SHA-256 中，輸入的訊息可以長達 **2⁶⁴ 位元**（約 2.3 EB），但輸出始終是 **256 位元（32 字節）** 的固定長度數據。

![image](https://github.com/user-attachments/assets/969a7e6d-add6-4868-b564-83b5473ca00f)

這個數學表示法描述了 **SHA-256 哈希函數** 的輸入與輸出關係，讓我們逐步解析：

### **1. SHA-256 的定義**
$$ \text{SHA-256} : B^1 \cup \dots \cup B^{2^{64}} \to B^{256} $$
這表示 **SHA-256 是一個函數**，它的作用是將 **不同長度的位元串（bit strings）** 轉換為固定長度的 **256 位元** 哈希值。

### **2. 輸入（Domain）**
$$ B^1 \cup \dots \cup B^{2^{64}} $$
這表示 SHA-256 接受的輸入範圍：
- \( B^n \) 表示長度為 \( n \) 的二進位字串（bit string）。
- 這個函數接受 **從 1 位到 \( 2^{64} \) 位** 的輸入（最大約 18 艾位元組，EB）。
- 換句話說，它可以處理**長度可變的訊息**。

### **3. 輸出（Codomain）**
$$ B^{256} $$
這表示 SHA-256 的輸出：
- 無論輸入的長度是多少，輸出始終是 **固定 256 位（32 字節）的哈希值**。

### **4. 映射表示**
$$ M \mapsto H $$
這表示：
- 任意輸入訊息 \( M \)（bit string）**經過 SHA-256 處理**後，對應到一個 **256 位長度的哈希值 \( H \)**。
- \( H \) 是訊息的 **摘要（digest）**，用來唯一標識訊息。


### **SHA-256 的步驟**  

#### **1. 預處理（Pre-processing）**
1. **填充（Padding）：**  
   - 讓訊息長度變成 **512 的倍數**，填充的過程會在訊息後面加上一些數據，最後 64 位元記錄原始訊息的長度，以防止不同訊息填充後變成相同的結果。
   
![image](https://github.com/user-attachments/assets/096f54c3-0286-4a95-940d-c966f70d77ed)

2. **分塊（Blocks）：**  
   - 將填充後的訊息切成 **512 位元** 的區塊，每個區塊再拆成 **16 個 32 位元的子區塊**。

![image](https://github.com/user-attachments/assets/118c3181-a670-4e29-bea3-8e186432b2ea)

3. **初始化哈希值（Hash Initialization）：**  
   - 設定 **初始哈希值 H⁰**，這些值來自於前 **8 個質數的平方根小數部分**，轉換為 32 位元。

![image](https://github.com/user-attachments/assets/153be57c-1c91-4bea-ab73-55b152332b25)

> 計算 SHA-256 初始化哈希值（ Initial Hash Values, $𝐻^0$ ）。這些值來自於前 8 個質數的平方根小數部分，轉換為 32-bit 整數。
```javascript
for (i of [2, 3, 5, 7, 11, 13, 17, 19]) {  
  input_block = parseInt((Math.sqrt(i) % 1).toString(2).slice(2, 34), 2);  
  console.log(input_block.toString(16), input_block.toString(2).padStart(32, '0'));
}
```

>1. `[2, 3, 5, 7, 11, 13, 17, 19]` 質數是 SHA-256 初始化哈希值的來源
>2. 計算平方根小數部分 `Math.sqrt(i) % 1`
>3. 轉為二進位 `(Math.sqrt(i) % 1).toString(2)`
>4. 取 32 位 `.slice(2, 34)`
>5. 轉回 10 進位 `parseInt(..., 2)`
>6. 轉為 16 進位 & 補 0 `input_block.toString(2).padStart(32, '0')`

```
Output:
   6a09e667(hex)
   01101010000010011110011001100111(binary)
```

#### **2. 訊息處理（Message Processing）**
1. **訊息排程（Message Schedule）：**  
   - 產生 **64 個 32 位元的數據塊**，第一批來自訊息，後面的則是根據前面的數據計算得來。

![image](https://github.com/user-attachments/assets/06eb0f7c-d12d-48ae-b472-ba44f5b625a2)

2. **哈希計算（The Big Shuffle）：**  
   - 使用一系列邏輯運算（包括右旋轉、位移、XOR、AND 等）來更新哈希值。

![image](https://github.com/user-attachments/assets/438513a3-9944-416a-a758-36fb2fa81188)

3. **更新哈希值（New Hash）：**  
   - 透過模 2³² 加法，將處理結果加回原來的哈希值，更新為新哈希值。

#### **3. 最終哈希值（Final Hash）**
當所有區塊都處理完畢，最後得到的 **H 值** 就是訊息的最終哈希值（訊息指紋）。

### **關於 SHA-256 潛在問題**
- SHA-256 產生的哈希值有 **2⁷⁷（約 10⁷⁷）種可能**，極難發生碰撞（不同訊息產生相同哈希）。
- 雖然數學上碰撞是可能的，但目前 **尚未發現** 任何有效的碰撞攻擊。
- **不要在生產環境自己實作 SHA-256**，因為安全性極難保證。

## **SHA-256 與 HD Wallet 的關係**
SHA-256 在 HD Wallet（Hierarchical Deterministic Wallet，階層式確定性錢包）中扮演 **核心角色**，因為它是許多加密運算的基礎。HD Wallet 是 Bitcoin Improvement Proposal **BIP-32** 規範的一種金鑰管理方式，能夠從 **單一種子（seed）** 產生一個完整的金鑰樹。

SHA-256 在 HD Wallet 的主要應用包括：
1. **種子產生（Seed Generation）**
2. **子金鑰派生（Key Derivation）**
3. **地址產生（Address Generation）**


## **SHA-256 在 HD Wallet 的應用**

### **1. 種子產生（Seed Generation）**
HD Wallet 透過 **BIP-39**（Mnemonic Code）讓使用者輸入 12、15、18、21 或 24 個助記詞（Mnemonic），然後轉換為 512-bit 的種子（seed）。  
這個過程涉及 **SHA-256** 來驗證助記詞的完整性。

#### **流程**
1. **助記詞（Mnemonic）轉換為 entropy**（隨機熵）
2. **SHA-256 計算 entropy 的哈希值**（確保一致性）
3. **取前幾個位元作為 Checksum**，加回 entropy
4. **PBKDF2-HMAC-SHA512 延展** 來產生 512-bit 的種子

這個種子最終被餵給 **BIP-32** 來產生 HD Wallet 的根金鑰（Master Key）。

---

### **2. 子金鑰派生（Key Derivation）**
HD Wallet 使用 **BIP-32** 規範，從 **主金鑰（Master Key）** 產生無限多個 **子金鑰（Child Key）**。

SHA-256 在這個過程中被用來：
- **哈希處理金鑰派生資料**
- **驗證金鑰的完整性**

#### **計算方式**
每個子金鑰是透過 **HMAC-SHA512**（基於 SHA-256）計算：
$$ (\text{IL}, \text{IR}) = \text{HMAC-SHA512}(\text{parent key}, \text{child index}) $$
其中：
- `IL`（左邊 256 位元）用來計算子私鑰
- `IR`（右邊 256 位元）用來產生新的 chain code（確保金鑰一致性）

---

### **3. 地址產生（Address Generation）**
從 **公鑰（Public Key）** 產生 **Bitcoin Address**，SHA-256 會出現在：
1. **公鑰哈希（Public Key Hash, PKH）**
   - **SHA-256 計算公鑰哈希**
   - **再用 RIPEMD-160 計算最終的公鑰哈希**
   
   $$ \text{PKH} = \text{RIPEMD-160}(\text{SHA-256}(\text{Public Key})) $$
   
2. **雙重 SHA-256 計算 checksum**
   - **Bitcoin 地址會用 Base58Check 編碼**
   - 其中，Checksum 是：
     $$ \text{Checksum} = \text{SHA-256}(\text{SHA-256}(\text{Payload})) $$
   - 取前 4 個位元組作為 checksum，防止輸入錯誤。


## **SHA-256 與 BIP 規範的關係**
HD Wallet 依賴 SHA-256，而 SHA-256 主要參與了多個 **Bitcoin Improvement Proposals（BIPs）**，其中：
1. **BIP-32（HD Wallet）**
   - 定義 **主金鑰（Master Key）** 及其 **子金鑰（Child Key）** 如何從種子衍生
   - HMAC-SHA512 依賴 SHA-256 來計算金鑰雜湊值

2. **BIP-39（Mnemonic Code）**
   - 定義 **助記詞** 轉換成 entropy，並用 SHA-256 計算 checksum
   - 產生 HD Wallet 所需的種子（seed）

3. **BIP-44（多幣種派生路徑）**
   - 定義 **HD Wallet 路徑結構**
   - 使用 SHA-256 來驗證擴展公鑰（xpub）

---
 
#### SHA-256 它確保：
>**種子的一致性與完整性**（BIP-39）  
>**子金鑰派生的安全性**（BIP-32）  
>**比特幣地址的唯一性與抗碰撞性**（BIP-44）  

That's why SHA-256 是加密貨幣世界的基石之一

參考：

[Part 5: Hashing with SHA-256](https://medium.com/biffures/part-5-hashing-with-sha-256-4c2afc191c40)

[FIPS 180–4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)

[cedricbellet/_sha256.js from github](https://gist.github.com/cedricbellet/aca1fbecb5847c94be4b8f3bf96df3bc#file-_sha256-js)

### 2025.03.09

<!-- Content_END -->
