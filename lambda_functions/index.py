# coding=utf-8

"""
This code sample is a part of a simple demo to show beginners how to create a skill (app) for the Amazon Echo using AWS Lambda and the Alexa Skills Kit.

For the full code sample visit https://github.com/pmckinney8/Alexa_Dojo_Skill.git


TO-DO
1) Change the code such that the program runs like a multichoice quizzical
2) Initially focus on NFL cities and teams
3) Expand into player stats
4) Expand into other sports
5) Implement a peristent point heme based on user data

"""
from __future__ import print_function

import random

### ---------- START Game specific data ----------
# Get our speech output variables defined here
welcomeMessage = "Welcome to Quizzical. " \
                 "You have several games to choose from. " \
                 "Depending on your game choice, you can either choose from options, or give a one word answer. " \
                 "You can move along in the game by saying, " \
                 "repeat, to repeat a question, " \
                 "skip, to skip a question, " \
                 "hint, to get a hint, " \
                 "eliminate, to remove a choice, " \
                 "start over, to restart the game, " \
                 "or, stop, to end the game. " \
                 "If you didn't get all that, don't worry, you can always say, help. and I will assist you. " \
                 "Now, say which game would you like to play. continents, or, capitals."
rePromptWelcome = "Welcome to Quizzical, say the name of the game. "
rePromptContinent = "Say the name of the continent"
rePromptCapital = "Give me the number choice for the capital"
rePromptGameSelection = "what is your selection. "
rePromptIDK = "what is your choice"
rePrompt = "what is your choice"
helpMessage = {
    'starting': "Quizzical help. Simply say the name of the selection, continents or capitals. Or if you want to start over simply say, start over. To end the game say, stop",
    'playing': "Quizzical help. You can say, " \
               "repeat to repeat a question, " \
               "skip, to skip a question, " \
               "hint, to get a hint, " \
               "eliminate, to remove a choice, " \
               "start over, to restart the game, " \
               "or, stop, to end the game."

}
endOfCategoryMessage = "Congratulations!, you have reached the end of this category, say, start over, to choose a new one. "
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
                    # TODO: The 'city' keyword is a remnant that needs to be changed to comething meaningful
                }
        },

    'capitals':
        {
            'aliases': ['capital', 'capitals'],
            'choices':
                {
                    'city': 'capitals'
                    # TODO: The 'city' keyword is a remnant that needs to be changed to comething meaningful
                }
        }
}

