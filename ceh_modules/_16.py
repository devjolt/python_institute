from random import choice

#wireless concepts
(['GSM', 'Global System for Mobile Communications'],['universal system used for mobile data transmission in wireless networkds']),
('bandwidth', ['the amount of information that can be broadcast over a connection','data transfer rate', f"measured in {choice(['bps','bits per second'])}"]),
(['access point','AP'],[f"can connect wireless devices to a {choice(['wireless','wired'])} network", f"allows wireless communication devices to connect to a wireless network through wireless standards such as {choice(['Wi-Fi','Bluetooth'])}","It serves as a switch or hub between a wired LAN and wireless network"]),
(['Basic service set identifier', 'BSSID')],['the media access control (MAC) address of an access point (AP)','base station that has set up a basic service set (BSS)','users are generally unaware of the BSS to which they belong','When a user moves a device, the BSS used by the device could change because of a variation in the range covered by the AP']), 
(['Industrial, scientific, and medical band','ISM band'],['set of frequencies used by the international industrial, scientific, and medical communities',f"set of frequencies used by the international {choice(['industrial','scientific','medical'])} communities"]),
('Hotspot',['places where wireless networks are available for public use','areas with Wi-Fi availability','where users can enable Wi-Fi on their devices and connect to the Internet']),
('Association','the process of connecting a wireless device to an AP'), 
(['Service set identifier','SSID'],['32-alphanumeric-character unique identifier given to a wireless WLAN','that acts as a wireless identifier of the network','permits connections to the desired network among available independent networks','a Device connecting to a wan WLAN should use the same SSID to establish connections']),
(['Orthogonal frequency-division multiplexing','OFDM'],['method of digital modulation of data','a signal, at a chosen frequency, is split into multiple carrier frequencies that occurring at right angles to each other','maps information on the changes in the carrier phase, frequency, amplitude, or a combination of these','shares bandwidth with other independent channels','produces a transmission scheme that supports higher bit rates than parallel channel operation','a method of encoding digital data on multiple carrier frequencies']),
(['Multiple input, multiple output-orthogonal frequency-division multiplexing', 'MIMO-OFDM'],'influences the spectral efficiency of 4G and 5G wireless communication services','reduces interference and increases the channel robustness']),
(['Direct-sequence spread spectrum','DSSS'],['a spread spectrum technique','multiplies the original data signal with a pseudo-random noise-spreading code','referred to as a data transmission scheme or modulation scheme','protects signals against interference or jamming']),
(['frequency-hopping spread spectrum','FHSS', 'frequency-hopping code-division multiple access', 'FH-CDMA'],['method of transmitting radio signals by rapidly switching a carrier among many frequency channels','decreases the efficiency of unauthorized interception or jamming of telecommunications','a transmitter hops between available frequencies using a specified algorithm','uses a pseudorandom sequence known to both the sender and receiver']),


#types of network
 
(['Software APs','SAPs'],'run on a computer equipped with a wireless network interface card (NIC)'),
(['Hardware APs','HAPs'], 'support most wireless features'),
('Extension to a Wired Network',['the AP acts as a switch, providing connectivity for computers that use a wireless NIC','AP can connect wireless clients to a wired LAN, which allows wireless access to LAN resources such as file servers and Internet connections']),
('multiple access points', ['connects computers wirelessly using multiple APs','if a single AP cannot cover an area, multiple APs or extension points can be established','area of each AP must overlap its neighbor\'s area','provides users the ability to move around seamlessly using a feature called roaming','can be strung together to provide wireless access to locations far from the central AP']),
('LAN-to-LAN',['APs provide wireless connectivity to local computers, and local computers on different networks can be interconnected','All hardware APs have this capability','complex task']),
('3G/4G hotspot', ['provides Wi-Fi access to Wi-Fi-enabled devices, including MP3 players, notebooks, tablets, cameras, PDAs, netbooks, and more']),

#wireless standards

#antennas
 Directional Antenna
A directional antenna can broadcast and receive radio waves from a single direction. In order to improve transmission and reception, the directional antenna’s design allows it to work effectively in only a few directions. This also helps in reducing interference.

Omnidirectional Antenna Omnidirectional antennas radiate electromagnetic (EM) energy in all directions. It
provides a 360° horizontal radiation pattern. They radiate strong waves uniformly in two dimensions, but the waves are usually not as strong in the third dimension. These antennas are efficient in areas where wireless stations use time-division multiple access technology. A good example for an omnidirectional antenna is the antenna used by radio stations. These antennas are effective for radio signal transmission because the receiver may not be stationary. Therefore, a radio can receive a signal regardless of its location.

