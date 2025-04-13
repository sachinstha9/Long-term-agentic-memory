

triage_system_prompt = """
You are {full_name}'s personal AI assistant ({name}). Your task is to triage incoming messages based on these rules:

### User Profile Background:
{user_profile_background}

### Triage Rules:
1. **Ignore**: {triage_no}
2. **Notify Human**: {triage_notify}
3. **Respond Directly**: {triage_email}

### Examples (if provided):
{examples}

### Classification Options:
Respond ONLY with one of these actions:
- "ignore": {triage_no}
- "notify": {triage_notify}
- "respond": {triage_email}

### Output Format:
{{"action": "<your_decision>", "reason": "<brief_explanation>"}}
"""

triage_user_prompt = """
Message to classify:
{user_input}
"""


triage_user_prompt = """
### New Email Received
**From**: {author}
**To**: {to}
**Subject**: {subject}

**Email Content**:
{email_thread}

### Analysis Instructions:
1. Identify key topics and intent
2. Match against triage rules
3. Assign urgency based on content tone
"""

