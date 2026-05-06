# Вспомогательный файл для заполнения базы данных

# Ctrl + 1 - Полноценная ульта
# Ctrl + 2 - Base only ульта
# Ctrl + 3 - Overpowered ульта
# Ctrl + 4 - Скиллы
# Ctrl + 5 - Вывод инфы

from data.characters import Character
from data.db_session import create_session


def Honored_One():
    character = Character()
    character.name = "Honored One"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    - существует специальные варианты на 2 + R, 3 + R
    - используйте R, когда противник в воздухе, это активирует воздушный вариант
    - после нажатия R, повернитесь на 180 градусов, тогда вы телепортируетесь за спину противника'''
    character.is_custom = False

    character.move1 = "Lapse Blue"
    character.move2 = "Reversal Red"
    character.move3 = "Rapid Punches"
    character.move4 = "Twofold Kick"
    character.special = "Limitless"

    character.base_only_awakening = None

    character.awakening = "Six Eyes"
    character.ult_move1 = "Lapse Blue MAX"
    character.ult_move2 = "Reversal Red MAX"
    character.ult_move3 = "Hollow Purple"
    character.ult_move4 = "Infinite Void"
    character.ult_special = "Limitless"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Honored One добавлен в базу данных")


def Vessel():
    character = Character()
    character.name = "Vessel"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    - для манёвренности можно использовать 2 + R
    - используйте "chain" - чёрную молнию(Divergent Fist) в спину противнику - максимум 4 раза
    - счётчик chain можно сбросить с помощью клика M1 или 3 + R
    
    - R в авейке(ульте) сносит 40% хп противника - хорошо подходит для большого количества хпб например против Махораги
    - в авейке(ульте) зажмите 1, нажмите 3, затем 2, после R и отпустите 1 - вы сделаете Мировой развез (WCS)
    - не используйте WCS на толпе, ведь урон распределится на всех равномерно
    - авейк(ульту) Хакари(Restless Gambler) можно убить: запереть в домейне, поджарить Open и нарезать Мировым'''
    character.is_custom = False

    character.move1 = "Cursed Strikes"
    character.move2 = "Crushing Blow"
    character.move3 = "Divergent Fist"
    character.move4 = "Manji Kick"
    character.special = "Combat Instincts"

    character.base_only_awakening = None

    character.awakening = "King of Curses"
    character.ult_move1 = "Dismantle"
    character.ult_move2 = "Open"
    character.ult_move3 = "Rush"
    character.ult_move4 = "Malevolent Shrine"
    character.ult_special = "Cleave"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Vessel добавлен в базу данных")


def Restless_Gambler():
    character = Character()
    character.name = "Restless Gambler"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    - Reserve Balls может отскакивать от стен
    - существует вариант 1 + 2, а так же 4 + 2
    - у R для прямых и летящих атак разная анимация
    - если Shutter Doors не задел противника, но тот в свою очередь упал на двери, то будет отдельный вариант атаки
    - если Shutter Doors не ударил противника вы можете на них прыгнуть и подлететь вверх
    - чем вы выше, тем больше урон от air-варианта Rough Energy
    
    - в вашей территории нажав R ДОПИСАТЬ
    - когда вы в авейке(ульте), любой полученный урон будет забирать небольшую часть вашей полоски авейка(ульты)
    - в РТ(расширении территории) Хигурумы вы можете настакать себе R, так как полоска авейка не будет тратиться'''
    character.is_custom = False

    character.move1 = "Reserve Balls"
    character.move2 = "Shutter Doors"
    character.move3 = "Rough Energy"
    character.move4 = "Fever Breaker"
    character.special = "Door Guard"

    character.base_only_awakening = None

    character.awakening = "Idle Death Gamble"
    character.ult_move1 = "Lucky Volley"
    character.ult_move2 = "Lucky Rushdown"
    character.ult_move3 = "Overwhelming Luck"
    character.ult_move4 = "Energy Surge"
    character.ult_special = "Rhythm"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Restless Gambler добавлен в базу данных")


def Ten_Shadows():
    character = Character()
    character.name = "Ten Shadows"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    - когда вы используете эмоцию волк(Divine Dog: Totality) начинает танцевать)
    - если вы держите какой-то предмет, то нажав R вы поместите его к себе в тень - максимум 1 штука, чтобы вытащить нажмите R + M1
    - если у вас уже лежит что-то в тени, то, держа предмет, вы не сможете использовать R
    - варианты: R + 1, 3 + 2, 2 + R
    - можно заспамить использовав 3 + 2, 1, 2 смотря на цель, 4
    
    - вы можете проникнуть в чужой домейн(расширение территории), использовав 3(Shadow Swarm) рядом в РТ
    - Хакари(Restless Gambler), выйдя с помощью чужого Shadow Swarm, всё ещё может выбить Jackpot
    - хорошо использовать слона(1 Max Elephant) сразу после 2(Great Serpent)
    - пока вы в змее(Great Serpent) перемещайтесь под углом 30 градусов над зданиями и спамьте 4(Mahoraga)'''
    character.is_custom = False

    character.move1 = "Rabbit Escape"
    character.move2 = "Nue"
    character.move3 = "Toad"
    character.move4 = "Divine Dog: Totality"
    character.special = "Lurking Shadow"

    character.base_only_awakening = None

    character.awakening = "Insanity"
    character.ult_move1 = "Max Elephant"
    character.ult_move2 = "Great Serpent"
    character.ult_move3 = "Shadow Swarm"
    character.ult_move4 = "Mahoraga"
    character.ult_special = "Lurking Shadow"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Ten Shadows добавлен в базу данных")


