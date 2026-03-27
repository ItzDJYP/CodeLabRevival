'use client';
import { useState, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import CodeLogo from '@/components/CodeLogo';
import { api, setToken, setUser } from '@/lib/api';

export default function RegisterPage() {
  const router = useRouter();
  const [name, setName]         = useState('');
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [confirm, setConfirm]   = useState('');
  const [role, setRole]         = useState<'student' | 'instructor'>('student');

  const [nameErr, setNameErr]       = useState('');
  const [emailErr, setEmailErr]     = useState('');
  const [passwordErr, setPasswordErr] = useState('');
  const [confirmErr, setConfirmErr] = useState('');
  const [submitErr, setSubmitErr]   = useState('');
  const [loading, setLoading]       = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setNameErr('');
    setEmailErr('');
    setPasswordErr('');
    setConfirmErr('');
    setSubmitErr('');

    let valid = true;
    if (!name.trim()) {
      setNameErr('Please enter your full name');
      valid = false;
    }
    if (!email.trim()) {
      setEmailErr('Please enter your email address');
      valid = false;
    }
    if (password.length < 6) {
      setPasswordErr('Password must be at least 6 characters');
      valid = false;
    }
    if (password !== confirm) {
      setConfirmErr('Passwords do not match');
      valid = false;
    }
    if (!valid) return;

    setLoading(true);
    try {
      const res = await api.register(name.trim(), email.trim(), password, role);
      setToken(res.access_token);
      setUser(res.user);
      router.push('/courses');
    } catch (err: unknown) {
      setSubmitErr(err instanceof Error ? err.message : 'Registration failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="login-wrap">
      <header className="login-hdr">
        <CodeLogo />
      </header>

      <main className="login-main">
        <div className="login-card">
          <h2>Create an Account</h2>

          {submitErr && (
            <p style={{ color: '#c0392b', textAlign: 'center', marginBottom: 12, fontSize: 13 }}>
              ⚠ {submitErr}
            </p>
          )}

          <form onSubmit={handleSubmit} noValidate>
            <div className="login-row">
              <label htmlFor="name">Full Name</label>
              <div className="login-field">
                <input
                  id="name"
                  type="text"
                  autoComplete="name"
                  className={`login-input${nameErr ? ' error' : ''}`}
                  value={name}
                  onChange={e => setName(e.target.value)}
                  placeholder="Your full name"
                />
                {nameErr && <span className="field-error">⚠ {nameErr}</span>}
              </div>
            </div>

            <div className="login-row">
              <label htmlFor="email">Email</label>
              <div className="login-field">
                <input
                  id="email"
                  type="email"
                  autoComplete="email"
                  className={`login-input${emailErr ? ' error' : ''}`}
                  value={email}
                  onChange={e => setEmail(e.target.value)}
                  placeholder="you@example.com"
                />
                {emailErr && <span className="field-error">⚠ {emailErr}</span>}
              </div>
            </div>

            <div className="login-row">
              <label htmlFor="password">Password</label>
              <div className="login-field">
                <input
                  id="password"
                  type="password"
                  autoComplete="new-password"
                  className={`login-input${passwordErr ? ' error' : ''}`}
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                />
                {passwordErr && <span className="field-error">⚠ {passwordErr}</span>}
              </div>
            </div>

            <div className="login-row">
              <label htmlFor="confirm">Confirm</label>
              <div className="login-field">
                <input
                  id="confirm"
                  type="password"
                  autoComplete="new-password"
                  className={`login-input${confirmErr ? ' error' : ''}`}
                  value={confirm}
                  onChange={e => setConfirm(e.target.value)}
                />
                {confirmErr && <span className="field-error">⚠ {confirmErr}</span>}
              </div>
            </div>

            <div className="login-row">
              <label htmlFor="role">Role</label>
              <div className="login-field">
                <select
                  id="role"
                  className="login-input"
                  value={role}
                  onChange={e => setRole(e.target.value as 'student' | 'instructor')}
                >
                  <option value="student">Student</option>
                  <option value="instructor">Instructor</option>
                </select>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'center', marginTop: 8 }}>
              <button
                type="submit"
                className="btn btn-green"
                disabled={loading}
                style={{ minWidth: 130 }}
              >
                {loading ? '⏳ Registering…' : '⚙ Register'}
              </button>
            </div>
          </form>

          <div className="login-links">
            Already have an account? <a href="/login">Sign in here</a>
          </div>
        </div>
      </main>
    </div>
  );
}