Parabolic Grid Antenna
A parabolic grid antenna uses the same principle as a satellite dish, but it does not have a solid dish. It consists of a semi-dish in the form of a grid consisting of aluminum wires. Parabolic grid antennas can achieve very-long-distance Wi-Fi transmissions through highly focused radio beams. This type of antenna is useful for transmitting weak radio signals over very long distances on the order of 10 miles. This enables attackers to obtain a better signal quality, resulting in more data to eavesdrop on, more bandwidth to abuse, and a higher power output, which is essential in Layer-1 denial-of-service (DoS) and man-in-the-middle (MITM) attacks. The design of this antenna saves weight and space, and it can receive Wi-Fi signals that are either horizontally or vertically polarized.
 Yagi Antenna
A Yagi antenna, also called Yagi–Uda antenna, is a unidirectional antenna commonly used in communications at a frequency band of 10 MHz to VHF and UHF. This antenna has a high gain and low signal-to-noise (SNR) ratio for radio signals. Furthermore, it not only has a unidirectional radiation and response pattern, but also concentrates the radiation and response. It consists of a reflector, dipole, and many directors. This antenna develops an end-fire radiation pattern.
 Dipole Antenna
A dipole antenna is a straight electrical conductor measuring half a wavelength from end to end, and it is connected at the center of the radio frequency (RF) feed line. Also called a doublet, the antenna is bilaterally symmetrical; therefore, it is inherently a balanced antenna. This kind of antenna feeds on a balanced parallel-wire RF transmission line.
 Reflector Antennas
Reflector antennas are used to concentrate EM energy that is radiated or received at a focal point. These reflectors are generally parabolic. If the surface of the parabolic antenna is within a tolerance limit, it can be used as a primary mirror for all frequencies. This can prevent interference while communicating with other satellites. A larger antenna reflector in terms of wavelength multiples results in a higher gain. Reflector antennas reflect radio signals and has a high manufacturing cost


Shared key authentication process: In this process, each wireless station receives a shared secret key over a secure channel that is distinct from the 802.11 wireless network communication channels. The following steps illustrate the establishment of a connection in the shared key authentication process:
o The station sends an authentication frame to the AP. o The AP sends a challenge text to the station.
o The station encrypts the challenge text using its configured 64-bit or 128-bit key and sends the encrypted text to the AP.
o The AP uses its configured Wired Equivalent Privacy (WEP) key to decrypt the encrypted text. The AP compares the decrypted text with the original challenge text. If they match, the AP authenticates the station.
o The station connects to the network.
The AP can reject the station if the decry

Open system authentication process: In this process, any wireless client that attempts to access a Wi-Fi network sends a request to the wireless AP for authentication. In this process, the station sends an authentication management frame containing the identity of the sending station for authentication and connection with the other wireless station, which is the wireless AP. The AP then returns an authentication frame to confirm access to the requested station, thereby completing the authentication process.

#wireless encryption
802.11i: It is an IEEE amendment that specifies security mechanisms for 802.11 wireless networks.
 WEP: WEP is an encryption algorithm for IEEE 802.11 wireless networks. It is an old wireless security standard and can be cracked easily.
 EAP: The Extensible Authentication Protocol (EAP) supports multiple authentication methods, such as token cards, Kerberos, and certificates.
LEAP: Lightweight EAP (LEAP) is a proprietary version of EAP developed by Cisco.  WPA: It is an advanced wireless encryption protocol using TKIP and Message Integrity Check (MIC) to provide strong encryption and authentication. It uses a 48-bit initialization vector (IV), 32-bit cyclic redundancy check (CRC), and TKIP encryption for wireless security.
 TKIP: It is a security protocol used in WPA as a replacement for WEP.  WPA2: It is an upgrade to WPA using AES and the Counter Mode Cipher Block Chaining Message Authentication Code Protocol (CCMP) for wireless data encryption.
 AES: It is a symmetric-key encryption used in WPA2 as a replacement for TKIP.  CCMP: It is an encryption protocol used in WPA2 for strong encryption and authentication.
 WPA2 Enterprise: It integrates EAP standards with WPA2 encryption.  RADIUS: It is a centralized authentication and authorization management system.  PEAP: It is a protocol that encapsulates the EAP within an encrypted and authenticated Transport Layer Security (TLS) tunnel.
 WPA3: It is a third-generation Wi-Fi security protocol that provides new features for personal and enterprise usage. It uses Galois/Counter Mode-256 (GCMP-256) for encryption and the 384-bit hash message authentication code with the Secure Hash Algorithm (HMAC-SHA-384) for authentication.

