from functions import connect_to_page, get_title, get_links, get_article, create_excel

def main():
    soups = connect_to_page()
    get_links(soups)
    get_title(soups)
    get_article()
    create_excel()

if __name__ == "__main__":
    main()
