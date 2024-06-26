from random import randint

from ._3_logic import *

"""
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
#posneg_pairs - at least two pairs, both containing 3 items
"""

#basically, aggressive, targeted reconainsance
#describe concepts - identifying hosts, ports, services, active machines and OS
#use scanning tools - 
#host discovery
#port and service discovery
#scan beyond intrusion systems
#perform os system discovery
#draw network diagrams

questions = {
    'uk_government_data_classifications_in_order':uk_government_data_classifications_in_order,

    'UK government data classifications': {
        'question':'Which of the following is PLACEHOLDER a UK government data classification?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('official'),
            ('secret'),
            ('top secret'),
        ),
        'incorrect': (
            'official-secret',
            'official top-secret',
            'classified',
            'unclassified',
            'sensitive',
            'unofficial'
        ),
    },
    'Creation of policies': {
        'question':'Regarding the creation of acceptable use policies, which of the following statements is PLACEHOLDER best practise?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('define target audience'),
            ('the policy should be built according to IS027003'),
            ('consider the impact of the policy'),
            ('establish rules, compliance and legal concerns'),
            ('gather feedback from stakeholders'),
            ('consider updating existing policy'),
            ('consider using a template'),
            ('consider being explicit about legal use of a product'),
            ('defensive coding makes sure that only valid data is processed by the system'),
            ('security requirements must be a part the overall requirement specification'),
        ),
        'incorrect': (
            'share the completed policy with GDPR',
            'mark the completed policy as top-secret',
            'always generate an original structure to avoid copyright issues',
            'keep language vague to increase buy-in',
            'do not overcomplicate with different headings and sections',
            'do not refer to the laws of the land - keeping them is implicit',
            'establish penalties for disobeying rules',
        ),
    },
    'organisations and standards': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(

            ('The Turnbull Report', 'The document that describes a risk based approach to establishing a system of internal control and reviewing effectiveness'),
            ('Accreditation', 'independent process by which organisations can show they have met the requirements of ISO/IEC27001:2015'),
            (['Intellectual Property', 'IP'], ['the legal rights which result from activity in the industrial, scientific, literary and artistic fields']),
            (['ISO/IEC 27001'], ['a specification for an Information Security Management System', 'provides best practise recommendations on information security management']),
            (['ISO/IEC 27002'], ['information Security Management System implementation guidance']),
            (['ISO/IEC 15408'], ['the standards relating to the certification of security products']),
            (['ISO/IEC 13335'], ['addresses the general management issues that are essential to the successful planning, implementation and operation of IT security','international standard deals with the management of IT security, focusing on the technical security control measures']),
            (['ISO/IEC 24762', 'BS2577'], ['the standards relating to disaster recovery']),
            (['ISO/IEC 22301'], ['the standards relating to business continuity']),
            (['NIST 800-53'], ['provides a catalog of security and privacy controls for all U.S. federal information systems except those related to national security']),
            (['ISACA', 'Information Systems Audit and Control Association'], [' international professional association focused on IT governance']),
            (['SABSA', 'Sherwood Applied Business Security Architecture'], ['a framework and methodology for enterprise security architecture and service management']),
            (['OWASP', 'The Open Web Application Security Project'], ['an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security']),
            (['DevSecOps'], ['an approach to culture, automation, and platform design that integrates security as a shared responsibility throughout the entire IT lifecycle']),
            (['BS25999-1'], ['general guidance on the processes, principles and terminology']),
            (['BS25999-2'], ['a set of requirements for implementing, operating and improving a BCM System']),
            (['BS25777'], ['the collection andanalysis of information that is gathered from public sources']),
            (['ISO/IEC 27017'], ['the standards relating to practice for information security controls for cloud sevices']),
            (['ISO 31000'], ['an information risk management standard for any industry']),
            (['ISO 9001'], ['a quality manament standard']),
            (['CMBD','configuration management database'],'a list of information about all assets in a system'),
            (['SIEM'], ['aggregates and analyses activity from many different entities on a network']),
        ),
        'fillers': ()
    },
    'ISO standards': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['ISO/IEC 27001'], ['a specification for an Information Security Management System']),
            (['ISO/IEC 27002'], ['information Security Management System implementation guidance']),
            (['ISO/IEC 15408'], ['the standards relating to the certification of security products']),
            (['ISO/IEC 24762', 'BS2577'], ['the standards relating to disaster recovery']),
            (['ISO/IEC 22301'], ['the standards relating to business continuity']),
            (['ISO/IEC 27017'], ['the standards relating to practice for information security controls for cloud sevices']),
            (['ISO 31000'], ['an information risk management standard for any industry']),
            (['ISO 9001'], ['a quality manament standard']),
            ),
        'fillers': ()
    },
    'standards': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['ISO/IEC 27001'], ['a specification for an Information Security Management System']),
            (['ISO/IEC 27002'], ['information Security Management System implementation guidance', 'information security code of practice']),
            (['ISO/IEC 15408'], ['the standards relating to the certification of security products']),
            (['ISO/IEC 24762', 'BS2577'], ['the standards relating to disaster recovery']),
            (['ISO/IEC 22301'], ['the standards relating to business continuity']),
            (['NIST 800-53'], ['provides a catalog of security and privacy controls for all U.S. federal information systems except those related to national security']),
            (['SABSA', 'Sherwood Applied Business Security Architecture'], ['a framework and methodology for enterprise security architecture and service management']),
            (['BS25999-1'], ['general guidance on the processes, principles and terminology']),
            (['BS25999-2'], ['a set of requirements for implementing, operating and improving a BCM System']),
            (['BS25777'], ['the collection and analysis of information that is gathered from public sources']),
            (['ISO/IEC 27017'], ['the standards relating to practice for information security controls for cloud sevices']),
            (['ISO 31000'], ['an information risk management standard for any industry']),
            (['ISO 9001'], ['a quality manament standard']),
            ),
        'fillers': ()
    },
    'why use a framework': {
        'question':'Regarding security frameworks, which of the following statements is PLACEHOLDER accurate?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'makes sure that assurance requirements are understood',
            'ensures that responsiblities are allocated appropriately',
            'helps to clearly define accountabilities',
            'helps assurance activities to be coordinated',
            'provides consistency in approach to infosec',
        ),
        'incorrect': (
            'cheaper than using an ad hoc approach',
            'more expensive than using an ad hoc approach',
            'provides guidelines which must be followed',
        ),
    },

    'why top secret': {
        'question':'Why would a document be classified as top secret?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'so that users understand the level of confidentiality',
            'so that users understand how to use the document',
            'so that users understand how to dispose of the document',
        ),
        'incorrect': (
            'so that users know they must lock it away when not being used',
            'so that users know that leaving it out will be violating a clear desk policy',
            'so that users understand that it is only to be viewed by senior management',
            'so that users undestand how to encrypt the document',
            'so that users can confirm the hash',
        ),
    },

    'the steering commitee should consist of': {
        'question':'Which of the following does PLACEHOLDER need to be on a steering committee?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'line managers',
            'application owners',
            'regional managers',
            'IT managers',
            'the IT director',
            'chief security officer',
            'coorporate risk manager',
            'chief internal auditor',
        ),
        'incorrect': (
            'union rep',
            'local councillor',
            'all who wish to attend',
            'only the company directors',
            'external auditors',
        ),
    },
    'policies, standards, procedures, guidelines': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('policies',['high level statement or organisation\'s values, goals and objecives', 'a general approach to achieving an organisation\'s values, goals and objectives']),
            ('standards',['drawn from policies quantifies what needs to be done',  'provides consistency in controls can be measured']),
            ('proceedures',['obligations', 'specific things which must be done']),
            ('guidelines',['best practce', 'not mandatory', 'provides advice'])
            ),
        'fillers': ()
    },
    'security policy within an organisation': {
        'question':'What should a security policy PLACEHOLDER be within an organisation?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'mandatory',
        ),
        'incorrect': (
            'discretionary',
            'optional',
            'advisory',
            'implemented where possible',
        ),
    },
    
}

