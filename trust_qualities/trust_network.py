from pyvis import network as net
from IPython.display import display, HTML
from icecream import ic
import random

#
# import pandas as pd #read csv
#
# read_excel_remote = False
# if read_excel_remote:
#     # read data from O365/sharepoint/excel
#     # see https://github.com/O365/python-o365
#     from O365 import Account
#     app_name = 'tas_excel_reader'
#     # Application (client) ID
#     client_id = 'a8c6de78-c7b8-422e-b6a7-d2c228c39681'
#     client_secret = 'tas_excel_reader'
#     secret_value = 'qfF8Q~mkrTkKoU_lQu-A8P5zmFAha8vu50vY2byx'
#     secret_id = '0df7ae5f-f1b9-4910-be9d-b75981adf277'
#     credentials = (client_id, client_secret)
#     account = Account(credentials)
#     if account.authenticate(scopes=['basic', 'onedrive_all', 'sharepoint_dl']):
#         print('Office 365 authenticated...')
#     # not tested:
#     excel_file = WorkBook(my_file_instance)  # my_file_instance should be an instance of File.
#     ws = excel_file.get_worksheet('my_worksheet')
#     cella1 = ws.get_range('A1')
#     # and
#     table = ws.get_table('my_table')
#     column = table.get_column_at_index(1)
#     values = column.values[0]  # values returns a two dimensional array.
#
# # Read in qualities, frequency and definitions
# READ_DATA = True
# if READ_DATA:
#     data = pd.read_csv('trust_quals.csv', sep='\t')
#     ic(data.shape)
#     ic(data.syns)
#     # split syns into single words based on newline character
#     # str.splitlines()
#
# # Qualities
# quals = ['ability','accessibility','accountability','accuracy','adaptability','adept','analysability','appropriateness recognisibility','assurance','authenticity','Autonomy','availability','beneficence','benevolence','capacity','communicative','competency','concern','confidential','congeniality','consistency','cooperative','coordination','deferential','dependable','efficient','ethical','experienced','expertise','explainability','fairness','faithfulness','flexible','functionality','governance','harmony','honesty','initialise','integrity','intelligibility','intentional','intentionality','interoperability','interpersonal','interpretability','Justice','learnability','loyalty','maturity','modifiability','modularity','negotiation','non-discriminatory','non‑maleficence','openness','operability','persistence','predictable','principled','privacy','reasonable','reciprocity','regulation','reliability','replaceability','resilient','responsibility','responsive','responsivity','reusability','robustness','safe','satisfying','scalability','security','sensible','sensitive','sincerity','SLEEC','specialist','sustainability','tactfulness','testability','timely','tolerance','traceability','transparency','trustworthy','understandability','understanding','usability','utility','validate','volitional','well-behaved']
# node_size = [2,2,4,1,2,1,1,1,2,1,1,3,1,1,1,2,6,1,3,1,1,4,1,1,2,1,2,1,3,2,2,4,2,1,1,1,1,1,5,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,3,1,1,3,1,2,2,1,1,6,1,1,1,1,1,1,3,3,1,1,2,1,1,1,1,1,1,1,1,3,2,1,2,1,1,2,2,1,1,1,1]
# ic(len(quals))
# ic(len(node_size))
# frmt_lee = ['performance','purpose','process','performance','purpose','performance','purpose','process','purpose','purpose','process','process','purpose','purpose','process','process','performance','purpose','process','performance','process','performance','process','purpose','process','process','purpose','performance','performance','process','purpose','purpose','process','performance','purpose','process','purpose','process','process','process','purpose','purpose','purpose','performance','process','purpose','process','purpose','performance','purpose','process','process','purpose','purpose','process','performance','process','performance','purpose','process','purpose','purpose','process','process','purpose','performance','purpose','performance','purpose','process','performance','process','purpose','process','process','process','purpose','process','purpose','performance','purpose','process','process','performance','performance','purpose','purpose','default','purpose','process','performance','process','process','purpose','process']
# col_lee = {'performance': '#DC143C', 'process': '#2E8B57', 'purpose': '#4169E1', 'default': '#cccccc'}
# ic(len(frmt_lee))
# # palette from https://coolors.co/palettes/trending
# frmt_iso = ['Functional Stability','Usability','Regulatability','Functional Stability','Maintainability','Functional Stability','Maintainability','Usability','Regulatability','Security','Usability','Usability','Compatibility','Compatibility','Performance Efficiency','Usability','Functional Stability','Compatibility','Security','Compatibility','Functional Stability','Compatibility','Usability','Security','Functional Stability','Performance Efficiency','Security','Functional Stability','Functional Stability','Regulatability','Security','Security','Compatibility','Functional Stability','Regulatability','Compatibility','Security','Portability','Security','Usability','Functional Stability','Functional Stability','Compatibility','Usability','Security','Security','Usability','Security','Reliability','Maintainability','Maintainability','Compatibility','Security','Security','Regulatability','Usability','Reliability','Reliability','Compatibility','Security','Reliability','Compatibility','Regulatability','Functional Stability','Portability','Reliability','Reliability','Usability','Reliability','Maintainability','Performance Efficiency','Functional Stability','Usability','Portability','Security','Reliability','Usability','Compatibility','Usability','Functional Stability','Maintainability','Compatibility','Maintainability','Performance Efficiency','Reliability','Regulatability','Regulatability','default','Regulatability','Compatibility','Usability','Functional Stability','Security','Reliability','Compatibility']
# ic(len(frmt_iso))
# # col_iso =  {'Functional Stability':'#AE2012',
# #             'Performance Efficiency':'#bb3e03',
# #             'Compatibility':'#ca6702',
# #             'Usability':'#ee9b00',
# #             'Reliability':'#e9d8a6',
# #             'Security':'#94d2bd',
# #             'Maintainability':'#0a9396',
# #             'Portability':'#005f73',
# #             'Regulatability': '#ffc000',
# #             'default': '#cccccc'}
# col_iso =  {'Functional Stability':'#540D6E',
#             'Performance Efficiency':'#A1286A',
#             'Compatibility':'#EE4266',
#             'Usability':'#F78A53',
#             'Reliability':'#FFD23F',
#             'Security':'#9DD076',
#             'Maintainability':'#3BCEAC',
#             'Portability':'#25BE8B',
#             'Regulatability':'#0EAD69',
# =======
import pandas


