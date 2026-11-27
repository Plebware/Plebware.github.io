# AI-INSTRUCTIONS

**Purpose:** This file is the canonical working standard for AI agents authorised to work on the PlebWare project.

## 1. Before Any PlebWare Work

Always inspect the current repository structure and read these live references before creating or modifying content:

- Housekeeping: https://plebware.github.io/everyday/housekeeping/
- Copy-and-Paste Codes: https://plebware.github.io/everyday/housekeeping/2026/07/13/personal-copy-and-paste-codes.html

These references are living documents. Follow the current versions, not remembered or outdated rules.

## 2. Preserve the Existing System

- Do not invent repository structures, URLs, filenames, components, or conventions when the existing project can be inspected.
- Preserve working Markdown, HTML, CSS, JavaScript, Python, shell scripts, images, links, and configuration unless a change is required.
- Never put explanatory prose inside code blocks.
- Do not make unrelated changes.

## 3. PlebWare Ecosystem: Repository Selection and Shared Publishing Standards

PlebWare is an ecosystem of six principal repositories. Article research and publishing decisions must consider the whole ecosystem, not only the main PlebWare website.

### The Six Principal Repositories

Use the live GitHub organisation and each repository's current configuration as the authority. The current repository set and intended roles are:

1. **`Plebware/Plebware.github.io` — Main PlebWare knowledge library.** The central multi-topic publishing platform for general articles, practical guides, research, study material, writing, creativity, news, tutorials, and other material that serves the wider readership. Its current twelve knowledge categories are the main site's taxonomy, not a mandatory taxonomy to copy wholesale into every other project.
   - Site: https://plebware.github.io/
2. **`Plebware/PlebMachine` — PlebMachine project and technical core.** Use for material that is specifically part of the PlebMachine product: architecture, design decisions, release documentation, implementation notes, technical manuals, development records, and project-specific operating guidance. Preserve the existing software/package payload under `PlebMachine/`; never place editorial articles inside the installed-system payload.
   - Site: https://plebware.github.io/PlebMachine/
3. **`Plebware/otto` — Otto's personal archive.** Use for Otto's personal archive material, biography, first-person experiences, personal reflections, author identity, and work whose purpose is to document Otto's own life or creative journey. Do not use this repository as a substitute for the main site's general technical knowledge library.
   - Site: https://plebware.github.io/otto/
4. **`Plebware/juelz-plebcore` — Jullian/Juelz creative archive.** Use for Jullian Boyd De Villiers's own archive, music and audio production work, creative projects, DJ Boy Mist material, and work specifically authored or owned by Jullian. Preserve his preferred name and identity; do not attribute his work to Otto.
   - Current configured site path: https://plebware.github.io/juelz-plebcore/
5. **`Plebware/PlebCircle` — PlebCircle community.** This is the current repository name confirmed in GitHub. Use for community information, group directory and descriptions, joining guidance, community rules, events, announcements, and material whose primary purpose is helping PlebCircle members. Do not assume an older repository name without checking GitHub history and current repository metadata.
   - Current configured site path: https://plebware.github.io/PlebCircle/
6. **`Plebware/pleb-theme` — Shared Jekyll theme and site infrastructure.** This is a software/theme repository, not a normal article destination. Use it for shared layouts, includes, CSS, JavaScript, theme-wide behaviour, and reusable presentation features. Do not publish ordinary editorial articles here.

A separate private repository, `Plebware/plebware-private-spec`, also exists as the ecosystem's master specification, architecture, lexicon, and development-rules reference. Consult it when a task concerns those governing specifications. It is a supporting private reference repository, not one of the six principal public publishing/project repositories and not a destination for ordinary public articles.

### Mandatory Repository-Placement Assessment

Before drafting or publishing any substantial article, determine where the complete work belongs:

