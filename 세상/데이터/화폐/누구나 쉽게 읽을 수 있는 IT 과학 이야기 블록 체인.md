# Story One - Talking About [[Blockchain]]
## The Relationship Between [[Cryptocurrency]] and [[Blockchain]]
### [[Bitcoin]]!! [[Blockchain]]??
[[Bitcoin]] is a [[cryptocurrency]].
[[Cryptocurrency]] is related to [[blockchain]].
### [[Cryptocurrency]] and the Public Ledger, [[Blockchain]]
[[Cryptocurrency]] is digital money used online, and [[blockchain]] is the ledger that records transactions of this [[cryptocurrency]].
## Linking Blocks into a Chain
### The Internet Revolution Opened by [[Blockchain]]
[[Blockchain]] is a technical term about how to store, process, and share [[data]].
Based on [[blockchain]] technology, [[cryptocurrencies]] were created and are being used in logistics and medical fields.
The concept of the [[internet]], initially used in one region, has been connected with new technologies to allow computers worldwide to connect.
This connection has led to more technological advancements through [[information]] exchange, one of which is the [[Internet of Things]].
### Linking Blocks into a Chain
[[Blockchain]] is a combination of the words "block" and "chain." It is a "[[software]] method of managing [[data]].
" The method of finding meaning in stored [[data]] is called "[[big data]]." [[Artificial intelligence]] is used for [[big data]].
## The Relationship Between [[Blockchain]], [[Data]], and [[Software]]
### Blocks are Ledgers, Ledgers Connected Like a Chain
In the medical field, blocks contain patients' information.
In transportation and logistics, blocks contain [[data]] like routes and movement paths.
### The Relationship Between [[Data]] and [[Blockchain]]
[[Bitcoin]] functions much like a type of financial sector, generating [[data]] known as transaction records.
These [[data]] are gathered to form and link together into "blocks."
### Application of [[Blockchain]] in Distribution
It can be used to track how cattle raised on farms end up in slaughterhouses and ultimately reach mart shelves.
### Application of [[Blockchain]] in Administration
Seoul has introduced the 'Seoul [[Blockchain]] 1st Project' to prevent fraud and tampering-related damages during the sale of used cars.
### Application of [[Blockchain]] in Real Estate and Goods Transactions
In real estate transactions, after certification by a licensed agent, contracts proceed, ensuring the authenticity of the counterparty's [[information]].
> [[Blockchain]] technology can turn all [[data]] into blocks, enhancing [[security]] over time as new blocks are created and linked.
# Second Story: [[Decentralized System]] and Role Allocation
## [[Decentralized System]]
### Limitations of [[Central System]]
[[Central System]] transactions are appealing targets for malicious [[hackers]]. To prevent [[hacking]], [[ActiveX]] was created but it is user-unfriendly.
### [[Blockchain]]: The best distributed storage technology
Because [[data]] for [[verification]] is distributed across multiple locations, if [[hackers]] cannot change all the [[data]] at the same time, the [[hack]] will fail. The reason why [[data]] can be stored in multiple locations is because [[blockchain]] technology users want to use [[IT]] and are connected to [[network]].
Using [[blockchain]] [[network]] instead of [[central system]] is one way to reduce [[security]] and system maintenance costs.
## Role Allocation
### Understanding Block Size with [[Bitcoin]] as an Example
In the case of [[Bitcoin]], which utilizes [[blockchain]] technology, a new block is created approximately every 10 minutes. Each block contains [[data]] such as user transaction information, occupying around 1MB of space.
### How is Block Size Divided?
It is divided between those who manage the [[data]] and those who generate it.
In the [[network]], each component is referred to as a [[node]].
[[Computer]] and [[smartphone]]s connected to the same [[network]] are also referred to as [[node]]s.
There are [[node]]s that generate the [[data]] to be included in the block.
For financial transactions, this could include transaction records, or for tracking histories, it could record movement paths or current statuses.
[[Node]]s that create blocks typically use [[storage]] spaces like their [[hard drive]]s to link and [[store]] Block A and Block B.
# The Third Story: Technologies Underpinning [[Blockchain]]
## [[P2P]] [[Data]] [[Sharing]]
### Technology for individuals [[exchanging]] [[data]]
[[Blockchain]] fundamentally utilizes [[P2P]] technology for [[exchanging]] [[data]]. A prominent example of [[P2P]] [[technology]] is torrenting, widely used for [[sharing videos]] and [[data]] among people.
A [[server]] is someone who sends [[data]] they possess, while a [[client]] is someone who requests [[data]].
### Relationship Between [[Server]] and [[Client]]
When there are many [[clients]] connected to a [[server]] simultaneously trying to [[download]] [[data]], the server gets overloaded with tasks to handle, slowing down the [[download]] speed.
### Slightly Different Roles of [[Server]] and [[Client]] in [[P2P]]
In a [[P2P]] system, every [[node]] can act as both a [[server]] and a [[client]].
While this setup can pose problems if one person turns out to be a [[hacker]] when [[receiving]] [[data]], the [[network]]'s interconnected nature allows for faster block [[verification]] and quicker [[sharing]] of newly created blocks.
## Connecting Different [[Node]]s in [[Blockchain]]
Just as we use an [[internet]] [[browser]] to access the [[internet]], special [[program]]s are needed to participate in a [[blockchain network]], such as [[Bitcoin]]'s [[wallet]] [[program]]s.
The [[internet]] [[connects]] to [[server]]s using numbers called [[IP]] addresses. Domain names such as naver.com and daum.net are called [[domain name]]s, also known as [[URL]] or [[web]] addresses.
We can access [[websites]] by their [[domain names]] because there are [[server]]s that provide [[DNS]] ([[Domain Name Service]]) assistance.
[[Node]]s connected to a [[blockchain network]] use the [[internet]] like any other [[server]] and need to use [[IP]] addresses, which are known as [[seed servers]]
## Let's Break It Down: [[Hash Function]]
### How [[Blockchain]] Gains Trust
The interconnected [[blockchain]] [[data]] between blocks is a robust security [[system]] because multiple [[node]]s store the same [[data]].
If other [[node]]s do not acknowledge a block, a [[blockchain]] created by someone cannot propagate to other [[node]]s, and it can be subject to [[hacking]], changing the block's contents. To solve this issue, information called headers is used.
Among the various pieces of information in the header, there are values used to ensure the proper connection with other blocks and guarantee that the [[data]] inside the blocks are legitimate.
These values are called [[hash values]], [[hash codes]], or simply [[hashes]], derived from the results of [[hash functions]].
### Where Are [[Hash Functions]] Used?
[[Hash functions]] are extensively used in the field of [[cryptography]].
Among the most commonly used types of [[hash functions]] are those known as [[sha-1]] and [[sha-2]]. These types have the characteristic that while they can [[transform]] input [[data]] into new [[data]], it is practically impossible to reverse-engineer the original [[data]] from the newly generated characters.
## How [[Hash Function]] Works
### Generating [[Hash Values]]
There is an empty space of 64 [[byte]]s, exactly the same size as the input 64-[[byte]] [[message]].
You mix the input [[message]] of 64 bytes into this empty space, copying one [[byte]] at a time.
The first 16 bytes are copied as they are, and from the next [[byte]] order, you continue to add and modify them, repeating the process until all 64 [[byte]]s of [[data]] are copied.
The copied [[data]] is then compressed into 8 spaces that will ultimately become the [[hash value]].
The [[hash value]] is 32 [[byte]]s in size, so the 64 [[byte]]s of [[data]] need to be compressed.
The compressed data that will be the [[hash value]] in the 8 spaces is continuously [[update]]d each time you process 64 [[byte]]s of [[data]].
After processing the entire 640-[[byte]] [[message]], the final [[hash value]] of 32 [[byte]]s in length is used.