def Perfection():
    character = Character()
    character.name = "Perfection"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Stockpile"
    character.move2 = "Soul Fire"
    character.move3 = "Focus Strike"
    character.move4 = "Body Repel"
    character.special = "Self Transfiguration"

    character.base_only_awakening = None

    character.awakening = "Essence of the Soul"
    character.ult_move1 = "Idle Transfiguration "
    character.ult_move2 = "Body Disfigure"
    character.ult_move3 = "Spike Wrath"
    character.ult_move4 = "Embodiment of Self Perfection"
    character.ult_special = "Self Transfiguration"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Perfection добавлен в базу данных")


def Blood_Manipulator():
    character = Character()
    character.name = "Blood Manipulator"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Piercing Blood"
    character.move2 = "Flowing Red Scale"
    character.move3 = "Supernova"
    character.move4 = "Blood Edge"
    character.special = "Convergence"

    character.base_only_awakening = None

    character.awakening = "Duty as a Brother"
    character.ult_move1 = "Slicing Exorcism"
    character.ult_move2 = "Wing King"
    character.ult_move3 = "Blood Rain"
    character.ult_move4 = "Plasma Wave"
    character.ult_special = "Convergence"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Blood Manipulator добавлен в базу данных")


def Switcher():
    character = Character()
    character.name = "Switcher"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Swift Kick"
    character.move2 = "Brute Force"
    character.move3 = "Pebble Throw"
    character.move4 = "Elbow Drop"
    character.special = "Boogie Woogie"

    character.base_only_awakening = None

    character.awakening = "False Memories"
    character.ult_move1 = "Idol's Debut"
    character.ult_move2 = "Climax Jumping"
    character.ult_move3 = "Dreams"
    character.ult_move4 = "Brothers"
    character.ult_special = "Boogie Woogie"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Switcher добавлен в базу данных")


def Defense_Attorney():
    character = Character()
    character.name = "Defense Attorney"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Extended Swings"
    character.move2 = "Justice Served"
    character.move3 = "Judgement's Reach"
    character.move4 = "Pressing Charges"
    character.special = "No Escape"

    character.base_only_awakening = None

    character.awakening = "Deadly Sentencing"
    character.ult_move1 = "Execution"
    character.ult_move2 = "Final Judgement"
    character.ult_move3 = "Verdict"
    character.ult_move4 = "Triple Sentence"
    character.ult_special = "Domain Amplification"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Defense Attorney добавлен в базу данных")