WEP is a component of the IEEE 802.11 WLAN standards. Its primary purpose is to ensure data confidentiality on wireless networks at a level equivalent to that of wired LANs, which can use physical security to stop unauthorized access to a network. In a WLAN, a user or an attacker can access the network without physically connecting to the LAN. Therefore, WEP utilizes an encryption mechanism at the data link layer for minimizing unauthorized access to the WLAN. This is accomplished by encrypting data with the symmetric Rivest Cipher 4 (RC4) encryption algorithm, which is a cryptographic mechanism used to defend against threats. 
 64-bit WEP uses a 40-bit key  128-bit WEP uses a 104-bit key  256-bit WEP uses 232-bit key
It depends on a secret key shared by a mobile station and an AP. This key encrypts packets before transmission. Performing an integrity check ensures that packets are not altered during transmission. 802.11 WEP encrypts only the data between network clients.


How WEP Works  CRC-32 checksum is used to calculate a 32-bit integrity check value (ICV) for the data, which, in turn, is added to the data frame.
 A 24-bit arbitrary number known as the initialization vector (IV) is added to the WEP key; the WEP key and IV are together called the WEP seed.
 The WEP seed is used as the input to the RC4 algorithm to generate a keystream, which is bit-wise XORed with a combination of the data and ICV to produce the encrypted data.
 The IV field (IV + PAD + KID) is added to the ciphertext to generate a MAC frame. 

How WPA Works  A TK, transmit address, and TKIP sequence counter (TSC) are used as input to the RC4 algorithm to generate a keystream. o The IV or TK sequence, transmit address or MAC destination address, and TK are combined with a hash function or mixing function to generate a 128-bit and 104-bit key.
o This key is then combined with RC4 to produce the keystream, which should be of the same length as the original message.
 The MAC service data unit (MSDU) and message integrity check (MIC) are combined using the Michael algorithm.
 The combination of MSDU and MIC is fragmented to generate the MAC protocol data unit (MPDU).
 A 32-bit ICV is calculated for the MPDU.  The combination of MPDU and ICV is bitwise XORed with the keystream to produce the encrypted data.
 The IV is added to the encrypted data to generate the MAC frame. 

Wi-Fi Protected Access (WPA) Encryption
Wi-Fi Protected Access (WPA) is a security protocol defined by the 802.11i standard. In the past, the primary security mechanism used between wireless APs and wireless clients was WEP encryption, which has a major drawback in that it uses a static encryption key. An attacker can exploit this weakness using tools that are freely available on the Internet. IEEE defines WPA as “an expansion to the 802.11 protocols that can allow for increased security.” Nearly every Wi-Fi manufacturer provides WPA.
WPA has better data encryption security than WEP because messages pass through a Message Integrity Check (MIC) using the Temporal Key Integrity Protocol (TKIP), which utilizes the RC4 stream cipher encryption with 128-bit keys and 64-bit MIC to provide strong encryption and authentication. WPA is an example of how 802.11i provides stronger encryption and enables pre-shared key (PSK) or EAP authentication. WPA uses TKIP for data encryption, which eliminates the weaknesses of WEP by including per-packet mixing functions, MICs, extended IVs and re-keying mechanisms. 

WPA2 Encryption
Wi-Fi Protected Access 2 (WPA2) is a security protocol used to safeguard wireless networks. WPA2 replaced WPA in 2006. It is compatible with the 802.11i standard and supports many security features that WPA does not. WPA2 introduces the use of the National Institute of Standards and Technology (NIST) FIPS 140-2-compliant AES encryption algorithm, which is a strong wireless encryption algorithm, and the Counter Mode Cipher Block Chaining Message Authentication Code Protocol (CCMP). It provides stronger data protection and network access control than WPA. Furthermore, it gives a high level of security to Wi-Fi connections so that only authorized users can access the network.

