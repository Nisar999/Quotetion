"""
Quotetion — Curated Motivation Dataset
========================================
Contains 20+ motivation entries across 10 categories.
Uses simple keyword matching — no AI/ML needed.
This keeps the project zero-cost and offline-capable.
"""

import random

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CURATED DATASET
# Each entry has: category, motivation, quote, action_step
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MOTIVATIONS = [
    # ── Placements ──
    {
        "category": "Placements",
        "motivation": "Keep going. Consistent effort always beats temporary fear.",
        "quote": "Success is the sum of small efforts repeated day in and day out. — Robert Collier",
        "action_step": "Spend 30 minutes solving one aptitude problem today.",
    },
    {
        "category": "Placements",
        "motivation": "Every rejection is redirection toward the right opportunity.",
        "quote": "Opportunities don't happen. You create them. — Chris Grosser",
        "action_step": "Update your resume and apply to two new companies today.",
    },
    # ── Exams ──
    {
        "category": "Exams",
        "motivation": "You've prepared more than you think. Trust the process.",
        "quote": "The secret of getting ahead is getting started. — Mark Twain",
        "action_step": "Review one chapter's key concepts for 25 minutes using the Pomodoro technique.",
    },
    {
        "category": "Exams",
        "motivation": "Exam stress is temporary. The knowledge you gain lasts forever.",
        "quote": "It always seems impossible until it's done. — Nelson Mandela",
        "action_step": "Write down the top 5 formulas or concepts you need to memorize and revise them.",
    },
    # ── Interviews ──
    {
        "category": "Interviews",
        "motivation": "They invited you for a reason. You belong in that room.",
        "quote": "Believe you can and you're halfway there. — Theodore Roosevelt",
        "action_step": "Practice answering 'Tell me about yourself' out loud three times.",
    },
    {
        "category": "Interviews",
        "motivation": "Confidence comes from preparation, not perfection.",
        "quote": "The only way to do great work is to love what you do. — Steve Jobs",
        "action_step": "Research the company's recent projects and prepare two thoughtful questions.",
    },
    # ── Projects ──
    {
        "category": "Projects",
        "motivation": "Every big project started with a single file. You've already begun.",
        "quote": "The best time to plant a tree was 20 years ago. The second best time is now. — Chinese Proverb",
        "action_step": "Break your project into 3 milestones and complete the first task today.",
    },
    {
        "category": "Projects",
        "motivation": "Don't aim for perfect code. Aim for working code, then improve.",
        "quote": "Done is better than perfect. — Sheryl Sandberg",
        "action_step": "Commit your current progress to Git, even if it's incomplete.",
    },
    # ── Health ──
    {
        "category": "Health",
        "motivation": "Your body is your most important tool. Take care of it first.",
        "quote": "Take care of your body. It's the only place you have to live. — Jim Rohn",
        "action_step": "Take a 15-minute walk outside and drink a full glass of water.",
    },
    {
        "category": "Health",
        "motivation": "Rest is not laziness. It's how high performers recharge.",
        "quote": "Almost everything will work again if you unplug it for a few minutes, including you. — Anne Lamott",
        "action_step": "Set a bedtime alarm for tonight and get at least 7 hours of sleep.",
    },
    # ── Career ──
    {
        "category": "Career",
        "motivation": "Your career is a marathon, not a sprint. Every step counts.",
        "quote": "The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
        "action_step": "Spend 20 minutes reading about a technology or skill you want to learn.",
    },
    {
        "category": "Career",
        "motivation": "Skills compound over time. What you learn today pays dividends for years.",
        "quote": "An investment in knowledge pays the best interest. — Benjamin Franklin",
        "action_step": "Identify one skill gap in your dream job description and find a free course for it.",
    },
    # ── Stress ──
    {
        "category": "Stress",
        "motivation": "It's okay to feel overwhelmed. Take one thing at a time.",
        "quote": "You don't have to see the whole staircase, just take the first step. — Martin Luther King Jr.",
        "action_step": "Write down everything stressing you, then pick just ONE thing to address today.",
    },
    {
        "category": "Stress",
        "motivation": "Breathe. You've survived 100% of your worst days so far.",
        "quote": "This too shall pass. — Persian Proverb",
        "action_step": "Try a 5-minute guided breathing exercise right now.",
    },
    # ── Coding ──
    {
        "category": "Coding",
        "motivation": "Every expert was once a beginner who refused to give up.",
        "quote": "First, solve the problem. Then, write the code. — John Johnson",
        "action_step": "Solve one easy problem on LeetCode or HackerRank today.",
    },
    {
        "category": "Coding",
        "motivation": "Bugs are not failures. They're puzzles waiting to be solved.",
        "quote": "Code is like humor. When you have to explain it, it's bad. — Cory House",
        "action_step": "Pick one function in your project and add comments explaining what it does.",
    },
    # ── Motivation (General) ──
    {
        "category": "Motivation",
        "motivation": "You are closer to your goals than you were yesterday. Keep pushing.",
        "quote": "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
        "action_step": "Write down 3 things you accomplished this week, no matter how small.",
    },
    {
        "category": "Motivation",
        "motivation": "The only person you need to be better than is who you were yesterday.",
        "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
        "action_step": "Set one small goal for tomorrow and write it on a sticky note.",
    },
    # ── Learning ──
    {
        "category": "Learning",
        "motivation": "Confusion means your brain is growing. Lean into it.",
        "quote": "Live as if you were to die tomorrow. Learn as if you were to live forever. — Mahatma Gandhi",
        "action_step": "Spend 15 minutes watching a tutorial on a topic you find confusing.",
    },
    {
        "category": "Learning",
        "motivation": "You don't need to learn everything. Focus on what matters most right now.",
        "quote": "Tell me and I forget. Teach me and I remember. Involve me and I learn. — Benjamin Franklin",
        "action_step": "Teach one concept you learned recently to a friend or write a short blog post about it.",
    },
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# KEYWORD → CATEGORY MAPPING
# Used for simple keyword matching from user input
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEYWORD_MAP: dict[str, str] = {
    # Placements
    "placement": "Placements",
    "placements": "Placements",
    "job": "Placements",
    "hiring": "Placements",
    "campus": "Placements",
    "recruit": "Placements",
    # Exams
    "exam": "Exams",
    "exams": "Exams",
    "test": "Exams",
    "marks": "Exams",
    "grade": "Exams",
    "semester": "Exams",
    "midterm": "Exams",
    "final": "Exams",
    # Interviews
    "interview": "Interviews",
    "interviews": "Interviews",
    "hr": "Interviews",
    "technical": "Interviews",
    # Projects
    "project": "Projects",
    "projects": "Projects",
    "deadline": "Projects",
    "assignment": "Projects",
    "hackathon": "Projects",
    "build": "Projects",
    # Health
    "health": "Health",
    "tired": "Health",
    "sleep": "Health",
    "sick": "Health",
    "exercise": "Health",
    "burnout": "Health",
    # Career
    "career": "Career",
    "future": "Career",
    "goal": "Career",
    "goals": "Career",
    "dream": "Career",
    "ambition": "Career",
    # Stress
    "stress": "Stress",
    "stressed": "Stress",
    "anxious": "Stress",
    "anxiety": "Stress",
    "overwhelm": "Stress",
    "worried": "Stress",
    "pressure": "Stress",
    # Coding
    "code": "Coding",
    "coding": "Coding",
    "programming": "Coding",
    "bug": "Coding",
    "debug": "Coding",
    "leetcode": "Coding",
    "dsa": "Coding",
    "algorithm": "Coding",
    # Learning
    "learn": "Learning",
    "learning": "Learning",
    "study": "Learning",
    "studying": "Learning",
    "course": "Learning",
    "tutorial": "Learning",
    "understand": "Learning",
    # Motivation (fallback)
    "motivation": "Motivation",
    "motivate": "Motivation",
    "inspire": "Motivation",
    "lazy": "Motivation",
    "procrastinate": "Motivation",
    "procrastinating": "Motivation",
}


def _match_category(situation: str) -> str:
    """
    Match user's situation text to a category using keyword matching.
    Returns 'Motivation' as the default fallback category.
    """
    words = situation.lower().split()
    for word in words:
        # Strip common punctuation for better matching
        clean_word = word.strip(".,!?;:'\"()-")
        if clean_word in KEYWORD_MAP:
            return KEYWORD_MAP[clean_word]
    return "Motivation"  # Default fallback


def get_by_situation(situation: str) -> dict:
    """
    Find a motivation entry matching the user's situation.
    Uses keyword matching to determine the category,
    then returns a random entry from that category.
    """
    category = _match_category(situation)
    matching = [m for m in MOTIVATIONS if m["category"] == category]
    return random.choice(matching)


def get_random() -> dict:
    """Return a completely random motivation entry."""
    return random.choice(MOTIVATIONS)
