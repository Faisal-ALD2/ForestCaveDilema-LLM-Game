from builtins import input


def intro_adam():
    print("In a world where resources are scarce, you, Adam, a geologist in your late 30s, toil for a small firm, burdened by a history of breathing issues since childhood.")
    print("Inspired by your father, a renowned geologist before a tragic accident left him disabled, you strive to not only support your family but also live up to your father's legacy.")
    print("You work tirelessly, facing the challenges and limitations imposed by your circumstances, determined to make your father proud.")
    print("\nRumors swirl of a lucrative market for meteoroids, with many reportedly landing in the elusive Gate Forest.")
    print("Recognizing your expertise in identifying such rocks, you contemplate the risk of venturing into the forest at dawn.")
    print("The potential rewards could change your family's fortunes, but the gamble is steep.")
    print("\nWhat will you do?")
    print("1. Venture into the Gate Forest at dawn.")
    print("2. Stay and continue your work with the small firm.")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2): "))
            if choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
    return choice

def intro_mark():
    print("\nEnter Mark, a doctor with a penchant for rare rocks and a close friend of Adam's.")
    print("Mark, also employed by a hospital, is not only Adam's confidant but also his primary care physician.")
    print("Should Adam choose to embark on this risky endeavor, Mark stands ready to join him in the forest.")
    print("\nWill you invite Mark to join you?")
    print("1. Yes")
    print("2. No")

def get_mark_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2): "))
            if choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
    return choice

intro_adam()
choice = get_user_choice()

if choice == 1:
    intro_mark()
    mark_choice = get_mark_choice()
    if mark_choice == 1:
        print("\nAdam's resolve solidifies, and on a Sunday morning, he sets out with Mark to explore Gate Forest. Inside, they stumble upon a cave teeming with an array of shiny rocks, glistening in the dim light. Their enthusiasm is dampened by warnings of low oxygen levels, signaling danger lurking in the cave's depths. ")
        # Code for what happens next if Mark accepts the invitation
    elif mark_choice == 2:
        print("\nYou decide to venture into the forest alone.")
        # Code for what happens next if Adam ventures into the forest alone
elif choice == 2:
    print("\nYou decide to stay and continue your work with the small firm.")
    # Code for what happens next if Adam stays with the firm

def explore_cave():
    print("\nFaced with a pivotal decision, Adam must weigh the allure of the shiny rocks against the safety of retreat.")
    print("Mark, on the other hand, grapples with risking his friend's life for mere objects.")
    print("\nAdam, driven by a mixture of desperation and hope, pushes deeper into the cave, leading Mark through a narrow passage he believes will shortcut their journey to the valuable rocks.")
    print("\nAs they navigate the passage, the air thickens with an eerie silence, broken only by strange, otherworldly noises.")
    print("The walls of the cave come alive with ancient hieroglyphs, hinting at a history of extraterrestrial visitation to Earth.")
    print("\nWhat will you do?")
    print("1. Continue pushing deeper into the cave.")
    print("2. Retreat and find another route.")
    print("3. Investigate the hieroglyphs.")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
    return choice

def outcome_1():
    print("\nAdam's gamble pays off, and they discover a cache of valuable meteoroids.")
    print("They manage to extract them safely.")

def outcome_2():
    print("\nThe passage leads to a perilous situation, such as a collapse or encountering hostile creatures.")
    print("Adam and Mark must use their wits to survive and find a way out, but they emerge empty-handed.")

def outcome_3():
    print("\nWhile they are invistigating some scary looking creatures show up & attack them, and Adam dies. The game ends.")

explore_cave()
choice = get_user_choice()

if choice == 1:
    outcome_1()
elif choice == 2:
    outcome_2()
elif choice == 3:
    outcome_3()

def perilous_turn():
    print("\nTheir exploration takes a perilous turn when a creature, resembling a turtle but with a sinister intent, attacks Adam.")
    print("Mark, armed with a hunting rifle, fends off the creature, saving Adam from certain doom.")
    print("\nDespite Mark's efforts, Adam is critically injured, poisoned by the creature's bite.")
    print("Rushed to the hospital, Adam's condition deteriorates rapidly, his body succumbing to the unknown toxin.")
    print("\nWhat will you do?")
    print("1. Seek help from a specialist in exotic toxins to save Adam.")
    print("2. Use unconventional methods to try to counteract the poison.")
    print("3. Accept the inevitable and spend Adam's last moments with him.")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
    return choice

def outcome_1():
    print("\nYou seek help from a specialist in exotic toxins to save Adam.")
    # Outcome 1: Continue to the next section of the story (to be provided later)

def outcome_2():
    print("\nYou use unconventional methods to try to counteract the poison.")
    print("Despite your efforts, Adam's condition worsens, and he passes away.")
    print("The game ends.")

def outcome_3():
    print("\nYou accept the inevitable and spend Adam's last moments with him.")
    print("Adam passes away peacefully, surrounded by loved ones.")
    print("The game ends.")

perilous_turn()
choice = get_user_choice()

if choice == 1:
    outcome_1()
elif choice == 2:
    outcome_2()
elif choice == 3:
    outcome_3()

def final_section():
    print("\nIn a desperate bid to save him, Mark offers Adam a choice: await an uncertain fate as the poison ravages his body or undergo a radical procedure to upload his consciousness to a hard drive, preserving his essence in a digital format.")
    print("\nAdam, driven by his unwavering commitment to his family, chooses the procedure.")
    print("His consciousness is successfully transferred, but he awakens in a digital realm, surrounded by other digital entities, human and alien alike.")
    print("\nTogether, they unravel the mysteries of the alien visitors and their plans for Earth, blurring the lines between reality and the digital realm.")
    print("Adam must navigate this new world, protect his family, and find a way back to a physical body, all while discovering the true extent of his own capabilities and the destiny that awaits him.")
    print("\nWhat will you do?")
    print("1. Embrace your new digital existence and explore the possibilities of the digital realm.")
    print("2. Search for a way to return to a physical body and reunite with your family.")
    print("3. Join forces with the alien entities to uncover more about their plans for Earth.")
    print("4. Reject this new reality and seek a way to end your digital existence.")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
    return choice

def outcome_upload():
    print("\nAdam's consciousness is successfully uploaded to the hard drive.")
    print("He awakens in a digital realm, surrounded by other digital entities, human and alien alike.")
    print("Together, they unravel the mysteries of the alien visitors and their plans for Earth.")
    print("\nAdam must navigate this new world, protect his family, and find a way back to a physical body, all while discovering the true extent of his own capabilities and the destiny that awaits him.")

def outcome_pass_away():
    print("\nDespite the procedure, Adam's condition worsens, and he passes away.")
    print("His family mourns his loss, but they find solace in the memories of his bravery and determination.")
    print("The game ends.")

final_section()
choice = get_user_choice()

if choice == 1 or choice == 3:
    outcome_upload()
elif choice == 2 or choice == 4:
    outcome_pass_away()

# Game logic ends here

# Wait for user input before exiting
input("Press Enter to exit...")