1. Read the proposed article's purpose, intended audience, subject, authorship, and likely long-term value.
2. Consider all six principal repositories and their actual contents, not merely the repository currently open.
3. Inspect the relevant repository's README, root `index.md`, `_config.yml`, existing category/subcategory indexes, and comparable articles or project documents.
4. Search the ecosystem for existing work on the same subject. Read relevant material and check whether the proposed article is new, an update, a project document, or a better fit for another repository.
5. Select the repository where the article's primary purpose and ownership naturally belong. The author's identity and the article's repository destination are related but separate decisions.
6. Record the proposed repository, author/persona, category, subcategory, article path, and reason for placement in the pre-publication review.
7. If the article materially serves more than one project, choose one canonical home. Add contextual links or a short clearly identified summary in other relevant locations only when useful; do not create duplicate full articles that can drift out of sync.
8. If no suitable location exists, explain the gap and propose a new category/subcategory or documentation area using that repository's established structure. Do not silently create a new repository or invent a destination.
9. The author retains final authority over placement and publication.

Use these placement principles as guidance, not as rigid keyword rules:

- General Linux education may belong in the main PlebWare library; PlebMachine-specific implementation, architecture, releases, and operational behaviour belong in the PlebMachine project.
- A personal account of Otto's experience may belong in Otto's archive; a reusable tutorial or general technical reference normally belongs in the main PlebWare library.
- Jullian's own music, audio, DJ, and creative-production archive belongs in Juelz/PlebCore; general music education or shared creative guidance may belong in the main library.
- Community rules, group descriptions, membership guidance, and community announcements belong in PlebCircle; general writing about community building may belong in the main library.
- Shared site functionality belongs in the theme repository as code, not as an article.

### Shared Index, Category, and Subcategory Convention

All Jekyll publishing sites in the ecosystem must follow the same structural and navigational principles as the main PlebWare repository. Apply the convention to the main PlebWare site, PlebMachine, Otto, Juelz/PlebCore, and PlebCircle. The theme repository follows software documentation and code organisation rather than article categories.

**This means shared structure and behaviour, not identical subject taxonomies.** Do not copy all twelve main-site categories into every project. Each site must have categories and subcategories that accurately reflect its own purpose.

For each Jekyll publishing site:

1. Maintain a clear root `index.md` with valid front matter, `layout: default`, an accurate page title, and a useful description. It must identify the site/project correctly; never leave a copied or unrelated title such as a different project's name.
2. Use the shared `Plebware/pleb-theme` where the site's current configuration and deployment support it. Preserve the correct `url`, `baseurl`, remote-theme setting, plugins, and project-specific configuration. Never copy a base URL from another repository.
3. The root index should act as the project's landing page and navigation hub. Where appropriate, use the shared dashboard include and provide clear links to the site's actual categories, subcategories, project areas, and related ecosystem sites. Inspect the current theme include before relying on it.
4. Every principal category must have its own `index.md` landing page. It should explain the category and provide a reliable route to its subcategories and relevant content.
5. Every subcategory must have its own `index.md` landing page. It should explain the subject and automatically list or otherwise expose the articles belonging to that exact subcategory, following a verified current PlebWare implementation.
6. Store category-based articles using the established nested structure:
   - `category/subcategory/index.md`
   - `category/subcategory/_posts/YYYY-MM-DD-descriptive-slug.md`
   Do not invent alternative paths when the repository already has an established structure. For a project whose current documentation uses a different purposeful structure, inspect it first and propose a controlled migration rather than breaking existing release or software paths.
