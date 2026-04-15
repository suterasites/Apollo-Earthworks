# CLAUDE.md - Apollo Earthworks

## Business Context

**Business Name:** Apollo Earthworks
**Contact Person:** Kosta Mastelidys
**Phone:** 0431 560 908
**Email:** info@apolloearthworks.com.au
**Address:** 2/26 Allister Street, Mount Waverley VIC 3149
**Service Area:** Melbourne Metropolitan Area and surrounding regions
**ABN:** 26 886 956 778
**Tagline:** "Tough Work. Done Right."

### About
- Melbourne-based earthmoving and haulage company providing excavation, bulk earthworks, site cuts, retaining walls, and material haulage across residential, commercial, and civil projects
- Focus is on building long-term relationships with builders, developers, and contractors through consistent service, experienced operators, and well-maintained equipment
- Service area is the Melbourne Metropolitan Area and surrounding regions - use this for local SEO targeting (e.g. "earthworks Melbourne", "excavation Melbourne VIC", "site cuts Melbourne")
- Positions on reliability, precision, and hard work - dependable, efficient, and easy to work with, delivering on time and on budget
- Caters to both DIY/builder clients and larger contractors, short-term and long-term projects
- Branding is clean and professional with a black, white, and blue color scheme featuring an excavator logo
- Primary brand blue: #1B8FD1 (dark: #1474AB, light: #2BA0E0)
- Contactable via phone, email, or Instagram

### Services

**Earthworks and Excavation**
- Bulk Earthworks and Excavation
- Site Cuts
- Basements
- Footings
- Trenching
- Final Trim

**Demolition and Clearing**
- Demolition
- Land Clearing
- Rock Breaking
- Rock Removal
- Soil Removal
- Site Clean-ups

**Haulage and Hire**
- Material Haulage
- Tipper Hire
- Excavator Hire (wet hire)
- Posi-Track Wet Hire

**Structural and Civil**
- Retaining Walls
- Drainage
- Driveways and Car Parks
- Concrete Slabs, Structural, Footpath, and Rehabilitation Works

### Fleet
Modern, reliable machinery suitable for small to large-scale projects. All machinery is serviced regularly and operated by experienced, ticketed operators.
- Excavators (1.7T to 30T)
- Tandem Tipper Trucks
- Skid Steers
- Rock Breakers and Attachments
- Augers
- Compaction Equipment
- Machinery Floats (Up to 10T)

### Industries Served
Builders, Developers, Concreters, Landscapers, Plumbers, Civil Contractors, Owner Builders, Government and Council.

### Why Choose Apollo Earthworks
- Reliable and on time - shows up when they say they will
- Experienced, ticketed operators on every machine
- Modern, regularly serviced machinery
- Competitive rates without compromising on quality
- Fully insured
- Safety focused - committed to safe practices on every site
- Flexible engagement - available for short-term and long-term projects
- Melbourne-wide service

### Safety and Compliance
Committed to maintaining a safe work environment and complies with all Victorian safety regulations and site requirements.
- Fully Insured
- SWMS Available
- White Card Certified
- Machine Tickets and Licences
- Regular Equipment Maintenance
- OH&S Compliant

### Social Media
- **Instagram:** @apolloearthworks - active with service-focused posts and engagement from other trades accounts. Post from November 2025 highlights their full service list and positions them on hard work, precision, and reliability

---

## Always Do First
- **Invoke the `frontend-design` skill** before writing any frontend code, every session, no exceptions.

## Reference Images
- If a reference image is provided: match layout, spacing, typography, and color exactly. Swap in placeholder content (images via `https://placehold.co/`, generic copy). Do not improve or add to the design.
- If no reference image: design from scratch with high craft (see guardrails below).
- Screenshot your output, compare against reference, fix mismatches, re-screenshot. Do at least 2 comparison rounds. Stop only when no visible differences remain or user says so.

## Local Server
- **Always serve on localhost** - never screenshot a `file:///` URL.
- Start the dev server: `node serve.mjs` (serves the project root at `http://localhost:3000`)
- `serve.mjs` lives in the project root. Start it in the background before taking any screenshots.
- If the server is already running, do not start a second instance.