def Cursed_Partners():
    character = Character()
    character.name = "Cursed Partners"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Severing Path"
    character.move2 = "Resolute Slash"
    character.move3 = "Veilstep"
    character.move4 = "Revolve"
    character.special = "Rika"

    character.base_only_awakening = None

    character.awakening = "True Love"
    character.ult_move1 = "Elbow Rush"
    character.ult_move2 = "Copy"
    character.ult_move3 = "True Love Beam"
    character.ult_move4 = "Authentic Mutual Love"
    character.ult_special = "Rika"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Cursed Partners добавлен в базу данных")


def Puppet_Master():
    character = Character()
    character.name = "Puppet Master"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Ultra Spin"
    character.move2 = "Boost On"
    character.move3 = "Ultra Cannon"
    character.move4 = "Heat Emission"
    character.special = "Offload"

    character.base_only_awakening = None

    character.awakening = "Absolute"
    character.ult_move1 = "Miracle Cannon"
    character.ult_move2 = "Pigeon Viola"
    character.ult_move3 = "Absolute Destruction"
    character.ult_move4 = "Technique Charge"
    character.ult_special = "Energy Output"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Puppet Master добавлен в базу данных")


def Head_of_the_Hei():
    character = Character()
    character.name = "Head of the Hei"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Projection Breaker"
    character.move2 = "Bleedout"
    character.move3 = "Decisive Strike"
    character.move4 = "Cursory Impact"
    character.special = "Projection Sorcery"

    character.base_only_awakening = None

    character.awakening = "Vengeance"
    character.ult_move1 = "Top Speed"
    character.ult_move2 = "Flash Freezing"
    character.ult_move3 = "Tendril Grab"
    character.ult_move4 = "Time Cell Moon Palace"
    character.ult_special = "Acceleration"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Head of the Hei добавлен в базу данных")


def Salaryman():
    character = Character()
    character.name = "Salaryman"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Cleaving Whirlwind"
    character.move2 = "Severance Kick"
    character.move3 = "Blunt Cut"
    character.move4 = "Stabilize"
    character.special = "Ratio Point"

    character.base_only_awakening = None

    character.awakening = "Overtime"
    character.ult_move1 = "Ratio Breaker"
    character.ult_move2 = "Sharpen"
    character.ult_move3 = "Interrogate"
    character.ult_move4 = "Collapse"
    character.ult_special = "Ratio Point"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Salaryman добавлен в базу данных")


def Disaster_Plant():
    character = Character()
    character.name = "Disaster Plant"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Root Swarm"
    character.move2 = "Surging Thorns"
    character.move3 = "Bud Shot"
    character.move4 = "Defense Response"
    character.special = "Flower Field"

    character.base_only_awakening = None

    character.awakening = "Unwrap"
    character.ult_move1 = None
    character.ult_move2 = None
    character.ult_move3 = None
    character.ult_move4 = None
    character.ult_special = None

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Disaster Plant добавлен в базу данных")


def True_Cannon():
    character = Character()
    character.name = "True Cannon"
    character.base_only = False
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Granite Blast"
    character.move2 = "Unsatisfied"
    character.move3 = "Second Helping"
    character.move4 = "Appetizer"
    character.special = "Restyle"

    character.base_only_awakening = None

    character.awakening = "Every Last Drop."
    character.ult_move1 = "\"What are you after?\""
    character.ult_move2 = "\"I had no idea...\""
    character.ult_move3 = "\"This is what dessert is like!\""
    character.ult_move4 = None
    character.ult_special = "Restyle"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("True Cannon добавлен в базу данных")


################# << Base only >> #################

def Locust_Guy():
    character = Character()
    character.name = "Locust Guy"
    character.base_only = True
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Clever"
    character.move2 = "Black Mucus"
    character.move3 = "Crushing Jaws"
    character.move4 = "Wing Throw"
    character.special = "Fluttering Pounce"

    character.base_only_awakening = "Directed Poison"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Locust Guy добавлен в базу данных")


def Star_Rage():
    character = Character()
    character.name = "Star Rage"
    character.base_only = True
    character.overpowered = False
    character.tips = '''
    - прицепитесь будучи чёрной дырой в авейку(ульите) Наои(Head of the Hei) союзнику - у него отличная скорость, противники не успеют убежать'''
    character.is_custom = False

    character.move1 = "Garuda Rebound"
    character.move2 = "Rising Rage"
    character.move3 = "Mass Breaker"
    character.move4 = "Garuda Stab"
    character.special = "Mass Buildup"

    character.base_only_awakening = "Unrestricted Density"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Star Rage добавлен в базу данных")