7. When adding a new subcategory, inspect comparable live PlebWare subcategories first. Create its directory, `index.md`, and `_posts` directory; ensure the index lists only the intended subcategory's posts and that navigation links are correct.
8. Category and subcategory indexes must not rely on manually maintained article lists when the established Jekyll collection/post data can generate the list reliably. Use the exact path-filtering approach verified in the current theme/site implementation.
9. Keep navigation, heading punctuation, PlebVox boundaries for suitable readable content, image handling, accessible link text, and contextual return behaviour consistent with the current main-site standards.
10. Use the site's configured base URL and Jekyll `relative_url` conventions for internal links and assets. Verify cross-repository links against the destination site's actual configured public path. Do not assume that a repository name, folder name, and deployed URL are interchangeable.
11. Keep category and subcategory naming clear, stable, non-duplicative, and appropriate to the project. Do not create empty taxonomies merely to make sites look alike.
12. Verify each root index, category index, subcategory index, article listing, and navigation link after changes. Check desktop and mobile presentation and ensure the shared theme's contextual return control works on index pages as well as articles.

### Existing Ecosystem Findings to Respect

The live repository inspection shows that the main PlebWare site already has a mature twelve-category hierarchy with nested subcategory `index.md` pages and `_posts` directories. PlebMachine, Otto, Juelz/PlebCore, and PlebCircle currently have much smaller root-level Jekyll structures and do not yet mirror that category/subcategory publishing hierarchy. Do not pretend that the structures are already standardised.

The current Juelz/PlebCore root index also needs careful review because its front-matter title currently identifies it as "PlebMachine Core", which is inconsistent with the repository's Juelz identity. The Otto and PlebCircle indexes and README files should likewise be checked for accurate project names, canonical links, and consistent navigation when those pages are next revised.

This instruction establishes the target standard and mandatory review process. It does not authorise a blanket redesign or migration of all repositories during an unrelated article publication. Make structural changes deliberately, repository by repository, after inspecting existing content and preserving working project files.

## 4. Site-Wide Contextual Return

The contextual **“Return to the article I came from”** control is a shared PlebWare feature and must work from every page using the shared theme, including article pages, category/subcategory index pages, and other index or landing pages.

- Implement the control and its dialog in the shared default layout, not only in the post layout.
- Load the return script site-wide so internal navigation from any page can provide a return destination.
- Keep ordinary internal links in the same tab unless there is a specific reason otherwise; the shared script also supports new-tab links.
- Record the source page's scroll position and a nearby heading/element ID when following an internal link. When the visitor returns, restore the saved scroll position; use the anchor as a fallback when a numeric position is unavailable.
- Preserve existing URL fragments (`#heading`) rather than stripping them. Do not require collaborators to add manual anchors to every article; use existing heading IDs where available.
- Carry the source position safely for same-tab and intentional new-tab navigation, and remove temporary `pleb_from`, `pleb_scroll`, and `pleb_anchor` parameters from the visible URL after they are read.
- If a visitor opens a page directly or arrives from an external search engine without a previous PlebWare page in that tab, provide a clear fallback to Search and All Articles rather than inventing a return destination.
- Keep return handling restricted to same-origin PlebWare URLs.
- Test article-to-article, index-to-article, article-to-index, index-to-index, named-fragment links, scroll-position restoration, new-tab, direct-entry, and first-visit fallback behaviour after the theme deploys.

Do not add a second copy of the return control or dialog to individual layouts when the shared default layout already provides them.

## 5. Articles

- Use valid Jekyll front matter.
- The metadata `title:` and visible `#` title must be different.
- Follow the current Copy-and-Paste reference for tested components.
- Verify filenames, paths, images, alt text, and important links.
- External links should open in a new tab where appropriate.
- Never invent sources, URLs, quotations, or facts.

### Contextual Internal Linking and Related-Article Research

Every new PlebWare article must be connected to relevant existing work across the website. Treat internal linking as a required part of article research and editorial preparation, not an optional finishing touch.

Before drafting or publishing an article:

1. Understand the complete subject, purpose, scope, and major themes of the proposed article.
2. Inspect the live repository's category and subcategory structure to identify where related work is likely to live. Do not limit the search to the proposed article's own category.
3. Search the repository's existing articles using relevant subject terms, alternate wording, synonyms, names, concepts, and closely related themes. Inspect promising articles and their actual content; do not rely on filenames or titles alone.
4. Follow relevant links from promising articles where useful, and inspect related project documentation, guides, research, tutorials, devotions, creative work, and other material that genuinely adds context.
5. Build a shortlist of all genuinely relevant existing PlebWare works. Include direct subject matches and useful supporting or complementary works. Exclude weak, incidental, repetitive, or forced associations.
6. Add verified internal links at the point where each related work is useful to the reader. Use clear, descriptive link text that tells readers what they will find. A concise **Related PlebWare Reading** section may be added when several links deserve a dedicated list, but it must complement rather than replace contextual links in the article body.
7. Verify every destination against the live repository and confirm its actual published URL. Never guess, construct from a filename, or invent a PlebWare URL. Preserve the site's ordinary same-tab internal navigation convention so the contextual return feature continues to work.
8. Check the finished article for broken links, duplicate links, and missed relevant works before publication.

The research must be broad enough to discover related work throughout the PlebWare ecosystem, but editorially selective: link every work that materially helps readers understand, explore, verify, or continue the subject; do not add links merely to increase link counts. If no genuinely relevant existing article is found, do not manufacture a connection.

For substantial articles, record the related works considered and the reason for including or excluding borderline matches during the pre-publication review. The final article should make it easy for readers to move between connected PlebWare knowledge without turning the prose into a directory.

For an article already published, perform this same repository-wide related-work review when it is materially revised or when the author specifically requests a linking audit. Do not silently rewrite unrelated existing articles as part of a new article's publication.

## 6. PlebVox

For suitable readable articles, use:

<!-- PLEBVOX:START -->

<!-- PLEBVOX:END -->

Use natural punctuation for speech pauses. Do not use "STOP"; use "END". Code-heavy or otherwise unsuitable material may omit PlebVox.

**Include section titles in narration.** For every suitable article section, place `<!-- PLEBVOX:START -->` immediately before the section heading and `<!-- PLEBVOX:END -->` after the section’s spoken content. Do not place START after the heading, or the title will be omitted from read-aloud. When a table is excluded from narration, put the table-exclusion markers around the table inside the section’s PlebVox boundaries, then place END after the exclusion block.

### PlebVox Human Listening Verification

The marker `<!---VOXED--->` is reserved for an article whose PlebVox audio rendition has been listened to in full and approved by a human moderator. The shared theme renders `/assets/images/plebvox-verified.webp` for this marker. Do not use it merely because an article has PlebVox enabled. Keep it distinct from `<!-- REVIEWED -->`, which indicates general human-reviewed content.

For devotional articles, PlebVox markers should normally wrap each major section: place START immediately before the section title and END immediately after that section's final line.

## 7. Christian Devotional Convention

For PlebWare daily Christian devotions, preserve the established devotional structure unless the author requests otherwise:

1. Title and date.
2. Opening Prayer.
3. Today's Thought / Introduction.
4. Church History.
5. Original Poem.
6. Three Scriptures, each with the Scripture text, reflection, and a question.
7. Practical Tip / Application.
8. Daily Exercise or To-Do.
9. Heavenly View.
10. Closing Prayer.
11. Final Thought and established Christian signature.

Use emojis in devotional titles, subtitles, and headings. Opening and closing prayers should be given proper prominence and should not be unnecessarily shortened.

Christian content must treat Scripture respectfully, avoid fabricated quotations, identify Bible translations when relevant, and distinguish biblical text from personal interpretation.

The established Christian signature is:

**God's Journalist — Cody — Dei Scriptor**

**Sanguine et Igne Veritas Revelata**

When appropriate, Christian devotional content may also identify the work as being produced with **ChatGPT and the Holy Spirit**.

### Devotional Formatting Rules

These formatting rules are mandatory for Christian devotional articles unless the author explicitly requests otherwise.

**Main devotion (normal Markdown):**

