try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

try:
    import argparse
except ImportError:
    print("No module named 'argparse' found")

print("""
███████╗ █████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
█████╗  ███████║███████╗█████╗  ███████║██████╔╝██║     ███████║
██╔══╝  ██╔══██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║     ██║  ██║███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
            Your Google search tool 
            Made by Batuhanaydn
""")
print("Normal Search = 1")
print("Advanced Search = 2")
print("Social Media Search = 3")
print("Related Search = 4")
print("Hashtag Search = 5")
select = int(input("Enter the query you want to select: "))
tld_list = input("Enter top level domain: ")
number_queries = int(input("Enter the number of queries: "))
number = number_queries

if select == 1:
    search_word = input("The word you are looking for: ")
    search_site = input("The site you are looking for: ")
    normal_query = f"{search_word}" + f" site:{search_site}"
    for normal in search(query=normal_query, tld=tld_list, num=number, stop=10, pause=2):
        f = open("search_list.txt", "a")
        f.writelines(normal+"\n")
        f.close()
        print(normal)
if select == 2:
    searched_specific_word = input("The word you are looking for: ")
    search_site = input("The site you are looking for: ")
    not_included_word = input("Type of query not included: ")
    advanced_query = f"{searched_specific_word}" + f" site:{search_site}" + f" -{not_included_word}"
    for advanced in search(query=advanced_query, tld=tld_list, num=number, stop=10, pause=2):
        f = open("search_list.txt", "a")
        f.writelines(advanced+"\n")
        f.close()
        print(advanced)
if select == 3:
    search_site = input("The social media site you are looking for: ")
    search_person = input("Name of the wanted account (example=@telumak):")
    social_media_query = f'"{search_site}"' + f" @{search_person}" 

    for social in search(query=social_media_query, tld=tld_list, num=number, stop=10, pause=2):
        f = open("search_list.txt", "a")
        f.writelines(social+"\n")
        f.close()
        print(social)
if select == 4:    
    search_related = input("The site you are looking for: ")
    
    related_query = f"{search_related}"

    for related in search(query=related_query, tld=tld_list, num=number, stop=10, pause=2):
        f = open("search_list.txt", "a")
        f.writelines(related+"\n")
        f.close()
        print(related)
if select == 5:
    search_site = input("Social media site to search hashtag: ")
    search_hashtag = input("Hashtag to search: ")

    hashtag_query = f'"{search_site}"' + f" #{search_hashtag}"

    for hashtag in search(query=hashtag_query, tld=tld_list, num=number, stop=10, pause=2):
        f = open("search_list.txt", "a")
        f.writelines(hashtag+"\n")
        f.close()
        print(hashtag)