WPA3 Encryption
Wi-Fi Protected Access 3 (WPA3) was announced by the Wi-Fi Alliance on January 2018 as an advanced implementation of WPA2 that provides trailblazing protocols. Like WPA2, the WPA3 protocol has two variants: WPA3-Personal and WPA3-Enterprise. WPA3 provides cutting-edge features to simplify Wi-Fi security and provides the capabilities necessary to support different network deployments ranging from corporate networks to home networks. It also ensures cryptographic consistency using encryption algorithms such as AES and TKIP to defend against network attacks. Furthermore, it provides network resilience through Protected Management Frames (PMF) that deliver a high level of protection against eavesdropping and forging attacks. WPA3 also disallows outdated legacy protocols. 


Issues in WEP
WEP encryption is insufficient to secure wireless networks because of certain issues and anomalies, which include the following.  CRC32 is insufficient to ensure the complete cryptographic integrity of a packet: By capturing two packets, an attacker can reliably flip a bit in the encrypted stream and modify the checksum so that the packet is accepted.
 IVs are of 24 bits: The IV is a 24-bit field, which is too small to be secure, and is sent in the cleartext portion of a message. An AP broadcasting 1500-byte packets at 11 Mbps would exhaust the entire IV space in five hours.
 WEP is vulnerable to known plaintext attacks: When an IV collision occurs, it becomes possible to reconstruct the RC4 keystream based on the IV and the decrypted payload of the packet.
 WEP is vulnerable to dictionary attacks: Because WEP is based on a password, it is prone to password-cracking attacks. The small IV space allows the attacker to create a decryption table, which is a dictionary attack.
 WEP is vulnerable to DoS attacks: This is because associate and disassociate messages are not authenticated.
An attacker can eventually construct a decryption table of reconstructed keystreams: With approximately 24 GB of space, an attacker can use this table to decrypt WEP packets in real time.
 A lack of centralized key management makes it difficult to change WEP keys regularly.  IV is a value used to randomize the keystream value, and each packet has an IV value: The standard IV allows only a 24-bit field, which is too small to be secure, and is sent in the cleartext portion of a message. All available IV values can be used up within hours at a busy AP. IV is a part of the RC4 encryption key and is vulnerable to an analytical attack that recovers the key after intercepting and analyzing a relatively small amount of traffic. Identical keystreams are produced with the reuse of the IV for data protection because the short IV keystreams are repeated within a short time. Furthermore, wireless adapters from the same vendor may all generate the same IV sequence. This enables attackers to determine the keystream and decrypt the ciphertext.
 The standard does not require each packet to have a unique IV: Vendors use only a small part of the available 24-bit possibilities. Consequently, a mechanism that depends on randomness is not random at all, and attackers can easily determine the keystream and decrypt other messages.
 The use of RC4 was designed to be a one-time cipher and not intended for use with multiple messages.


Issues in WPA WPA is an improvement over WEP in many ways because it uses TKIP for data encryption and helps in secured data transfer. However, WPA has many security issues as well. Some of the security issues of WPA are as described follows.
 Weak passwords: If users depend on weak passwords, the WPA PSK is vulnerable to various password-cracking attacks.
 Lack of forward secrecy: If an attacker captures a PSK, they can decrypt all the packets encrypted with that key (i.e., all the packets transmitted or being transmitted can be decrypted).
 Vulnerability to packet spoofing and decryption: Clients using WPA-TKIP are vulnerable to packet-injection attacks and decryption attacks, which further allows attackers to hijack Transmission Control Protocol (TCP) connections.
 Predictability of the group temporal key (GTK): An insecure random number generator (RNG) in WPA allows attackers to discover the GTK generated by the AP. This further allows attackers to inject malicious traffic in the network and decrypt all the transmissions in progress over the Internet.
 Guessing of IP addresses: TKIP vulnerabilities allow attackers to guess the IP address of the subnet and inject small packets into the network to downgrade the network performance.

