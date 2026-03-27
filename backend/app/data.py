"""
In-memory mock data store for CodeLab Revival.
Replace with a real database (PostgreSQL/MongoDB) in production.
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ── Users ─────────────────────────────────────────────────────
USERS = [
    {
        "id": 1,
        "name": "Patrick Haye",
        "email": "patrick@codelab.edu",
        "hashed_password": pwd_context.hash("password123"),
        "role": "instructor",
    },
    {
        "id": 2,
        "name": "David Arnow",
        "email": "arnow@codelab.edu",
        "hashed_password": pwd_context.hash("password123"),
        "role": "instructor",
    },
    {
        "id": 3,
        "name": "Student One",
        "email": "student@codelab.edu",
        "hashed_password": pwd_context.hash("student123"),
        "role": "student",
    },
    {
        "id": 4,
        "name": "Test User",
        "email": "testuser@codelab.edu",
        "hashed_password": pwd_context.hash("test123"),
        "role": "student",
    },
]

# ── Courses ───────────────────────────────────────────────────
SEMESTERS = [
    {
        "term": "Spring 2026",
        "courses": [
            {
                "course_id": "59094",
                "number": "CS1-Java",
                "title": "Generic JAVA For Development",
                "section": "A",
                "instructor": "Arnow",
                "language": "Java",
                "access_code": "TCAB-32741-HWYW-67",
            },
            {
                "course_id": "59097",
                "number": "CS1-Java",
                "title": "PH-Generic JAVA For Development",
                "section": "PH",
                "instructor": "Haye",
                "language": "Java",
                "access_code": "CODE-32744-KAHZ-67",
            },
        ],
    }
]

# ── Lab Structure (course 59094) ──────────────────────────────
LAB_STRUCTURES = {
    "59094": {
        "course_id": "59094",
        "title": "JAVA CODELAB",
        "tree": [
            {
                "id": "new-exercises",
                "label": "NEW EXERCISES",
                "children": [],
                "exercises": [],
            },
            {
                "id": "codelab-warmup",
                "label": "CODELAB WARMUP",
                "children": [],
                "exercises": [],
            },
            {
                "id": "imperative-programming",
                "label": "IMPERATIVE PROGRAMMING",
                "children": [],
                "exercises": [],
            },
            {
                "id": "oop",
                "label": "OBJECT ORIENTED PROGRAMMING",
                "children": [
                    {
                        "id": "references-objects",
                        "label": "REFERENCES and OBJECTS",
                        "children": [
                            {
                                "id": "reference-variable-declaration",
                                "label": "reference variable declaration",
                                "children": [],
                                "exercises": [
                                    {"id": "20518", "label": "Exercise 20518", "status": "blank"},
                                    {"id": "20516", "label": "reference variable declaration", "status": "blank"},
                                    {"id": "20517", "label": "Exercise 20517", "status": "blank"},
                                    {"id": "21055", "label": "Exercise 21055", "status": "blank"},
                                    {"id": "21051", "label": "Exercise 21051", "status": "blank"},
                                    {"id": "21079", "label": "Exercise 21079", "status": "blank"},
                                    {"id": "21063", "label": "Exercise 21063", "status": "blank"},
                                    {"id": "21067", "label": "Exercise 21067", "status": "blank"},
                                    {"id": "21075", "label": "Exercise 21075", "status": "blank"},
                                    {"id": "21071", "label": "Exercise 21071", "status": "blank"},
                                    {"id": "21059", "label": "Exercise 21059", "status": "blank"},
                                ],
                            },
                            {
                                "id": "object-creation-expression",
                                "label": "object creation expression",
                                "children": [],
                                "exercises": [
                                    {"id": "21056", "label": "Exercise 21056", "status": "blank"},
                                    {"id": "21052", "label": "Exercise 21052", "status": "blank"},
                                    {"id": "21080", "label": "Exercise 21080", "status": "blank"},
                                    {"id": "21064", "label": "Exercise 21064", "status": "blank"},
                                    {"id": "21068", "label": "Exercise 21068", "status": "blank"},
                                    {"id": "21072", "label": "Exercise 21072", "status": "blank"},
                                    {"id": "21076", "label": "Exercise 21076", "status": "blank"},
                                    {"id": "21060", "label": "Exercise 21060", "status": "blank"},
                                ],
                            },
                            {
                                "id": "object-creation-reference",
                                "label": "object creation and reference",
                                "children": [],
                                "exercises": [],
                            },
                        ],
                        "exercises": [],
                    }
                ],
                "exercises": [],
            },
            {
                "id": "advanced-topics",
                "label": "ADVANCED TOPICS",
                "children": [],
                "exercises": [],
            },
            {
                "id": "graphics-gui",
                "label": "GRAPHICS AND GUI",
                "children": [],
                "exercises": [],
            },
            {
                "id": "patrick-haye-exercises",
                "label": "Patrick Haye Exercises",
                "children": [
                    {
                        "id": "uncategorized",
                        "label": "Uncategorized",
                        "children": [],
                        "exercises": [
                            {"id": "00001", "label": "Run-Length Encoding", "status": "blank"},
                            {"id": "00002", "label": "Exercise 00002", "status": "blank"},
                            {"id": "00003", "label": "Exercise 00003", "status": "blank"},
                            {"id": "00004", "label": "Hello World", "status": "blank"},
                            {"id": "00005", "label": "Exercise 00005", "status": "blank"},
                        ],
                    }
                ],
                "exercises": [{"id": "00004", "label": "Hello World", "status": "blank"}],
            },
        ],
    }
}

# ── Exercises ─────────────────────────────────────────────────
EXERCISES = {
    "00001": {
        "id": "00001",
        "title": "Run-Length Encoding",
        "instructions": (
            "Write a <strong>program</strong> that compresses a <strong>string</strong> "
            "using <strong>run-length encoding</strong>.<br><br>"
            "Your class should be named <strong>RunLength</strong>.<br>"
            "Read a single line from standard input and print the encoded result."
        ),
        "sample_runs": [
            {"input": "aaabbcaaaa", "output": "a3b2c1a4"},
            {"input": "xyz", "output": "x1y1z1"},
        ],
        "starter_code": "public class RunLength {\n    public static void main(String[] args) {\n        // your code here\n    }\n}\n",
        "course_id": "59094",
        "topic": "Patrick Haye Exercises",
    },
    "20516": {
        "id": "20516",
        "title": "reference variable declaration",
        "instructions": (
            "Declare a <strong>reference variable</strong> of type <code>File</code> "
            "named <code>myFile</code>.<br><br>"
            "Use the appropriate import statement if needed."
        ),
        "sample_runs": [],
        "starter_code": "import java.io.File;\n\npublic class Declare {\n    public static void main(String[] args) {\n        // declare myFile here\n    }\n}\n",
        "course_id": "59094",
        "topic": "reference variable declaration",
    },
    "00004": {
        "id": "00004",
        "title": "Hello World",
        "instructions": (
            "Write a Java program that prints <strong>Hello, World!</strong> "
            "to standard output.<br><br>"
            "Your class should be named <strong>HelloWorld</strong>."
        ),
        "sample_runs": [
            {"input": "", "output": "Hello, World!"},
        ],
        "starter_code": "public class HelloWorld {\n    public static void main(String[] args) {\n        // your code here\n    }\n}\n",
        "course_id": "59094",
        "topic": "Patrick Haye Exercises",
    },
}

# ── Submissions (in-memory store) ─────────────────────────────
SUBMISSIONS: list[dict] = []
_submission_counter = 0


def next_submission_id() -> int:
    global _submission_counter
    _submission_counter += 1
    return _submission_counter


def get_user_by_email(email: str) -> dict | None:
    for u in USERS:
        if u["email"].lower() == email.lower():
            return u
    return None


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
