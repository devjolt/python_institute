from random import choice
from ceh.utilities import utilities as utl

from ._19_logic import *

"""
question_logic={
                'correct_incorrect':utl.make_items_question_from_correct_incorrect,
                'multi_from_correct':utl.multi_option_from_correct_incorrect,
                'old_pairs':utl.make_items_question_from_pairs,
                'posneg_pairs':utl.posneg_pairs,
                'new_pairs':utl.new_pairs,
                'multi_option_pairs':utl.multi_option_pairs,
                'order_from_pairs':utl.order_from_pairs
            }

resource = {
    'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
    'question_with_1':'What best describes the following: PLACEHOLDER?',
    'positive_negative':('',' not'),
    'question_order':'What best describes the killchain from PLACEHOLDER?',
    'ascending_descending':('first to last', 'last to first'),
    'type':['vanilla_pairs','posneg_pairs', 'multi_pairs', 'order_pairs'],
    'course_code':'',
    'pairs':[
        ('correct',['A','B','C','D']),
        ('incorrect',['1', '2', '3','4']),
        ('ambiguous',['0', '9', '8','7']),
        
    ],
    'fillers': (
        ('backwards',['z', 'y', 'x','w']),
    )
},



'definition of attack': {
'question_with_0':'which of the following POSNEG PLACEHOLDER?',
'positive_negative':('are','could not be described as'),
'type':['posneg_pairs', 'multi_option_pairs'],
'course_code':'1',
'pairs':(
    ('elements of an attack', ['motive','goal','method','vulnerability']),
    ('something other than the elements of an attack', ['risk','threat','identification','disruption','backdoor']),
),
'fillers': ([])  
},

'formula of attack': {
'question':'Which of the following PLACEHOLDERcorrectly describes the formula of an attack?',
'type':'correct_incorrect',
'positive':'',
'negative':'in',
'course_code':'',
'correct':(
    'attacks = motive + method + vulnerability',
    'attacks = goal + method + vulnerability',
    'attacks=goal+method+vulnerability',
),
'incorrect': (
    f"attacks = goal + method + {choice(words)}",
    f"attacks = goal + {choice(words)} + vulnerability",
    f"attacks = {choice(words)} + method + vulnerability",
),
},

resource = {
        'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['multi_pairs'],
        'course_code':'',
        'pairs':[
            ('correct',['A','B','C','D']),
            ('incorrect',['1', '2', '3','4']),
            ('ambiguous',['0', '9', '8','7']),
            
        ],
        'fillers': (
            ('backwards',['z', 'y', 'x','w']),
        )
    }

"""

questions = {

}

