import requests
from bs4 import BeautifulSoup



def extract_plot(soup):
    # Find the 'Plot' heading
    plot_heading = soup.find(text='Plot')
    
    plot_content = []
    if plot_heading:
        # Traverse all the next elements after the plot heading
        next_element = plot_heading.parent.find_next()

        # Keep collecting content until we reach another heading or unrelated section
        while next_element:
            # Stop when we hit another heading (i.e., h2, h3)
            if next_element.name in ['h2', 'h3', 'h4']:
                break
            
            # Collect paragraph content (or other text-based tags)
            if next_element.name in ['p', 'div', 'span']:
                plot_content.append(next_element.get_text(strip=True))
            
            # Move to the next element
            next_element = next_element.find_next()

    # Join the content into a single string
    return '\n'.join(plot_content)

def scrape_bleach_character(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = {}
    

    def getchar_info(label):
        element = soup.find(string=label)
        if element:
            parent = element.find_parent()
            if parent and parent.find_next_sibling():
                return parent.find_next_sibling().get_text(strip=True)
        return None

    data['Race'] = getchar_info('Race')
    data['Plot'] = extract_plot(soup)

    return data


