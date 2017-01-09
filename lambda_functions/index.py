# coding=utf-8

"""
Quizzical - An Alexa Skill
Code is based on original code from https://github.com/pmckinney8/Alexa_Dojo_Skill.git
"""
from __future__ import print_function
import random

### ---------- START Game specific data ----------
# Get our speech output variables defined here
welcomeMessage = "Welcome to Quizzical. say which game would you like to play. continents, or, capitals."
'''
                 "You have several games to choose from. " \
                 "Depending on your game choice, you can either choose from options, or give a one word answer. " \
                 "You can move along in the game by saying, " \
                 "repeat, to repeat a question, " \
                 "skip, to skip a question, " \
                 "hint, to get a hint, " \
                 "eliminate, to remove a choice, " \
                 "start over, to restart the game, " \
                 "or, stop, to end the game. " \
                 "If you didn't get all that, don't worry, you can always say, help. and I will assist you. "
'''


rePromptWelcome = "Welcome to Quizzical, say the name of the game. "
rePromptContinent = "Say the name of the continent"
rePromptCapital = "Give me the number choice for the capital"
rePromptGameSelection = "what is your selection. "
rePromptIDK = "what is your choice"
rePrompt = "what is your choice"
helpMessage = {
    'starting': "Quizzical help. Simply say the name of the selection, continents or capitals. "
                "Or if you want to start over simply say, start over. To end the game say, stop",
    'playing': "Quizzical help. You can say, "
               "repeat to repeat a question, "
               "skip, to skip a question, "
               "hint, to get a hint, "
               "eliminate, to remove a choice, "
               "start over, to restart the game, "
               "or, stop, to end the game."

}
endOfCategoryMessage = "Congratulations!, you have reached the end of this category, " \
                       "say, start over, to choose a new one. "
endMessage = "Thank you for playing quizzical, goodbye!"

# Amazon applicationID
skillID = "amzn1.ask.skill.e86383ae-412c-4678-9a8d-dbbba92a3ced"

