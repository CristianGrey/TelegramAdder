from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserNotMutualContactError, UserChannelsTooMuchError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import os
import json

def adder():
    if os.path.isdir('/Program Files/Telegram') == False:
        os.mkdir('/Program Files/Telegram')
    try:
        if os.path.isfile(os.path.join(os.getcwd(), 'added.json')) == True:
            pass
        else:
            added = []
            person = {}

            person['username'] = ''
            person['user_id'] = ''
            added.append(person.copy())

            person['username'] = ''
            person['user_id'] = ''
            added.append(person.copy())

            with open(os.path.join(os.getcwd(), 'added.json'), 'w') as file:
                json.dump(added, file, indent=2)


        if os.path.isfile(os.path.join(os.getcwd(), 'tried.json')) == True:
            pass
        else:
            added = []
            person = {}

            person['username'] = ''
            person['user_id'] = ''
            added.append(person.copy())

            person['username'] = ''
            person['user_id'] = ''
            added.append(person.copy())

            with open(os.path.join(os.getcwd(), 'tried.json'), 'w') as file:
                json.dump(added, file, indent=2)


        if os.path.isfile(os.path.join(os.getcwd(), 'config.json')) == True:
            pass
        else:
            config = {}
            config['api_id'] = '0'
            config['api_hash'] = 'your api hash'
            config['phone'] = '+0'
            with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                json.dump(config, config_file, indent=2)

        session = False
        for item in os.listdir():
            if '.session' in item:
                number = item.split('.')[0]
                session = True

        if session:
            while True:
                a = input(f'Do you want to recover your login session with number {number}? [y/n] ').lower()
                if a == 'y':
                    print('Program Started...')
                    with open(os.path.join(os.getcwd(), 'config.json'), 'r') as config_file:
                        config = json.load(config_file)
                        api_id = config['api_id']
                        api_hash = config['api_hash']
                        phone = config['phone']
                    break
                elif a == 'n':
                    for item in os.listdir():
                        if '.session' in item:
                            os.remove(item)
                    print('Program Started...')
                    api_id = input('Paste here your account api id: ')
                    api_hash = input('Paste here your account api hash: ')
                    phone = input('Paste here your phone number (International Format): ')
                    config = {}
                    config['api_id'] = api_id
                    config['api_hash'] = api_hash
                    config['phone'] = phone
                    with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                        json.dump(config, config_file, indent=2)
                    break

        else:
            print('No session found. Lets define a new one...')
            api_id = input('Paste here your account api id: ')
            api_hash = input('Paste here your account api hash: ')
            phone = input('Paste here your phone number (International Format): ')
            config = {}
            config['api_id'] = api_id
            config['api_hash'] = api_hash
            config['phone'] = phone
            with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                json.dump(config, config_file, indent=2)

        # ========================== FIXING BUGS ================================
        with open(os.path.join(os.getcwd(), 'config.json'), 'r') as config_file:
            config = json.load(config_file)

            if api_id == '0':
                api_id = input('Paste here your account api id: ')
                config['api_id'] = api_id
                with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                    json.dump(config, config_file, indent=2)

            if api_hash == 'your api hash':
                api_hash = input('Paste here your account api hash: ')
                config['api_hash'] = api_hash
                with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                    json.dump(config, config_file, indent=2)
            if phone == '+0':
                phone = input('Paste here your phone number (International Format): ')
                config['phone'] = phone
                with open(os.path.join(os.getcwd(), 'config.json'), 'w') as config_file:
                    json.dump(config, config_file, indent=2)

        # ====================== END OF FIXING BUGS ===============================

        client = TelegramClient(phone, api_id, api_hash)
        async def main():
            # Now you can use all client methods listed below, like for example...
            await client.send_message('me', 'Hello !!!!!')


        SLEEP_TIME_1 = 100
        SLEEP_TIME_2 = 100
        with client:
            client.loop.run_until_complete(main())
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('40779'))

        users = []
        # with open(r"/Program Files/Telegram/Scrapped.csv", encoding='UTF-8') as f:  #Enter your file name
        #     rows = csv.reader(f,delimiter=",",lineterminator="\n")
        #     next(rows, None)
        #     for row in rows:
        #         user = {}
        #         user['username'] = row[0]
        #         user['id'] = int(row[1])
        #         user['access_hash'] = int(row[2])
        #         user['name'] = row[3]
        #         users.append(user)

        with open(os.path.join(os.getcwd(), 'Scraped.json'), "r", encoding='utf-8', errors='ignore') as f:
            list = json.load(f, strict=False)
            for dict in list:
                user = {}
                user['username'] = dict['username']
                user['id'] = dict['id']
                user['access_hash'] = dict['access_hash']
                user['name'] = dict['name']
                users.append(user)

        chats = []
        last_date = None
        chunk_size = 200
        groups = []

        result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue

        print('Choose a group to add members:')
        i = 0
        for group in groups:
            group.title = group.title.encode('utf-8')
            group.title = group.title.decode('ascii', 'ignore')
            print(f'{str(i)} - {str(group.title)}')
            i += 1

        g_index = input("Enter a Number: ")
        target_group = groups[int(g_index)]

        #Start of scrappe members from that group to avoid repetition

        try:
            all_participants = []
            all_participants = client.get_participants(target_group, aggressive=True)

            scrapedusers = []
            jsonuser = {}
            for user in all_participants:
                jsonuser.clear()
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                jsonuser['username'] = username
                jsonuser['id'] = user.id
                jsonuser['access_hash'] = user.access_hash
                jsonuser['name'] = name
                scrapedusers.append(jsonuser.copy())

            print('Members scraped successfully.......')
        except:
            print('Error scrapping members of this group. Danger of false positives.')

        #End of scrappe members of that group to avoid repetition

        target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

        # mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
        mode = 2

        n = 0

        with open(os.path.join(os.getcwd(), 'tried.json'), 'r') as file:
            tried = json.load(file)

        for user in users:
            if user not in scrapedusers:
                if user not in tried:
                    tried.append(user.copy())
                    with open(os.path.join(os.getcwd(), 'tried.json'), 'w') as file:
                        json.dump(tried, file, indent=2)
                    try:
                        n += 1
                        if n % 80 == 0:
                            sleep(60)
                        try:
                            print("Trying to add user {}".format(user['id']))
                            if mode == 1:
                                if user['username'] == "":
                                    continue
                                user_to_add = client.get_input_entity(user['username'])
                            elif mode == 2:
                                user_to_add = InputPeerUser(user['id'], user['access_hash'])
                            else:
                                sys.exit("Invalid Mode Selected. Please Try Again.")
                            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
                            print("Waiting for 60-180 Seconds...")
                            time.sleep(random.randrange(60, 90))
                        except PeerFloodError:
                            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                            print("Waiting {} seconds".format(SLEEP_TIME_2))
                            time.sleep(SLEEP_TIME_2)
                            continue #continues adicionado por mim
                        except UserPrivacyRestrictedError:
                            print("The user's privacy settings do not allow you to do this. Skipping.")
                            print("Waiting for 5 Seconds...")
                            time.sleep(random.randint(0, 5)) #Alterei, antes era randrange(5,0)
                            continue # adicionado por mim
                        except UserNotMutualContactError:
                            continue
                        except UserChannelsTooMuchError:
                            print('This user is already in too many channels/supergroups.')
                            continue
                        except Exception as e:
                            # traceback.print_exc()
                            print(f"Unexpected Error: {e}")
                            continue

                        with open(os.path.join(os.getcwd(), 'added.json'), 'r') as file:
                            added = json.load(file)
                            added.append(user.copy())

                        with open(os.path.join(os.getcwd(), 'added.json'), 'w') as file:
                            json.dump(added, file, indent=2)
                            try:
                                print(f'User {user["name"]} with id: {user["id"]} has been sucessfully added to your group.')
                            except UnicodeEncodeError:
                                print(f'User with id: {user["id"]} has been sucessfully added your group.')

                    except Exception as e:
                        print(f'An unnespected error ocureed: {e}')

                else:
                    print(f'This user has been checked by me before. Skipping. If you want o erase data, delete "tried.json".')
            else:
                print('This user already is in this group. Skipping.')
    except Exception as e:
        e = str(e)
        print(e)
        try:
            client.disconnect()
        except:
            print('Unable to disconnect client')
            time.sleep(30000)
        if 'database' in e:
            print('The last time program was executed it was not closed properly. Please delete the .session files and restart the program.')
            time.sleep(30000)
            try:
                client.disconnect()
            except:
                print('Unable to disconnect client')

    try:
        client.disconnect()
    except:
        print('Unable to disconnect client')

