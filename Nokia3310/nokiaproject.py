welcome = '''

====================================
=                                  =
=                                  =
=                                  =
=                                  =
=                                  =
=                                  =
=                                  =            
=   ======= WELCOME 🤝️ ========    =
=                                  =
=                                  =
=                                  =
=                                  =
=                                  =
=                                  =                     
====================================
'''

print(welcome)

exit = False
main_menu = 0
submenu_choice = 0
user_input = 0

while not exit :
    print("\n ===== NOKIA 3310 MENU =====")
    print("1.  Phone book")
    print("2.  Mesages")
    print("3.  Chat")
    print("4.  Call Register")
    print("5.  Tones")
    print("6.  Settings")
    print("7.  Call divert")
    print("8.  Games")
    print("9.  Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")
    print("0.  EXit")

    main_menu = int(input())

    match main_menu :
        case 1:
            print("\n--- Phone book ---")
            print("1.  Search")
            print("2.  Service Nos.")
            print("3.  Add name")
            print("4.  Erase")
            print("5.  Edit")
            print("6.  Assign tone")
            print("7.  Send b'card")
            print("8.  Options")
            print("9.  Speed dials")
            print("10. Voice tags")
            print("Enter choice: ")
            submenu_choice = int(input())
            match submenu_choice:
                case 1:
                    print("Search: Find name and phone number")
                case 2:
                    print("Service Nos.: Call service provider")
                case 3:
                    print("Add name: Store name and phone number")
                case 4:
                    print("Erase: Delete names and numbers")
                case 5:
                    print("Edit: Modify stored names/numbers")
                case 6:
                    print("Assign tone: Set ringing tone for caller")
                case 7:
                    print("Send b'card: Send name/number to another phone") 
                case 8:
                    print("Options: Type of view / Memory status")
                case 9:
                    print("Speed dials: Assign number keys for speed dialing")
                case 10:
                    print("Voice tags: Record voice tags for dialing")
                case _:
                    print("Invalid option")
    
    match main_menu :
        case 2:
            print("\n--- Messages ---")
            print("1. Write messages")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Picture messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message settings")
            print("8. Info service")
            print("9. Voice mailbox number")
            print("10. Service command editor")
            print("Enter choice: ")
            submenu_choice = int(input())

            match submenu_choice:
                case 1:
                    print("Write message (max 201 characters)")
                case 2:
                    print("Inbox: Read received messages")
                case 3:
                    print("Outbox: View saved messages")
                case 4:
                    print("Picture messages: Send/receive picture messages")
                case 5:
                    print("Templates: Use preset messages")
                case 6:
                    print("Smileys: Edit smiley characters like :)")
                case 7:
                    print("Message settings: Set message centre number")
                case 8:
                    print("Info service: Receive topic-based messages")
                case 9:
                    print("Voice mailbox number: Store voice mail number")
                case 10:
                    print("Service command editor: Send service requests")
                case _:
                    print("Invalid option")    
    
    match main_menu :
        case 3:
            print("\n--- Chat ---")
            print("Start conversation using text messages")
            print("Enter phone number and nickname to begin")

    match main_menu :
        case 4:
            print("\n--- Call register ---")
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialled numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("6. Show call costs")
            print("7. Call cost settings")
            print("8. Prepaid credit")
            print("Enter choice: ")
            submenu_choice = int(input())
            match submenu_choice:
                case 1:
                    print("Missed calls: Last 10 unanswered calls")
                case 2:
                    print("Received calls: Last 10 answered calls")
                case 3:
                    print("Dialled numbers: Last 20 called numbers")
                case 4:
                    print("Erase recent call lists")
                case 5:
                    print("Show call duration: Last/All calls duration")
                case 6:
                    print("Show call costs: Cost of calls")
                case 7:
                    print("Call cost settings: Set cost limit")
                case 8:
                    print("Prepaid credit: Check remaining credit")
                case _:
                    print("Invalid option") 
    match main_menu :
        case 5:
            print("\n--- Tones ---")
            print("1. Ringing tone")
            print("2. Ringing volume")
            print("3. Incoming call alert")
            print("4. Composer")
            print("5. Message alert tone")
            print("6. Keypad tones")
            print("7. Warning and game tones")
            print("8. Vibrating alert")
            print("9. Screen saver")
            print("Enter choice: ")
            submenu_choice = int(input()) 
            match submenu_choice:
                case 1:
                    print("Ringing tone: Select ringtone")
                case 2:
                    print("Ringing volume: Adjust volume")
                case 3:
                    print("Incoming call alert: Set alert type")
                case 4:
                    print("Composer: Create your own ringing tone")
                case 5:
                    print("Message alert tone: Select message tone")
                case 6:
                    print("Keypad tones: Turn keypad sounds on/off")
                case 7:
                    print("Warning and game tones")
                case 8:
                    print("Vibrating alert: Turn vibration on/off")
                case 9:
                    print("Screen saver: Set screen saver")
                case _:
                    print("Invalid option")

    match main_menu :
        case 6:
            print("\n--- Settings ---")
            print("1. Call settings")
            print("2. Phone settings")
            print("3. Security settings")
            print("4. Restore factory settings")
            print("Enter choice: ")
            submenu_choice = int(input())
            match submenu_choice:
                case 1:
                    print("Call settings: Auto redial, Speed dialing, Call waiting")
                case 2:
                    print("Phone settings: Language, Welcome note, Lights")
                case 3:
                    print("Security settings: PIN code, Call barring, Fixed dialing")
                case 4:
                    print("Restore factory settings: Reset to original values")
                case _:
                    print("Invalid option")

    match main_menu :
        case 7:
            print("\n--- Call divert ---")
            print("Direct incoming calls to voice mailbox or another number")
            print("Options: Divert when busy, Divert if not answered, etc.")

    match main_menu :
        case 8:
            print("\n--- Games ---")
            print("1. Snake II")
            print("2. Space Impact")
            print("3. Bantumi")
            print("4. Pairs II")
            print("Choose game: ")
            submenu_choice = int(input())
            match submenu_choice:
                case 1:
                    print("Snake II: Classic snake game")
                case 2:
                    print("Space Impact: Space shooter game")
                case 3:
                    print("Bantumi: African board game")
                case 4:
                    print("Pairs II: Memory matching game")
                case 5:
                    print("Invalid option")

    match main_menu :
        case 9:
            print("\n--- Calculator ---")
            print("Use +, -, *, /, %  for calculations")
            print("Also supports currency conversion")
    match main_menu :
        case 10: 
            print("\n--- Reminders ---")
            print("1. Add new")
            print("2. Erase")
            print("3. View all")
            print("Enter choice: ")
            match submenu_choice:
                case 1:
                    print("Add new note with or without alarm")
                case 2:
                    print("Erase notes one by one or all at once")
                case 3:
                    print("View all reminders")
                case _:
                    print("Invalid option")

    match main_menu :
        case 11:
            print("\n--- Clock ---")
            print("1. Alarm clock")
            print("2. Clock settings")
            print("3. Date setting")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Auto update of date and time")
            print("Enter choice: ")
            submenu_choice = int(input()) 
            match submenu_choice :
                case 1:
                    print("Alarm clock: Set alarm time")
                case 2:
                    print("Clock settings: Set time and format")
                case 3:
                    print("Date setting: Set current date")
                case 4:
                    print("Stopwatch: Measure time")
                case 5:
                    print("Countdown timer: Set timer")
                case 6:
                    print("Auto update: Network updates time")
                case _:
                    print("Invalid option")

    match main_menu :
        case 12:
            print("\n--- Profiles ---")
            print("1. General")
            print("2. Silent")
            print("3. Meeting")
            print("4. Outdoor")
            print("5. Pager")
            print("Select profile: ")
            submenu_choice = int(input())
            match submenu_choice :
                case 1:
                    print("General: Normal profile")
                case 2:
                    print("Silent: Mute all tones")
                case 3:
                    print("Meeting: Discreet tones")
                case 4:
                    print("Outdoor: Loud tones")
                case 5:
                    print("Pager: Beep only")
                case _:
                    print("Invalid option")

    match main_menu :
        case 13:
            print("\n--- SIM services ---")
            print("Additional services provided by your SIM card")
            print("Contact your service provider for details")

    match main_menu :
        case 0:
            print("Poweroff")
            exit = True
    match main_menu :
        case _: 
            print("Invalid choice! Please enter 0-13")