# Game questions and answers
continents = {
    'andorra': 'europe',
    'united arab emirates': 'asia',
    'afghanistan': 'asia',
    'antigua and barbuda': 'north america',
    'anguilla': 'north america',
    'albania': 'europe',
    'armenia': 'asia',
    'angola': 'africa',
    'antarctica': 'antarctica',
    'argentina': 'south america',
    'american samoa': 'oceania',
    'austria': 'europe',
    'australia': 'oceania',
    'aruba': 'north america',
    'Åland': 'europe',
    'azerbaijan': 'asia',
    'bosnia and herzegovina': 'europe',
    'barbados': 'north america',
    'bangladesh': 'asia',
    'belgium': 'europe',
    'burkina faso': 'africa',
    'bulgaria': 'europe',
    'bahrain': 'asia',
    'burundi': 'africa',
    'benin': 'africa',
    'saint barthélemy': 'north america',
    'bermuda': 'north america',
    'brunei': 'asia',
    'bolivia': 'south america',
    'bonaire': 'north america',
    'brazil': 'south america',
    'bahamas': 'north america',
    'bhutan': 'asia',
    'bouvet island': 'antarctica',
    'botswana': 'africa',
    'belarus': 'europe',
    'belize': 'north america',
    'canada': 'north america',
    'cocos [keeling] islands': 'asia',
    'democratic republic of the congo': 'africa',
    'central african republic': 'africa',
    'republic of the congo': 'africa',
    'switzerland': 'europe',
    'ivory coast': 'africa',
    'cook islands': 'oceania',
    'chile': 'south america',
    'cameroon': 'africa',
    'china': 'asia',
    'colombia': 'south america',
    'costa rica': 'north america',
    'cuba': 'north america',
    'cape verde': 'africa',
    'curacao': 'north america',
    'christmas island': 'asia',
    'cyprus': 'europe',
    'czechia': 'europe',
    'germany': 'europe',
    'djibouti': 'africa',
    'denmark': 'europe',
    'dominica': 'north america',
    'dominican republic': 'north america',
    'algeria': 'africa',
    'ecuador': 'south america',
    'estonia': 'europe',
    'egypt': 'africa',
    'western sahara': 'africa',
    'eritrea': 'africa',
    'spain': 'europe',
    'ethiopia': 'africa',
    'finland': 'europe',
    'fiji': 'oceania',
    'falkland islands': 'south america',
    'micronesia': 'oceania',
    'faroe islands': 'europe',
    'france': 'europe',
    'gabon': 'africa',
    'united kingdom': 'europe',
    'grenada': 'north america',
    'georgia': 'asia',
    'french guiana': 'south america',
    'guernsey': 'europe',
    'ghana': 'africa',
    'gibraltar': 'europe',
    'greenland': 'north america',
    'gambia': 'africa',
    'guinea': 'africa',
    'guadeloupe': 'north america',
    'equatorial guinea': 'africa',
    'greece': 'europe',
    'south georgia and the south sandwich islands': 'antarctica',
    'guatemala': 'north america',
    'guam': 'oceania',
    'guinea-bissau': 'africa',
    'guyana': 'south america',
    'hong kong': 'asia',
    'heard island and mcdonald islands': 'antarctica',
    'honduras': 'north america',
    'croatia': 'europe',
    'haiti': 'north america',
    'hungary': 'europe',
    'indonesia': 'asia',
    'ireland': 'europe',
    'israel': 'asia',
    'isle of man': 'europe',
    'india': 'asia',
    'british indian ocean territory': 'asia',
    'iraq': 'asia',
    'iran': 'asia',
    'iceland': 'europe',
    'italy': 'europe',
    'jersey': 'europe',
    'jamaica': 'north america',
    'jordan': 'asia',
    'japan': 'asia',
    'kenya': 'africa',
    'kyrgyzstan': 'asia',
    'cambodia': 'asia',
    'kiribati': 'oceania',
    'comoros': 'africa',
    'saint kitts and nevis': 'north america',
    'north korea': 'asia',
    'south korea': 'asia',
    'kuwait': 'asia',
    'cayman islands': 'north america',
    'kazakhstan': 'asia',
    'laos': 'asia',
    'lebanon': 'asia',
    'saint lucia': 'north america',
    'liechtenstein': 'europe',
    'sri lanka': 'asia',
    'liberia': 'africa',
    'lesotho': 'africa',
    'lithuania': 'europe',
    'luxembourg': 'europe',
    'latvia': 'europe',
    'libya': 'africa',
    'morocco': 'africa',
    'monaco': 'europe',
    'moldova': 'europe',
    'montenegro': 'europe',
    'saint martin': 'north america',
    'madagascar': 'africa',
    'marshall islands': 'oceania',
    'macedonia': 'europe',
    'mali': 'africa',
    'myanmar': 'asia',
    'mongolia': 'asia',
    'macao': 'asia',
    'northern mariana islands': 'oceania',
    'martinique': 'north america',
    'mauritania': 'africa',
    'montserrat': 'north america',
    'malta': 'europe',
    'mauritius': 'africa',
    'maldives': 'asia',
    'malawi': 'africa',
    'mexico': 'north america',
    'malaysia': 'asia',
    'mozambique': 'africa',
    'namibia': 'africa',
    'new caledonia': 'oceania',
    'niger': 'africa',
    'norfolk island': 'oceania',
    'nigeria': 'africa',
    'nicaragua': 'north america',
    'netherlands': 'europe',
    'norway': 'europe',
    'nepal': 'asia',
    'nauru': 'oceania',
    'niue': 'oceania',
    'new zealand': 'oceania',
    'oman': 'asia',
    'panama': 'north america',
    'peru': 'south america',
    'french polynesia': 'oceania',
    'papua new guinea': 'oceania',
    'philippines': 'asia',
    'pakistan': 'asia',
    'poland': 'europe',
    'saint pierre and miquelon': 'north america',
    'pitcairn islands': 'oceania',
    'puerto rico': 'north america',
    'palestine': 'asia',
    'portugal': 'europe',
    'palau': 'oceania',
    'paraguay': 'south america',
    'qatar': 'asia',
    'réunion': 'africa',
    'romania': 'europe',
    'serbia': 'europe',
    'russia': 'europe',
    'rwanda': 'africa',
    'saudi arabia': 'asia',
    'solomon islands': 'oceania',
    'seychelles': 'africa',
    'sudan': 'africa',
    'sweden': 'europe',
    'singapore': 'asia',
    'saint helena': 'africa',
    'slovenia': 'europe',
    'svalbard and jan mayen': 'europe',
    'slovakia': 'europe',
    'sierra leone': 'africa',
    'san marino': 'europe',
    'senegal': 'africa',
    'somalia': 'africa',
    'suriname': 'south america',
    'south sudan': 'africa',
    'são tomé and príncipe': 'africa',
    'el salvador': 'north america',
    'sint maarten': 'north america',
    'syria': 'asia',
    'swaziland': 'africa',
    'turks and caicos islands': 'north america',
    'chad': 'africa',
    'french southern territories': 'antarctica',
    'togo': 'africa',
    'thailand': 'asia',
    'tajikistan': 'asia',
    'tokelau': 'oceania',
    'east timor': 'oceania',
    'turkmenistan': 'asia',
    'tunisia': 'africa',
    'tonga': 'oceania',
    'turkey': 'asia',
    'trinidad and tobago': 'north america',
    'tuvalu': 'oceania',
    'taiwan': 'asia',
    'tanzania': 'africa',
    'ukraine': 'europe',
    'uganda': 'africa',
    'u.s. minor outlying islands': 'oceania',
    'united states': 'north america',
    'uruguay': 'south america',
    'uzbekistan': 'asia',
    'vatican city': 'europe',
    'saint vincent and the grenadines': 'north america',
    'venezuela': 'south america',
    'british virgin islands': 'north america',
    'u.s. virgin islands': 'north america',
    'vietnam': 'asia',
    'vanuatu': 'oceania',
    'wallis and futuna': 'oceania',
    'samoa': 'oceania',
    'kosovo': 'europe',
    'yemen': 'asia',
    'mayotte': 'africa',
    'south africa': 'africa',
    'zambia': 'africa',
    'zimbabwe': 'africa'
}

