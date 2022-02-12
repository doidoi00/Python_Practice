from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="bc36a4a686bb02ac326d016239d74f058417680ff5ab0b9adec50fa09a15063d4ab0c81dc73c88ace4277676ebd629ea8932dca8f0761a6943db19e7813bee374e12f32e4bd3d9bf1031c17cd08c")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/Python-9561439916b340a5a64b6f65bf43732d")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"
