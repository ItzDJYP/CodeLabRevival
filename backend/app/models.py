from typing import Optional
from pydantic import BaseModel


# ── Auth ──────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str  # student | instructor


class UserPublic(BaseModel):
    id: str
    name: str
    email: str
    role: str  # instructor | student


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic


# ── Courses ───────────────────────────────────────────────────
class Course(BaseModel):
    course_id: str
    number: str
    title: str
    section: str
    instructor: str
    language: str
    access_code: str = ""


class Semester(BaseModel):
    term: str
    courses: list[Course]


class CoursesResponse(BaseModel):
    role: str
    total: int
    semesters: list[Semester]


# ── Lab / TOC ─────────────────────────────────────────────────
class ExerciseRef(BaseModel):
    id: str
    label: str
    status: str = "blank"  # blank | correct | wrong | attempted


class TopicNode(BaseModel):
    id: str
    label: str
    exercises: list[ExerciseRef] = []
    children: Optional[list["TopicNode"]] = None


TopicNode.model_rebuild()


class LabStructure(BaseModel):
    course_id: str
    title: str
    tree: list[TopicNode]


# ── Exercise ──────────────────────────────────────────────────
class SampleRun(BaseModel):
    input: str
    output: str


class Exercise(BaseModel):
    id: str
    title: str
    instructions: str
    sample_runs: list[SampleRun] = []
    starter_code: str = ""
    course_id: str = ""
    topic: str = ""


# ── Submission ────────────────────────────────────────────────
class SubmitRequest(BaseModel):
    exercise_id: str
    code: str


class SubmissionResult(BaseModel):
    submission_id: str
    exercise_id: str
    status: str   # correct | compiler_error | runtime_error | wrong_output
    message: str
    compiler_output: str
    your_code: str
    score: int  # 0–100