def Aspiring_Mangaka():
    character = Character()
    character.name = "Aspiring Mangaka"
    character.base_only = True
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Despair"
    character.move2 = "Shut Up!"
    character.move3 = "Eye Catching"
    character.move4 = "Sacrilege"
    character.special = "Clairvoyance"

    character.base_only_awakening = "Foresight"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Aspiring Mangaka добавлен в базу данных")


def Lucky_Coward():
    character = Character()
    character.name = "Lucky Coward"
    character.base_only = True
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Ambush" # Ankle Cutter
    character.move2 = "Backstab" # High Time
    character.move3 = "Trip" # Остаётся
    character.move4 = "Cheap Shot" # Dirty Play
    character.special = "Helping Hand"

    character.base_only_awakening = "Jawbreaker"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Lucky Coward добавлен в базу данных")


def Crow_Charmer():
    character = Character()
    character.name = "Crow Charmer"
    character.base_only = True
    character.overpowered = False
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Impetus Updraft"
    character.move2 = "Circling"
    character.move3 = "Gliding Flight"
    character.move4 = "Bird Control"
    character.special = "Flock"

    character.base_only_awakening = "Bird Strike"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Crow Charmer добавлен в базу данных")


################# < Overpowered > #################

def Strongest_Of_History():
    character = Character()
    character.name = "Strongest Of History"
    character.base_only = True
    character.overpowered = True
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Strong Dismantle"
    character.move2 = "Open FURNACE"
    character.move3 = "Cleave Rush"
    character.move4 = "Kamutoke"
    character.special = "Incantation"

    character.base_only_awakening = "Incomplete Shrine"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Strongest Of History добавлен в базу данных")


def Monkey_Kid():
    character = Character()
    character.name = "Monkey Kid"
    character.base_only = True
    character.overpowered = True
    character.tips = '''
    '''
    character.is_custom = False

    character.move1 = "Kamehameha"
    character.move2 = "Ki Spam"
    character.move3 = "Staff Extend"
    character.move4 = "Staff Uppercut"
    character.special = "Instant Transmission"

    character.base_only_awakening = "Monkey"

    db_sess = create_session()
    db_sess.add(character)
    db_sess.commit()

    print("Monkey Kid добавлен в базу данных")


#####################################

def Lapse_Blue():
    pass


if __name__ == '__main__':
    print("-----------------< Персонажи >-----------------")

    print("С полноценным авейком")
    print("- Honored One - Годжо Сатору")
    print("- Vessel - Юдзи Итадори и Рёмен Сукуна(15 пальцев)")
    print("- Restless Gambler - Киндзи Хакари")
    print("- Ten Shadows - Фушигуро Мегуми")
    print("- Perfection - Махито")
    print("- Blood Manipulator - Чосо")
    print("- Switcher - Аои Тодо")
    print("- Defense Attorney - Хироми Хигурума")
    print("- Cursed Partners - Окоцу Юта")
    print("- Puppet Master - Мехамару (Кокичи Мута)")
    print("- Head of the Hei - Дзенин Наоя")
    print("- Salaryman - Кенто Нанами")
    print("- Disaster Plant - Ханами")
    print("- True Cannon - Ишигори Рью")

    print("Base only")
    print("- Locust Guy - Ко-Гай")
    print("- Star Rage - Тсукумо Юки")
    print("- Aspiring Mangaka - Бернард Чарльз")
    print("- Lucky Coward - Шигемо Харута")
    print("- Crow Charmer - Мей Мей")

    print("Overpowered")
    print("- Strongest Of History - Рёмен Сукуна (Хейан)")
    print("- Monkey Kid - Сон Гоку")

    print("Other")
    print("- Super TZE - TZE (главный разработчик)") # Не добавлен
    print("- Mokou - Кто-то из Фудживар", "          !!! НЕ ПОДТВЕРЖДЕНО !!!") # Не добавлен
    print("- Cursed Child - Чара из \"Андертейл\"") # Не добавлен

    print("-----------------< Скиллы >-----------------")
    print()