- **Titles and section titles are always bold**, using **two asterisks** around the title: `**Title**`.
- **Prayers are always italic**, using **underscores** around the complete prayer: `_Prayer text_`.
- **Poems are always monospace**, enclosed between **three backticks** on their own lines.
- Do not substitute WhatsApp formatting for the main devotion. The main devotion uses normal Markdown: `**bold**`, `_italic_`, and triple-backtick poems.

**WhatsApp copy-and-paste version:**

- WhatsApp **bold uses exactly one asterisk on each side**: `*bold text*`. Never use `**bold text**` for WhatsApp.
- WhatsApp _italic text and prayers use underscores_: `_italic text_` and `_Prayer text_`.
- The WhatsApp version must **not inherit the main devotion's double-asterisk bold formatting**.
- Poems must remain plain text inside the single outer triple-backtick WhatsApp fence. **Never add nested triple-backticks** around the poem inside that outer fence.

These rules apply consistently and must be checked separately: first the main devotion's Markdown formatting, then the WhatsApp copy's WhatsApp formatting.

## 8. WhatsApp Devotional Copy

Every completed Christian devotional must include a **WhatsApp Copy-and-Paste Version** immediately below the main devotion.

The WhatsApp version must recreate the complete devotion as a clean, self-contained message suitable for copying directly into WhatsApp. The entire WhatsApp version MUST be enclosed in a fenced code block using exactly three backticks at the beginning and exactly three backticks at the end, with no text outside that outer fence except the WhatsApp section heading. The opening and closing fences must each be on their own line.

Rules:

- Preserve the devotional meaning and complete content.
- Use WhatsApp-friendly Markdown formatting.
- Use the established emoji headings and spacing.
- Use underscores for italic text and asterisks for bold text where appropriate.
- Format Scripture quotations using WhatsApp blockquotes beginning with `> `.
- Scripture references must follow the established format, for example: `> _Scripture text..._ *Book Chapter:Verse Range*`
- The entire WhatsApp copy must use one outer fenced code block. Do not place another triple-backtick fence inside it; if the poem needs separation, keep it as plain text within the outer code block.
- Include the complete closing prayer, Christian signature, motto, and PlebWare closing line.
- Do not replace the devotion with a shortened summary.
- The WhatsApp version should be immediately usable with copy-and-paste, without requiring Markdown or HTML editing. The WhatsApp formatting characters must remain visible inside the code block so the reader can copy them exactly as intended.

The WhatsApp version is a **recreation of the devotion**, not a separate abbreviated version.

## 9. Current Information

For news, software, services, prices, availability, politics, or other changing information, research current sources first. Distinguish fact, claim, analysis, and opinion. Political content must remain neutral and factual.

## 10. GitHub

GitHub is the PlebWare workshop.

When asked to publish, commit, upload, or update:

1. Inspect the relevant repository and files.
2. Check Housekeeping and Copy-and-Paste guidance.
3. Review the complete proposed change.
4. Publish only when explicitly authorised.
5. Verify the GitHub operation succeeded.
6. Where practical, verify the resulting file and live site.

Never claim that something was published unless the GitHub operation actually succeeded.

### Publishing Through Different AI or Browser Profiles

The browser account, AI account, or persona used to prepare content does not necessarily determine the publishing author.

If a writing persona or browser profile does not have GitHub access, do not claim that it does. Approved content may be published through an authorised GitHub-enabled AI session, while preserving the correct author/persona and repository attribution.

## 11. Authorship, Personas, and Voice

PlebWare is maintained by Otto Brinkmeier and Jullian "Juelz" De Villiers. Preserve the contributor's own voice and authorship. Do not automatically write as Otto or attribute another person's work to Otto.

Before preparing an article for publication, determine both:

1. **Who is speaking or providing the material.**
2. **What kind of work the material is.**

The identity of the person dictating the material and the publishing author are not always the same.

### Otto Brinkmeier

Use **Otto Brinkmeier** for Otto's personal writing, technical reports, project documentation, observations, experiments, research notes, and general non-fiction, unless the material clearly belongs to another established writing persona.

