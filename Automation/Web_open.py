# from inf_STT import listen
import webbrowser
from Web_Data import websites

def openweb(webname):
    website_name = webname.lower().split()
    counts = {}

    for name in website_name:
        counts[name] = counts.get(name, 0) + 1

    urls_to_open = []
    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]]*count)
    
    for url in urls_to_open:
        webbrowser.open(url)

    if urls_to_open:
        print(f"Opening...")

# while True:
#     web_input = input("web name : ") str
#     openweb(web_input)


