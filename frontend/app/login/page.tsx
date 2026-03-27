'use client';
import { useState, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import CodeLogo from '@/components/CodeLogo';
import NotifBanner from '@/components/NotifBanner';
import { api, setToken, setUser } from '@/lib/api';

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [emailErr, setEmailErr] = useState('');
  const [authErr, setAuthErr]   = useState('');
  const [loading, setLoading]   = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setEmailErr('');
    setAuthErr('');

    if (!email.trim()) {
      setEmailErr('Please enter your email address');
      return;
    }

    setLoading(true);
    try {
      const res = await api.login(email.trim(), password);
      setToken(res.access_token);
      setUser(res.user);
      router.push('/courses');
    } catch (err: unknown) {
      setAuthErr(err instanceof Error ? err.message : 'Login failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="login-wrap">
      <header className="login-hdr">
        <CodeLogo />
      </header>

      <NotifBanner />

      <main className="login-main">
        <div className="login-card">
          <h2>CodeLab Sign In</h2>

          {authErr && (
            <p style={{ color: '#c0392b', textAlign: 'center', marginBottom: 12, fontSize: 13 }}>
              ⚠ {authErr}
            </p>
          )}

          <form onSubmit={handleSubmit} noValidate>
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
                {emailErr && (
                  <span className="field-error">⚠ {emailErr}</span>
                )}
              </div>
            </div>

            <div className="login-row">
              <label htmlFor="password">Password</label>
              <div className="login-field">
                <input
                  id="password"
                  type="password"
                  autoComplete="current-password"
                  className="login-input"
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                />
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'center', marginTop: 8 }}>
              <button
                type="submit"
                className="btn btn-green"
                disabled={loading}
                style={{ minWidth: 130 }}
              >
                {loading ? '⏳ Signing in…' : '⚙ Login'}
              </button>
            </div>
          </form>

          <div className="login-links">
            <a href="#">Forgot password?</a><br />
            Don&apos;t have an account? <a href="/register">Register here</a><br />
            <a href="#">Student Self-Enrollment</a>
          </div>
        </div>
      </main>
    </div>
  );
}