Issues in WPA2
Although WPA2 is more secure than WPA, it also has some security issues, which are discussed below.  Weak passwords: If users depend on weak passwords, the WPA2 PSK is vulnerable to various attacks such as eavesdropping, dictionary, and password-cracking attacks.
 Lack of forward secrecy: If an attacker captures a PSK, they can decrypt all the packets encrypted with that key (i.e., all the packets transmitted or being transmitted can be decrypted).
 Vulnerability to man-in-the-middle (MITM) and denial-of-service (DoS) attacks: The Hole96 vulnerability in WPA2 allows attackers to exploit a shared group temporal key (GTK) to perform MITM and DoS attacks.
 Predictability of GTK: An insecure random number generator (RNG) in WPA2 allows attackers to discover the GTK generated by the AP. This further allows attackers to inject malicious traffic in the network and decrypt all the transmissions in progress over the Internet.
 KRACK vulnerabilities: WPA2 has a significant vulnerability to an exploit known as key reinstallation attack (KRACK). This exploit may allow attackers to sniff packets, hijack connections, inject malware, and decrypt packets.
 Vulnerability to wireless DoS attacks: Attackers can exploit the WPA2 replay attack detection feature to send forged group-addressed data frames with a large PN to perform a DoS attack.
 Insecure WPS PIN recovery: In some cases, disabling WPA2 and WPS can be a time-consuming process, in which the attacker needs to control the WPA2 PSK used by the clients. When WPA2 and WPS are enabled, the attacker can disclose the WPA2 key by determining the WPS personal identification number (PIN) through simple steps.


Access Control Attacks Wireless access-control attacks aim to penetrate a network by evading WLAN access-control measures, such as AP MAC filters and Wi-Fi port access controls.
WarDriving: In a wardriving attack, WLANs are detected either by sending probe requests over a connection or by listening to web beacons. An attacker who discovers a penetration point can launch further attacks on the LAN. Some of the tools that the attacker may use to perform wardriving attacks are KisMAC and NetStumbler.
 Rogue access points: In order to create a backdoor to a trusted network, an attacker may install an unsecured AP or fake AP inside a firewall. The attacker may also use software or hardware APs to perform this kind of attack. A wireless AP is termed a rogue access point when it is installed on a trusted network without authorization. An inside or outside attacker can install rogue APs on a trusted network with malicious intentions.
 MAC spoofing: Using the MAC spoofing technique, an attacker can reconfigure a MAC address to appear as an authorized AP to a host on a trusted network. The attacker may use tools such as SMAC to perform this kind of attack.
 AP misconfiguration: If a user improperly configures any of the critical security settings at any of the APs, the entire network could be exposed to vulnerabilities and attacks. The AP cannot trigger alerts in most intrusion-detection systems, because these systems recognize them as a legitimate device.
 Ad hoc associations: An attacker may perform this kind of attack using any Universal Serial Bus (USB) adapter or wireless card. The attacker connects the host to an unsecured client to attack a specific client or to avoid AP security.
Promiscuous client: Using a promiscuous client, an attacker exploits the behavior of 802.11 wireless cards: they always attempt to find a stronger signal to connect. An attacker places an AP near the target Wi-Fi network and gives it a common SSID, offering an irresistibly stronger signal and higher speed than the target Wi-Fi network. The intent is to lure the client to connect to the attacker's AP, rather than a legitimate Wi-Fi network. Promiscuous clients allow an attacker to transmit target network traffic through a fake AP. It is very similar to the evil-twin threat on wireless networks, in which an attacker launches an AP that poses as an authorized AP by beaconing the WLAN's SSID.
 Client mis-association: The client may intentionally or accidentally connect or associate with an AP outside the legitimate network because the WLAN signals travel through the air, walls, and other obstructions. This kind of client mis-association can lead to access-control attacks.
 Unauthorized association: Unauthorized association is a major threat to wireless networks. The prevention of this kind of attack depends on the method or technique that the attacker uses to get associated with a network.


Integrity Attacks
An integrity attack involves changing or altering data during transmission. In wireless integrity attacks, attackers send forged control, management, or data frames over a wireless network to

Confidentiality Attacks
These attacks attempt to intercept confidential information sent over a wireless network, regardless of whether the system transmits data in cleartext or an encrypted format. If the system transmits data in an encrypted format (such as WEP or WPA), an attacker may attempt to break the encryption. The below table summarizes different types of confidentiality attacks on wireless networks.


Availability Attacks Availability attacks aim at obstructing the delivery of wireless services to legitimate users, either
by crippling WLAN resources or by denying them access to these resources. This attack makes wireless network services unavailable to legitimate users. Attackers can perform availability attacks in various ways, obstructing the availability of wireless networks. The below table summarizes different types of availability attacks on wireless networks.

Authentication Attacks
The objective of authentication attacks is to steal the identity of Wi-Fi clients, their personal information, login credentials, etc. to gain unauthorized access to network resources. The below table summarizes different types of authentication attacks on wireless networks.