In software, the meaning of padding is filling in empty spaces.
Even a slight change results in the [[data]] taking on a completely new form, known as the avalanche effect.
[[Blockchain]] uses [[hash functions]] to create strong [[security system]]s.
[[Hash functions]] serve as proof of [[data]] integrity against changes.
## Proof of Block [[Data]]
### How [[Data]] Proof Works
Contracts in [[blockchain]] are called [[smart contracts]] because they can automatically execute contracts due to their intelligence.
To link blocks like a chain in a [[blockchain]], they undergo a process of verifying that newly connected blocks are legitimate using each other's [[hash values]].
Once created, a [[blockchain]] cannot be altered because it is made using [[hash values]].
## Unhackable [[Data]] Proof Technology
### In Financial Transactions Using [[Blockchain]]
The content and [[hash values]] are included in transaction [[data]].
The [[hash value]] in the block header proves that the blocks are properly linked.
The [[hash value]] inside the block proves that the content of the block has not been altered.
### [[Encrypt]] [[data]] with a [[public key]].
A [[private key]] and a [[public key]] can be used to [[encrypt]] [[data]] with the [[private key]] and [[decrypt]] it with the [[public key]], or [[encrypt]] [[data]] with the [[public key]] and [[decrypt]] it with the [[private key]].
One method is [[RSA]] [[public key]] [[encryption]].
Public and private keys must be created simultaneously in [[software]].
If you want to include [[data]] in a [[blockchain]] block, you need to prove that the content of the [[data]] has not been changed and that the person who wrote the [[data]] is genuine.
### Proving Unchanged Content of [[Data]] - [[Hash Function]]
### Proving Authenticity of the Author of [[Data]] - [[RSA]]