"""
concepts


('cloud computing','IT infrastructure and applications are provided to subscribers as metered services over networks'),
('On-demand self-service',['A type of service rendered by cloud service providers that allow provisions for cloud resources','could include computing power, storage, and network','always on-demand, without the need for human interaction with the service providers']),
('Distributed storage',['Distributed storage in the cloud offers better scalability, availability, and reliability of data','can potentially raise security and compliance concerns']),
('Rapid elasticity',['instant provisioning of capabilities to rapidly scale up or down, according to demand','the resources available for provisioning seem to be unlimited and can be purchased in any quantity at any point of time']),
('Automated management','speeds up the process and reduces labor costs and the possibility of human error'),
('Broad network access',['resources are available over the network','accessed through standard procedures via a wide variety of platforms, including laptops, mobile phones, and personal digital assistants']),
('Resource pooling',['service provider servea multiple customers in the multi-tenant environment','physical and virtual resources dynamically assigned and reassigned on demand by the consumer of the cloud']),
('Measured service',['pay-per-use metering method','Subscribers pay for cloud services by monthly subscription or according to the usage of resources','ca include storage levels, processing power, and bandwidth','providers monitor, control, report, and charge consumption of resources by customers with complete transparency']),
('Virtualization technology','enables the rapid scaling of resources in a way that non-virtualized environments cannot achieve')


Limitations of Cloud Computing  Limited control and flexibility of organizations  Proneness to outages and other technical issues  Security, privacy, and compliance issues  Contracts and lock-ins  Dependence on network connections  Potential vulnerability to attacks as every component is online  Difficulty in migrating from one service provider to another


types of cloud computing services


(['Infrastructure-as-a-Service','IaaS'],['enables subscribers to use on-demand fundamental IT resources, such as computing power, virtualization, data storage, and network','provides virtual machines and other abstracted hardware and operating systems (OSs)','may be controlled through a service application programming interface (API)','service providers are responsible for managing the underlying cloud computing infrastructure, subscribers can avoid costs of human capital, hardware, and others','Amazon EC2','GoGrid','Microsoft OneDrive','Rackspace']),
(['Platform-as-a-Service','PaaS'],['allows for the development of applications and services','Subscribers need not buy and manage software and infrastructure underneath it but have authority over deployed applications and perhaps application hosting environment configurations','offers development tools, configuration management, and deployment platforms on-demand, which can be used by subscribers to develop custom applications','Google App Engine','Salesforce','Microsoft Azure']),
(['Software-as-a-Service','SaaS'],['offers application software to subscribers on-demand over the Internet','provider charges for the service on a pay-per-use basis, by subscription, by advertising, or by sharing among multiple users','web-based office applications like Google Docs or Calendar','Salesforce CRM','Freshbooks']),
(['Identity-as-a-Service','IDaaS'],['offers authentication services to the subscribed enterprises and is managed by a third-party vendor to provide identity and access management services','provides services such as Single-Sign-On (SSO), Multi-Factor-Authentication (MFA), Identity Governance and Administration (IGA), access management, and intelligence collection','allow subscribers to access sensitive data more securely both on and off-premises','OneLogin','Centrify Identity Service','Microsoft Azure Active Directory','Okta']),
(['Security-as-a-Service','SECaaS'],['integrates security services into corporate infrastructure in a cost-effective way','developed based on SaaS and does not require any physical hardware or equipment','drastically reduces the cost compared to that spent when organizations establish their own security capabilities','provides services such as penetration testing, authentication, intrusion detection, anti-malware, security incident and event management','eSentire MDR','Switchfast Technologies','OneNeck IT Solutions']),
(['Container-as-a-Service','CaaS'],['provides containers and clusters as a service to its subscribers','provides services such as virtualization of container engines, management of containers, applications, and clusters through a web portal, or an API','subscribers can develop rich scalable containerized applications through the cloud or on-site data centers','inherits features of both IaaS and PaaS','Amazon AWS EC2','Google Kubernetes Engine (GKE)']),
(['Function-as-a-Service','FaaS'],['provides a platform for developing, running, and managing application functionalities without the complexity of building and maintaining necessary infrastructure (serverless architecture)','mostly used while developing applications for microservices','provides on-demand functionality to the subscribers that powers off the supporting infrastructure and incurs no charges when not in use','provides data processing services, such as Internet of Things (IoT) services for connected devices, mobile and web applications, and batch-and-stream processing','AWS Lambda','Google Cloud Functions','Microsoft Azure Functions','Oracle Cloud Fn']),

(f"an advantage of {choice['Infrastructure-as-a-Service','IaaS']}",['Dynamic infrastructure scaling','Guaranteed uptime','Automation of administrative tasks','Elastic load balancing (ELB)','Policy-based services','Global accessibility']),
(f"an advantage of {choice['Platform-as-a-Service','PaaS']}",['Simplified deployment','Prebuilt business functionality','Lower security risk compared to IaaS','Instant community','Pay-per-use model','Scalability']),
(f"an advantage of {choice['Software-as-a-Service','SaaS']}",['Low cost','Easy administration','Global accessibility','High compatibility (no specialized hardware or software is required']),
(f"an advantage of {choice['Identity-as-a-Service','IDaaS']}",['Low cost','Improved security','Simplify compliance','Reduced time','Central management of user accounts']),
(f"an advantage of {choice['Security-as-a-Service','SECaaS']}",['Low cost','Reduced complexity','Continuous protection','Improved security through best security expertise','Latest and updated security tools','Rapid user provisioning','Greater agility','Increased time on core competencies']),
(f"an advantage of {choice['Container-as-a-Service','CaaS']}",['Streamlined development of containerized applications','Pay-per-resource','Increased quality','Portable and reliable application development','Low cost','Few resources','Crash of application container does not affect other containers','Improved security','Improved patch management','Improved response to bugs','High scalability','Streamlined development']),
(f"an advantage of {choice['Function-as-a-Service','FaaS']}",['Pay-per-use','Low cost','Efficient security updates','Easy deployment','High scalability']),
(f"a disadvantage of {choice['Infrastructure-as-a-Service','IaaS']}",['Software security is at high risk (third-party providers are more prone to attacks)','Performance issues and slow connection speeds']),
(f"a disadvantage of {choice['Platform-as-a-Service','PaaS']}",['Vendor lock-in','Data privacy','Integration with the rest of the system applications']),
(f"a disadvantage of {choice['Software-as-a-Service','SaaS']}",['Security and latency issues','Total dependency on the Internet','Switching between SaaS vendors is difficult']),
(f"a disadvantage of {choice['Identity-as-a-Service','IDaaS']}",['Single server failure may disrupt the service or create redundancy on other authentication servers','Vulnerable to account hijacking attacks']),
(f"a disadvantage of {choice['Security-as-a-Service','SECaaS']}",['Increased attack surfaces and vulnerabilities','Unknown risk profile','Insecure APIs','No customization to business needs','Vulnerable to account hijacking attacks']),
(f"a disadvantage of {choice['Container-as-a-Service','CaaS']}",['High operational overhead','Platform deployment is the developer’s responsibility']),
(f"a disadvantage of {choice['Function-as-a-Service','FaaS']}",['High latency','Memory limitations','Monitoring and debugging limitations','Unstable tools and frameworks','Vendor lock-in'])


seperation of responsiblities

('on-premesis',['subscriber responsible for applications, data, runtime, middleware, OS, virtualisation, servers, storage, networking', 'service provider responsible for nothing']),
(['Infrastructure-as-a-Service','IaaS'],['subscriber responsible for applications, data, runtime, middleware and OS','service provider responsible for virtualisation, servers, storage and networking']),
(['Platform-as-a-Service','PaaS'],['subscriber responsible for applications and data','service provider responsible for runtime, middleware OS, virtualisation, servers, storage and networking']),
(['Software-as-a-Service','SaaS'],['service provider responsible for applications, data, runtime, middleware, OS, virtualisation, servers, storage, networking', 'subscriber responsible for nothing']),

cloud deployment modeels

NIST reference architecture

('cloud consumer',['person or organization that maintains a business relationship with the cloud service providers (CSPs) and utilizes the cloud computing services','browses the CSP\'s service catalog requests for the desired services','sets up service contracts with the CSP (either directly or via cloud broker)','billed based on the services provided','specifies service level agreement detailing the technical performance requirements, such as the quality of service, security, and remedies for performance failure','must accept limitations and obligations defined by CSP']),
('cloud provider','person or organization who acquires and manages the computing infrastructure intended for providing services (directly or via a cloud broker) to interested parties via network access']),
('cloud carrier',['acts as an intermediary that provides connectivity and transport services between CSPs and cloud consumers','provides access to consumers via a network, telecommunication, or other access devices']),
('cloud auditor',['party that performs an independent examination of cloud service controls to express an opinion thereon','can evaluate the services provided by a CSP regarding security controls (management, operational, and technical safeguards intended to protect the confidentiality, integrity, and availability of the system and its information), privacy impact (compliance with applicable privacy laws and regulations governing an individual\'s privacy), performance']),
('cloud broker','entity that manages cloud services regarding use, performance, and delivery and maintains the relationship between CSPs and cloud consumers'),
('Service Intermediation','Improves a given function by a specific capability and provides value-added services to cloud consumers'),
('Service Aggregation','Combines and integrates multiple services into one or more new services'),
('Service Arbitrage','Similar to service aggregation but without the fixing of the aggregated services (the cloud broker can choose services from multiple agencies)'),


containers

Portability and consistency An application or software developed in a container includes all the resources required to perform. This portability helps clients or end-users run an application on various platforms and private or public cloud environments.
 Security Owing to the independent nature of containers, security risks are reduced. If an
application is attacked or compromised, its infections do not extend across the remaining containers.
 High efficiency and cost effectiveness Containers can run with fewer resources compared to virtual machines (VMs) because they do not need independent operating systems. Additionally, containers need a few megabytes of memory to run, enabling users to run multiple containers on a single server. These containers are isolated in a cloud server because if an application is down for one container, other containers can utilize it without technical glitches.
 Scalability
Containers are scalable and enable subscribers or users to integrate more similar containers under the same cluster to increase their size. The smart scaling technology enables users to run only the intended container and put unwanted containers at rest, making it cost-effective.
Robustness
Containers can be generated, deployed, and destroyed in seconds because they do not require operating systems. This feature allows a quick development process, increased operational speed, and the launch of new software versions within the specified time. It also speeds up the user’s experience with the application, making it easier for developers and organizations to quickly address bugs and integrate the latest features.

Container Technology Architecture
As shown in the below figure, container technology has a five-tier architecture and undergoes a three-phase lifecycle:  Tier-1: Developer machines - image creation, testing and accreditation  Tier-2: Testing and accreditation systems - verification and validation of image contents, signing images and sending them to the registries
 Tier-3: Registries - storing images and disseminating images to the orchestrators based on requests
 Tier-4: Orchestrators - transforming images into containers and deploying containers to hosts
 Tier-5: Hosts - operating and managing containers as instructed by the orchestrator 




serverless

threats

hacking

security measures

tools



"""