"""Portfolio content — edit this file to fill in your details.

Replace every PLACEHOLDER below with your real info:
  - NAME / TAGLINE: how you introduce yourself
  - PROFILE_IMAGE: public URL of your photo (here, a Linode object-storage object)
  - RESUME_URL: public URL of your resume PDF (here, a Linode object-storage object)
  - the "url" of each link in LINK_GROUPS (all currently "#")

Each link uses either an ``icon`` (an inline brand SVG, see app/templates/_icons.html)
or an ``emoji`` for apps without a clean brand mark.
"""

# PLACEHOLDER: your name (also shown in the navbar)
NAME = "Peter Li"

# Edit to taste.
TAGLINE = "Senior Software Engineer"

# Profile photo, hotlinked from Linode object storage (object must be public-read).
PROFILE_IMAGE = (
    "https://personal-us-lax.us-lax-1.linodeobjects.com/personal/waiola.webp"
)

# Resume PDF, hotlinked from Linode object storage (object must be public-read).
RESUME_URL = (
    "https://personal-us-lax.us-lax-1.linodeobjects.com/personal/nov-2024-resume.pdf"
)

# Grouped links shown on the landing page. Fill in each "url".
LINK_GROUPS = [
    {
        "title": "Professional",
        "links": [
            {
                "label": "LinkedIn",
                "url": "https://www.linkedin.com/in/peteclimbs/",
                "icon": "linkedin",
                "target": "_blank",
            },
            {
                "label": "GitHub",
                "url": "https://github.com/peteli3",
                "icon": "github",
                "target": "_blank",
            },
            {
                "label": "Resume (PDF)",
                "url": RESUME_URL,
                "icon": "resume",
                "target": "_blank",
            },
        ],
    },
    {
        "title": "Sports",
        "links": [
            {
                "label": "KAYA",
                "url": "https://kaya-app.kayaclimb.com/share/profile?id=86231",
                "emoji": "🧗",
                "target": "_blank",
            },
            {
                "label": "Strava",
                "url": "https://www.strava.com/athletes/45904550",
                "icon": "strava",
                "target": "_blank",
            },
            {
                "label": "Slopes",
                "url": "https://my.getslopes.com/app/addFriend/p0QWArnmwV",
                "emoji": "⛷️",
                "target": "_blank",
            },
        ],
    },
    {
        "title": "Life",
        "links": [
            {
                "label": "Beli",
                "url": "https://beliapp.co/lists/peteli",
                "emoji": "🍽️",
                "target": "_blank",
            },
        ],
    },
    {
        "title": "Talks",
        "links": [
            {
                "label": "Conference Talk",
                "url": "https://youtu.be/g4f2lHz8meo?t=383",
                "icon": "youtube",
                "target": "_blank",
            },
        ],
    },
    {
        "title": "Side Quests",
        "links": [
            # Internal link to the mortgage-calculator app, served by the same
            # reverse proxy under /mortgage-calculator. Uses that app's favicon
            # (at its prefixed static path) as the button icon via "image".
            {
                "label": "Mortgage Calculator",
                "url": "/mortgage-calculator/",
                "image": "/mortgage-calculator/static/favicon.ico",
            },
        ],
    },
]