# read_excel_remote = False
# if read_excel_remote:
#     from O365.excel import WorkBook
#     # read data from O365/sharepoint/excel
#     # see https://github.com/O365/python-o365
#     from O365 import Account
#     app_name = 'tas_excel_reader'
#     # Application (client) ID
#     client_id = 'a8c6de78-c7b8-422e-b6a7-d2c228c39681'
#     client_secret = 'tas_excel_reader'
#     secret_value = 'qfF8Q~mkrTkKoU_lQu-A8P5zmFAha8vu50vY2byx'
#     secret_id = '0df7ae5f-f1b9-4910-be9d-b75981adf277'
#     credentials = (client_id, client_secret)
#     account = Account(credentials)
#     if account.authenticate(scopes=['basic', 'onedrive_all', 'sharepoint_dl']):
#         print('Office 365 authenticated...')
#     # not tested:
#     excel_file = WorkBook(my_file_instance)  # my_file_instance should be an instance of File.
#     ws = excel_file.get_worksheet('my_worksheet')
#     cella1 = ws.get_range('A1')
#     # and
#     table = ws.get_table('my_table')
#     column = table.get_column_at_index(1)
#     values = column.values[0]  # values returns a two dimensional array.

# palette from https://coolors.co/palettes/trending
col_lee = {'performance': '#DC143C', 'process': '#2E8B57', 'purpose': '#4169E1', 'default': '#cccccc'}

col_iso =  {'Functional Stability':'#AE2012',
            'Performance Efficiency':'#bb3e03',
            'Compatibility':'#ca6702',
            'Usability':'#ee9b00',
            'Reliability':'#e9d8a6',
            'Security':'#94d2bd',
            'Maintainability':'#0a9396',
            'Portability':'#005f73',
            'default': '#cccccc'}

col_gc =  {'Functionality':'#540D6E',
            'Compatibility':'#A1286A',
            'Usability':'#EE4266',
            'Reliability':'#F78A53',
            'Security':'#FFD23F',
            'Robustness':'#9DD076',
            'Ethical':'#3BCEAC',
            'Regulatability':'#25BE8B',
            'default': '#cccccc'}

