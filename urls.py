from django.urls import path, include

from . import views
from .views import *

from .pcep_modules import e1, e2, e3, e4
from .pcap_modules import a1, a2, a3, a4
from .pcpp1_modules import p11, p12, p13, p14
#from .pcpp2_modules import p21, p22, p23, p24

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
    path('random/', RandomModuleView.as_view(modules = (p11, p12, p13, p14,)), name = 'random_pcpp1'),
    path('1/', RandomModuleView.as_view(modules = (p11,)), name = 'OOP'),
    path('2/', RandomModuleView.as_view(modules = (p12,)), name = 'PEP'),
    path('3/', RandomModuleView.as_view(modules = (p13,)), name = 'GUI'),
    path('4/', RandomModuleView.as_view(modules = (p14,)), name = 'REST'),
    path('5/', RandomModuleView.as_view(modules = (p15,)), name = 'Files'),
]

pcpp2_patterns = [
    path('', PCPP2View.as_view(), name='pcpp2_home'),
    #path('random/', RandomModuleView.as_view(modules = (p21, p22, p23, p24)), name = 'random_pcpp2'),
]

urlpatterns = [
    path('', HomeView.as_view(), name='python_institute_home'),
    path('pcep/', include(pcep_patterns)),
    path('pcap/', include(pcap_patterns)),
    path('pcpp1/', include(pcpp1_patterns)),
    path('pcpp2/', include(pcpp2_patterns)),   
]