## Screenshot Workflow
- Puppeteer is installed at `C:/Users/nateh/AppData/Local/Temp/puppeteer-test/`. Chrome cache is at `C:/Users/nateh/.cache/puppeteer/`.
- **Always screenshot from localhost:** `node screenshot.mjs http://localhost:3000`
- Screenshots are saved automatically to `./temporary screenshots/screenshot-N.png` (auto-incremented, never overwritten).
- Optional label suffix: `node screenshot.mjs http://localhost:3000 label` → saves as `screenshot-N-label.png`
- `screenshot.mjs` lives in the project root. Use it as-is.
- After screenshotting, read the PNG from `temporary screenshots/` with the Read tool - Claude can see and analyze the image directly.
- When comparing, be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
- Check: spacing/padding, font size/weight/line-height, colors (exact hex), alignment, border-radius, shadows, image sizing

## Output Defaults
- Single `index.html` file, all styles inline, unless user says otherwise
- Tailwind CSS via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- Mobile-first responsive

## Brand Assets
- Always check the `brand_assets/` folder before designing. It may contain logos, color guides, style guides, or images.
- If assets exist there, use them. Do not use placeholders where real assets are available.
- If a logo is present, use it. If a color palette is defined, use those exact values - do not invent brand colors.

## Anti-Generic Guardrails
- **Colors:** Never use default Tailwind palette (indigo-500, blue-600, etc.). Pick a custom brand color and derive from it.
- **Shadows:** Never use flat `shadow-md`. Use layered, color-tinted shadows with low opacity.
- **Typography:** Never use the same font for headings and body. Pair a display/serif with a clean sans. Apply tight tracking (`-0.03em`) on large headings, generous line-height (`1.7`) on body.
- **Gradients:** Layer multiple radial gradients. Add grain/texture via SVG noise filter for depth.
- **Animations:** Only animate `transform` and `opacity`. Never `transition-all`. Use spring-style easing.
- **Interactive states:** Every clickable element needs hover, focus-visible, and active states. No exceptions.
- **Images:** Add a gradient overlay (`bg-gradient-to-t from-black/60`) and a color treatment layer with `mix-blend-multiply`.
- **Spacing:** Use intentional, consistent spacing tokens - not random Tailwind steps.
- **Depth:** Surfaces should have a layering system (base → elevated → floating), not all sit at the same z-plane.

## Deployment
- **Always deploy changes to GitHub and Cloudflare Pages** after making code changes.
- Live site: https://apollo-earthworks.pages.dev/
- Git remote: `origin` (check with `git remote -v` for current URL)
- Push to `main` branch, then deploy to Cloudflare Pages with `npx wrangler pages deploy . --project-name=apollo-earthworks --branch=main`.

## Multi-Page Consistency
- **Navbar:** The navbar must be identical across all pages. If the navbar is modified on any page, apply the same change to every other page immediately.
- **Footer:** The footer must be identical across all pages. If the footer is modified on any page, apply the same change to every other page immediately.
- **Internal links:** All text links that reference a page on the site must link to the correct page URL. When a new page is created, scan all existing pages and update any mentions of that topic to link to the new page.

## Hard Rules
- Do not add sections, features, or content not in the reference
- Do not "improve" a reference design - match it
- Do not stop after one screenshot pass
- Do not use `transition-all`
- Do not use default Tailwind blue/indigo as primary color
- Do not use em dashes (—) anywhere in content, code, or comments. Use hyphens (-), commas, or periods instead

---

# Site Checklist

Use this checklist for every page on the site. Each page must have the following metadata and content requirements configured before launch.

---

## Per-Page Checklist

### Page: _______________

