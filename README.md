# NOVERA ROBOTICS

Independent concept-stage human-centered robotics research venture, separate from VELTARO.

## Website

Open `index.html` in any browser. This is a dependency-free bilingual Greek/English responsive static website.

## GitHub Pages

In GitHub, open **Settings → Pages → Build and deployment → Deploy from a branch**, select `main` and `/ (root)`, then Save. Publication can take a few minutes. Expected project URL after successful deployment: `https://panagiotagrosdouli.github.io/NOVERA/`.

## Notes

NOVERA ONE is a concept, not a built or certified humanoid robot. Images are third-party reference imagery, not product photographs. Emotion-aware interaction does not imply real feelings or consciousness. The contact form posts to FormSubmit for email delivery to the project inbox. The inbox owner must confirm the FormSubmit activation email following the first submission before delivery is active. Submissions are processed by this third-party service; publish appropriate privacy information before wider use. Obtain suitable imagery rights, domain/trademark clearance, and implement real form handling and privacy materials before commercial launch.


## Startup foundation branch — 13 November 2026

Start at `research-hub.html`. Corporate homepage, proposed original identity, review documents and local research tools are added without removing founder-selected imagery. Run `python3 scripts/check-all.py`; optional browser/accessibility checks: `CHROMIUM_PATH=/usr/bin/chromium python3 tests/browser-smoke.py` with Playwright 1.62.0 installed. See `docs/mission/READINESS.md` for incomplete gates and `docs/mission/BUSINESS-PLAN.md`, `financial-model.xlsx`, `investor-deck.pptx` and `investor-deck.pdf` for founder review materials.

Local twin: `python3 research/server.py`, then http://127.0.0.1:8765/digital-twin.html. This is a 2D kinematic simulator, not the complete ROS/Gazebo MVP. See `ros2/README.md` for the unexecuted scaffold.