# dict that stores the soeech responses for each game and tracks the questions
gameData = {

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

# Initialize a game - this is useful for testing if the game selection has not been done by the user
game = "continents"
### ---------- END Game specific data ----------


### ---------- START Variables used in the game ----------
# Initialize variables
question = ""
answer = ""
answerPosition = 0
gameMode = ""  # it will be realanswer or answernumber
context = "starting"
choices = []
questionKey = ""

strikes = 0
strikesAllowed = 3
skips = 0
skipsAllowed = 2
hints = 0
hintsAllowed = 2
eliminates = 0
eliminatesAllowed = 2
points = 0

strikesMessage = {
    1: 'You have one strike! ',
    2: 'You have a second strike!, better watch out! '
}

hintsMessage = "I can give you a hint Here it is. "
skipMessage = "No problems, skipping. "
eliminateMessage = "I can eliminate one of your choices. "
alreadySkipped = "Sorry, you have already used the " + str(skipsAllowed) + " skips you are allowed. "
alreadyHinted = "Sorry, you have already used the " + str(hintsAllowed) + " hints you are allowed. "
alreadyEliminated = "Sorry, you have already used the " + str(eliminatesAllowed) + " eliminations you are allowed. "

gameContext = ['starting', 'playing', 'ending']

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


### ---------- END Variables used in the game ----------

### ---------- START Functions that control the game ----------
def pick_qa(teamDictName):
    # this function picks the random key:value pair and returns key:value and three other random values from the dictionary
    # print teamdict
    if teamDictName in gameData:
        teamdict = eval(teamDictName)
        if (len(gameData[teamDictName]['usedQuestions']) < len(teamdict)):
            question = random.choice(teamdict.keys())
            while (question in gameData[teamDictName]['usedQuestions']):
                question = random.choice(teamdict.keys())
            gameData[teamDictName]['usedQuestions'].append(question)
            answer = teamdict[question]
            choices = [answer]
            while (len(choices) < 4):
                otherKey = random.choice(teamdict.keys())
                if (otherKey != question and (teamdict[otherKey] not in choices)):
                    choices.append(teamdict[otherKey])
            random.shuffle(choices)
            position = choices.index(answer)
            return (question, answer, position, choices)
        else:
            return ("End of category", "answer", 0, ["answer", "answer", "answer", "answer"])
    else:
        return ("question", "answer", 0, ["answer", "answer", "answer", "answer"])


def pick_hint(teamDictName, questionKey):
    teamdict = eval(teamDictName)
    # pick two other keys that have the same answer and return them
    answer = teamdict[questionKey]
    if len(teamdict) > 15:
        hintstogive = 3
    else:
        hintstogive = 2

    hintKeys = [questionKey]
    while (len(hintKeys) <= hintstogive):
        hintKey = random.choice(teamdict.keys())
        if (hintKey != question) and (hintKey not in hintKeys) and (teamdict[hintKey] == answer):
            hintKeys.append(hintKey)
    return hintKeys


def eliminate_choice(teamDictName, questionKey, choices):
    teamdict = eval(teamDictName)
    question = questionKey
    answer = teamdict[questionKey]

    numToWord = {
        0: "one",
        1: "two",
        2: "three",
        3: "four"
    }
    numEliminates = 0
    # eliminate one choice from the choices list
    for choice in choices:
        if numEliminates < 1 and choice != teamdict[questionKey]:
            choices.remove(choice)
            numEliminates += 1

    # Mix up the choices remaining
    random.shuffle(choices)

    # find the new position of the answer
    position = choices.index(answer)

    if gameData[teamDictName]["gameMode"] == "answerChoice":
        choiceString = ""
        for i in range(0, len(choices) - 1):
            choiceString += numToWord[i] + "," + choices[i] + '. '
        choiceString += "and " + numToWord[len(choices) - 1] + "," + choices[len(choices) - 1] + "."
        speech_question = gameData[teamDictName]['questionPrefix'] + question + gameData[teamDictName]['questionSuffix']
        speech_choices = gameData[teamDictName]['choicesPrefix'] + choiceString + gameData[teamDictName][
            'choicesSuffix']
        speech_output = speech_question + speech_choices
        return (speech_output, answer, str(position + 1), questionKey, choices)
    elif gameData[teamDictName]["gameMode"] == "realAnswer":
        speech_question = gameData[teamDictName]['questionPrefix'] + question + gameData[teamDictName]['questionSuffix']
        speech_output = speech_question
        return (speech_output, answer, '0', questionKey, choices)


def create_question(teamDictName):
    # this the function that creates a question. It returns a speech output string and an answer string as a list
    # Call item picker to get a random key:value pair out of our dict and three other random values that re not the same as our key:value
    # Keep track of which random key:value pair we picked so we dont pick it again
    # Also keep track of how many key:value pais we picked out of the list so we know when we run out
    (question, answer, position, choices) = pick_qa(teamDictName)
    questionKey = question
    if (question == "End of category"):
        speech_output = endOfCategoryMessage
        answer = ""
        return (speech_output, answer, 0)
    # print "Question = " + question
    # print "Answer = " + answer
    # print "Position of answer in the list is = " + str(position)
    # print "Choices: ", choices
    numToWord = {
        0: "one",
        1: "two",
        2: "three",
        3: "four"
    }
    if gameData[teamDictName]["gameMode"] == "answerChoice":
        choiceString = ""
        for i in range(0, len(choices) - 1):
            choiceString += numToWord[i] + "," + choices[i] + '. '
        choiceString += "and " + numToWord[len(choices) - 1] + "," + choices[len(choices) - 1] + "."
        speech_question = gameData[teamDictName]['questionPrefix'] + question + gameData[teamDictName]['questionSuffix']
        speech_choices = gameData[teamDictName]['choicesPrefix'] + choiceString + gameData[teamDictName][
            'choicesSuffix']
        speech_output = speech_question + speech_choices
        return (speech_output, answer, str(position + 1), questionKey, choices)
    elif gameData[teamDictName]["gameMode"] == "realAnswer":
        speech_question = gameData[teamDictName]['questionPrefix'] + question + gameData[teamDictName]['questionSuffix']
        speech_output = speech_question
        return (speech_output, answer, '0', questionKey, choices)


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
    global strikes, skips, hints, eliminates, points
    """ Called when the user launches the skill without specifying what they
    want
    """
    strikes = skips = hints = eliminates = points = 0
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
    global strikes, skips, hints, eliminates, points
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    strikes = skips = hints = eliminates = points = 0

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
    global game, question, answer, answerPosition, context, strikes, questionKey, choices
    session_attributes = {}
    card_title = "Quizzical Game Select"
    selectedGame = intent_request["intent"]["slots"]["Game"]["value"]

    # Select the name of the "game" that we will use throughout the game
    for key in gameSelections:
        if selectedGame in gameSelections[key]['aliases']:
            # TODO: rather than fixing this as city or team, make the next level selection of sub game choices
            game = gameSelections[key]['choices']['city']

    if game != "":
        speech_output = "ok, " + selectedGame + "! let's begin!  "
        (question, answer, answerPosition, questionKey, choices) = create_question(game)
        speech_output += question
        # Since this is the first time we are playing, we should give mire detailed instructions
        speech_output += gameData[game]["welcomeSuffix"]
    else:
        speech_output = rePromptGameSelection

    context = 'playing'
    reprompt_text = rePromptGameSelection
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_answer_response(intent_request):
    global question, answer, answerPosition, context, strikes, points, questionKey, choices
    session_attributes = {}
    card_title = "Quizzical Game Answer"

    # The AnswerIntent returns a Answer object with no "value" set if the answer was not in the slots
    # We need to check that to create an incorrect answer if we dont get any "value"
    if ("value" in intent_request["intent"]["slots"]["Answer"].keys()):
        playerAnswer = intent_request["intent"]["slots"]["Answer"]["value"]
    else:
        playerAnswer = "Incorrect"

    if gameData[game]["gameMode"] == "answerChoice":
        if (playerAnswer == answerPosition):
            speech_output = random.choice(correctAnswerPrompts) + ". "
            audiosrc = correctAudio
            points += 1
        else:
            speech_output = "Incorrect. The right answer was," + str(answerPosition) + " ,which was," + answer + ". "
            strikes += 1
            if (strikes >= strikesAllowed):
                return game_over()
            else:
                audiosrc = strikesAudio[strikes]
                speech_output += strikesMessage[strikes]

    elif gameData[game]["gameMode"] == "realAnswer":
        if (playerAnswer.lower() == answer.lower()):
            speech_output = random.choice(correctAnswerPrompts) + ". "
            audiosrc = correctAudio
            points += 1
        else:
            speech_output = "Incorrect. The right answer was," + answer + ". "
            strikes += 1
            if (strikes >= strikesAllowed):
                return game_over()
            else:
                audiosrc = strikesAudio[strikes]
                speech_output += strikesMessage[strikes]

    (question, answer, answerPosition, questionKey, choices) = create_question(game)
    speech_output += question
    reprompt_text = question
    should_end_session = False
    context = 'playing'

    return build_response(session_attributes,
                          build_ssml_response(card_title, speech_output, audiosrc, reprompt_text, should_end_session))


def get_skip_response():
    global gameData, game, question, answer, answerPosition, skips, questionKey, choices
    session_attributes = {}
    card_title = "Quizzical Skip"
    skips += 1
    if skips <= skipsAllowed:

        if gameData[game]["gameMode"] == "answerChoice":
            speech_output = "Skipping this question. For future use, the right answer was," + answerPosition + " ,which was," + answer + ". Moving on to the next question, "
        elif gameData[game]["gameMode"] == "realAnswer":
            speech_output = "Skipping this question. For future use, the right answer was," + answer + ". Moving on to the next question, "
        (question, answer, answerPosition, questionKey, choices) = create_question(game)
        speech_output += question
    else:
        speech_output = "Sorry you dont have any skips left. "
        if gameData[game]["gameMode"] == "answerChoice":
            if eliminates < eliminatesAllowed:
                speech_output += "You could say, eliminate, to reduce your choices if you want. "
        elif gameData[game]["gameMode"] == "realAnswer":
            if hints < hintsAllowed:
                speech_output += "You could ask for hint by saying, hint, if you would like. "

        speech_output += "Again, the question is, " + question
    reprompt_text = question
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_hint_response():
    global gameData, game, question, answer, answerPosition, hints, questionKey, choices
    session_attributes = {}
    card_title = "Quizzical Hint"

    hints += 1
    if hints <= hintsAllowed:

        if gameData[game]["gameMode"] == "answerChoice":
            speech_output = "Sorry I dont have a hint to give you, but you can say, eliminate, to eliminate a choice. "
        elif gameData[game]["gameMode"] == "realAnswer":
            speech_output = "Ok, here is a hint. "
            hintKeys = pick_hint(game, questionKey)
            for hint in range(0, len(hintKeys) - 2):
                speech_output += hintKeys[hint] + ", "
            speech_output += "and " + hintKeys[len(hintKeys) - 1] + ", "
            speech_output += "all have the same answer. what is yours? "
    else:
        speech_output = "Sorry, you dont have any hints left. "
        speech_output += "Again, the question is, " + question

    reprompt_text = question
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_eliminate_response():
    global gameData, game, question, answer, answerPosition, hints, questionKey, choices, eliminates
    session_attributes = {}
    card_title = "Quizzical Eliminate"

    eliminates += 1
    if eliminates <= eliminatesAllowed:

        if gameData[game]["gameMode"] == "answerChoice":
            speech_output = "ok, let me eliminate a choice for you. "
            (question, answer, answerPosition, questionKey, choices) = eliminate_choice(game, questionKey, choices)
            speech_output += question

        elif gameData[game]["gameMode"] == "realAnswer":
            return get_hint_response()
    else:
        speech_output = "Sorry, you dont have any eliminates left. "
        speech_output += "Again, the question is, " + question

    reprompt_text = question
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_dont_know_response():
    global gameData, game, question, answer, answerPosition
    session_attributes = {}
    card_title = "Quizzical Don't Know"

    if context == 'starting':
        return get_help_response()

    if gameData[game]["gameMode"] == "answerChoice":
        speech_output = "That is ok. The right answer was," + answerPosition + " ,which was," + answer + ". Better luck with the next question, "
    elif gameData[game]["gameMode"] == "realAnswer":
        speech_output = "That is ok. The right answer was," + answer + ". Better luck with the next question, "
    (question, answer, answerPosition, questionKey, choices) = create_question(game)
    speech_output += question
    reprompt_text = question
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_repeat_response():
    global game, question, answer, answerPosition
    session_attributes = {}
    card_title = "Quizzical Repeat"
    speech_output = "ok, again. " + question
    reprompt_text = question
    should_end_session = False
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_start_over_response():
    global context, points, strikes
    session_attributes = {}
    card_title = "Quizzical Restart Game"
    for key in gameData:
        gameData[key]['usedQuestions'] = []
    context = 'starting'
    points = 0
    strikes = 0
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
    speech_output = "You got " + str(points) + " points. "
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