capitals = {
    'andorra': 'andorra la vella',
    'united arab emirates': 'abu dhabi',
    'afghanistan': 'kabul',
    'antigua and barbuda': 'saint johns',
    'anguilla': 'the valley',
    'albania': 'tirana',
    'armenia': 'yerevan',
    'angola': 'luanda',
    'argentina': 'buenos aires',
    'american samoa': 'pago pago',
    'austria': 'vienna',
    'australia': 'canberra',
    'aruba': 'oranjestad',
    'Åland': 'mariehamn',
    'azerbaijan': 'baku',
    'bosnia and herzegovina': 'sarajevo',
    'barbados': 'bridgetown',
    'bangladesh': 'dhaka',
    'belgium': 'brussels',
    'burkina faso': 'ouagadougou',
    'bulgaria': 'sofia',
    'bahrain': 'manama',
    'burundi': 'bujumbura',
    'benin': 'porto novo',
    'saint barthélemy': 'gustavia',
    'bermuda': 'hamilton',
    'brunei': 'bandar seri begawan',
    'bolivia': 'sucre',
    'bonaire': 'kralendijk',
    'brazil': 'brasília',
    'bahamas': 'nassau',
    'bhutan': 'thimphu',
    'botswana': 'gaborone',
    'belarus': 'minsk',
    'belize': 'belmopan',
    'canada': 'ottawa',
    'cocos or keeling islands': 'west island',
    'democratic republic of the congo': 'kinshasa',
    'central african republic': 'bangui',
    'republic of the congo': 'brazzaville',
    'switzerland': 'bern',
    'ivory coast': 'yamoussoukro',
    'cook islands': 'avarua',
    'chile': 'santiago',
    'cameroon': 'yaoundé',
    'china': 'beijing',
    'colombia': 'bogotá',
    'costa rica': 'san josé',
    'cuba': 'havana',
    'cape verde': 'praia',
    'curacao': 'willemstad',
    'christmas island': 'flying fish cove',
    'cyprus': 'nicosia',
    'czechia': 'prague',
    'germany': 'berlin',
    'djibouti': 'djibouti',
    'denmark': 'copenhagen',
    'dominica': 'roseau',
    'dominican republic': 'santo domingo',
    'algeria': 'algiers',
    'ecuador': 'quito',
    'estonia': 'tallinn',
    'egypt': 'cairo',
    'western sahara': 'laâyoune / el aaiún',
    'eritrea': 'asmara',
    'spain': 'madrid',
    'ethiopia': 'addis ababa',
    'finland': 'helsinki',
    'fiji': 'suva',
    'falkland islands': 'stanley',
    'micronesia': 'palikir',
    'faroe islands': 'tórshavn',
    'france': 'paris',
    'gabon': 'libreville',
    'united kingdom': 'london',
    'grenada': 'saint georges',
    'georgia': 'tbilisi',
    'french guiana': 'cayenne',
    'guernsey': 'saint peter port',
    'ghana': 'accra',
    'gibraltar': 'gibraltar',
    'greenland': 'nuuk',
    'gambia': 'bathurst',
    'guinea': 'conakry',
    'guadeloupe': 'basse terre',
    'equatorial guinea': 'malabo',
    'greece': 'athens',
    'south georgia and the south sandwich islands': 'grytviken',
    'guatemala': 'guatemala city',
    'guam': 'hagåtña',
    'guinea-bissau': 'bissau',
    'guyana': 'georgetown',
    'hong kong': 'hong kong',
    'honduras': 'tegucigalpa',
    'croatia': 'zagreb',
    'haiti': 'port-au-prince',
    'hungary': 'budapest',
    'indonesia': 'jakarta',
    'ireland': 'dublin',
    'israel': 'jerusalem',
    'isle of man': 'douglas',
    'india': 'new delhi',
    'iraq': 'baghdad',
    'iran': 'tehran',
    'iceland': 'reykjavik',
    'italy': 'rome',
    'jersey': 'saint helier',
    'jamaica': 'kingston',
    'jordan': 'amman',
    'japan': 'tokyo',
    'kenya': 'nairobi',
    'kyrgyzstan': 'bishkek',
    'cambodia': 'phnom penh',
    'kiribati': 'tarawa',
    'comoros': 'moroni',
    'saint kitts and nevis': 'basseterre',
    'north korea': 'pyongyang',
    'south korea': 'seoul',
    'kuwait': 'kuwait city',
    'cayman islands': 'george town',
    'kazakhstan': 'astana',
    'laos': 'vientiane',
    'lebanon': 'beirut',
    'saint lucia': 'castries',
    'liechtenstein': 'vaduz',
    'sri lanka': 'colombo',
    'liberia': 'monrovia',
    'lesotho': 'maseru',
    'lithuania': 'vilnius',
    'luxembourg': 'luxembourg',
    'latvia': 'riga',
    'libya': 'tripoli',
    'morocco': 'rabat',
    'monaco': 'monaco',
    'moldova': 'chişinău',
    'montenegro': 'podgorica',
    'saint martin': 'marigot',
    'madagascar': 'antananarivo',
    'marshall islands': 'majuro',
    'macedonia': 'skopje',
    'mali': 'bamako',
    'myanmar': 'naypyitaw',
    'mongolia': 'ulan bator',
    'macao': 'macao',
    'northern mariana islands': 'saipan',
    'martinique': 'fort-de-france',
    'mauritania': 'nouakchott',
    'montserrat': 'plymouth',
    'malta': 'valletta',
    'mauritius': 'port louis',
    'maldives': 'malé',
    'malawi': 'lilongwe',
    'mexico': 'mexico city',
    'malaysia': 'kuala lumpur',
    'mozambique': 'maputo',
    'namibia': 'windhoek',
    'new caledonia': 'noumea',
    'niger': 'niamey',
    'norfolk island': 'kingston',
    'nigeria': 'abuja',
    'nicaragua': 'managua',
    'netherlands': 'amsterdam',
    'norway': 'oslo',
    'nepal': 'kathmandu',
    'nauru': 'yaren',
    'niue': 'alofi',
    'new zealand': 'wellington',
    'oman': 'muscat',
    'panama': 'panama city',
    'peru': 'lima',
    'french polynesia': 'papeete',
    'papua new guinea': 'port moresby',
    'philippines': 'manila',
    'pakistan': 'islamabad',
    'poland': 'warsaw',
    'saint pierre and miquelon': 'saint-pierre',
    'pitcairn islands': 'adamstown',
    'puerto rico': 'san juan',
    'palestine': 'east jerusalem',
    'portugal': 'lisbon',
    'palau': 'melekeok',
    'paraguay': 'asunción',
    'qatar': 'doha',
    'réunion': 'saint-denis',
    'romania': 'bucharest',
    'serbia': 'belgrade',
    'russia': 'moscow',
    'rwanda': 'kigali',
    'saudi arabia': 'riyadh',
    'solomon islands': 'honiara',
    'seychelles': 'victoria',
    'sudan': 'khartoum',
    'sweden': 'stockholm',
    'singapore': 'singapore',
    'saint helena': 'jamestown',
    'slovenia': 'ljubljana',
    'svalbard and jan mayen': 'longyearbyen',
    'slovakia': 'bratislava',
    'sierra leone': 'freetown',
    'san marino': 'san marino',
    'senegal': 'dakar',
    'somalia': 'mogadishu',
    'suriname': 'paramaribo',
    'south sudan': 'juba',
    'são tomé and príncipe': 'são tomé',
    'el salvador': 'san salvador',
    'sint maarten': 'philipsburg',
    'syria': 'damascus',
    'swaziland': 'mbabane',
    'turks and caicos islands': 'cockburn town',
    'chad': 'ndjamena',
    'french southern territories': 'port-aux-français',
    'togo': 'lomé',
    'thailand': 'bangkok',
    'tajikistan': 'dushanbe',
    'east timor': 'dili',
    'turkmenistan': 'ashgabat',
    'tunisia': 'tunis',
    'tonga': 'nuku alofa',
    'turkey': 'ankara',
    'trinidad and tobago': 'port of spain',
    'tuvalu': 'funafuti',
    'taiwan': 'taipei',
    'tanzania': 'dodoma',
    'ukraine': 'kiev',
    'uganda': 'kampala',
    'united states': 'washington d.c.',
    'uruguay': 'montevideo',
    'uzbekistan': 'tashkent',
    'vatican city': 'vatican city',
    'saint vincent and the grenadines': 'kingstown',
    'venezuela': 'caracas',
    'british virgin islands': 'road town',
    'u.s. virgin islands': 'charlotte amalie',
    'vietnam': 'hanoi',
    'vanuatu': 'port vila',
    'wallis and futuna': 'mata utu',
    'samoa': 'apia',
    'kosovo': 'pristina',
    'yemen': 'sanaa',
    'mayotte': 'mamoudzou',
    'south africa': 'pretoria',
    'zambia': 'lusaka',
    'zimbabwe': 'harare'
}