# read syns from tsv
READ_TSV = True
if READ_TSV:
    data = pandas.read_csv('trust_quals.csv',delimiter='\t', skipinitialspace=True)
    # ic(data.head(5))
    # ic(data.shape)
    # ic(data['quality'])
    quals = data['quality'].tolist()
    ic(type(quals))
    node_size = data['frequency'].tolist()
    syns_raw = data['syns'].str.replace(" ","")#.str.strip()
    syns_raw = syns_raw.str.split(pat='\n')
    syns_raw = syns_raw.tolist()
    # frmt_lee = data['col_lee']
    # frmt_iso = data['col_iso']
    # frmt_gc = data['col_gc']
    frmt_lee, frmt_iso, frmt_gc = data['col_lee'].tolist(), data['col_iso'].tolist(), data['col_gc'].tolist()
    ic(syns_raw[0:5])
    # syns = syns_raw
    # ic(syns.iloc[0:5])
    syns = dict(zip(list(quals), list(syns_raw)))
    ic(syns)

else:
    quals = ['ability','accessibility','accountability','accuracy','adaptability','adept','aesthetic','analysability','appropriateness recognisibility','assurance','authenticity','autonomy','availability','beneficence','benevolence','capacity','communicative','competency','composability','concern','confidential','congeniality','consistency','controllability','cooperative','coordination','deferential','dependability','dependable','efficient','ethical','experienced','expertise','explainability','fairness','faithfulness','flexible','functionality','governance','harmony','honesty','independent','initialise','integrity','intelligibility','intentional','intentionality','interoperability','interpersonal','interpretability','justice','learnability','liveness','loyalty','maintainability','maturity','modifiability','modularity','negotiation','non-discriminatory','non‑maleficence','openness','operability','persistence','predictable','principled','privacy','reasonable','reciprocity','redundancy','regulation','reliability','replaceability','resilient','responsibility','responsive','responsivity','reusability','robustness','safe','satisfying','scalability','security','sensible','sensitive','sincerity','SLEEC','specialist','survivability','sustainability','tactfulness','testability','timely','tolerance','traceability','transparency','trustworthy','understandability','understanding','usability','utility','validate','volitional','well-behaved']
    node_size = [2,2,4,2,3,1,2,1,1,2,1,2,6,1,1,1,3,8,1,1,4,2,1,1,4,3,1,5,3,1,2,1,4,2,2,4,2,1,1,1,1,1,1,7,1,2,1,1,2,1,1,1,1,2,2,1,1,1,1,1,1,3,1,1,4,1,2,2,1,1,1,14,1,2,1,1,1,1,4,5,1,1,5,1,1,1,1,1,1,1,1,1,3,2,1,3,1,2,3,2,1,1,1,2]
    frmt_lee = ['performance','purpose','process','performance','purpose','performance','process','purpose','process','purpose','purpose','process','performance','purpose','purpose','process','process','performance','purpose','purpose','process','performance','process','process','performance','process','purpose','process','process','process','purpose','performance','performance','process','purpose','purpose','process','performance','purpose','process','purpose','process','process','purpose','process','purpose','purpose','purpose','performance','process','purpose','process','performance','purpose','purpose','performance','purpose','process','process','purpose','purpose','process','performance','process','performance','purpose','process','purpose','purpose','purpose','process','performance','purpose','performance','purpose','performance','purpose','process','performance','process','purpose','process','process','process','purpose','process','purpose','performance','purpose','purpose','process','process','performance','performance','purpose','purpose','default','purpose','process','performance','process','process','purpose','process']
    frmt_iso = ['Functional Stability','Regulatability','Regulatability','Functional Stability','Portability','Functional Stability','Compatibility','Regulatability','Usability','Regulatability','Security','Usability','Reliability','Compatibility','Compatibility','Performance Efficiency','Usability','Functional Stability','Portability','Compatibility','Security','Compatibility','Functional Stability','Usability','Compatibility','Usability','Security','Reliability','Functional Stability','Performance Efficiency','Security','Functional Stability','Functional Stability','Regulatability','Security','Security','Compatibility','Functional Stability','Regulatability','Compatibility','Security','Security','Portability','Reliability','Usability','Functional Stability','Compatibility','Compatibility','Usability','Security','Security','Usability','Functional Stability','Security','Maintainability','Reliability','Maintainability','Maintainability','Compatibility','Security','Security','Regulatability','Usability','Reliability','Reliability','Compatibility','Security','Compatibility','Compatibility','Maintainability','Regulatability','Reliability','Portability','Reliability','Reliability','Usability','Reliability','Maintainability','Portability','Functional Stability','Usability','Portability','Security','Reliability','Usability','Compatibility','Usability','Functional Stability','Reliability','Maintainability','Compatibility','Maintainability','Performance Efficiency','Reliability','Regulatability','Regulatability','default','Regulatability','Compatibility','Usability','Functional Stability','Security','Reliability','Compatibility']
    frmt_gc = ['Functionality','Regulatability','Regulatability','Functionality','Robustness','Functionality','Compatibility','Regulatability','Usability','Regulatability','Security','Ethical','Usability','Ethical','Ethical','Functionality','Usability','Functionality','Compatibility','Ethical','Security','Compatibility','Reliability','Usability','Compatibility','Usability','Ethical','Reliability','Reliability','Functionality','Ethical','Functionality','Functionality','Regulatability','Ethical','Reliability','Compatibility','Functionality','Regulatability','Compatibility','Security','Functionality','Usability','Ethical','Ethical','Ethical','Ethical','Compatibility','Usability','Ethical','Ethical','Usability','Functionality','Ethical','Robustness','Reliability','Robustness','Robustness','Compatibility','Ethical','Ethical','Regulatability','Usability','Robustness','Reliability','Ethical','Security','Ethical','Ethical','Robustness','Regulatability','Reliability','Robustness','Robustness','Ethical','Usability','Compatibility','Robustness','Robustness','Security','Usability','Robustness','Security','Ethical','Compatibility','Ethical','Ethical','Functionality','Robustness','Robustness','Compatibility','Regulatability','Functionality','Robustness','Regulatability','Regulatability','default','Regulatability','Compatibility','Usability','Functionality','Security','Functionality','Ethical']


    # Synonyms from https://www.collinsdictionary.com/dictionary/english-thesaurus/
    syns = {'trustworthy': ['dependable','responsible','principled','mature','sensible','reliable','ethical','upright','true','honourable','honest','staunch','righteous','reputable','truthful','trusty','steadfast','level-headed'],
            'competency': ['ability','skill','talent','capacity','expertise','proficiency','capability','fitness','suitability','adequacy','appropriateness'],
            'persistence': ['determination','resolution','pluck','stamina','grit','endurance','tenacity','diligence','perseverance','constancy','steadfastness','doggedness','pertinacity','indefatigability','tirelessness'],
            'responsibility' : ['duty','business','job','role','task','function','burden','liability','accountability','onus','answerability','fault','blame','guilt','culpability','burden','obligation','charge','care','authority','power','control','management','leadership','importance'],
            'integrity': ['honesty','principle','honour','virtue','goodness','morality','purity','righteousness','probity','rectitude','truthfulness','trustworthiness','incorruptibility','uprightness','scrupulousness','reputability'],
            'consistency': ['agreement','harmony','correspondence','accordance','regularity','coherence','compatibility','uniformity','constancy','steadiness','steadfastness','evenness','congruity'],
            'openness': ['frankness','honesty','truthfulness','naturalness','bluntness','forthrightness','ingenuousness','artlessness','guilelessness','candidness','freeness','open-heartedness','unreserved','candour','sincerity','sincereness','unreservedness'],
            'ability': ['capability','power','potential','facility','capacity','qualification','competence ','proficiency','competency','potentiality','skill','talent','gift','expertise','faculty','flair','competence','energy','accomplishment','knack','aptitude','proficiency','dexterity','cleverness','potentiality','adroitness','adeptness','expertness','force','craft','endowment'],
            'intentional':['deliberate','meant','planned','studied','designed','purposed','intended','calculated','wilful','premeditated','prearranged','preconcerted'],
            'reasonable': ['sensible','reasoned','sound','practical','wise','intelligent','rational','logical','sober','credible','plausible','sane','judicious','grounded'],
            'confidential': ['secret','private','intimate','classified','privy','protected','secretive','trusted','familiar','faithful','trustworthy','trusty'],
            'interpersonal': ['pleasant','pleasing','nice','attractive','charming','handsome','good-looking','winning','agreeable','amiable','affable','presentable','likable','likeable'],
            'sensible': ['wise','practical','prudent','shrewd','well-informed','judiciousv','well-advised','intelligent','practical','reasonable','rational','sound','realistic','sober','discriminating','discreet','sage','down-to-earth','matter-of-fact','sane','canny','far-sighted','sagacious','grounded'],
            'expertise': ['skill','knowledge','know-how','facility','grip','craft','judgment','grasp','mastery','knack','proficiency','dexterity','cleverness','deftness','adroitness','aptness','expertness','ableness','masterliness','skilfulness'],
            'honesty': ['integrity','honour','virtue','morality','fidelity','probity','rectitude','veracity','faithfulness','truthfulness','trustworthiness','straightness','incorruptibility','scrupulousness','uprightness','reputability','frankness','openness','sincerity','candour','bluntness','outspokenness','genuineness','plainness','straightforwardness'],
            'loyalty': ['faithfulness','commitment','devotion','allegiance','reliability','fidelity','homage','patriotism','obedience','constancy','dependability','trustworthiness','steadfastness','troth','fealty','staunchness','trueness','trustiness','true-heartedness'],
            'predictable': ['likely','expected','sure','certain','anticipated','reliable','foreseen','on the cards','foreseeable','sure-fire','calculable'],
            'accessibility': ['approachability','availability','readiness','nearness','handiness','possibility','attainability','obtainability','friendliness','informality','cordiality','affability','openness','susceptibility','exposedness'],
            'availability': ['accessibility','readiness','handiness','attainability','obtainability'],
            'benevolence': ['kindness','understanding','charity','grace','sympathy','humanity','tolerance','goodness','goodwill','compassion','generosity','indulgence','decency','altruism','clemency','gentleness','philanthropy','magnanimity','fellow feeling','beneficence','kindliness','kind-heartedness'],
            'reliability': ['dependable','trustworthy','honest','responsible','sure','sound','true','certain','regular','stable','faithful','predictable','upright','staunch','reputable','trusty','unfailing','safe','failesafe','definitive','attested'],
            'concern' : ['care','interest','regard','consideration','solicitude','attentiveness'],
            'tactful': ['diplomatic','politic','discreet','prudent','understanding','sensitive','polished','careful','subtle','delicate','polite','thoughtful','perceptive','considerate','judicious'],
            'sincerity': ['honesty','truth','candour','frankness','seriousness','good faith','probity','bona fides','genuineness','straightforwardness','artlessness','guilelessnes'],
            'congenial':['pleasant','kindly','pleasing','friendly','agreeable','cordial','sociable','genial','affable','convivial','companionable','favourable','complaisan'],
            'timely': ['opportune','appropriate','well-timed','prompt','suitable','convenient','at the right time','judicious','punctual','propitious','seasonable'],
            'dependable': ['reliable','sure','responsible','steady','faithful','staunch','reputable','trustworthy','trusty','go-to','unfailin'],
            'faithfulness': ['loyalty','devotion','fidelity','constancy','dependability','trustworthiness','fealty','adherence','accuracy','justice','truth','closeness','strictness','exactnes'],
            'principled': ['moral','ethical','upright','honourable','just','correct','decent','righteous','conscientious','virtuous','scrupulous','right-minded','high-minde'],
            'experienced': ['knowledgeable','trained','professional','skilled','tried','tested','seasoned','expert','master','qualified','familiar','capable','veteran','practised','accomplished','competent','skilful','adept','well-verse'],
            'understanding': ['compassionate','sympathetic','sensitive','considerate','tender','kind','kindly','kind-hearted','thoughtful','tolerant','patient','forbearing','lenient','merciful','forgiving','humane','human','good-natured','approachable','supportive','reassuring','tactful','diplomatic','perceptive','subtle','pruden','comprehension','apprehension','grasp','grip','mastery','perception','discernment','appreciation','interpretation','cognizance','ken','conception','digestion','assimilation','absorption','knowledge','awareness','consciousnes'],
            'adept': ['skilful','able','skilled','expert','masterly','practised','accomplished','versed','tasty (British, informal)','masterful','proficient','adroit','dexterou'],
            'utility': ['functional','useful','practical','plain','efficient','sensible','pragmatic','unpretentious','soulless','serviceable','unadorned','workad'],
            'efficient': ['effective','successful','structured','productive','powerful','systematic','streamlined','cost-effective','methodical','well-organized','well-planned','labour-saving','effectual'],
            'capacity': ['ability','power','strength','facility','gift','intelligence','efficiency','genius','faculty','capability','forte','readiness','aptitude','aptness','competence','competency'],
            'harmony': ['balance','consistency','fitness','correspondence','coordination','symmetry','compatibility','suitability','concord','parallelism','consonance','congruity'],
            'interoperability': ['communication'],
            'appropriateness recognisibility':['appropriate'],
            'learnability':['openness','explainable','satisfying'],
            'operability':['practicable','user-friendly'],
            'usability':['fit','convenient'],
            'satisfying': ['satisfactory','pleasing','enjoyable','gratifying','pleasurable','cheering'],
            'maturity': ['responsibility','experience','sense','wisdom','sophistication','level-headedness','matureness'],
            'tolerance': ['broad-mindedness','charity','sympathy','patience','indulgence','forbearance','permissiveness','magnanimity','open-mindedness','sufferance','lenity','endurance','resistance','stamina','fortitude','resilience','toughness','staying power','hardness','hardines','resistance','immunity','resilience'],
            'validate': ['confirm','prove','certify','substantiate','corroborate','authorize','endorse','ratify','legalize','authenticate'],
            'accountability': ['answerable','subject','responsible','obliged','to blame','liable','amenable','obligated','chargeable','responsibility','liability','culpability','answerability','chargeability'],
            'authenticity': ['accuracy','truth','certainty','validity','reliability','legitimacy','verity','actuality','faithfulness','truthfulness','dependability','trustworthiness','authoritativeness','factualness'],
            }

