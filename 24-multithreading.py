import threading
import requests
import time

def fetch_data(url):
    return requests.get(url)

if __name__ == '__main__':
    time0 = time.perf_counter()
    slug_list = [
        "If-we-quantify-the-alarm-we-can-get-to-the-FTP-pixel-through-the-online-SSL-interface!-120863",
        "Try-to-transmit-the-HTTP-card-maybe-it-will-override-the-multi-byte-hard-drive!-120863",
        "Try-to-generate-the-TCP-bus-maybe-it-will-override-the-neural-bandwidth!-120863",
        "You-cant-transmit-the-firewall-without-copying-the-1080p-SDD-interface!-120863",
        "You-cant-connect-the-interface-without-programming-the-virtual-PNG-protocol!-120863",
        "Try-to-bypass-the-SAS-card-maybe-it-will-transmit-the-solid-state-system!-120863",
        "Use-the-auxiliary-EXE-monitor-then-you-can-hack-the-haptic-port!-120863",
    ]

    threads = []

    for slug in slug_list:
        thread = threading.Thread(target=fetch_data, args=(f'https://api.realworld.io/api/articles/{slug}',))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    time1 = time.perf_counter()
    print(time1 - time0)