# Game metadata
gameSelections = {
    'continent':
        {
            'aliases': ['continents', 'continent'],
            'choices':
                {
                    'city': 'continents'
                    # TODO: The 'city' keyword is a remnant that needs to be changed to something meaningful
                }
        },

    'capitals':
        {
            'aliases': ['capital', 'capitals'],
            'choices':
                {
                    'city': 'capitals'
                    # TODO: The 'city' keyword is a remnant that needs to be changed to something meaningful
                }
        }
}

# dict that stores the soeech responses for each game and tracks the questions
gameMetaData = {

    'continents':
        {
            'welcomeSuffix': 'simply say the name of the continent',
            'questionPrefix': ' ',
            'questionSuffix': '. ',
            'choicesPrefix': ' ',
            'choicesSuffix': ' ',
            'usedQuestions': [],
            'gameMode': 'realAnswer'
        },

    'capitals':
        {
            'welcomeSuffix': 'simply say the number of your choice',
            'questionPrefix': 'what is the capital of ',
            'questionSuffix': '. ',
            'choicesPrefix': ' ',
            'choicesSuffix': ' ',
            'usedQuestions': [],
            'gameMode': 'answerChoice'
        },
}

### ---------- END Game specific data ----------


### ---------- START Variables used in the game ----------
# Initialize variables
gameMode = ""
context = "starting"
strikesAllowed = 3
skipsAllowed = 2
hintsAllowed = 2
eliminatesAllowed = 2

