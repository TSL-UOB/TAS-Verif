from pyvis import network as net
from IPython.display import display, HTML
from icecream import ic
import random

read_excel_remote = False
if read_excel_remote:
    # read data from O365/sharepoint/excel
    # see https://github.com/O365/python-o365
    from O365 import Account
    app_name = 'tas_excel_reader'
    # Application (client) ID
    client_id = 'a8c6de78-c7b8-422e-b6a7-d2c228c39681'
    client_secret = 'tas_excel_reader'
    secret_value = 'qfF8Q~mkrTkKoU_lQu-A8P5zmFAha8vu50vY2byx'
    secret_id = '0df7ae5f-f1b9-4910-be9d-b75981adf277'
    credentials = (client_id, client_secret)
    account = Account(credentials)
    if account.authenticate(scopes=['basic', 'onedrive_all', 'sharepoint_dl']):
        print('Office 365 authenticated...')
    # not tested:
    excel_file = WorkBook(my_file_instance)  # my_file_instance should be an instance of File.
    ws = excel_file.get_worksheet('my_worksheet')
    cella1 = ws.get_range('A1')
    # and
    table = ws.get_table('my_table')
    column = table.get_column_at_index(1)
    values = column.values[0]  # values returns a two dimensional array.

# Qualities
quals = ['trustworthy', 'competency','persistence','responsibility','integrity','consistency','loyalty','openness','ability','intentional','reasonable','confidential','interpersonal','sensible','expertise','honesty','predictable','accessibility','availability','benevolence','reliability','concern','tactful','sincerity','congenial','timely','dependable','faithfulness','principled','experienced','understanding','adept','utility','efficient','capacity','harmony','interoperability','appropriateness recognisibility','learnability','operability','usability','satisfying','maturity','tolerance','validate','accountability','authenticity','modularity','reusability','analysability','modifiability','testability','adaptability','initialise','replaceability','intentionality','specialist']
node_size = [10, 6,1,1,5,1,2,3,3,2,2,3,1,1,3,1,3,2,2,1,3,1,1,1,1,2,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1]

frmt_lee = ['default','performance','process','purpose','performance','process','process','purpose','process','performance','purpose','performance','purpose','purpose','purpose','process','process','performance','performance','performance','performance','process','performance','purpose','purpose','process','process','process','performance','purpose','performance','process','purpose','performance','performance','process','purpose','process','process','process','performance','process','process','performance','performance','performance','process','purpose','performance','purpose','performance','process','process','purpose','performance','performance','process','process','process','process','process','purpose']
col_lee = {'performance': '#DC143C', 'process': '#2E8B57', 'purpose': '#4169E1', 'default': '#87CEFA'}

# palette from https://coolors.co/palettes/trending
frmt_iso = ['default','Functional Stability','Reliability','Reliability','Functional Stability','Security','Functional Stability','Security','Usability','Functional Stability','Functional Stability','Functional Stability','Functional Stability','Reliability','Reliability','Usability','Security','Functional Stability','Usability','Functional Stability','Reliability','Functional Stability','Security','Security','Reliability','Usability','Usability','Functional Stability','Compatibility','Functional Stability','Reliability','Compatibility','Functional Stability','Functional Stability','Usability','Compatibility','Reliability','Reliability','Security','Functional Stability','Compatibility','Compatibility','Compatibility','Performance Efficiency','Reliability','Functional Stability','Security','Functional Stability','Compatibility','Functional Stability','Compatibility','Compatibility','Security','Functional Stability','Functional Stability','Functional Stability','Performance Efficiency','Performance Efficiency','Performance Efficiency','Compatibility','Compatibility','Usability','Usability','Usability','Usability','Usability','Usability','Reliability','Reliability','Reliability','Reliability','Security','Security','Security','Security','Security','Maintainability','Maintainability','Maintainability','Maintainability','Maintainability','Portability','Portability','Portability','Functional Stability','Reliability','Functional Stability','Functional Stability']
col_iso =  {'Functional Stability':'#AE2012',
            'Performance Efficiency':'#bb3e03',
            'Compatibility':'#ca6702',
            'Usability':'#ee9b00',
            'Reliability':'#e9d8a6',
            'Security':'#94d2bd',
            'Maintainability':'#0a9396',
            'Portability':'#005f73',
            'default': '#87CEFA'}

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

# Add in Dhamindas qualities from Specifying for Trustwortjiness paper

#Checking synonym from WordNet - not that good!
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
                                g.add_edge(n_id, n2_id, width=0.5)
    return line_thickness


# Chose the category colours
COLOUR_LEE = False
COLOUR_ISO = True

# use 2nd order synonym links in network, i.e. shared synonyms with other qualities
SECONDARY_LINKS = True

g=net.Network(height='1200px', width='100%',heading='AS-Qualities Network Graph',bgcolor='black',font_color="white")
for i,label in enumerate(quals):

    if COLOUR_LEE:
        chosen_colour = col_lee[frmt_lee[i]]
    elif COLOUR_ISO:
        chosen_colour = col_iso[frmt_iso[i]]
    else:
        chosen_colour = '#87CEFA'

    g.add_node(i, label=label, value=node_size[i], color=chosen_colour)


line_thickness = syn_nodes(g, syns)
ic(len(line_thickness))


g.show('example.html')
display(HTML('example.html'))