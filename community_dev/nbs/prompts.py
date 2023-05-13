PROMPT_TEMPLATES = {
    "summary_template": """This is a chaotic Generative AI Group Chat transcript. Write detailed, exhaustive bullet point recap of topics discussed. Extract COMPLETE URL of web and social links with context. Please organize it into sections, only when needed:

{text}

Use Markdown. Add ## for section titles. TOPICS RECAP:""",
    "link_context_template": """For the given URL, there is some context. Newlines may or may not be related to the link, but the message in the same link as link is related to the link.
        
{text}
        
Mention URL with context. Single bullet point:""",
    "title_description_template": """For the given discussion, write a short title and description, separate both by \n\n

{text}
        
Return a single valid JSON with 
```
"title":
"description:":
```:""",
}
