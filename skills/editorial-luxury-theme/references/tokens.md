# Editorial Luxury — starter stylesheet

Framework-agnostic CSS. Drop into any stack (Blade `app.css`, Astro global CSS, a Tailwind `@layer base`, etc.) and adjust class names to the project's conventions — the values and relationships are what matter, not these exact selectors.

```css
:root {
  --primary-color: #3F352C;
  --secondary-color: #BDA18C;
  --accent-color: #BDA18C;
  --background-color: #FFFFFF;
  --text-color: #000000;

  --heading-font: 'Poppins', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --body-font: 'Poppins', system-ui, -apple-system, 'Segoe UI', sans-serif;

  --ivory: var(--background-color);
  --ivory-2: #FFFFFF;
  --card: #ffffff;
  --espresso: var(--primary-color);
  --ink: var(--text-color);
  --mocha: #3F352C;
  --taupe: #B4A79E;
  --line: #E6DCD3;
  --line-soft: #E6DCD3;
  --gold: var(--accent-color);
  --gold-deep: #3F352C;
  --gold-soft: #BDA18C;
  --blush: #E6DCD3;

  --surface: #ffffff;
  --muted: #B4A79E;
  --border: #E6DCD3;

  --radius: 0px; /* keep at 0 everywhere: cards, buttons, inputs, media */

  --shadow-sm: 0 2px 10px -4px rgba(0, 0, 0, 0.16);
  --shadow-md: 0 18px 44px -26px rgba(0, 0, 0, 0.30);
  --shadow-lg: 0 30px 70px -30px rgba(0, 0, 0, 0.38);

  --container: 80%;
  --space: clamp(4rem, 9vw, 8rem);
  --transition: 0.35s cubic-bezier(.22,.61,.36,1);
  --ease: cubic-bezier(.22,.61,.36,1);
}

body {
  font-family: var(--body-font);
  color: var(--text-color);
  background: var(--background-color);
  line-height: 1.72;
}

h1, h2, h3, h4, h5 {
  font-family: var(--heading-font);
  font-weight: 500;
  line-height: 1.14;
  letter-spacing: -0.015em;
}
h1 { font-size: clamp(2.6rem, 6vw, 5rem); }
h2 { font-size: clamp(2rem, 4vw, 3.1rem); }
h3 { font-size: clamp(1.25rem, 2.2vw, 1.6rem); font-weight: 600; }

/* Eyebrow label — precedes every section heading */
.eyebrow {
  display: inline-flex; align-items: center; gap: 0.7em;
  text-transform: uppercase; letter-spacing: 0.28em; font-size: 0.72rem; font-weight: 600;
  color: var(--gold-deep); margin-bottom: 1.1rem;
}
.eyebrow::before { content: ""; width: 34px; height: 1px; background: var(--gold); }

/* Buttons */
.btn {
  --btn-fg: #fff; --btn-bg: var(--espresso);
  display: inline-flex; align-items: center; justify-content: center; gap: 0.6em;
  padding: 15px 32px; border-radius: 0;
  font-weight: 600; font-size: 0.8rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--btn-fg); background: var(--btn-bg); border: 1px solid var(--btn-bg);
  cursor: pointer; transition: transform var(--transition), background var(--transition), color var(--transition), border-color var(--transition);
}
.btn:hover { background: var(--gold-deep); border-color: var(--gold-deep); color: #fff; transform: translateY(-2px); }
.btn--outline { --btn-fg: var(--espresso); background: transparent; border-color: #B4A79E; }
.btn--outline:hover { background: var(--espresso); color: #fff; border-color: var(--espresso); }
.btn--ghost { --btn-fg: #fff; background: transparent; border-color: rgba(255,255,255,0.45); }
.btn--ghost:hover { background: #fff; color: var(--espresso); border-color: #fff; }

/* Header */
.site-header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}
.main-nav a { color: var(--espresso); font-weight: 600; font-size: 0.76rem; letter-spacing: 0.12em; text-transform: uppercase; position: relative; padding: 6px 0; }
.main-nav a::after { content: ""; position: absolute; left: 0; bottom: 0; height: 1px; width: 100%; background: var(--gold); transform: scaleX(0); transform-origin: left; transition: transform var(--transition); }
.main-nav a:hover::after, .main-nav a[aria-current="page"]::after { transform: scaleX(1); }

/* Hero */
.hero { position: relative; overflow: hidden; min-height: calc(100dvh - 78px); display: flex; align-items: flex-end; color: #fff; isolation: isolate; }
.hero__overlay { position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, rgba(0,0,0,0.44) 0%, rgba(0,0,0,0.10) 34%, rgba(0,0,0,0.70) 100%),
              linear-gradient(90deg, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0) 58%); }
.hero__trust { margin-top: 2.5rem; display: flex; flex-wrap: wrap; gap: 14px 34px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 1.6rem; color: rgba(255,255,255,0.85); font-size: 0.82rem; }

/* Cards */
.card { background: var(--surface); border: 1px solid var(--line-soft); border-radius: 0; overflow: hidden; transition: transform var(--transition), box-shadow var(--transition), border-color var(--transition); display: flex; flex-direction: column; }
.card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); border-color: var(--line); }
.card__media { aspect-ratio: 4 / 5; background: var(--blush); overflow: hidden; position: relative; }
.card__media img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.7s var(--ease); }
.card:hover .card__media img { transform: scale(1.05); }
.card__footer { margin-top: auto; display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding-top: 1.1rem; border-top: 1px solid var(--line-soft); }
.price { font-family: var(--heading-font); font-size: 1.35rem; font-weight: 600; color: var(--gold-deep); }

/* CTA band / footer */
.cta-band { background: var(--espresso); color: #fff; padding: clamp(3rem, 7vw, 5.5rem); text-align: center; }
.site-footer { background: var(--espresso); color: rgba(255,255,255,0.72); padding-block: 4.5rem 1.75rem; }
.site-footer h4 { color: #fff; font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.16em; }
.footer-links a { color: rgba(255,255,255,0.72); }
.footer-links a:hover { color: var(--gold-soft); }

/* Forms */
.form-group label { display: block; font-weight: 600; margin-bottom: 0.45rem; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--espresso); }
.form-control { width: 100%; padding: 14px 16px; border: 1px solid var(--line); border-radius: 0; background: var(--card); color: var(--espresso); }
.form-control:focus { outline: none; border-color: var(--gold); box-shadow: 0 0 0 3px rgba(189,161,140,0.25); }

/* Booking / quote wizard step indicator */
.wizard-steps { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; counter-reset: step; }
.wizard-steps li::before { counter-increment: step; content: counter(step); width: 30px; height: 30px; border-radius: 50%; background: var(--ivory-2); border: 1px solid var(--line); color: var(--taupe); display: grid; place-items: center; }
.wizard-steps li.is-active::before { background: var(--espresso); color: #fff; border-color: var(--espresso); }
.wizard-steps li.is-done::before { background: var(--gold); color: #fff; border-color: var(--gold); content: '✓'; }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; scroll-behavior: auto !important; }
}
```

## Notes for adapting to a stack

- **Tailwind**: move the token values into `tailwind.config` theme (`colors.espresso`, `borderRadius: { DEFAULT: '0px' }`, `fontFamily.sans: ['Poppins', ...]`) and keep the component patterns as documented utility combinations or `@apply` classes.
- **Astro/React/Vue**: keep these as plain CSS custom properties in a global stylesheet; component files consume the classes/vars directly.
- Always wire `--primary-color` / `--secondary-color` etc. to the confirmed business brand colors from intake when they exist — the palette above is the fallback, not a fixed brand.
