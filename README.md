
---

# YouTube Video Uploader with AI-Generated Descriptions

This Python project automates the process of uploading YouTube videos and generating engaging descriptions for them using AI. The tool uses the Google YouTube API for video uploads and Google Generative AI for generating descriptions.

---

## Features

- **Automated YouTube Video Upload**: The script uploads videos from a designated folder to YouTube with specified metadata.
- **AI-Generated Descriptions**: Generates attention-grabbing descriptions for videos using AI.
- **Duplicate Prevention**: Ensures that the same video is not uploaded twice by maintaining a log of uploaded videos.
- **Customizable Upload Options**: Allows customization of video title, description, tags, category, and privacy status.
- **Delay Between Uploads**: Configurable delay to manage upload intervals.

---

## Prerequisites

### 1. Python Dependencies
Install the required Python libraries:
```bash
pip install google-auth-oauthlib google-auth google-api-python-client google-generativeai
```

### 2. Google API Credentials
- Set up a Google Cloud project and enable the **YouTube Data API v3**.
- Download the `client_secrets.json` file for OAuth 2.0 credentials and place it in the root directory of your project.

### 3. Folder Structure
Ensure the following folder structure exists:
```
.
├── Videos/                  # Folder containing the video files to be uploaded
├── Genral_Infos/            # Folder for metadata storage
│   └── Uploaded_Videos.txt  # Text file to log uploaded video titles
├── client_secrets.json      # OAuth 2.0 credentials file
├── script.py                # The main script
```

---

## How to Use

### 1. Initial Setup
- Place your videos in the `Videos/` folder.
- Add the `client_secrets.json` file to the root directory.

### 2. Update AI API Key
Replace the placeholder `AIzaSyAEmfhYB--XuyPAlZDtBbRz9Skou4BdhRU` in the `AI` class with your Google Generative AI API key:
```python
ai = AI(API="your-google-generative-ai-api-key")
```

### 3. Run the Script
Execute the script:
```bash
python script.py
```

### 4. Monitor the Process
- The script will:
  1. Iterate through all videos in the `Videos/` folder.
  2. Generate a description using AI for each video.
  3. Upload the video to YouTube.
  4. Log the uploaded video in `Genral_Infos/Uploaded_Videos.txt`.

---

## Configuration

### Delay Between Uploads
To avoid overwhelming the API or triggering rate limits, adjust the delay in seconds between uploads:
```python
Delay = 300  # Set to 5 minutes (300 seconds)
```

### Privacy Settings
Set the default privacy status for uploads:
```python
privacy_status="public"  # Options: "public", "private", "unlisted"
```

### Video Categories
Change the default category ID as needed:
```python
category_id="22"  # Example: "22" for People & Blogs
```

---

## Limitations

- **AI Accuracy**: The quality of descriptions generated depends on the AI model and prompt provided.
- **Rate Limits**: Be mindful of API rate limits for both the YouTube API and Google Generative AI API.
- **Dependency on External APIs**: Requires active internet connectivity and valid API keys for both services.

---

## Troubleshooting

1. **Authentication Issues**:
   - Ensure the `client_secrets.json` file is correctly configured.
   - Check that the YouTube Data API is enabled for your Google Cloud project.

2. **AI Description Errors**:
   - Validate your AI API key.
   - Check for rate limits or service availability.

3. **Duplicate Uploads**:
   - Verify the contents of `Uploaded_Videos.txt` to ensure proper logging.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments

- **Google APIs**: Powered by the YouTube Data API v3 and Google Generative AI.
- **Python Libraries**: Utilized `google-auth-oauthlib`, `google-api-python-client`, and `google.generativeai` for functionality.

---