strikesMessage = {
    1: 'You have one strike! ',
    2: 'You have a second strike!, better watch out! '
}


gameContext = ['starting', 'playing', 'ending']

# Prompts that are used at random for correct answers
correctAnswerPrompts = [
    'you got! it ',
    'nice! ',
    'way to go! ',
    'good going! ',
    'you seem to know! ',
    'you know your stuff! ',
    'start a band because you are a rockstar! ',
    'congratulations!',
    'nice work!',
    'nice job!',
    'beautiful!',
    'baby you can be on a roll',
    'good!',
    'perfect',
    'alright!',
    'smart choice!',
    'fantastic!',
    'coolio!',
    'cool!',
    'keep it going!',
    'is your middle name smart?',
    'wise answer!',
    "wonderful!",
    "groovy!",
    "super!",
    "marvelous!",
    "fabulous!",
    "excellent!",
    "brilliant!",
    "swell!",
    "terrific!",
    "awesome!",
    "superb!",
    "outstanding!",
    "dynamite",
    "incredible!"
]

correctAudio = "https://s3.amazonaws.com/themakeshack/bell.mp3"
fail1Audio = "https://s3.amazonaws.com/themakeshack/fail1.mp3"
fail2Audio = "https://s3.amazonaws.com/themakeshack/fail2.mp3"
strikesAudio = ["", fail1Audio, fail2Audio]
gameoverAudio = "https://s3.amazonaws.com/themakeshack/gameover.mp3"
questionAudio = "https://s3.amazonaws.com/themakeshack/question.mp3"

