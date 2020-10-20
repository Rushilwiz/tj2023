# Django
SECRET_KEY = ""  # Add your django secret key

# Notion Client
NOTION_URL = ""  # Add the notion url manually
NOTION_COOKIE = ""  # Follow the steps listed below

# 1. Login to notion and navigate to the home page of your page. (Not in Guest or Incognito)
# 2. Open up developer tools by pressing Ctrl + Shift + i, and navigate to the application tab
# 3. Click on the cookie dropdown and click on the single cookie that is located there.
# 4. Copy the token_v2 info and paste it into NOTION_COOKIE