"""
('port scanning', ['lists services', 'checking the services running on the target', 'sending a sequence of messages', f"{choice(['connecting to', 'probing'])} {choice(['UDP', 'TCP'])} ports to determine whether services are {choice(['running', 'in a listening state'])}", f"a listening state may provide information about the {choice(['OS', 'application currently in use'])}", f"active services may allow unauthorised users to {choice(['misconfigure systems', 'run software with vulnerabilities'])}"]),
    ('network scanning', f"lists {choice(['active hosts', 'IP addresses'])} to {choice(['assess security of the network', 'attack them'])}"), 
    ('vulnerability scanning', ['shows the presence of known weaknesses', 'identifies a system\'s main vulnerabilities', 'performed with an engine and a catalogue', ''])
    (['SYN', 'ACK', 'FIN', 'RST'], 'TCP flag governing the establistment, maintenance and termination of a connection'),
    (['PSH', 'URG'], 'provide instructions to the system'),

    ('correct', [f"{choice(['SYN', 'ACK', 'FIN', 'RST'])} governs the establistment, maintenance and termination of a connection",f"{choice(['PSH', 'URG'])} provides instructions to the system", 'each TCP flag is 1 bit', 'the six TCP flags are 6 bits altogether', 'the TCP header contains flag controlling the transmission of data', 'SYN is used to launch a connection', 'RST is used to end a connection', 'FIN is used to end a connection']),
    ('incorrect', [f"{choice(['PSH', 'URG'])} governs the establistment, maintenance and termination of a connection",f"{choice(['SYN', 'ACK', 'FIN', 'RST'])} provides instructions to the system", f'each TCP flag is {randint(2, 6)} bits', f'the six TCP flags are {randint(1, 5)} bits altogether', f'the six TCP flags are {randint(7, 9)} bits altogether', f"the TCP {choice(['body', 'title', 'footer'])} contains flag controlling the transmission of data",f"{choice(['SYN', 'PSH'])} is used to end a connection",f"{choice(['FIN', 'RST', 'PSH', 'URG'])} is used to establish a connection",]),

    #comes before comes after
    ('source port', 'destination port', 'sequence no', 'acknowledgement no', 'offset', 'res', 'TCP flags', 'window', 'TCP checksum', 'urgent pointer', 'options')

    (['synchronise','SYN'], ['notified the transmission of a new sequence number', 'represents the establishment of a connection']),
    (['acknowledgement','ACK'], ['confirms the reciept of the transmission', 'identifies the next expected sequence number', 'sets value to 1 when a packet is successfully recieved']),
    (['Push','PSH'], ['remote system should inform the recieving application about buffered data coming from the sender', 'raised at the start and end of the data transfer', 'set on the last segment of a file to prevent buffer deadlocks']),
    (['Urgent','URG'], ['instructs the system to process data as soon as possible', 'specifies which data to process first']),
    (['Finish','FIN'], ['announce that no more transmissions will be sent to the remote system', 'announce that connection is terminated']),
    (['Reset','RST'], ['set to 1 when there is an error in the current connection', 'causes current connection to be aborted', 'can be used to identify open ports']),

    ('SYN from source'),
    ('SYN/ACK from destination')
    ('ACK from source')
    (['RST from source', 'FIN from source'])
    ('ACK from destination')
    ('FIN from destination')
    ('ACK from source')

    ('nmap', [''])


'UK government data classifications': {
        'question':'Regarding acceptable use policies, Which of the following statements is PLACEHOLDER?',
        'question_type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            ('a policy should direct behaviour'),
            ('the policy should be built according to IS027003'),
            ('a policy should establish rules, compliance and legal concerns'),
        ),
        'incorrect': (
        ),
    },

policy should direct
intro
scope
policy

upper case or lower case is a standard

Question:
policy should use ISO27003
categories
Which categories should x document have

How would you go about making a policy?

steering committee

bodies

27001 - requirements... things you must do
27002 - controls derived from 27002
"""

    
    



