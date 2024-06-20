from django.urls import path, include

from . import views
from .views import *

from .pcep_modules import e1, e2, e3, e4
from .pcap_modules import a1, a2, a3, a4
from .pcpp1_modules import p11, p12, p13, p14
#from .pcpp2_modules import p21, p22, p23, p24
from .cismp_modules import _1, _2, _3, _4, _5, _6, _7, _8, _9 
cismp_1, cismp_2, cismp_3, cismp_4, cismp_5, cismp_6, cismp_7, cismp_8, cismp_9  = _1, _2, _3, _4, _5, _6, _7, _8, _9 


pcep_patterns = [
    path('', PCEPView.as_view(), name='pcep_home'),
    path('random/', RandomModuleView.as_view(modules = (e1, e2, e3, e4)), name = 'random_pcep'),
    path('1/', RandomModuleView.as_view(modules = (e1,)), name = 'computer_programming_and_python_fundamentals'),
    path('2/', RandomModuleView.as_view(modules = (e2,)), name = 'control_flow_conditional_blocks_and_loops'),
    path('3/', RandomModuleView.as_view(modules = (e3,)), name = 'data_collections_tuples_dictionaries_lists_and_strings'),
    path('4/', RandomModuleView.as_view(modules = (e4,)), name = 'functions_and_exceptions'),
]

pcap_patterns = [
    path('', PCAPView.as_view(), name='pcap_home'),
    #path('random/', RandomModuleView.as_view(modules = (a1, a2, a3, a4)), name = 'random_pcap'),
]

pcpp1_patterns = [    
    path('', PCPP1View.as_view(), name='pcpp1_home'),
    path('random/', RandomModuleView.as_view(modules = (p11, p12, p13, p14, p15)), name = 'random_pcpp1'),
    path('p11/', RandomModuleView.as_view(modules = (p11,)), name = 'OOP'),
    path('p12/', RandomModuleView.as_view(modules = (p12,)), name = 'PEP'),
    path('p13/', RandomModuleView.as_view(modules = (p13,)), name = 'GUI'),
    path('p14/', RandomModuleView.as_view(modules = (p14,)), name = 'REST'),
    path('p15/', RandomModuleView.as_view(modules = (p15,)), name = 'Files'),
    path('<str:module_str>/<str:question>/', specific_question_view, name = 'Specific'),
]

pcpp2_patterns = [
    path('', PCPP2View.as_view(), name='pcpp2_home'),
    #path('random/', RandomModuleView.as_view(modules = (p21, p22, p23, p24)), name = 'random_pcpp2'),
]

pcat_patterns = [
    path('', PCATView.as_view(), name='pcat_home'),
    path('random/', RandomModuleView.as_view(modules = (t1,)), name = 'random_pcat1'),
    path('t1/', RandomModuleView.as_view(modules = (t1,)), name = 'OOP'),
]

cismp_patterns = [
    path('', CISMPHomeView.as_view(), name='cismp_home'),
    path('random/', CismpRandomModuleView.as_view(modules = (cismp_1, cismp_2, cismp_3, cismp_4, cismp_5, cismp_6, cismp_7, cismp_8, cismp_9)), name = 'all_random'),
    path('information_security_principles/', RandomModuleView.as_view(modules = (cismp_1,)), name = 'information_security_principles'),
    path('information_risk/', RandomModuleView.as_view(modules = (cismp_2,)), name = 'information_risk'),
    path('information_security_frameworks/', RandomModuleView.as_view(modules = (cismp_3,)), name = 'information_security_frameworks'),
    path('security_life_cycles/', RandomModuleView.as_view(modules = (cismp_4,)), name = 'security_life_cycles'),
    path('procedural_and_people_security_controls/', RandomModuleView.as_view(modules = (cismp_5,)), name = 'procedural_and_people_security_controls'),
    path('technical_security_controls/', RandomModuleView.as_view(modules = (cismp_6,)), name = 'technical_security_controls'),
    path('physical_and_environmental_security/', RandomModuleView.as_view(modules = (cismp_7,)), name = 'physical_and_environmental_security'),
    path('disaster_recovery_and_business_continuity_management/', RandomModuleView.as_view(modules = (cismp_8,)), name = 'disaster_recovery_and_business_continuity_management'),
    path('cryptography/', RandomModuleView.as_view(modules = (cismp_9,)), name = 'cryptography'),
    path('log_problem/', log_problem, name='log_problem'),
] 

urlpatterns = [
    path('pi/', PIHomeView.as_view(), name='python_institute_home'),
    path('pcep/', include(pcep_patterns)),
    path('pcap/', include(pcap_patterns)),
    path('pcpp1/', include(pcpp1_patterns)),
    path('pcpp2/', include(pcpp2_patterns)),
    path('pcat/', include(pcat_patterns)),

    path('cismp/', include(cismp_patterns)),
    path('log_problem/', log_problem, name='log_problem'),
]