#Checking synonym from WordNet - not that good!
USE_WORDNET = False
if USE_WORDNET:
    # import nltk # if using for first time
    # nltk.download()
    from nltk.corpus import wordnet as wn
    #Creating a list
    synonyms = []
    for syn in wn.synsets("travel"):
        for lm in syn.lemmas():
                 synonyms.append(lm.name())#adding into synonyms
    # ic(set(synonyms))


def syn_nodes(g, syns):

    nodes, edges, heading, height, width, options = g.get_network_data()
    line_thickness = [1,2,4,10]

    for i, node in enumerate(nodes):
        n_id = nodes[i]['id']
        n_label = nodes[i]['label']

        # check if key word is in thesaurus
        if n_label in syns:
            # go through each synonym and add edges to network
            for syn in syns[n_label]:
                # for each syn search nodes and return ID
                for j, node2 in enumerate(nodes):
                    n2_id = nodes[j]['id']
                    n2_label = nodes[j]['label']
                    if syn == n2_label:
                        # g.add_edge(n_id, n2_id, width=random.choice(line_thickness))
                        g.add_edge(n_id, n2_id, width=8)

        # drawn 2nd order links
        if SECONDARY_LINKS and n_label in syns:
            # for all synonyms of this node, check the synonyms of other nodes for match
            for syn in syns[n_label]:
                for j, node2 in enumerate(nodes):
                    n2_id = nodes[j]['id']
                    n2_label = nodes[j]['label']
                    if n_id == n2_id:
                        continue
                    else:
                        if n2_label in syns:
                            if syn in syns[n2_label]:
                                # TODO check node link doesn't already exist to prevent overwrite
                                g.add_edge(n_id, n2_id, width=0.5)
    return line_thickness


# Chose the category colours
COLOUR_LEE = False
COLOUR_ISO = False
COLOR_GC = True

# use 2nd order synonym links in network, i.e. shared synonyms with other qualities
SECONDARY_LINKS = True

g=net.Network(height='1200px', width='100%',heading='AS-Qualities Network Graph',bgcolor='black',font_color="white")
for i,label in enumerate(quals):

    if COLOUR_LEE:
        chosen_colour = col_lee[frmt_lee[i]]
    elif COLOUR_ISO:
        chosen_colour = col_iso[frmt_iso[i]]
    elif COLOR_GC:
        chosen_colour = col_gc[frmt_gc[i]]
    else:
        chosen_colour = '#87CEFA'

    g.add_node(i, label=label, value=node_size[i], color=chosen_colour)


line_thickness = syn_nodes(g, syns)
ic(len(line_thickness))


g.show('example.html')
display(HTML('example.html'))