Rogue AP Attack
APs connect to client NICs by authenticating with the help of SSIDs. Unauthorized (or rogue) APs can allow anyone with an 802.11-equipped device to connect to a corporate network. An unauthorized AP can give an attacker access to the network. 

Client Mis-Association Mis-association is a security flaw that can occur when a network client connects with a
neighboring AP. Client mis-associations can occur for various reasons such as misconfigured clients, insufficient coverage of corporate Wi-Fi, lack of a Wi-Fi policy, restrictions on the use of Internet in the office, ad-hoc connections that administrators do not manage regularly, and attractive SSIDs. They can occur with or without the knowledge of the wireless client and rogue AP.
To perform a client mis-association attack, an attacker sets up a rogue AP outside the corporation’s perimeter. The attacker first learns the SSID of the target wireless network. Using a spoofed SSID, the attacker may send beacons advertising the rogue AP in order to lure clients to connect. The attacker can use the rogue AP as a channel to bypass enterprise security policies. Once a client connects to the rogue AP, an attacker can retrieve sensitive information such as usernames and passwords by launching MITM, EAP dictionary, or Metasploit attacks to exploit client mis-association.

Misconfigured AP Attack Most organizations spend significant amounts of time defining and implementing Wi-Fi security policies, but it may be possible for a client of a wireless network to change the security settings of an AP unintentionally. This, in turn, may lead to misconfigurations in APs. A misconfigured AP can expose an otherwise well-secured network to attacks. It is difficult to detect a misconfigured AP because it is an authorized, legitimate device on the network. Attackers can easily connect to a secured network through misconfigured APs, which continue to function normally after an attacker connects because no alerts will be triggered even if the attacker uses the connection to compromise security. 

Unauthorized Association
Unauthorized association is a major threat to wireless networks. It has two forms: accidental association and malicious association. An attacker performs malicious association with the help of soft APs instead of corporate APs. The attacker creates a soft AP, typically on a laptop, by running a tool that makes the laptop’s NIC appear as a legitimate AP. 

Ad-Hoc Connection Attack Wi-Fi clients can communicate directly via an ad-hoc mode that does not require an AP to relay packets. Data can be conveniently shared among clients in ad-hoc networks, which are quite popular among Wi-Fi users. Security threats arise when an attacker forces a network to enable the ad-hoc mode. Some network resources are accessible only in the ad-hoc mode, but this mode is inherently insecure and does not provide strong authentication or encryption. Thus, an attacker can easily connect to and compromise a client operating in the ad-hoc mode. An attacker who penetrates a wireless network can also use an ad-hoc connection to compromise the security of the organization’s wired LAN.

Honeypot AP Attack
If multiple WLANs co-exist in the same area, a user can connect to any available network. Such areas are vulnerable to attacks. Normally, when a wireless client is switched on, it probes a nearby wireless network for a specific SSID. An attacker takes advantage of this behavior of wireless clients by setting up an unauthorized wireless network using a rogue AP. This AP has high-power (high-gain) antennas and uses the same SSID as the target network. Users who regularly connect to multiple WLANs may connect to the rogue AP. Such APs mounted by attackers are called “honeypot” APs. They transmit a stronger beacon signal than legitimate APs so that NICs searching for the strongest available signal may connect to the rogue AP. If an authorized user connects to a honeypot AP, a security vulnerability is created and sensitive user information such as identity, username, and password may be revealed to the attacker.

AP MAC Spoofing In wireless networks, the transmit probes of APs respond through beacons to advertise presence and availability. The probe responses contain information on the AP identity (MAC address) and the identity of the network it supports (SSID). Clients in the vicinity connect to the network through these beacons based on the MAC address and the SSID it contains. Many software tools and APs allow setting user-defined values for the MAC addresses and SSIDs of AP devices. An attacker can spoof the MAC address of the AP by programming a rogue AP to advertise the same identity information as that of the legitimate AP. An attacker connected to the AP as an authorized client can have full access to the network. This type of attack succeeds when the target wireless network uses MAC filtering to authenticate clients (users).


