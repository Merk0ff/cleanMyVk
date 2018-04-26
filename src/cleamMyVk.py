# Created by Philip Merk0ff
# Version: 1.0
import sys
import os
import getpass
import json
import vk_api

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

# Get vk api object and user id
def getVkApi():
    login = input('Login:')
    password = getpass.getpass('Password:')

    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        exit(0)

    return vk_session.get_api(), vk_session.token['user_id']

#print caution of deliting
def printЭщкеере(protected: list, name):
    print("You trying to delte next " + name + '\n')

    for i in protected:
        print('\t' + str(i))
    print('\n')

    return query_yes_no("You sure that you want delete these " + name, None)

# Get protected posts/messages
def getProtectedPosts() -> dict:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    try:
        F = open(os.path.join(__location__, 'protected.json'), "r")
    except BaseException as err:
        print("File protected.json not found " + str(err))
        exit(0)

    arr = json.load(F)

    F.close()
    return arr

# Delete unprotected posts
def removePosts(vk, ownerId,  protectedPosts: list):
    if not printЭщкеере(protectedPosts, "posts"):
        return

    vkWallGet = vk.wall.get(owner_id=ownerId, count=2)

    countMin = vkWallGet['count']
    countMax = max(vkWallGet['items'][0]['id'], vkWallGet['items'][1]['id'])
    countOfDeleted = 0

    for i in range(countMin, countMax):
        print(str(countOfDeleted) + '\r')
        if i in protectedPosts:
            print(str(i) + 'Not deleted')
            continue
        try:
            countOfDeleted += vk.wall.delete(owner_id=ownerId, post_id=i)
        except BaseException:
            continue

# Remove unprotected chats
def removeChats(vk, ownerId, protectedChats: list):
    if not printЭщкеере(protectedChats, "chats"):
        return

    countOfDeleted = 0
    messageCount = vk.messages.getDialogs(count=0)['count']

    for i in range(int(messageCount / 20) + 1):
        print(str(countOfDeleted) + '\r')

        dialogs = vk.messages.getDialogs(count=20, offset=(i * 20))['items']
        for j in range(20):
            if 'chat_id' in dialogs[j]['message']:
                gId = dialogs[j]['message']['chat_id']
                if gId in protectedChats:
                    print(str(gId) + ' Not deleted')
                    continue
                try:
                    countOfDeleted += vk.messages.deleteDialog(user_id=ownerId, peer_id=(2000000000 + gId))
                except BaseException as err:
                    print(err)
                    continue
            else:
                uId = dialogs[j]['message']['user_id']
                if uId in protectedChats:
                    print(str(uId) + ' Not deleted')
                    continue
                try:
                    countOfDeleted += vk.messages.deleteDialog(user_id=ownerId, peer_id=uId)
                except BaseException as err:
                    print(err)
                    continue

def main():
    protectedPosts = getProtectedPosts()

    vk, ownerId = getVkApi()
    removePosts(vk, ownerId, protectedPosts['posts'])
    removeChats(vk, ownerId, protectedPosts['messages'])

if __name__ == '__main__':
    main()
