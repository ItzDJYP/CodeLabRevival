/**
 * Typed API client — all requests route through Next.js /api/* proxy
 * to avoid CORS issues in development.
 */

const BASE = "/api";

// ── Token helpers ─────────────────────────────────────────────
export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("cl_token");
}

export function setToken(token: string): void {
  localStorage.setItem("cl_token", token);
}

export function clearToken(): void {
  localStorage.removeItem("cl_token");
  localStorage.removeItem("cl_user");
}

export function getUser(): User | null {
  if (typeof window === "undefined") return null;
  const raw = localStorage.getItem("cl_user");
  return raw ? (JSON.parse(raw) as User) : null;
}

export function setUser(user: User): void {
  localStorage.setItem("cl_user", JSON.stringify(user));
}

// ── Fetch wrapper ─────────────────────────────────────────────
async function apiFetch<T>(
  path: string,
  options: RequestInit = {},
): Promise<T> {
  const token = getToken();
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string>),
  };
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const res = await fetch(`${BASE}${path}`, { ...options, headers });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail?.detail ?? "Request failed");
  }
  return res.json() as Promise<T>;
}

// ── Types ─────────────────────────────────────────────────────
export interface User {
  id: string;
  name: string;
  email: string;
  role: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface Course {
  course_id: string;
  number: string;
  title: string;
  section: string;
  instructor: string;
  language: string;
  access_code: string;
}

export interface Semester {
  term: string;
  courses: Course[];
}

export interface CoursesResponse {
  role: string;
  total: number;
  semesters: Semester[];
}

export interface ExerciseRef {
  id: string;
  label: string;
  status: string;
}

export interface TopicNode {
  id: string;
  label: string;
  exercises: ExerciseRef[];
  children?: TopicNode[];
}

export interface LabStructure {
  course_id: string;
  title: string;
  tree: TopicNode[];
}

export interface SampleRun {
  input: string;
  output: string;
}

export interface Exercise {
  id: string;
  title: string;
  instructions: string;
  sample_runs: SampleRun[];
  starter_code: string;
  solution_code: string;
  course_id: string;
  topic: string;
}

export interface DiffLine {
  type: "equal" | "insert" | "delete" | "replace_old" | "replace_new";
  line_no_left: number | null;
  line_no_right: number | null;
  content: string;
}

export interface SubmissionResult {
  submission_id: string;
  exercise_id: string;
  course_id: string; // used to load the lab TOC on the results page
  status: string;
  message: string;
  compiler_output: string;
  your_code: string;
  solution_code: string;
  diff: DiffLine[];
  score: number; // 0-100 similarity-based
  grade: string; // A+, A, A-, B+, … F
}

export interface SubmissionHistory {
  submission_id: string;
  exercise_id: string;
  status: string;
  score: number;
  grade: string;
  submitted_at: string; // ISO-8601
  code: string;
}

export interface CreateExerciseRequest {
  title: string;
  instructions: string;
  sample_runs: SampleRun[];
  starter_code: string;
  topic: string;
}

// ── API calls ─────────────────────────────────────────────────
export const api = {
  login: (email: string, password: string) =>
    apiFetch<TokenResponse>("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),

  register: (name: string, email: string, password: string, role: string) =>
    apiFetch<TokenResponse>("/auth/register", {
      method: "POST",
      body: JSON.stringify({ name, email, password, role }),
    }),

  getCourses: () => apiFetch<CoursesResponse>("/courses"),

  getLabStructure: (courseId: string) =>
    apiFetch<LabStructure>(`/labs/${courseId}/structure`),

  getExercise: (exerciseId: string) =>
    apiFetch<Exercise>(`/exercises/${exerciseId}`),

  submitCode: (exerciseId: string, code: string) =>
    apiFetch<SubmissionResult>("/submissions", {
      method: "POST",
      body: JSON.stringify({ exercise_id: exerciseId, code }),
    }),

  getHistory: (exerciseId: string) =>
    apiFetch<SubmissionHistory[]>(`/submissions/history/${exerciseId}`),

  /** Instructor only — creates a new exercise and adds it to the TOC */
  createExercise: (data: CreateExerciseRequest) =>
    apiFetch<Exercise>("/exercises", {
      method: "POST",
      body: JSON.stringify(data),
    }),
};