Denial-of-Service Attack
Wireless networks are susceptible to DoS attacks. These networks operate in unlicensed bands with data transmission in the form of radio signals. The designers of the MAC protocol aimed at simplicity, but it is vulnerable to DoS attacks. WLANs usually carry mission-critical applications such as VoIP, database access, project data files, and Internet access. Disrupting these applications on WLANs through a DoS attack is easy and can cause a loss of productivity or network downtime. Examples of MAC DoS attacks are de-authentication flood attacks, virtual jamming, and association flood attacks. Wireless DoS attacks disrupt wireless network connections by broadcasting de-authenticate commands. The transmitted de-authentication forces the clients to disconnect from the AP.

Key Reinstallation Attack (KRACK)
The key reinstallation attack (KRACK) exploits the flaws in the implementation of the four-way handshake process in the WPA2 authentication protocol, which is used to establish a connection between a device and an AP. All secure Wi-Fi networks use the four-way handshake process to establish connections and to generate a fresh encryption key that will be used to encrypt the network traffic.
Figure 16.23: Four-way handshake process in WPA2
The attacker exploits the four-way handshake of the WPA2 protocol by forcing Nonce reuse. In this attack, the attacker captures the victim’s ANonce key that is already in use to manipulate and replay cryptographic handshake messages. This attack works against all modern protected Wi-Fi networks (both WPA and WPA2); personal and enterprise networks; and the ciphers WPA-TKIP, AES-CCMP, and GCMP. It allows the attacker to steal sensitive information such as credit-card numbers, passwords, chat messages, emails, and photos. Any device that runs Android, Linux, Windows, Apple, OpenBSD, or MediaTek are vulnerable to some variant of the KRACK attack.


Jamming Signal Attack
Jamming is an attack performed on a wireless network to compromise it. In this type of exploitation, overwhelming volumes of malicious traffic result in a DoS to authorized users, obstructing legitimate traffic. All wireless networks are prone to jamming, and spectrum jamming attacks usually block all communications completely.

aLTEr Attack
Long-Term Evolution (LTE), or 4G, is wireless broadband communication standard developed as a successor to 3G to improve the speed and security of wireless mobile networks. It features bandwidth scalability and supports preceding technologies, such as the Global System for Mobile Communications (GSM; 2G) and Universal Mobile Telecommunications System (UMTS; 3G). Although the technology is designed to overcome all the shortcomings of wireless networks, it is susceptible to data hijacking attacks. The aLTEr attack is usually performed on LTE devices that encrypt user data in the AES counter (AES-CTR) mode, which provides no integrity protection. To perform this attack, the attacker installs a virtual (fake) communication tower between two authentic endpoints to mislead the victim. The attacker uses this virtual tower to interrupt the data transmission between the user and real tower, attempting to hijack an active session. Upon receiving the user’s request, the attacker manipulates the traffic with the virtual tower and redirects the victim to malicious websites.
This attack is carried out on “Layer 2,” known as the datalink layer, which is responsible for sharing information through wireless networks with standard data encryption technologies. It also enables multiple users to access the network resources and defines how to transfer data between two nodes without any obstacles. By leveraging vulnerabilities or design flaws within this layer, the attacker attempts to take control over browsing data and modifies user inputs with a spoofed DNS server, redirecting the user to unintended or harmful websites. The steps involved in an aLTEr attack are summarized as follows. 

Wormhole Attack
A wormhole attack exploits dynamic routing protocols such as Dynamic Source Routing (DSR) and the Ad-Hoc On-Demand Distance Vector (AODV). In this attack, an attacker locates themselves strategically in the target network to sniff and record ongoing wireless transmissions. From this location, the attacker advertises that the malicious node has the shortest route for transmitting data to other nodes in the network. To perform sniffing and to record the ongoing communication, the attacker creates a tunnel to forward the data between the source and destination node.

Sinkhole Attack
A sinkhole attack is a variant of the selective forwarding attack in which the attacker advertises a compromised or malicious node as the shortest possible route to the base station. The attacker places the malicious node near the base station and attracts all the neighboring nodes
with fake routing path information and further performs a data forging attack. Attackers use the compromised node to sniff and manipulate all ongoing network transmissions.
A sinkhole attack can also be performed simultaneously with a wormhole attack, where the malicious node can occupy all the network traffic and use the tunneling technique to reach the base station faster than other nodes. A sinkhole attack is complex to detect, and it can adversely affect higher-layer applications in the Open Systems Interconnection (OSI) model.



 steps: Wi-Fi discovery  GPS mapping  Wireless traffic analysis  Launch of wireless attacks  Wi-Fi encryption cracking  Wi-Fi network compromisin