import os
from selenium import webdriver


def lambda_handler(event, context):
    # Set the path to the ChromeDriver executable
    driver_path = os.path.join(os.getcwd(), 'dependencies', 'chromedriver')

    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    # Run headless (without a visible browser window)
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    try:
        # Navigate to the URL
        driver.get("https://datacatalog.worldbank.org/home")

        # Get the title of the web page
        page_title = driver.title

        return {
            'statusCode': 200,
            'body': {
                'title': page_title
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': "An error occurred: " + str(e)
        }
    finally:
        # Close the WebDriver to release resources
        driver.quit()
