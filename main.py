from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Navigate to a URL
    page.goto('https://developer.nvidia.com/blog/mastering-llm-techniques-training/')

    # Extract text content from the page
    text_content = page.inner_text('body')

    # Define the output file name
    output_file = 'output.txt'

    # Save the text content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text_content)

    # Close the browser
    browser.close()