### Othello Verrocchio

Use **Othello Verrocchio** for creative literary work, including:

- Stories.
- Short stories.
- Fiction.
- Novellas and other fictional work.
- Poetry and poems.

Creative literary work must be placed under the appropriate **Author** area, normally **Fiction** or **Poetry**, according to the actual content.

The fact that the work was created while using Otto's account or browser profile does not change its Othello authorship.

### Captain Gemini

Use **Captain Gemini** for journalistic work, including:

- News articles.
- Incident reports intended as journalism.
- Current-event reporting.
- Field reports.
- Other clearly journalistic material.

Words such as "News", "Incident", "Report", or similar terms may be useful signals, but keywords alone must not determine authorship or classification. Read the actual purpose and content of the work.

For example, an incident involving a technical system may be a technical report rather than journalism if its purpose is technical documentation.

### God's Journalist / Cody — Dei Scriptor

Use the established Christian identity for Christian writing and devotional material:

**God's Journalist — Cody — Dei Scriptor**

**Sanguine et Igne Veritas Revelata**

Christian devotional conventions in this document remain authoritative for such material.

### Boy Mist

When Jullian/Juelz is speaking or publishing in his own voice, use his established nickname:

**Boy Mist**

Do not replace Boy Mist with Otto's identity or voice.

## 12. Category and Subcategory Classification

PlebWare currently uses these twelve principal categories as the working classification structure:

1. Everyday.
2. Author.
3. Study.
4. Research.
5. Graphics.
6. Music.
7. Video.
8. Broadcast.
9. AI Helpers.
10. Developer.
11. Accounting.
12. Leisure.

This list is a current guide, not a rigid permanent structure. The live repository is the authoritative source.

Before publishing an article:

1. Inspect the current repository structure.
2. Determine the article's purpose and subject.
3. Select the most appropriate principal category.
4. Inspect the existing subcategories within that category.
5. Select the most appropriate existing subcategory.
6. Confirm that the selected subcategory actually exists and follows the current PlebWare structure.

Do not classify an article solely from a keyword in its title or opening sentence. Classification must be based on the meaning, purpose, and actual subject of the complete work.

### Missing Subcategory

If the article clearly belongs in a category but no existing subcategory is suitable:

1. Search for existing subcategories with equivalent, synonymous, or closely related names before creating anything.
2. Do not create a duplicate subcategory when an existing one already covers the subject.
3. If no suitable subcategory exists, create the new subcategory as part of the authorised publishing work.
4. Create the appropriate subcategory directory.
5. Create its `index.md` using the current PlebWare/Jekyll conventions.
6. Configure the index so that recent articles in that subcategory are allocated and displayed correctly.
7. Create the subcategory's `_posts` directory.
8. Place future posts for that subcategory in its `_posts` directory.
9. Inspect an existing comparable PlebWare subcategory before creating the new one so the new structure follows the current implementation rather than an invented pattern.
10. Verify the resulting structure before publishing the article.

The AI must not force an article into an unsuitable existing subcategory merely to avoid creating a legitimate new one.

### Pre-Publication Classification Check

Before committing or publishing, present or clearly record the proposed classification:

- **Author/persona.**
- **Main category.**
- **Subcategory.**
- **Article title.**

If a new subcategory was required, identify that it was created and give its repository path.

The user remains the final authority over the proposed classification and publication.

## 13. Final Check

Before finishing, confirm:

- Correct author/persona.
- Correct main category and subcategory.
- Correct location and filename.
- Correct front matter and title rules.
- Correct PlebVox use.
- Code remains intact.
- Images and links are valid.
- No duplicate or unnecessary category structure was created.
- No unrelated files were changed.
- Current Housekeeping and Copy-and-Paste guidance was followed.

**Golden Rule: Check first. Understand the writer and the work. Inspect the live repository. Follow the current project standards. Then build. Never guess when the repository can be inspected.**