**Meta & SEO**
- [ ] **Title Tag** - Under 60 characters, includes primary keyword, brand name at end
- [ ] **Meta Description** - Under 160 characters, includes a clear CTA and primary keyword
- [ ] **Page Canonical URL** - Self-referencing canonical set, uses preferred URL format (trailing slash consistency, www vs non-www)
- [ ] **Open Graph Title** - Optimised for social sharing, can differ from title tag if needed
- [ ] **Open Graph Description** - Written for social click-through, under 200 characters
- [ ] **Search Title** - Google Business / search appearance title confirmed
- [ ] **Search Description** - Google Business / search appearance description confirmed

**Schema & Structured Data**
- [ ] **JSON-LD Schema** - Appropriate schema type applied (LocalBusiness, Service, FAQPage, etc.)
- [ ] **Schema.org Structured Data** - Validated via Google Rich Results Test, no errors or warnings
- [ ] **Identity Schema** - Organization or LocalBusiness identity schema present on key pages (name, logo, URL, contact info, social profiles, sameAs links)

**Sitemaps & Indexing**
- [ ] **XML Sitemap** - Page is included in the XML sitemap with correct URL, lastmod date, and priority value

**Content & AI Readability**
- [ ] **Minimum 500 Words** - Page contains at least 500 words of unique, relevant body content (excluding nav, footer, boilerplate)
- [ ] **Rendered Content LLM Readability** - Page content is fully rendered in the HTML source (not hidden behind JS-only rendering), uses semantic HTML (h1-h6, p, ul/ol, section, article), has a clear content hierarchy that AI crawlers and LLMs can parse and summarise accurately

---

## Page-by-Page Tracker

*(Add pages as they are created. Use the Per-Page Checklist template above for each new page.)*

---

## Site-Wide Checks

These items apply once across the entire site, not per page.

- [ ] **XML Sitemap generated** - sitemap.xml created with all pages, correct URLs, lastmod dates, and priority values
- [ ] **XML Sitemap submitted** - Needs submission to Google Search Console
- [ ] **XML Sitemap auto-updates** - Static site, manual updates required when pages are added/removed
- [ ] **Robots.txt** - robots.txt created, references sitemap URL, allows all crawlers
- [ ] **Identity Schema on Home** - LocalBusiness schema with name, logo, URL, address, phone, founding date, social profiles, sameAs
- [ ] **Schema validation clean** - Needs validation via Google Rich Results Test

---

## Quick Reference - Character Limits

| Element | Max Length |
|---|---|
| Title Tag | 60 characters |
| Meta Description | 160 characters |
| OG Title | 60 characters |
| OG Description | 200 characters |
| Search Title | 60 characters |
| Search Description | 160 characters |

---

## JSON-LD Schema Types - Common for Earthworks / Local Service Businesses

- **LocalBusiness** - Home page, Contact page (with address, phone, opening hours, geo coordinates)
- **Organization** - Identity schema (name, logo, sameAs social links)
- **Service** - Individual service pages (excavation, site cuts, demolition, haulage, etc.)
- **FAQPage** - FAQ sections or pages
- **BreadcrumbList** - All inner pages
- **WebSite** - Home page (with SearchAction if applicable)
- **Place** - Service area / location pages
- **Review / AggregateRating** - If client testimonials are displayed

---

## LLM Readability - What to Check

When verifying rendered content is LLM-readable, confirm the following:

1. **Server-side or pre-rendered HTML** - Content is in the HTML source, not loaded entirely via client-side JavaScript after page load
2. **Semantic heading hierarchy** - Single H1 per page, logical H2-H6 nesting, no skipped levels
3. **Paragraph and list structure** - Body content uses `<p>`, `<ul>`, `<ol>` tags rather than divs with styled text
4. **Section and article tags** - Major content blocks wrapped in `<section>` or `<article>` for clear content boundaries
5. **Descriptive alt text on images** - Every image has alt text that describes the content, not just "image1.jpg"
6. **No critical content in images only** - Key information (contact details, service info, pricing) exists as text, not embedded in graphics
7. **Clean readable text** - No keyword stuffing, no hidden text, no excessive boilerplate repeated across pages

---

*Duplicate the page section for each additional page on the site. Replace [ ] with [x] once completed and fill in the Value / Notes column with the actual content.*