# A dict to translate the list index position to spoken word
numToWord = {
    0: "one",
    1: "two",
    2: "three",
    3: "four"
}
### ---------- END Variables used in the game ----------

### ---------- START Functions that control the game ----------
class Game():
    def __init__(self, gamename):
        if gamename in gameMetaData:
            self.data = eval(gamename)
            self.metadata = gameMetaData[gamename]
            self.strikes = 0
            self.skips = 0
            self.eliminates = 0
            self.points = 0
            self.hints = 0
            self.choices = []
            self.position = 0
            self.answer = ""
            self.question = ""
            self.spokenQuestion = ""
            self.hintKeys = []
            self.pick_qa()
            self.make_spoken_qa()
        pass

    def pick_qa(self, numChoices=4):
        # this function picks the random key:value pair and returns key:value and three other random values
        # print teamdict
        if (len(self.metadata['usedQuestions']) < len(self.data)):
            self.question = random.choice(self.data.keys())
            while (self.question in self.metadata['usedQuestions']):
                self.question = random.choice(self.data.keys())
            self.metadata['usedQuestions'].append(self.question)
            self.answer = self.data[self.question]
            self.choices = [self.answer]
            while (len(self.choices) < numChoices):
                otherKey = random.choice(self.data.keys())
                if (otherKey != self.question and (self.data[otherKey] not in self.choices)):
                    self.choices.append(self.data[otherKey])
            random.shuffle(self.choices)
            self.position = self.choices.index(self.answer) + 1
        else:
            self.question = "End of category"

    def make_spoken_qa(self):
        # this the function that creates a question. It returns a speech output string and an answer string as a list
        # Call item picker to get a random key:value pair out of our dict and three other random values that re not the same as our key:value
        # Keep track of which random key:value pair we picked so we don't pick it again
        # Also keep track of how many key:value pairs we picked out of the list so we know when we run out

        if (self.question == "End of category"):
            self.speech_output = endOfCategoryMessage
            self.answer = ""
            self.position = 0

        if self.metadata["gameMode"] == "answerChoice":
            choiceString = ""
            for i in range(0, len(self.choices) - 1):
                choiceString += numToWord[i] + "," + self.choices[i] + '. '
            choiceString += "and " + numToWord[len(self.choices) - 1] + "," + self.choices[len(self.choices) - 1] + "."
            speech_question = self.metadata['questionPrefix'] + self.question + self.metadata['questionSuffix']
            speech_choices = self.metadata['choicesPrefix'] + choiceString + self.metadata['choicesSuffix']
            self.spokenQuestion = self.speech_output = speech_question + speech_choices
        elif self.metadata["gameMode"] == "realAnswer":
            speech_question = self.metadata['questionPrefix'] + self.question + self.metadata['questionSuffix']
            self.spokenQuestion = self.speech_output = speech_question

    def create_qa(self):
        self.pick_qa()
        self.make_spoken_qa()

    def pick_hints(self):
        # pick two other keys that have the same answer and return them
        if len(self.data) > 15:
            hintstogive = 3
        else:
            hintstogive = 2
        # setup a list of all hints - this will also reset if there are previous hints
        self.hintKeys = [self.question]
        while (len(self.hintKeys) <= hintstogive):
            hintKey = random.choice(self.data.keys())
            if (hintKey != self.question) and (hintKey not in self.hintKeys) and (self.data[hintKey] == self.answer):
                self.hintKeys.append(hintKey)

    def reduce_choices(self):
        numEliminates = 0

        # eliminate one choice from the choices list
        for choice in self.choices:
            if numEliminates < 1 and choice != self.data[self.question]:
                self.choices.remove(choice)
                numEliminates += 1
        # Mix up the choices remaining
        random.shuffle(self.choices)
        # find the new position of the answer
        self.position = self.choices.index(self.answer) + 1
        # Reconstruct the spoken question
        self.make_spoken_qa()

# Initialize a dummy game - this is useful for testing if the game selection has not been done by the user
#gameObject = Game('continents')

### ---------- END Functions that control the game ----------

