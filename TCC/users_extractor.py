import requests
import threading
import json

users = []

def more_than_subs(response, n_subs):
	return len(response['subs']) >= n_subs
def get_user_url(id):
	return "https://uhunt.onlinejudge.org/api/subs-user/{}".format(id)
def get_user(begin, finish, lock):
        print("THREAD:", begin, finish)
        subs = 10
        for i in range(begin, finish + 1):
                response = requests.get(get_user_url(i)).json()
                if(more_than_subs(response, 10)):
                    with open('users.json', 'a') as file, lock:
                        print(json.dumps(response), file=file)
                        file.flush()
                    file.close()
	
threads = []
lock = threading.Lock()
begin = 1
finish = 500
for i in range(1, 1001):
      threads.append(threading.Thread(target=get_user, args = (begin, finish, lock)).start())
      begin = finish + 1
      finish = finish + 500
for thread in threads:
    thread.join()
