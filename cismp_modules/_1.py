from random import randint

from ._1_logic import *

questions = {
    'terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            (['SIEM','security information and event management'],['software products and services combine security information management and security event management', 'real-time analysis of security alerts generated by applications and network hardware.']),
            ('volitile','forensic computer evidence such as cached data'),
            ('steganography','technology used to hide secret messages inside other messages or images'),
            ('hardening', 'securing a system by closing vulnerabilities'),
            ('repudiating', 'when someone sends and email pretending to be someone else'),
            ('ITIL', 'set of detailed practices for IT activities such as IT service management and IT asset management that focus on aligning IT services with the needs of business'), 
            ('Computer security should', 'be proportionate to the value of IT systems'), 
            ('employees', 'the leading source of computer crime losses'),
            ('Authorization', 'determines who is trusted for a given purpose'),
            ('audit trails ', 'required in order to provide accountability'),
            ('ISO 27002', 'determines who is trusted for a given purpose'),
            ('business impact',' effect on an organisation of a vulnerability being exploited'),
            ('security policy','sets out the organisation\'s formal stance on security for staff and contractors to see'),
            ('risk assessment', 'compile a risk register against all information assets'),
            ('Objective evidence', 'Information which can be proved true through observation, documents, records, orpersonal interview'),
            ('Classification labelling of information', 'a control which helps to protect against unintentional disclosure ofinformation'),
            ('the major purpose of information security in an organisation','supporting the effective and efficient achievement of the organisation\�s businessobjectives'),
            ('seperation of duties', 'the principle that no user should be given enough privileges to misuse the system on their own'),
            ('assurance', 'the amount of confidence that an organisation has that its controls satisfy necessary security requirements'),
            ('non-repudiation', ['the ability to prove that an event occurred','Protects against a person denying later that a communication or transaction tookplace']), 
            ('fail secure', 'disconnecting a system if an event occurs'),
            ('symmetric key encryption', 'the use of public key cryptography to prevent the republishing of keys'),
            ('defence in depth', ['the concept used in information security in which multiple layers of security controls are placed within a system','requires that an organisation should implement overlapping secuirty controls']),
            (['impact','likelihood'], ['one of the two terms used in combination to define levels of risk']),
            ('risk appetite', 'the amount and type of risk that an organisation is prepared to pursue, retain or take'),
            ('risk tolerance', 'the amount and type of risk that an organisation takes'),
            ('improved resilience against and recovery time from a harmful incident', ['the primary benefit of implementing appropriate information security within an organisation']),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['Open Source Intelligence', 'OSINT'], 'the collection andanalysis of information that is gathered from public sources'),
            (['the MOST IMPORTANT role of senior management in regard to information security'], ['Providing visible and material support for information security within the organisation']),
            ('Privacy', ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            (['Intellectual Property', 'IP'], ['the legal rights which result from activity in the industrial, scientific, literary and artistic fields']),
            (['ISO/IEC 27001'], ['a specification for an Information Security Management System']),
            (['ISO/IEC 27002'], ['information Security Management System implementation guidance']),
            (['ISO/IEC 15408'], ['the standards relating to the certification of security products']),
            (['ISO/IEC 24762', 'BS2577'], ['the standards relating to disaster recovery']),
            (['ISO/IEC 22301'], ['the standards relating to business continuity']),
            (['NIST 800-53'], ['provides a catalog of security and privacy controls for all U.S. federal information systems except those related to national security']),
            (['ISACA', 'Information Systems Audit and Control Association'], [' international professional association focused on IT governance']),
            (['SABSA', 'Sherwood Applied Business Security Architecture'], ['a framework and methodology for enterprise security architecture and service management']),
            (['OWASP', 'The Open Web Application Security Project'], ['an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security']),
            (['DevSecOps'], ['an approach to culture, automation, and platform design that integrates security as a shared responsibility throughout the entire IT lifecyclemm']),
            (['BS25999-1'], ['general guidance on the processes, principles and terminology']),
            (['BS25999-2'], ['a set of requirements for implementing, operating and improving a BCM System']),
            (['BS25777'], ['the collection andanalysis of information that is gathered from public sources']),
            (['ISO/IEC 27017'], ['the standards relating to practice for information security controls for cloud sevices']),
            (['ISO 31000'], ['an information risk management standard for any industry']),
            (['ISO 9001'], ['a quality manament standard']),
            (['need to know basis'], ['preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable']),
            (['flow down'], ['the passing on of contractual obligations from a supplier to a third party organisation']),
            (['ISMS','information security management system'], 'defines and manages controls that an organization needs to implement to ensure that it is sensibly protecting the confidentiality, availability, and integrity of assets from threats and vulnerabilities'),
            (['CMBD','configuration management database'],'a list of information about all assets in a system'),
            (['Business continuity and disaster recovery'], ['a set of processes and techniques used to help an organization recover from a disaster and continue or resume routine business operations']),
            (['SIEM'], ['aggregates and analyses activity from many different entities on a network']),
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
    'steps in setting out an information classification strategy': {
       
    'question':'What is the first step you should take when setting out an information classification strategy?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'',
        'course_code':'',
        'correct':(
            'determine the classification programme objectives',
        ),
        'incorrect': (
            'identify relevant information and process owners',
            'agree the relevant information classification labels',
            'develop the information classification policy',    
        ),
    },

    'information management cycle important': {
        'question':'From a security viewpoint, why is the information management cycle important?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'',
        'course_code':'',
        'correct':(
            'It reduces risk',
        ),
        'incorrect': (
            'It reduces costs',
            'It improves compliance',
            'It improves service',    
        ),
    },
    'confientiality integrity': {
        'question':'Which of the following CIA principles can be applied to ensure PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'confidentiality',
        'negative':'integrity',
        'course_code':'',
        'correct':(
            'encryption',
            'shredding',
            'lockable cabinets',
            'categorising documents', 
            'access control'
        ),
        'incorrect': (
            'hashing',
            'data validation',
            'input validation',
            'audit trails'
        ),
    },
    'confientiality availability': {
        'question':'Which of the following CIA techniques can be used to ensure PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'confidentiality',
        'negative':'availability',
        'course_code':'',
        'correct':(
            'encryption',
            'shredding',
            'lockable cabinets',
            'categorising documents', 
            'access control'
        ),
        'incorrect': (
            'backups',
            'use of redundancy',
            'failover',
            'RAID'
        ),

    
    },
    'integrity availability': {
        'question':'Concidering the CIA triad, which of the following techniques can be used to ensure PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'integrity',
        'negative':'availability',
        'course_code':'',
        'correct':(
            'hashing',
            'data validation',
            'input validation',
            'audit trails'
        ),
        'incorrect': (
            'backups',
            'use of redundancy',
            'failover',
            'RAID'
        ),
    },

    'cloud service contract': {
        'question':'When setting up a contract with a cloud services supplier, which of the following safeguards is PLACEHOLDER important?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'most',
        'negative':'not',
        'course_code':'',
        'correct':(
            'The ability to recover all information from the cloud if the contract is terminated',
            'The confidentiality and integrity of downloading information from the cloud',
            'The service level requirement for availability of the information'
        ),
        'incorrect': (
            'The make of hardware used by the hosting supplier',
            'The make of software used by the hosting supplier',
            'The location of the servers of the hosting supplier',
        ),
    },
    'integrity, availability and accountability': {
        'question_with_0':'Which of the following best describes PLACEHOLDER?',
        'question_with_1':'If PLACEHOLDER is important, which of the following would be the priority?',
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            ('integrity',['the accuracy of information', 'the completeness of information', 'guarantee that the message sent is the message received, and that the message was not intentionally or unintentionally altered']),
            ('confidentiality',['the privacy of information', 'information only being seen by those who are intended']),
            ('availability',['the accessibility of information','information being to hand when required']),
            
        ),
        'fillers': (
            (['applicability', 'security', 'scarcity','visiblity'], ['the safety of employees', 'the safety of servers', 'the speed of a processor', 'the size of storage'])
        )
    },
    'three pillars': {
        'question':'Which of the following is PLACEHOLDER one of the pillars of information security:',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'confidentiality',
            'availability',
            'integrity'
        ),
        'incorrect': (
            'strategy',
            'discretionary',
            'usability',
            'strategy',
            'risk avoidance',
            'managability',
        ),
    },
    'Good security practise': {
        'question':'Which of the following PLACEHOLDER correctly describe �good� security practice?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'does not',
        'course_code':'',
        'correct':(
            'Accounts should be monitored regularly',
            'You should have a procedure in place to verify password strength',
            'You should ensure that there are no accounts without passwords'
        ),
        'incorrect': (
            'Employees can create their own accounts',
            'You should ensure that employees passwords are memorable',
            'You should require users to manually record each use of an external network',
            'Accounts should be closed if not accessed for 24 hours'
        ),
    },

}

"""



'Good security practise': {
        'question':'A business impact analysis should PLACEHOLDER:",
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
        ),
        'incorrect': (
            'Employees can create their own accounts',
            'You should ensure that employees passwords are memorable',
            'You should require users to manually record each use of an external network',
            'Accounts should be closed if not accessed for 24 hours'
        ),
    },





('', 'The BEST way of protecting against the eavesdropping of email'),
('denial of service', ''),
('', 'role of the organisation's senior management in risk analysis'),
('', 'would require information security systems awareness training'),
('', 'Countermeasures are directly associated with'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),

('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),

('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('Regular incremental and full backups', ''),
('A formal disciplinary process, ''),


('trapdoor ', 'structured programming technique'),
('A gate access control system requiring a security token', 'prevent unauthorised access, damage and interference to IT services'),



('business continuity plan test results', 'record of Information Security Management System operation'),



In addition to identification, the only way to ensure the accountability of users for the actions taken within a system or domain would be?

(a) Oversight

(b) Authentication

(c) Authorization

(d) Credentials


"""



