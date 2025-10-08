from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
import sys

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Desired capabilities using AppiumOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "10BD531CFB0009J"  # Replace with your device ID
options.app_package = "com.mgarocord"  # Replace with your app's package name
options.app_activity = "com.mgarocord.MainActivity"  # Replace with your app's activity
options.no_reset = True

# Connect to the Appium server
try:
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",  # Appium server URL
        options=options  # Pass options here
    )
    print("Session started successfully")
    
    # Wait for the app to load
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    print(driver.page_source)
    
    # Wait for a few seconds
    time.sleep(2)

    # Quit the session
    driver.quit()

    print("Session closed successfully")

except Exception as e:

    except Exception as e:
    print(f"Error occurred: {str(e)}")
    sys.exit(1)  # <-- Add this line