### ---------- START handlers and routers for Alexa ----------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # Check to see if it is our application (skillID) that is sending this request, if not raise a ValueError
    if (event['session']['application']['applicationId'] != skillID):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    global gameObject
    """ Called when the user launches the skill without specifying what they
    want
    """
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "SelectGameIntent":
        return get_select_game_response(intent_request)
    elif intent_name == "AnswerIntent" or intent_name == "AnswerOnlyIntent":
        return get_answer_response(intent_request)
    elif intent_name == "SkipIntent":
        return get_skip_response()
    elif intent_name == "HintIntent":
        return get_hint_response()
    elif intent_name == "EliminateIntent":
        return get_eliminate_response()
    elif intent_name == 'RepeatIntent':
        return get_repeat_response()
    elif intent_name == "DontKnowIntent":
        return get_dont_know_response()
    elif intent_name == "AMAZON.StartOverIntent":
        return get_start_over_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    global gameObject
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # add cleanup logic here


### ---------- END handlers and routers for Alexa ----------

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ Welcome the user and provide the initial response """
    global context

    session_attributes = {}
    card_title = "Quizzical Welcome"
    speech_output = welcomeMessage
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with the same text.
    reprompt_text = rePromptWelcome
    should_end_session = False
    context = 'starting'  # we will use this context string to find context sensitive help
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_help_response():
    """ Get help response - this should be context sensitive depending on whether the user is just starting or if they are already playing"""
    global context
    session_attributes = {}
    card_title = "Quizzical Help"
    print(context)
    speech_output = helpMessage[context]
    reprompt_text = rePrompt
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_select_game_response(intent_request):
    """ Select the game type here """
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Game Select"
    selectedGame = intent_request["intent"]["slots"]["Game"]["value"]

    # Select the name of the "game" that we will use throughout the game
    for key in gameSelections:
        if selectedGame in gameSelections[key]['aliases']:
            # TODO: rather than fixing this as city or team, make the next level selection of sub game choices
            game = gameSelections[key]['choices']['city']
            gameObject = Game(gameSelections[key]['choices']['city'])

    if game != "":
        speech_output = "ok, " + selectedGame + "! let's begin!  "
        gameObject.create_qa()
        speech_output += gameObject.spokenQuestion
        # Since this is the first time we are playing, we should give more detailed instructions
        speech_output += gameObject.metadata["welcomeSuffix"]
    else:
        speech_output = rePromptGameSelection

    context = 'playing'
    reprompt_text = rePromptGameSelection
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_answer_response(intent_request):
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Game Answer"

    # The AnswerIntent returns a Answer object with no "value" set if the answer was not in the slots
    # We need to check that to create an incorrect answer if we dont get any "value"
    if ("value" in intent_request["intent"]["slots"]["Answer"].keys()):
        playerAnswer = intent_request["intent"]["slots"]["Answer"]["value"]
    else:
        playerAnswer = "Incorrect"

    if gameObject.metadata["gameMode"] == "answerChoice":
        if (playerAnswer == str(gameObject.position)):
            speech_output = random.choice(correctAnswerPrompts) + ". "
            audiosrc = correctAudio
            gameObject.points += 1
        else:
            speech_output = "Incorrect. The right answer was," + str(gameObject.position) + \
                            " ,which was," + gameObject.answer + ". "
            gameObject.strikes += 1
            if (gameObject.strikes >= strikesAllowed):
                return game_over()
            else:
                audiosrc = strikesAudio[gameObject.strikes]
                speech_output += strikesMessage[gameObject.strikes]

    elif gameObject.metadata["gameMode"] == "realAnswer":
        if (playerAnswer.lower() == gameObject.answer.lower()):
            speech_output = random.choice(correctAnswerPrompts) + ". "
            audiosrc = correctAudio
            gameObject.points += 1
        else:
            speech_output = "Incorrect. The right answer was," + gameObject.answer + ". "
            gameObject.strikes += 1
            if (gameObject.strikes >= strikesAllowed):
                return game_over()
            else:
                audiosrc = strikesAudio[gameObject.strikes]
                speech_output += strikesMessage[gameObject.strikes]

    gameObject.create_qa()
    speech_output += gameObject.spokenQuestion
    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    context = 'playing'

    return build_response(session_attributes,
                          build_ssml_response(card_title, speech_output, audiosrc, reprompt_text, should_end_session))


def get_skip_response():
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Skip"
    gameObject.skips += 1
    if gameObject.skips <= skipsAllowed:

        if gameObject.metadata["gameMode"] == "answerChoice":
            speech_output = "Skipping this question. For future use, the right answer was," + \
                            str(gameObject.position) + " ,which was," + gameObject.answer + \
                            ". Moving on to the next question, "
        elif gameObject.metadata["gameMode"] == "realAnswer":
            speech_output = "Skipping this question. For future use, the right answer was," + \
                            gameObject.answer + ". Moving on to the next question, "
        gameObject.create_qa()
        speech_output += gameObject.spokenQuestion
    else:
        speech_output = "Sorry you dont have any skips left. "
        if gameObject.metadata["gameMode"] == "answerChoice":
            if gameObject.eliminates < eliminatesAllowed:
                speech_output += "You could say, eliminate, to reduce your choices if you want. "
        elif gameObject.metadata["gameMode"] == "realAnswer":
            if gameObject.hints < hintsAllowed:
                speech_output += "You could ask for hint by saying, hint, if you would like. "

        speech_output += "Again, the question is, " + gameObject.spokenQuestion
    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_hint_response():
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Hint"

    gameObject.hints += 1
    if gameObject.hints <= hintsAllowed:

        if gameObject.metadata["gameMode"] == "answerChoice":
            speech_output = "Sorry I dont have a hint to give you, but you can say, eliminate, to eliminate a choice. "
        elif gameObject.metadata["gameMode"] == "realAnswer":
            speech_output = "Ok, here is a hint. "
            gameObject.pick_hints()
            for hint in range(0, len(gameObject.hintKeys) - 2):
                speech_output += gameObject.hintKeys[hint] + ", "
            speech_output += "and " + gameObject.hintKeys[len(gameObject.hintKeys) - 1] + ", "
            speech_output += "all have the same answer. what is yours? "
    else:
        speech_output = "Sorry, you don't have any hints left. "
        speech_output += "Again, the question is, " + gameObject.spokenQuestion

    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_eliminate_response():
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Eliminate"

    gameObject.eliminates += 1
    if gameObject.eliminates <= eliminatesAllowed:
        if gameObject.metadata["gameMode"] == "answerChoice":
            speech_output = "ok, let me eliminate a choice for you. "
            gameObject.reduce_choices()
            speech_output += gameObject.spokenQuestion

        elif gameObject.metadata["gameMode"] == "realAnswer":
            return get_hint_response()
    else:
        speech_output = "Sorry, you dont have any eliminates left. "
        speech_output += "Again, the question is, " + gameObject.spokenQuestion

    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_dont_know_response():
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Don't Know"

    if context == 'starting':
        return get_help_response()

    if gameObject.metadata["gameMode"] == "answerChoice":
        speech_output = "That is ok. The right answer was," + gameObject.position + " ,which was," + gameObject.answer + ". better luck with the next question, "
    elif gameObject.metadata["gameMode"] == "realAnswer":
        speech_output = "That is ok. The right answer was," + gameObject.answer + ". better luck with the next question, "
    gameObject.create_qa()
    speech_output += gameObject.spokenQuestion
    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_repeat_response():
    global gameObject
    session_attributes = {}
    card_title = "Quizzical Repeat"
    speech_output = "ok, again. " + gameObject.spokenQuestion
    reprompt_text = gameObject.spokenQuestion
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_start_over_response():
    global gameObject, context
    session_attributes = {}
    card_title = "Quizzical Restart Game"

    gameObject.metadata['usedQuestions'] = []
    context = 'starting'
    gameObject.points = 0
    gameObject.strikes = 0
    return get_welcome_response()


def handle_session_end_request():
    card_title = "Quizzical Session Ended"
    speech_output = endMessage
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def game_over():
    session_attributes = {}
    card_title = "Quizzical Game Over"
    speech_output = "You got " + str(gameObject.points) + " points. "
    speech_output += "Good effort, but you can only have " + str(strikesAllowed) + " strikes and you are out. "
    speech_output += "Thanks for playing Quizzical and hope to see you again soon"
    should_end_session = True
    audiosrc = gameoverAudio

    # return build_response({}, build_speechlet_response(
    #    card_title, speech_output, None, should_end_session))
    return build_response(session_attributes,
                          build_ssml_response(card_title, speech_output, audiosrc, None, should_end_session))


# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def build_ssml_response(title, output, audiosrc, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': '<speak> <audio src="' + audiosrc + '"/>' + output + ' </speak>'
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
